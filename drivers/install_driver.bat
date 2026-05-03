@echo off
echo Sürücü kurulumu baslatiliyor...
msiexec /i "%~dp0UsbDk_1.0.22_x64.msi" /quiet /norestart
echo Sürücü kurulumu basariyla tamamlandi.
exit /b 0
