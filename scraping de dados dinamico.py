#extracao de informçoes de forma dinamica
from selenium import webdriver  
from selenium.webdriver.common.by import By

#importando biblioteca time para adicionar uma pausa no codigo
from time import sleep

#abrindo o navegador para comecar a automacao,usando o webdriver
chrome = webdriver.Chrome()
chrome.get('https://books.toscrape.com/')

sleep(1)          #pausa para abrir o site

livros = chrome.find_elements(By.XPATH, '//article[@class="product_pod"]')

for livro in livros:
    titulo = livro.find_element (By.XPATH, './h3/a')
    print(titulo.get_attribute('title'))

sleep(10)