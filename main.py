import random
import time
import re

from selenium.webdriver.common.by import By
from selenium import webdriver

import mysql.connector
from mysql.connector import Error


def get_links(driver: webdriver.Chrome, xpath: str) -> dict:
    res = {}
    elems = driver.find_elements(by=By.XPATH,
                                 value=xpath)
    for e in elems:
        links = e.find_elements(by=By.CSS_SELECTOR, value='a')
        link = links[3].get_attribute('href')
        link_id = re.sub(r'/detail$', '', re.search(r'\d+/detail$', link).group())
        res[link_id] = link

    return res


def main():
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.sahibinden.com/en/for-sale-flat/istanbul?a20=38470')
        time.sleep(1)
        num_orders_pages = driver.find_element(by=By.XPATH, value="//p[@class='mbdef']").text
        num_orders_pages = int(
            re.sub(r',', '', re.sub(r'1\sof\s', '', re.search(r'1\sof\s\d,\d+', num_orders_pages).group())))

        print(f'Page 1 of {num_orders_pages}. Links:')

        links = get_links(driver,
                          "//table[@id='searchResultsTable']/tbody//tr[@data-id]//td[@class='searchResultsTitleValue "
                          "leafContent']")
        if len(links) < 1:
            time.sleep(10)

        add_to_db(links)
        print(f'Add {len(links)} records.')

        for n in range(1, num_orders_pages - 1):
            time.sleep(2 * random.random())
            np = driver.find_element(by=By.XPATH, value="//a[@class='prevNextBut'][@title='Sonraki']")
            link_str = np.get_attribute('href')
            print(link_str)
            driver.get(link_str)
            print(f'Page {n + 1} of {num_orders_pages}. Links: {len(links)}')
            links = get_links(driver,
                              "//table[@id='searchResultsTable']/tbody//tr[@data-id]//td["
                              "@class='searchResultsTitleValue leafContent']")
            add_to_db(links)
            print(f'Add {len(links)} records.')

        time.sleep(0.5)

    finally:
        driver.quit()
    return 0


def add_to_db(data: dict):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='real_estate',
                                             user='root',
                                             password='root')
        if connection.is_connected():
            cursor = connection.cursor()

            for item in data.items():
                try:
                    mySql_insert_query = """INSERT INTO links (id, link) VALUES (%s, %s) """

                    record = (item[0], item[1])
                    cursor.execute(mySql_insert_query, record)
                    connection.commit()
                except Error as e:
                    print("Error while insert record", e)

            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    main()
