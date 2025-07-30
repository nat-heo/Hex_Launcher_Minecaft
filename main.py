import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import minecraft_launcher_lib
import subprocess
import threading
import ctypes
import json
import os

user_log_1 = "user_log.json"

def load_user_log():
    if os.path.exists(user_log_1):
        with open(user_log_1, "r") as f:
            return json.load(f)
    return {}

game_settings = load_user_log()

roaming_path = os.path.join(os.getenv('APPDATA'))
minecraft_directory = os.path.join(roaming_path, ".hexlauncher")
if not os.path.exists(minecraft_directory):
    os.makedirs(minecraft_directory)

def get_versions():
    versions = minecraft_launcher_lib.utils.get_version_list()
    return [v['id'] for v in versions if v['type'] == 'release']

def launch_minecraft():
    global username
    version = version_var.get()

    if version == "Sürüm":
        messagebox.showwarning("Uyarı!", "Lütfen bir Minecraft sürümü seçiniz!")
        return
    
    with open(user_log_1, "w") as f:
        json.dump({
            "username": username,
            "version": version
        }, f)

    messagebox.showinfo("Hex Launcher", "İndiriliyor veya dosyalar derleniyor bu işlem birkaç dakika sürebilir lütfen bekleyiniz...")

    minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)

    user = {
        "username": username,
        "uuid": "2337468d-982e-4a7a-9591-db971df4eca1",
        "token": "token",
    }

    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, user)

    messagebox.showinfo("Hex Launcher", "Minecraft başlatılıyor...")

    CREATE_NO_WINDOW = 0x08000000
    def run_minecraft(command):
        try:
            command[0] = command[0].replace("java.exe", "javaw.exe")

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )

            for line in process.stdout:
                log_box.insert(END, line)
                log_box.see(END)

            process.stdout.close()
        except Exception as e:
            log_box.insert(END, f"Hata oluştu: {str(e)}\n")
            log_box.see(END)

    threading.Thread(target=lambda: run_minecraft(command), daemon=True).start()

def start_main_window():
    global root, nameent, version_var, log_box

    root = ctk.CTk()
    root.title("Hex Launcher")
    root.resizable(False, False)
    root.iconbitmap("icon.ico")
    root.config(bg="#000000")
    root.overrideredirect(True)
    WIDTH, HEIGHT = 1250, 700
    RADIUS = 40
    root.geometry(f"{WIDTH}x{HEIGHT}+100+100")
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, WIDTH, HEIGHT, RADIUS, RADIUS)
    ctypes.windll.user32.SetWindowRgn(hwnd, region, True)
    offset_x = 0
    offset_y = 0
    def start_move(event):
        nonlocal offset_x, offset_y
        offset_x = event.x_root
        offset_y = event.y_root
    def do_move(event):
        nonlocal offset_x, offset_y
        delta_x = event.x_root - offset_x
        delta_y = event.y_root - offset_y
        x = root.winfo_x() + delta_x
        y = root.winfo_y() + delta_y
        root.geometry(f"+{x}+{y}")
        offset_x = event.x_root
        offset_y = event.y_root
    root.bind("<Button-1>", start_move)
    root.bind("<B1-Motion>", do_move)
    bg_image1 = Image.open("bg_2.png")
    bg_image1 = bg_image1.resize((1250, 700))
    bg_photo1 = ImageTk.PhotoImage(bg_image1)
    bg_label1 = Label(root, image=bg_photo1)
    bg_label1.place(x=625, y=350,anchor="center")

    font2 = ctk.CTkFont(family="Impact", size=29)

    def ext():
        root.destroy()

    WIDGET_WIDTH = 180

    version_var = ctk.StringVar(value=game_settings.get("version", "Sürüm"))
    version_menu = ctk.CTkOptionMenu(
        root,
        fg_color="#BEBEBE",
        button_color="#BEBEBE",
        button_hover_color="#BEBEBE",
        text_color="#141414",
        font=font2,
        values=get_versions(),
        variable=version_var,
        width=120
    )
    version_menu.place(x=560, y=470,anchor="center")

    playbtn = ctk.CTkButton(
        root,
        text="Oyna",
        fg_color="#BEBEBE",
        bg_color="#393737",
        hover_color="#7B7B7B",
        text_color="#141414",
        font=font2,
        command=launch_minecraft,
        width=50
    )
    playbtn.place(x=560, y=520,anchor="center")

    extbtn = ctk.CTkButton(
        root,
        text="❌",
        fg_color="#0A0A0A",
        bg_color="#0A0A0A",
        hover_color="#0A0A0A",
        text_color="#FFFFFF",
        command=ext,
        width=15
    )
    extbtn.place(x=1100, y=20,anchor="center")
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    log_box = ctk.CTkTextbox(
        root,
        width=325,
        height=500,
        bg_color="#232525",
        fg_color="#232525"
    )
    log_box.place()
    log_box.insert(END, "Hex Launcher Log\n")
    log_box.see(END)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    root.mainloop()

