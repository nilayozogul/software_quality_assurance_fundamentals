from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time

API_KEY = "0cafdadef0eff3ba08abe8b0c3608581" 

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

def get_ui_temperature(driver):
    driver.get("https://openweathermap.org/city/745044")
    time.sleep(4)

    try:
        temp_text = driver.find_element(By.CLASS_NAME, "current-temp").text
        temp_value = int(temp_text.strip().replace("°C", "").replace("°", ""))
        return temp_value
    except Exception as e:
        print("❌ UI sıcaklık alınamadı:", str(e))
        return None

def get_api_temperature():
    url = f"https://api.openweathermap.org/data/2.5/weather?id=745044&units=metric&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return round(data["main"]["temp"])
    except Exception as e:
        print("❌ API sıcaklık alınamadı:", str(e))
        return None

def test_ui_10_ui_api_karsilastirma():
    driver = create_driver()

    print("📊 UI-10: UI ve API verisi karşılaştırılıyor...")

    ui_temp = get_ui_temperature(driver)
    driver.save_screenshot("ui10_ui_api_karsilastirma.png")
    driver.quit()

    api_temp = get_api_temperature()

    if ui_temp is None or api_temp is None:
        print("⚠️ UI veya API sıcaklık değeri alınamadı.")
        return

    fark = abs(ui_temp - api_temp)
    print(f"🌡️ UI sıcaklık: {ui_temp}°C")
    print(f"📡 API sıcaklık: {api_temp}°C")
    print(f"🔍 Fark: {fark}°C")

    if fark <= 1:
        print("✅ UI-10: UI ve API verileri uyumlu.")
    else:
        print("❌ UI-10: UI ve API verileri arasında fark var.")

# Testi çalıştır
test_ui_10_ui_api_karsilastirma()
