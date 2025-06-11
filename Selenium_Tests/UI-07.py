from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

def test_ui_07_dil_secimi_turkce():
    driver = create_driver()
    driver.get("https://openweathermap.org/city/745044?lang=tr")  # İstanbul için Türkçe sayfa
    time.sleep(4)

    print("📄 UI-07: İstanbul şehir sayfası Türkçe olarak açıldı mı?")

    try:
        # Tüm içeriği al
        container = driver.find_element(By.CLASS_NAME, "current-container.mobile-padding").text.lower()

        # Türkçe kelimelerden biri var mı kontrol et
        turkce_kelimeler = ["açık", "kapalı", "bulutlu", "yağmur", "parçalı", "sis", "gök gürültülü"]

        if any(kelime in container for kelime in turkce_kelimeler):
            print("✅ UI-07: Açıklama Türkçe görünüyor.")
            test_durumu = "Başarılı"
        else:
            print("❌ UI-07: Açıklama Türkçe değil.")
            test_durumu = "Başarısız"

        print("📋 Görünen açıklama:\n", container)

    except Exception as e:
        print("⚠️ UI-07: Element bulunamadı ama test hata vermedi.")
        test_durumu = "Element Yok"

    driver.save_screenshot("ui07_dil_secimi_turkce.png")
    driver.quit()

    print("🧾 Test Durumu:", test_durumu)

# Testi çalıştır
test_ui_07_dil_secimi_turkce()
