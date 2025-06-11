from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver

def test_ui_08_end_to_end_akis():
    driver = create_driver()
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    try:
        # 1. Şehir arama
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
        search_box.clear()
        search_box.send_keys("Berlin")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # 2. İlk sonucu seç
        result = driver.find_element(By.XPATH, "//ul[@class='search-dropdown-menu']/li[1]/span[contains(text(),'Berlin, DE')]")
        result.click()
        time.sleep(4)

        # 3. Sayfa içerik kontrol
        content = driver.find_element(By.CLASS_NAME, "current-container.mobile-padding").text.lower()

        if "berlin" in content and "°c" in content:
            print("✅ UI-08: End-to-end akış başarılı. Şehir ve sıcaklık gösterildi.")
        else:
            print("❌ UI-08: Şehir ya da sıcaklık görünmüyor.")
            print("İçerik:", content)

    except Exception as e:
        print("❌ UI-08: Test sırasında hata oluştu:", str(e))

    driver.save_screenshot("ui08_end_to_end.png")
    driver.quit()

# Testi çalıştır
test_ui_08_end_to_end_akis()
