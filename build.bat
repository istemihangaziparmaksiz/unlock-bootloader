@echo off
echo Uygulama derleniyor... Lutfen bekleyin.

:: PyInstaller command to build the app
:: --noconsole hides the command prompt
:: --onefile packages everything into a single .exe
:: --add-data "drivers;drivers" includes the drivers folder in the build
:: --add-data "payloads;payloads" includes the payloads folder in the build

pyinstaller --noconfirm --onefile --windowed --icon=app_icon.ico --collect-all customtkinter --collect-all mtkclient --add-data "app_icon.ico;." --add-data "drivers;drivers" --add-data "payloads;payloads" --name "Bootloader_Unlocker by ISTMHN" main.py

echo.
echo Derleme tamamlandi. Ciktilar "dist" klasorundedir.
pause
