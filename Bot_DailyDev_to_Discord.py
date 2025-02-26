
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# teste merge dev-test to dev

WEBHOOK_URL = "" #SELECIONE A URL DO SEU WEBHOOK

def send_message(content):
    payload = {"content": content}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204: # alterado
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar: {response.status_code}, {response.text}") 

send_message("Olá, este é um teste do Webhook!")

def get_first_news_link():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver_path = "chromedriver-win64/chromedriver.exe"  
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)


    try:
        driver.get("https://app.daily.dev/posts")
        time.sleep(5)  

        articles = driver.find_elements(By.CSS_SELECTOR, "article a")
        news_links = [article.get_attribute("href") for article in articles[:10]] 
        
        print("Links encontrados:")
        for link in news_links:
            send_message(link)
        
        return news_links

    except Exception as e:
        print(f"Erro ao pegar link: {e}")
        return None

    finally:
        driver.quit()




news_link = get_first_news_link()
