import subprocess
import threading
import sys
import os

class MTKRunner:
    def __init__(self, log_callback, finish_callback):
        self.process = None
        self.log_callback = log_callback
        self.finish_callback = finish_callback
        self.is_running = False

    def start(self, command):
        if self.is_running:
            return
        self.is_running = True
        
        def run_thread():
            cmd = [sys.executable, "--run-mtk"] + command.split()
            
            creation_flags = 0
            if os.name == 'nt':
                creation_flags = subprocess.CREATE_NO_WINDOW
                
            try:
                self.log_callback(f"İşlem başlatılıyor: mtk {command}")
                self.process = subprocess.Popen(
                    cmd, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT,
                    text=True,
                    creationflags=creation_flags,
                    bufsize=1,
                    universal_newlines=True
                )
                
                for line in self.process.stdout:
                    self._parse_and_log(line.strip())
                    
                self.process.wait()
                if self.process.returncode == 0:
                    self.log_callback("İşlem başarıyla tamamlandı.")
                else:
                    self.log_callback(f"[HATA] İşlem hata koduyla sonlandı: {self.process.returncode}", error=True)
                    
            except Exception as e:
                self.log_callback(f"[HATA] Beklenmeyen bir hata oluştu: {str(e)}", error=True)
            finally:
                self.is_running = False
                self.finish_callback()
                
        threading.Thread(target=run_thread, daemon=True).start()

    def stop(self):
        if self.process and self.is_running:
            self.log_callback("İŞLEMİ DURDUR komutu alındı. Süreç sonlandırılıyor...", error=True)
            try:
                if os.name == 'nt':
                    subprocess.call(['taskkill', '/F', '/T', '/PID', str(self.process.pid)], creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    self.process.terminate()
            except Exception as e:
                self.log_callback(f"[HATA] İşlem durdurulamadı: {str(e)}", error=True)
            self.is_running = False

    def _parse_and_log(self, line):
        if not line: return
        
        lower_line = line.lower()
        
        # User friendly translations
        if "port - device detected" in lower_line or "preloader - cpu" in lower_line:
            self.log_callback("Cihaz algılandı, handshake başarılı.")
        elif "waiting for device" in lower_line or "wait for device" in lower_line:
            self.log_callback("Cihaz bekleniyor... Lütfen cihazı kapalı konumda Ses Açma + Ses Kısma tuşlarına basılı tutarak bağlayın.")
        elif "seccfg unlocked" in lower_line or ("unlock" in lower_line and "success" in lower_line):
            self.log_callback("Bootloader kilidi başarıyla açıldı. Cihaz yeniden başlatılıyor...")
        elif "seccfg locked" in lower_line or ("lock" in lower_line and "success" in lower_line):
            self.log_callback("Bootloader kilidi başarıyla kapatıldı. Cihaz yeniden başlatılıyor...")
        elif "error" in lower_line or "failed" in lower_line or "exception" in lower_line:
            self.log_callback(f"[HATA] {line}", error=True)
        else:
            self.log_callback(f"> {line}")
