'''#scraping de dados com python,biblioteca selenium(serve para extrair dados /raspagem )
# Importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep

# Abrindo o navegador para começar a automacação, utilizando o webdriver
chrome = webdriver.Chrome()
# Abrindo uma url
chrome.get('https://books.toscrape.com/')
sleep(1)

#Buscando o elemento do titulo do livro utilizando o xpath
titulo = chrome.find_element(By.XPATH, '/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a')
#Clicando no titulo do livro
titulo.click()
sleep(1)

#Buscando o elemento do titulo do livro dentro da pagina do livro utilizando o xpath
titulo_especifico = chrome.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1')
#Imprimindo conteudo que esta entre as tags do html
print(titulo_especifico.text)

#Voltando a pagina do chrome para a anterior
chrome.back()

sleep(10)

'''


'''
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

'''


#extração de informçoes de forma dinamica
#intuito é entrar no site,clicar no nome do livro pegar
#NOME,VALOR E SE TEM EM ESTOQUE

 #importar a biblioteca selenium 
from selenium import webdriver           
from selenium.webdriver.common.by import By

#importando a biblioteca time para adicionar uma pausa no codigo
from time import sleep

#Para abrir o navegador ,o webdriver serve para escolher qual navegador deseja usar
chrome = webdriver.Chrome()
chrome.get('https://books.toscrape.com/')              #o GET serve para abrir o site

livros = chrome.find_elements(By.XPATH, '//article[@class="product_pod"]')

for livro in livros:
    titulo = livro.find_element (By.XPATH, './h3/a')
    titulo.click()
    sleep(5)

titulo = chrome.find_element(By.TAG_NAME, )
preco = chrome.find_element(By.XPATH, '//article[@class="price_color"]')
estoque = chrome.find_element(By.XPATH, '//article[@class="instock availability"]')



print(titulo.text)
print(preco.text)
print(estoque.text.



sleep(5)