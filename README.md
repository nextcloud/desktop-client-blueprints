# 🖥️ Nextcloud Desktop Client blueprints

:blue_book: We decided to use [KDE Craft](https://community.kde.org/Craft) to get all binary dependencies of the [Nextcloud files desktop client](https://github.com/nextcloud/desktop).

## System requirements

- Windows 10 or Windows 11
- The desktop client code
- Python 3
- PowerShell
- KDE Craft
- Microsoft Visual Studio 2022
- Inkscape
- A Nextcloud server

> [!TIP]
> We highly recommend [Nextcloud development environment on Docker Compose](https://juliushaertl.github.io/nextcloud-docker-dev/) for testing/bug fixing/development.<br>
> ▶️ https://juliushaertl.github.io/nextcloud-docker-dev/

### Set up Windows 10 or Windows 11

- If you don't have Windows as your main system, you could try to run it as a virtual machine:
  https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/

### Set up Microsoft Visual Studio

1. Open the `Visual Studio Installer`.
2. Click on `Modify`:

![vs-studio-2022](https://github.com/user-attachments/assets/6df5e7b9-d1e0-43a9-897e-98f4c37726a9)

3. Select `Desktop development with C++`:

![vs-studio-dev](https://github.com/user-attachments/assets/6fef8b8d-d8e3-4ced-b23d-8818f9813c5f)

### Install Inkscape

- Install the latest version of [Inkscape](https://inkscape.org/release).
 
### Set up KDE Craft

1. You will need to install Python 3: https://www.python.org/downloads/windows/
2. Set up KDE Craft as instructed in [Get Involved/development/Windows - KDE Community Wiki](https://community.kde.org/Get_Involved/development/Windows).
3. Use the default options, including Qt6 (since desktop 3.14, we are using Qt 6).

> [!IMPORTANT]
> `C:\CraftRoot` is the path used by default by `KDE Craft`. <br>
> When you are setting it up <b>you may choose a different folder</b>: you will need to<br>
⚠️ change from `C:\CraftRoot` to the path you picked ⚠️ in the next steps listed here.

## How to use the desktop client blueprints

1. After following the instructions in [Get Involved/development/Windows - KDE Community Wiki](https://community.kde.org/Get_Involved/development/Windows).
2. Open `PowerShell`.
3. Run `craftenv.ps1` as described in the instructions above:
```
C:\CraftRoot\craft\craftenv.ps1
```
4. Add the blueprints from this repository:
```
craft --add-blueprint-repository https://github.com/nextcloud/desktop-client-blueprints.git
```
5.
```
$ craft craft
```
6. Install all desktop client dependencies:
```
craft --install-deps nextcloud-client
```

### Compiling the desktop client

1. Make sure your environment variable `%PATH%` has no conflicting information to the environment you will use to compile the client. For instance, if you have installed `OpenSSL` previously and have added it to `%PATH%`, the `OpenSSL` installed might be a different version than what was installed via `KDE Craft`.
2. To use the tools installed with Visual Studio, you need the following in your %PATH%:
![path](https://github.com/user-attachments/assets/ce99a488-22d9-4cf5-8b55-d6ae9e683845)
3. Open the `Command Prompt` (cmd.exe).

> [!IMPORTANT]
> The next steps has only been tested and proven to work when using `Command Prompt`.

4. Run:
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```
> [!TIP]
> Alternatively you can use the tools installed with `KDE Craft` by adding them to `%PATH%` in your current session:
> ```
> set "PATH=C:\CraftRoot\bin;C:\CraftRoot\dev-utils\bin;%PATH%"
> ```
> This will result in using the `cmake` version downloaded with `KDE Craft`.
5. Clone the desktop client repository.
```
git clone https://github.com/nextcloud/desktop.git
```
6. Create the build folder `<build-folder>`.
```
mkdir <build-folder>
```
7. Go into the build folder.
```
cd <build-folder>
```
8. Run cmake.
```
cmake ..\<desktop-cloned-repo> -G Ninja -DCMAKE_INSTALL_PREFIX=. -DCMAKE_PREFIX_PATH=C:\CraftRoot -DCMAKE_BUILD_TYPE=RelWithDebInfo
```
9. Compile the desktop client
```
cmake --build .
```

> [!NOTE]
> ❓ If you have questions about it, you may use the forums at https://help.nextcloud.com to ask them.<br>
> 🐛 If you find bugs with these steps, you may open a GH issue at https://github.com/nextcloud/desktop/issues.
