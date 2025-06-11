from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_ui_04_bos_sehir_arama():
    driver = webdriver.Chrome()
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    try:
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
        search_box.send_keys("")  # boş gönderiyoruz
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Arama sonucu listesi gelmemeli
        try:
            result_menu = driver.find_element(By.CLASS_NAME, "search-dropdown-menu")
            if result_menu.is_displayed() and len(result_menu.text.strip()) > 0:
                print("❌ UI-04: Boş arama sonucu listesi gösterildi.")
            else:
                print("✅ UI-04: Boş aramada sonuç çıkmadı.")
        except:
            print("✅ UI-04: Arama sonucu listesi oluşmadı (beklenen).")

    except Exception as e:
        print("❌ UI-04: Test sırasında hata oluştu:", str(e))

    driver.save_screenshot("ui04_bos_arama.png")
    driver.quit()

test_ui_04_bos_sehir_arama()
