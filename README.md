# Hex Launcher - Minecraft

Hex Launcher, Java ile geliştirilmiş açık kaynaklı bir Minecraft başlatıcısıdır. Basit ve özelleştirilebilir yapısıyla, kullanıcıların Minecraft'ı hızlı ve kolay bir şekilde başlatmasına olanak tanır.

---

Hex Launcher is an open-source Minecraft launcher developed in Java. With a simple and customizable structure, it allows users to launch Minecraft quickly and easily.

---

## Özellikler | Features

- Java tabanlı Minecraft başlatıcı  
- Hafif ve hızlı arayüz  
- Sunucu bağlantısı desteği  
- Otomatik sürüm yönetimi  
- Açık kaynak ve özelleştirilebilir yapı

---

- Java-based Minecraft launcher  
- Lightweight and fast UI  
- Server connection support  
- Automatic version management  
- Open-source and customizable

---

## Ekran Görüntüleri | Screenshots

> Görselleri `/screenshots` klasörüne ekleyebilir veya buraya bağlantı verebilirsiniz.  
> You can add images in the `/screenshots` folder or link them here.

---

## Gereksinimler | Requirements

- Java 8 veya üzeri  
- İnternet bağlantısı  
- Minecraft hesap bilgisi (orijinal hesap)

---

- Java 8 or higher  
- Internet connection  
- Minecraft account (official account)

---

## Kurulum | Installation

1. Reposu klonlayın:  
    ```bash
    git clone https://github.com/nat-heo/Hex_Launcher_Minecraft.git
    ```

2. Bir Java IDE’si ile açın (örneğin IntelliJ IDEA, Eclipse).  
3. Gerekli bağımlılıkları yükleyin.  
4. `Main` sınıfını çalıştırarak başlatıcıyı başlatın.

---

1. Clone the repository:  
    ```bash
    git clone https://github.com/nat-heo/Hex_Launcher_Minecraft.git
    ```

2. Open it with a Java IDE (e.g., IntelliJ IDEA, Eclipse).  
3. Install required dependencies.  
4. Run the `Main` class to launch the application.

---

## Derleme | Build

```bash
javac -d out src/**/*.java
jar cfe HexLauncher.jar Main -C out .
```

## Yasal Uyarı

Bu proje Mojang Studios veya Microsoft ile hiçbir şekilde ilişkili değildir.
Minecraft, Mojang Studios'a ait tescilli bir ticari markadır.

Bu başlatıcı yalnızca eğitim ve deneysel kullanım amacıyla geliştirilmiştir.
Resmî Minecraft başlatıcısı yerine geçmez ve Mojang/Microsoft tarafından desteklenmemektedir.

Proje kapsamında Mojang’a ait herhangi bir oyun dosyası dağıtılmamaktadır.
Launcher, yalnızca sürüm başlatıcı işlevi görür ve tüm dosyalar minecraft_launcher_lib adlı açık kaynak kütüphane aracılığıyla Mojang sunucularından yasal olarak edinilir.

Bu başlatıcı korsan/crack kullanımı desteklemez.
Launcher'ı indiren kullanıcılar, tüm yasal sorumlulukların kendilerine ait olduğunu kabul eder.

## Legal Disclaimer

This project is in no way affiliated with Mojang Studios or Microsoft.
Minecraft is a registered trademark of Mojang Studios.

This launcher was developed for educational and experimental use only.
It is not a replacement for the official Minecraft launcher and is not endorsed by Mojang/Microsoft.

No Mojang game files are distributed as part of the project.
The launcher functions solely as a version launcher, and all files are obtained legally from Mojang servers via the open-source library minecraft_launcher_lib.

This launcher does not support pirated/cracked content.
By downloading the launcher, users agree to bear all legal responsibility.

