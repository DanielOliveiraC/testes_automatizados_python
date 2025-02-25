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


def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # 🔹 1. Fazer login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # 🔹 2. Adicionar um item ao carrinho
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    # 🔹 3. Verificar se o número no ícone do carrinho é 1
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1", "Erro: O carrinho não foi atualizado corretamente"

    # 🔹 4. Ir até o carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 🔹 5. Verificar se o item está na lista de produtos no carrinho
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item == "Sauce Labs Backpack", "Erro: O item não está no carrinho"

    print("-> Teste passou: Produto foi adicionado corretamente ao carrinho!")