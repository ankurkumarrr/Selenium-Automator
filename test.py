from selenium import webdriver


login = "test"
chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars") 
chromeOptions.add_argument("--headless") 
chromeOptions.add_argument(r"user-data-dir=.\cookies\\" + login) 
b = webdriver.Chrome(chrome_options=chromeOptions) 
b.get("https://google.com/") 
b.quit() 