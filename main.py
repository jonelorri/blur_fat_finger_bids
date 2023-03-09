from bs4 import BeautifulSoup
import time
import datetime
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

TOKEN = "<< YOUR TELEBOT TOKEN >>"
chat_id = "<< YOUR CHAT_ID >>"
bot = telebot.TeleBot(TOKEN)
chrome_options = ChromeOptions()
chrome_options.add_extension('./crx/MetaMask.crx')
driver = webdriver.Chrome('./driver/chromedriver', options=chrome_options)
lista = []
i = 0

driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase')
time.sleep(1)
frase = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input").send_keys("broken praise marble dynamic trim dog dignity abuse time bundle ask veteran")
frase2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input").send_keys("Borracho4.0")
frase3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input").send_keys("Borracho4.0")
time.sleep(2)
boton1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[7]/div").click()
time.sleep(2)
boton2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/button").click()
time.sleep(2)
boton3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button").click()
time.sleep(2)
driver.get('https://blur.io')

#* MANUAL LOGIN

time.sleep(30)

while (1):
    try:
        bid = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]").text
        if (float(bid) > 1.0):
            bot.send_message(chat_id, "ALERT BID " + bid + " MurakamiFlowers")
        time.sleep(10)
    except:
        print("Error")