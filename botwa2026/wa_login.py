Import random, time, os, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SESSION_FOLDER = os.path.join(os.getcwd(), "chrome_session")

def setup_driver():
    options = Options()
    options.add_argument(f"--user-data-dir={SESSION_FOLDER}")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)
    return driver

def login_dengan_nomor():
    print("\n--- PROSES LINKING NOMOR ---")
    driver = setup_driver()
    try:
        driver.get("https://web.whatsapp.com")
        wait = WebDriverWait(driver, 100)
        print("[*] Memuat WhatsApp Web...")
        time.sleep(25)
        
        target_xpath = "//*[contains(text(), 'Link with phone number') or contains(text(), 'Tautkan dengan nomor telepon')]"
        link_btn = wait.until(EC.presence_of_element_located((By.XPATH, target_xpath)))
        driver.execute_script("arguments[0].click();", link_btn)
        time.sleep(5)

        # Otomatis coba pilih Indonesia
        try:
            dropdown = driver.find_element(By.XPATH, "//div[@role='button'][@aria-haspopup='listbox']")
            dropdown.click()
            time.sleep(2)
            driver.switch_to.active_element.send_keys("Indonesia")
            driver.switch_to.active_element.send_keys(Keys.ENTER)
        except: pass

        nomor_hp = input("[?] Masukkan nomor WA (contoh: 6285656067725): ")
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text'][@dir='ltr']")))
        input_box.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        input_box.send_keys(nomor_hp + Keys.ENTER)
        
        print("[*] Menunggu kode pairing... Cek terminal ini dalam 20 detik.")
        time.sleep(20)
        
        kode_elements = driver.find_elements(By.XPATH, "//div[@aria-details='link-device-qrcode-error-description']//span")
        pairing_code = "".join([e.text for e in kode_elements if e.text.isalnum()])
        
        if pairing_code:
            print(f"\n>>> KODE ANDA: {pairing_code} <<<\n")
        else:
            driver.save_screenshot("debug_kode.png")
            print("[!] Kode tidak terbaca teks, cek debug_kode.png")
            
        input("Tekan Enter jika sudah selesai...")
    finally:
        driver.quit()

def tampilkan_menu():
    print("\n" + "="*30)
    print("  WA BOT MENU")
    print("="*30)
    print("1. Login (Link Code)")
    print("2. Keluar")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        login_dengan_nomor()

# BAGIAN PALING PENTING (PASTIKAN ADA DI BARIS PALING BAWAH)
if __name__ == "__main__":
    tampilkan_menu()
