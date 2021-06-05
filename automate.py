from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import logging
import time
import sys


performance_metric = datetime.now()
logging.basicConfig(filename="allLogs.log", level=logging.INFO, filemode="w")

logging.info(f'Selenium scrape started at {datetime.now().strftime("%H:%M:%S")}')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.nintendo.com/games/game-guide/#filter/:q=&dFR[generalFilters][0]=Deals&dFR[platform][0]=Nintendo%20Switch"
driver.get(url)
total_count = 0


while True:
    total_count = total_count + 1
    try:
        if EC.presence_of_element_located((By.ID, "btn-load-more")):
            driver.find_element_by_id("btn-load-more").click()

        if total_count > 100:
            logging.info(f"not normal, button pressed {total_count} times")
            break

    except ElementNotInteractableException as e:
        logging.info(f"No more button presses, ending system {e}")
        break

    except StaleElementReferenceException as e:
        logging.debug(f"stale element, waiting a 0.5s {e}")
        time.sleep(0.5)
    
    except:
        e = sys.exc_info()[0]
        logging.error( f"Unseen Error: {e}")
        break

html_source = driver.page_source

file = open("data.txt", "w")
file.write(html_source)
file.close()

logging.info("Finished saving html source")
logging.info(f'Selenium scrape ended at {datetime.now().strftime("%H:%M:%S")}')
logging.info(f'Performance: scraping data took {datetime.now() - performance_metric} amount of time')

driver.close()