nickname_window = ctk.CTk()
nickname_window.title("Nickname Girişi")
nickname_window.iconbitmap("icon.ico")
nickname_window.resizable(False, False)
nickname_window.overrideredirect(True)
WIDTH, HEIGHT = 1250, 700
RADIUS = 40
nickname_window.geometry(f"{WIDTH}x{HEIGHT}+100+100")
hwnd = ctypes.windll.user32.GetParent(nickname_window.winfo_id())
region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, WIDTH, HEIGHT, RADIUS, RADIUS)
ctypes.windll.user32.SetWindowRgn(hwnd, region, True)
offset_x = 0
offset_y = 0
def start_move(event):
    global offset_x, offset_y
    offset_x = event.x_root
    offset_y = event.y_root
def do_move(event):
    global offset_x, offset_y
    delta_x = event.x_root - offset_x
    delta_y = event.y_root - offset_y
    x = nickname_window.winfo_x() + delta_x
    y = nickname_window.winfo_y() + delta_y
    nickname_window.geometry(f"+{x}+{y}")
    offset_x = event.x_root
    offset_y = event.y_root
nickname_window.bind("<Button-1>", start_move)
nickname_window.bind("<B1-Motion>", do_move)
bg_image = Image.open("bg_1.png")
bg_image = bg_image.resize((1250, 700))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(nickname_window, image=bg_photo)
bg_label.place(x=625, y=350,anchor="center")

font2 = ctk.CTkFont(family="Impact", size=29)
WIDGET_WIDTH = 180

nameent = ctk.CTkEntry(
    nickname_window,
    font=font2,
    placeholder_text="Nickname",
    bg_color="#2B2A2A",
    width=WIDGET_WIDTH)
nameent.place(x=560, y=320,anchor="center")
username_value = game_settings.get("username", "")
if username_value:
    nameent.insert(0, username_value)
username = nameent.get()

def continue_to_main():
    global username
    username = nameent.get()
    if not username:
        messagebox.showwarning("Uyarı!", "Lütfen kullanıcı adını giriniz!")
        return
    nickname_window.destroy()
    start_main_window()

next_button = ctk.CTkButton(
    nickname_window,
    text="Devam",
    fg_color="#BEBEBE",
    bg_color="#393737",
    hover_color="#7B7B7B",
    text_color="#141414",
    font=font2,
    command=continue_to_main,
    width=150
    )
next_button.place(x=560, y=370,anchor="center")

def ext2():
    nickname_window.destroy()
extbtn2 = ctk.CTkButton(
    nickname_window,
    text="❌",
    fg_color="#0A0A0A",
    bg_color="#0A0A0A",
    hover_color="#0A0A0A",
    text_color="#FFFFFF",
    command=ext2,
    width=15
    )
extbtn2.place(x=1100, y=20,anchor="center")

nickname_window.mainloop()
