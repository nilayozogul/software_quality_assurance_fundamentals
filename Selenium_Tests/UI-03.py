from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Sessiz ve konumsuz Chrome başlatıcı
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

def test_ui_03_sayfa_basligi():
    driver = create_driver()
    driver.get("https://openweathermap.org/city/2643743")
    time.sleep(3)

    # Sayfa başlığını kontrol et
    title = driver.title
    print("Sayfa Başlığı:", title)

    if "weather" in title.lower():
        print("✅ UI-03: Sayfa başlığı doğru.")
    else:
        print("❌ UI-03: Sayfa başlığı 'Weather' içermiyor.")

    driver.save_screenshot("ui03_baslik_kontrol.png")
    driver.quit()

# Testi çalıştır
test_ui_03_sayfa_basligi()
