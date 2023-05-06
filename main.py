import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Account Info
from selenium.webdriver.common.by import By

USER_ID = "sh0946@naver.com"
USER_PASSWORD = "hk419spas"

# URL
URL = "https://www.humblebundle.com/"
URL_KEY = "https://www.humblebundle.com/home/keys"
URL_LOGIN = "https://www.humblebundle.com/login"

### Log-in process
session = requests.session()

login_info = {
    "access_token": "",
    "access_token_provider_id": "",
    "goto": "",
    "password": USER_PASSWORD,
    "qs": "",
    "username": USER_ID
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
# 헤더 업데이트
session.headers.update(headers)


# POST로 데이터를 보냄
# res = session.post(URL_LOGIN, data=login_info, allow_redirects=True)
# res.raise_for_status()


def selenium_login():  # selenium 로그인 과정 + 쿠키 받아오기
    driver = webdriver.Chrome()
    driver.get(URL_LOGIN)

    ## 로그인
    # 로그인 아이디 입력
    put_id = driver.find_element(By.CSS_SELECTOR,
                                 "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section.primary-section > form > div:nth-child(1) > div.email-field.input-field-container > input")
    put_id.send_keys(USER_ID)

    # 로그인 패스워드 입력
    put_password = driver.find_element(By.CSS_SELECTOR,
                                       "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section.primary-section > form > div:nth-child(2) > div.password-field.input-field-container > input")
    put_password.send_keys(USER_PASSWORD)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section.primary-section > form > button")
    login_button.click()

    ## 인증
    # 인증코드 입력 창이 나타날 때까지 대기
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                   "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section > form > div.js-field-wrapper.field-wrapper > div.code-field.input-field-container > input")))

    # 인증코드 입력
    print("인증 코드를 입력해주세요: ")
    verify_code = input()
    put_code = driver.find_element(By.CSS_SELECTOR,
                                   "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section > form > div.js-field-wrapper.field-wrapper > div.code-field.input-field-container > input")
    put_code.send_keys(verify_code)

    # 인증 버튼 클릭
    verify_button = driver.find_element(By.CSS_SELECTOR,
                                        "body > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > div > div > div > section > form > button")
    verify_button.click()

    # 페이지 갱신 대기
    driver.implicitly_wait(5)

    # 쿠키 얻어오기
    _cookies = driver.get_cookies()
    cookie_dict = {}
    for cookie in _cookies:
        cookie_dict[cookie['name']] = cookie['value']

    print(cookie_dict)
    # driver.quit()

# keys = soup.find('table', attrs={"class": "unredeemed-keys-table"})
# key = keys.find_all('td')
#
# print(keys)

# headers = {"User-Agent": "[WhatIsMyBrowser에 나타난 나의 유저 정보]"}
# res = requests.get(url, headers=headers)
