from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
import time

def get(url, driver):

    driver.get(url = url)
    driver.implicitly_wait(time_to_wait=5)

    res = []
    page = 1
    i = 0

    while True:
        for info in driver.find_elements(By.XPATH, "//div[@data-sokoban-container]"):
            try:
                i += 1
                header = info.find_element(
                    By.XPATH, "div[@data-header-feature]")
                #content = info.find_element(By.XPATH, "//div[@data-content-feature]")
                url = header.find_element(
                    By.TAG_NAME, "a").get_attribute('href')
                title = header.find_element(
                    By.TAG_NAME, "h3").get_attribute('innerHTML')
                #body = content.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                print(i, '\t', title, '\t'*2, url)
                res.append({
                    "url": url,
                    "title": title
                })
            except Exception as E:
                print(f"---error---\n{E}\n---content---\n{info.text}\n\n")
                pass
        page += 1
        try:
            driver.find_element(
                By.XPATH, f'//*[@aria-label="Page {page}"]').click()
            driver.implicitly_wait(time_to_wait=5)
            time.sleep(2)
        except:
            break

    return res

if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2])
    driver_path = sys.argv[1]
    url = sys.argv[2]

    driver = webdriver.Chrome(driver_path)
    try:
        get(url, driver)
    except Exception as e:
        print(e)
    finally:
        driver.close()