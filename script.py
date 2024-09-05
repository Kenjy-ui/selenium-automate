from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do navegador (headless)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://portal-de-colombo.com/nf")

# Login utilizando variáveis de ambiente
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys(os.getenv('USERNAME'))
password.send_keys(os.getenv('PASSWORD'))

driver.find_element(By.ID, "login-button").click()
# Continuação do script...

driver.quit()
