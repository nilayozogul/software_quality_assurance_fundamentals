from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Konum ve bildirim izinlerini devre dışı bırakan sürücü oluşturucu
def create_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2,        # Konum izni engellendi
        "profile.default_content_setting_values.notifications": 2       # Bildirim izni engellendi
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver

def test_ui_06_gecersiz_sehir():
    driver = create_driver()
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    try:
        # Arama kutusuna geçersiz şehir gir
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
        search_box.clear()
        search_box.send_keys("xyzabc")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Arama sonucu listesi varsa, içinde "not found" mesajı olup olmadığına bak
        try:
            result_menu = driver.find_element(By.CLASS_NAME, "search-dropdown-menu")
            result_text = result_menu.text.strip().lower()
            if "not found" in result_text:
                print("✅ UI-06: 'City not found' mesajı görünüyor.")
            elif result_text == "":
                print("✅ UI-06: Arama sonucu listesi boş. Beklenen durum.")
            else:
                print("❌ UI-06: Beklenmeyen arama sonucu gösterildi.")
                print("Görünen içerik:", result_text)
        except:
            print("✅ UI-06: Arama sonucu listesi hiç oluşmadı. Beklenen durum.")

    except Exception as e:
        print("❌ UI-06: Test sırasında hata oluştu:", str(e))

    driver.save_screenshot("ui06_gecersiz_sehir.png")
    driver.quit()

# Testi çalıştır
test_ui_06_gecersiz_sehir()
