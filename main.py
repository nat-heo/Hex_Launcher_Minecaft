import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import *
from tkinter import messagebox
from PIL import Image
import minecraft_launcher_lib
import subprocess
import os

minecraft_directory = "C:/hexlauncher"

if not os.path.exists(minecraft_directory):
    os.makedirs(minecraft_directory)

def get_versions():
    versions = minecraft_launcher_lib.utils.get_version_list()
    return [v['id'] for v in versions if v['type'] == 'release']

def launch_minecraft():
    username = nameent.get()
    version = version_var.get()

    if not username or not version:
        messagebox.showwarning("Uyarı!", "Lütfen kullanıcı adını giriniz veya sürümü seçiniz!")
        return
    
    messagebox.showinfo("Bilgi", "İndiriliyor lütfen bekleyiniz...")

    minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)

    user = {
        "username": username,
        "uuid": "2337468d-982e-4a7a-9591-db971df4eca1",
        "token": "token",
    }

    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, user)

    messagebox.showinfo("Bilgi", "Minecraft başlatılıyor...")
    subprocess.Popen(command)

root = ctk.CTk()
root.title("Hex Launcher")
root.geometry("350x550")
root.resizable(False, False)
root.iconbitmap("icon.ico")
root.config(bg="#232525")

image = Image.open("bg.png")
bg_image = ctk.CTkImage(light_image=image, size=(350,550))
background_label = ctk.CTkLabel(root, image=bg_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

font1 = ctk.CTkFont(family="Impact", size=40)
font2 = ctk.CTkFont(family="Impact", size=29)

frame1 = ctk.CTkFrame(master=root, width=300, height=500, corner_radius=50, bg_color="#232525",fg_color="#232525")
frame1.place(x=22, y=40)

logo_image_1 = Image.open("icon.png")
logo_image_2 = CTkImage(light_image=logo_image_1, size=(200, 200)) 
logo_label = ctk.CTkLabel(frame1, text="", image=logo_image_2)
logo_label.place(relx=0.5, y=120, anchor="center")

def ext():
    root.destroy()

WIDGET_WIDTH = 180

nameent = ctk.CTkEntry(frame1, font=font2, corner_radius=15, placeholder_text="Nickname", width=WIDGET_WIDTH)
nameent.place(relx=0.5, y=265, anchor="center")

version_var = ctk.StringVar(value="Sürüm")
version_menu = ctk.CTkOptionMenu(
    frame1,
    fg_color="#087B08",
    font=font2,
    corner_radius=20,
    values=get_versions(),
    variable=version_var,
    width=WIDGET_WIDTH
)
version_menu.place(relx=0.5, y=312, anchor="center")

playbtn = ctk.CTkButton(
    frame1,
    text="Oyna",
    fg_color="#087B08",
    corner_radius=300,
    font=font1,
    command=launch_minecraft,
    width=WIDGET_WIDTH
)
playbtn.place(relx=0.5, y=368, anchor="center")

extbtn = ctk.CTkButton(
    frame1,
    text="Çıkış",
    fg_color="#087B08",
    corner_radius=300,
    font=font1,
    command=ext,
    width=WIDGET_WIDTH
)
extbtn.place(relx=0.5, y=430, anchor="center")

root.mainloop()
