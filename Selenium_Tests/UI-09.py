from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def create_driver_mobil():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(360, 740)  # Mobil boyut
    return driver

def test_ui_09_mobil_gorunum():
    driver = create_driver_mobil()
    driver.get("https://openweathermap.org/")
    time.sleep(4)

    print("📱 UI-09: Mobil görünüm testine başlandı (360x740)")

    try:
        # Sayfa içeriğinden görsel ya da önemli yazı yüklenmiş mi kontrol et
        body_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        if any(kelime in body_text for kelime in ["weather", "openweather", "search city", "guide"]):
            print("✅ UI-09: Sayfa mobilde düzgün açıldı.")
        else:
            print("❌ UI-09: Sayfa mobilde eksik görünüyor.")

    except Exception as e:
        print("⚠️ UI-09: Test sırasında hata oluştu:", str(e))

    driver.save_screenshot("ui09_mobil_gorunum.png")
    driver.quit()

# Testi çalıştır
test_ui_09_mobil_gorunum()
