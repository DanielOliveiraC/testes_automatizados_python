import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_add_and_remove_product(driver):
    """Testa adicionar e remover um produto do carrinho no React Shopping Cart."""
    driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

    # 🔹 1. Adicionar um produto ao carrinho
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/main/div/div[1]/button'))
    ).click()

    # 🔹 2. Verificar se o carrinho tem 1 item
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div'))
    ).text
    assert cart_count == "1", f"Erro: Carrinho tem {cart_count} itens, esperado 1"

    # 🔹 3. Abrir o carrinho e remover o item
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/button'))
    ).click()

    # 🔹 4. Verificar se o carrinho está vazio
    empty_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/p'))
    ).text
    assert "Add some products in the cart" in empty_message, "Erro: O carrinho não está vazio após remoção."

    print("-> Teste passou: Produto adicionado e removido com sucesso!")