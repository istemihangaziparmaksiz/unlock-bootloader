import sys
import os

# PyInstaller ile paketlendiğinde mtkclient'ı çalıştırabilmek için argüman yakalayıcı
if len(sys.argv) > 1 and sys.argv[1] == "--run-mtk":
    sys.argv.pop(1)
    try:
        from mtkclient import mtk
        sys.exit(mtk.main())
    except ImportError as e:
        print(f"Error importing mtkclient: {e}")
        sys.exit(1)

import ctypes
import threading
import subprocess
import customtkinter as ctk
from mtk_runner import MTKRunner

# Yönetici hakları kontrolü
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bootloader Unlocker by #ISTMHN")
        self.geometry("900x550")
        self.resizable(False, False)

        # Set window icon if available
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_path, "app_icon.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        # 1x2 Grid 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # Sol Panel (Kontrol Merkezi)
        self.left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.left_frame, text="Bootloader Unlocker by #ISTMHN", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))

        self.btn_driver = ctk.CTkButton(self.left_frame, text="Sürücü Kur", height=40, command=self.install_drivers)
        self.btn_driver.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_unlock = ctk.CTkButton(self.left_frame, text="Bootloader Kilidini Aç", height=40, fg_color="green", hover_color="darkgreen", command=self.unlock_bootloader)
        self.btn_unlock.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_lock = ctk.CTkButton(self.left_frame, text="Bootloader Kilidini Kapat", height=40, fg_color="#C62828", hover_color="#8E0000", command=self.lock_bootloader)
        self.btn_lock.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # Sağ Panel (Log Ekranı)
        self.right_frame = ctk.CTkFrame(self, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.log_box = ctk.CTkTextbox(self.right_frame, font=ctk.CTkFont(family="Consolas", size=13))
        self.log_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.log_box.configure(state="disabled")

        self.btn_stop = ctk.CTkButton(self.right_frame, text="İŞLEMİ DURDUR", fg_color="red", hover_color="darkred", height=50, font=ctk.CTkFont(weight="bold", size=15), command=self.stop_process)
        self.btn_stop.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))

        self.mtk_runner = MTKRunner(self.append_log, self.on_process_finish)

        self.append_log("Yazılım başlatıldı. Lütfen işlem seçin.")
        self.append_log("Yönetici yetkileri doğrulandı. Sistem hazır.\n")

    def append_log(self, text, error=False):
        # Tkinter thread-safe işlemi
        self.after(0, self._update_log_box, text, error)

    def _update_log_box(self, text, error):
        self.log_box.configure(state="normal")
        
        start_index = self.log_box.index("insert")
        self.log_box.insert("end", text + "\n")
        end_index = self.log_box.index("insert")

        if error:
            self.log_box.tag_add("error", start_index, end_index)
            self.log_box.tag_config("error", foreground="red")
        
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def toggle_buttons(self, state):
        mode = "normal" if state else "disabled"
        self.btn_driver.configure(state=mode)
        self.btn_unlock.configure(state=mode)
        self.btn_lock.configure(state=mode)

    def on_process_finish(self):
        self.toggle_buttons(True)
        self.append_log("\n--- İşlem Sonlandırıldı ---")

    def install_drivers(self):
        self.append_log("Sürücü kurulumu başlatılıyor...")
        
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        driver_script = os.path.join(base_path, "drivers", "install_driver.bat")
        
        if os.path.exists(driver_script):
            def run_driver():
                try:
                    subprocess.call([driver_script], shell=True)
                    self.append_log("Sürücü kurulum scripti tamamlandı.")
                except Exception as e:
                    self.append_log(f"[HATA] Sürücü kurulumunda hata: {str(e)}", error=True)
            threading.Thread(target=run_driver, daemon=True).start()
        else:
            self.append_log(f"[HATA] Sürücü yükleyici bulunamadı: {driver_script}", error=True)

    def unlock_bootloader(self):
        self.append_log("\n--- Bootloader Açma İşlemi ---")
        self.append_log("Cihaz bekleniyor... Lütfen cihazı kapalıyken Ses Açma + Ses Kısma tuşlarına basılı tutarak USB'ye bağlayın.")
        self.toggle_buttons(False)
        self.mtk_runner.start("da seccfg unlock")

    def lock_bootloader(self):
        self.append_log("\n--- Bootloader Kapatma İşlemi ---")
        self.append_log("Cihaz bekleniyor... Lütfen cihazı kapalıyken Ses Açma + Ses Kısma tuşlarına basılı tutarak USB'ye bağlayın.")
        self.toggle_buttons(False)
        self.mtk_runner.start("da seccfg lock")

    def stop_process(self):
        self.mtk_runner.stop()
        self.toggle_buttons(True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
