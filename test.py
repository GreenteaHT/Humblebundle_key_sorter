import selenium.webdriver

webdriver.driver.find_element(By.CSS_SELECTOR, '#root > div.charcoal-token > div > div.sc-12xjnzy-0.dIGjtZ > div.sc-oh3a2p-0.lfaZnj > div > div.sc-oh3a2p-4.gHKmNu > a.sc-oh3a2p-3.dfWiNJ').click()

username = "아이디"
password = "비밀번호"

put_id = driver.find_element(By.CSS_SELECTOR, '#app-mount-point > div > div.sc-fvq2qx-4.idshsY > div.sc-2oz7me-0.fJsfdC > div.sc-fg9pwe-2.gZSHsw > div > div > div > form > fieldset.sc-bn9ph6-0.kJkgq.sc-2o1uwj-3.diUbPW > label > input')
put_id.send_keys(username)

put_pass = driver.find_element(By.CSS_SELECTOR, '#app-mount-point > div > div.sc-fvq2qx-4.idshsY > div.sc-2oz7me-0.fJsfdC > div.sc-fg9pwe-2.gZSHsw > div > div > div > form > fieldset.sc-bn9ph6-0.kJkgq.sc-2o1uwj-4.hZIeVE > label > input')
put_pass.send_keys(password)

driver.find_element(By.CSS_SELECTOR, '#app-mount-point > div > div.sc-fvq2qx-4.idshsY > div.sc-2oz7me-0.fJsfdC > div.sc-fg9pwe-2.gZSHsw > div > div > div > form > button').click()

def set_chrome_driver():
    options = Options()
    options.add_argument("user-data-dir=C:/Users/goawa/AppData/Local/Google/Chrome/User Data")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    logging.basicConfig(level=logging.ERROR)

    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = set_chrome_driver()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")