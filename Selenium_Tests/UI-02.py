from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # Uyarıları bastır
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver

def test_ui_02_sehir_arama():
    driver = create_driver()
    driver.get("https://openweathermap.org/")
    time.sleep(3)

    try:
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
        search_box.send_keys("Paris")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        result = driver.find_element(By.XPATH, "//ul[@class='search-dropdown-menu']/li[1]/span[text()='Paris, FR ']")
        result.click()
        time.sleep(3)

        city_name = driver.find_element(By.CLASS_NAME, "current-container.mobile-padding").text
        if "Paris" in city_name:
            print("✅ UI-02: Paris başarıyla yüklendi.")
        else:
            print("❌ UI-02: Paris bilgisi bulunamadı.")
    except:
        print("❌ UI-02: Arama ya da yükleme başarısız.")

    driver.save_screenshot("ui02_paris_arama.png")
    driver.quit()

test_ui_02_sehir_arama()
