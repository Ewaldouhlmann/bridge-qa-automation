import dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(username, password):
    # Essa função faz login no sistema caso tudo ocorra bem, retorna True, caso contrário, retorna False
    try:
        driver.get("https://desafio.qa.bridge.ufsc.br/")
        
        # Insere os dados de login e clica no botão de login
        driver.find_element(By.ID, "usuario").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "termos-de-uso").click()
        driver.find_element(By.CLASS_NAME, "btn-acessar").click() 
        return True
    except:
        return False

def start_challenge():
    # Passa a pagina de orientações e vai para a página de cadastro
    driver.get("https://desafio.qa.bridge.ufsc.br/orientacoes")
    driver.find_element(By.CLASS_NAME, "btn-acessar").click()

def get_dados():
    # Aqui estão os dados que serão preenchidos no formulário, para testar um novo cadastro, basta alterar os valores abaixo
    cpf = '12345678909'
    cns = 992347895343935 
    nome = 'Andre Pereira'
    data_nascimento = '30/05/2024'
    sexo = '#!3662'
    fone_residencial = '08997065135'
    fone_celular = '08997065aa135'
    return cpf, cns, nome, data_nascimento, sexo, fone_residencial, fone_celular

def fill_form(cpf, cns, nome, data_nascimento, sexo, fone_residencial, fone_celular):
    # Essa função preenche o formulário com os dados passados e retorna o span, informando se o cadastro foi realizado com sucesso ou teve algum erro
    driver.get("https://desafio.qa.bridge.ufsc.br/cadastro")
    driver.find_element(By.ID, "cpf").send_keys(cpf)
    driver.find_element(By.ID, "cns").send_keys(cns)
    driver.find_element(By.ID, "nome-completo").send_keys(nome)
    driver.find_element(By.ID, "data-nascimento").send_keys(data_nascimento)
    driver.find_element(By.ID, "sexo").send_keys(sexo)
    driver.find_element(By.ID, "telefone-residencial").send_keys(fone_residencial)
    driver.find_element(By.ID, "telefone-celular").send_keys(fone_celular)
    driver.find_element(By.CLASS_NAME, "btn-salvar").click()

    try:
        span_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "footer span"))
        )
        return span_element.text 
    except Exception as e:
        return 1






if __name__ == "__main__":
    # Lê as variáveis de ambiente e inicializando o driver do navegador
    dotenv.load_dotenv(dotenv.find_dotenv())
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Tenta realizar login, passar para a tela de cadastro e preencher o formulário e exibir a mensagem de sucesso caso tudo ocorra bem.
        if login(email, password): 
            start_challenge() 
            cpf, cns, nome, data_nascimento, sexo, fone_residencial, fone_celular = get_dados() 
            msg = fill_form(cpf, cns, nome, data_nascimento, sexo, fone_residencial, fone_celular) 
            print(msg)
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")
    finally:
        time.sleep(2) 
        driver.quit() 
    
