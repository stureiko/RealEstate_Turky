import time

from selenium.webdriver.common.by import By

from realest.runner import main as run_main
from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.sahibinden.com/satilik-daire/istanbul?a20=38470')
    time.sleep(1)

    elem = driver.find_element(by=By.XPATH, value="//table[@id='searchResultsTable']/tbody//tr[@data-id]//td[@class='searchResultsTitleValue leafContent']/a")
    #


    time.sleep(5)
    driver.quit()
    return 0


if __name__ == '__main__':
    # run_main()
    main()