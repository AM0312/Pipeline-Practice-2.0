from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service=Service(
    executable_path='/usr/local/bin/chromedriver'
)

options=webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service,options=options)
driver.get('https://am0312.github.io/Pipeline-Practice-2.0/')

try:
    # Wait for the h1 element to be present on the page
    h1_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )

    # Check if the h1 element contains the word "magic"
    if 'magic' in h1_element.text.lower():
        print('The webpage has an h1 tag with the word "magic"')
    else:
        print('The webpage does not have an h1 tag with the word "magic"')

except Exception as e:
    print("Failed, ",e)

finally:
    driver.quit()
