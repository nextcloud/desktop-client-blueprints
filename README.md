# Desktop Client blueprints for KDE Craft

:blue_book: We decided to use https://community.kde.org/Craft to get all binary dependencies of the desktop client.

## Windows

1. Follow the instructions in https://community.kde.org/Get_Involved/development/Windows
2. When asked for `where you want us to install Craft`, give the path to `C:\Craft64`

:warning: `C:\Craft64` is in case you are trying to create a installer using the scripts from https://github.com/nextcloud/client-building/:

:eyes: [nextcloud/client-building/blob/common.inc.bat line 14](https://github.com/nextcloud/client-building/blob/7501c37bf9f5322e880c0a8252c11bff11f774e2/common.inc.bat#L14)
```
if "%BUILD_ARCH%" == "Win64" ( set "CRAFT_PATH=c:\Craft64" )
```
Otherwise you can keep the install path suggested by Craft.

3. Add the blueprints from this repository:
```
$ craft --add-blueprint-repository [git]https://github.com/nextcloud/desktop-client-blueprints.git
```

4.

```
$ craft craft
```

5. Install all desktop client dependencies:
```
$ craft --install-deps nextcloud-client
```

6. Create the folder `resources` in the Craft install path.

7. Copy the following files from the Craft install path `bin` folder the `resources` folder:
- icudtl.dat
- qtwebengine_devtools_resources.pak
- qtwebengine_resources.pak
- qtwebengine_resources_100p.pak
- qtwebengine_resources_200p.pak

8. Now when building the desktop client, you can point cmake to the Craft install folder with:
```
-DCMAKE_PREFIX_PATH=%CRAFT_PATH%
```

:eyes: [nextcloud/client-building/single-build-desktop.bat line 142](https://github.com/nextcloud/client-building/blob/7501c37bf9f5322e880c0a8252c11bff11f774e2/single-build-desktop.bat#L142):
```
cmake "-G%CMAKE_GENERATOR%" .. -DMIRALL_VERSION_SUFFIX="%VERSION_SUFFIX%" -DWITH_CRASHREPORTER=OFF -DBUILD_UPDATER=%BUILD_UPDATER% -DBUILD_WIN_MSI=%BUILD_INSTALLER_MSI% -DMIRALL_VERSION_BUILD="%BUILD_DATE%" -DCMAKE_INSTALL_PREFIX="%MY_INSTALL_PATH%" -DCMAKE_BUILD_TYPE="%BUILD_TYPE%" -DCMAKE_PREFIX_PATH=%CRAFT_PATH% -DPng2Ico_EXECUTABLE="%Png2Ico_EXECUTABLE%" %CMAKE_EXTRA_FLAGS_DESKTOP%
```

## Linux
TBD.

## Mac OS
TBD.