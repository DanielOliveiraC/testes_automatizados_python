import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configuração do ChromeDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Executa sem abrir o navegador (remova para ver o navegador)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/local/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver  # Retorna o driver para os testes
    driver.quit()  # Fecha o navegador após os testes

def test_login(driver):
    """Testa o login no site."""
    driver.get("https://the-internet.herokuapp.com/login")  # 🔹 Substitua pelo URL correto

    # Preencher login e senha
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

    # Verificar se o login foi bem-sucedido
    success_message = driver.find_element(By.XPATH, '//*[@id="flash"]').text
    assert "You logged into a secure area!" in success_message 
    print("-> Login realizado com sucesso!")
