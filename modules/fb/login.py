from modules.cookie import cookie
from selenium import webdriver
import os, time

FB_PAGE = "https://www.facebook.com/"

chrome = webdriver.Chrome()

'''''''''''
    Login módulo
    Este módulo sempre retornará um driver configurado
    com cookies setados para uso dos demais módulos em 
    determinadas páginas do FB
'''''''''''

def login(conta):
    try:
        # se um arquivo de cookie exisir carregue-o
        # e seta os cookies no driver
        os.path.isfile(cookie.get_file(conta['email']))
        cookie.load_cookies(chrome, conta['email'], FB_PAGE)
        chrome.get(FB_PAGE)
        return chrome
    except FileNotFoundError :
        # se não existir entra na página e gere o cookie
        return enter_in_page(chrome, conta)

def enter_in_page(driver, conta):    
    # faz o login
    driver.get(FB_PAGE)
    cookie.save_cookies(driver, conta['email'])
    driver.find_element_by_xpath("//input[@id='email']").send_keys(conta['email'])
    driver.find_element_by_xpath("//input[@id='pass']").send_keys(conta['senha'])
    driver.find_element_by_id("loginbutton").click()
    time.sleep(2)
    cookie.save_cookies(driver, conta['email'])
    return chrome