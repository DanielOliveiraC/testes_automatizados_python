import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configuração do ChromeDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/local/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_form_submission(driver):
    """Testa o envio do formulário no site GlobalSQA."""
    driver.get("https://www.globalsqa.com/samplepagetest/")

    # 🔹 1. Preencher os campos do formulário
    driver.find_element(By.XPATH, '//*[@id="g2599-name"]').send_keys("Daniel Oliveira")
    driver.find_element(By.XPATH, '//*[@id="g2599-email"]').send_keys("daniel@email.com")
    driver.find_element(By.XPATH, '//*[@id="contact-form-comment-g2599-comment"]').send_keys("Este é um teste de envio de formulário.")

    # 🔹 2. Clicar no botão "Submit"
    driver.find_element(By.CLASS_NAME, "pushbutton-wide").click()

    # 🔹 3. Verificar se a mensagem de sucesso aparece
    success_message = driver.find_element(By.XPATH, '//*[@id="contact-form-2599"]/h3').text
    assert "Message Sent (go back)" in success_message, "Erro: Mensagem de sucesso não encontrada"

    print("-> Teste Bem Sucedido: Formulário enviado com sucesso!")

