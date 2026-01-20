import random, time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SESSION_FOLDER = os.path.join(os.getcwd(), "chrome_session")

def load_pesan():
    if not os.path.exists("pesan.txt"): return ""
    with open("pesan.txt", "r", encoding="utf-8") as f:
        # Mengambil seluruh isi file sebagai satu pesan panjang
        return f.read().strip()

def setup_driver():
    options = Options()
    options.add_argument(f"--user-data-dir={SESSION_FOLDER}")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1366, 768)
    return driver

def mulai_kirim(mode):
    if not os.path.exists("nomor.txt"):
        print("[!] File nomor.txt tidak ditemukan!"); return
        
    nomor_list = [line.strip() for line in open("nomor.txt", "r") if line.strip()]
    pesan_full = load_pesan()
    
    if not nomor_list or not pesan_full:
        print("[!] Daftar nomor atau pesan kosong!"); return

    driver = setup_driver()
    wait = WebDriverWait(driver, 60)
    
    try:
        while True:
            print(f"\n[*] Memulai Mode: {mode}")
            for nomor in nomor_list:
                print(f"[*] Mengirim ke {nomor}...")
                driver.get(f"https://web.whatsapp.com/send?phone={nomor}&text={pesan_full}")
                
                try:
                    # Tunggu kotak chat muncul
                    chat_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")))
                    
                    # JEDA PENTING untuk pesan panjang agar ter-render sempurna
                    time.sleep(12) 
                    
                    # Kirim dengan Enter
                    chat_box.send_keys(Keys.ENTER)
                    
                    # Backup Klik Tombol Send
                    time.sleep(2)
                    try:
                        driver.find_element(By.XPATH, "//span[@data-icon='send']").click()
                    except: pass

                    print(f"--> [✔] Berhasil")
                except:
                    print(f"--> [X] Gagal (Timeout)")
                
                # Jeda antar nomor (30-50 detik)
                time.sleep(random.randint(30, 50))
            
            if mode == "Sekali Jalan": break
            print("\n[#] Putaran selesai. Istirahat 5 menit..."); time.sleep(300)
            
    finally:
        driver.quit()

if __name__ == "__main__":
    print("\n" + "="*30 + "\n   WA SENDER FINAL V2.3\n" + "="*30)
    print("1. Kirim Sekali Jalan\n2. Kirim Berulang (Looping)\n3. Keluar")
    p = input("Pilih menu (1-3): ")
    if p == "1": mulai_kirim("Sekali Jalan")
    elif p == "2": mulai_kirim("Looping")
