from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver

def test_ui_01_sayfa_goruntulendi_mi():
    driver = create_driver()
    driver.get("https://openweathermap.org/city/2643743")
    time.sleep(3)

    try:
        sehir = driver.find_element(By.CLASS_NAME, "current-container.mobile-padding").text
        if "London" in sehir:
            print("✅ UI-01: London sayfası yüklendi.")
        else:
            print("❌ UI-01: Beklenen bilgi görünmüyor.")
    except:
        print("❌ UI-01: Sayfa elemanı bulunamadı.")

    driver.save_screenshot("ui01_sayfa_goruntusu.png")
    driver.quit()

test_ui_01_sayfa_goruntulendi_mi()
