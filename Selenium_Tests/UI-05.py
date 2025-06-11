from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_ui_05_case_sensitivity():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)  
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    def search_city(city_name, screenshot_name):
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
        search_box.clear()
        search_box.send_keys(city_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        try:
            result = driver.find_element(By.XPATH, "//ul[@class='search-dropdown-menu']/li[1]")
            result_text = result.text.strip()
            driver.save_screenshot(screenshot_name)  # Arama sonucunun ekran görüntüsünü al
            result.click()
            time.sleep(2)
            return result_text
        except Exception as e:
            driver.save_screenshot(screenshot_name)  # Hata olsa bile ekran alınmalı
            print(f"Hata: {e}")
            return None

    # 1. Arama: "london"
    result_london = search_city("london", "ui05_london_sonucu.png")

    # Sayfayı yenile
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    # 2. Arama: "London"
    result_London = search_city("London", "ui05_London2_sonucu.png")

    # Karşılaştırma
    if result_london == result_London:
        print("✅ UI-05: 'london' ve 'London' aynı sonucu verdi.")
    else:
        print("❌ UI-05: Büyük-küçük harf duyarlılığı var. Sonuçlar farklı.")
        print(f"   - london sonucu: {result_london}")
        print(f"   - London sonucu: {result_London}")

    driver.quit()

# Testi çalıştır
test_ui_05_case_sensitivity()
