import asyncio
import time
import selenium.webdriver
import selenium.webdriver.common.action_chains
import selenium.webdriver.common.by
import bs4

from handlers.user_privats import bot


def get_business_info(lat, lon, biz_type):
        driver = selenium.webdriver.Chrome()
        driver.maximize_window()
        time.sleep(1)
        driver.get(f'https://yandex.ru/maps/47/nizhny-novgorod/?ll={lon}%2C{lat}&z=11')
        time.sleep(3)
        search_box = driver.find_element('class name', 'input__control')
        search_box.send_keys(biz_type)
        search_box.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
        time.sleep(3)

        html = driver.page_source
        soup = bs4.BeautifulSoup(html, 'html.parser')
        first_image = driver.find_elements('class name', 'search-snippet-gallery-view__item')

        if first_image:
            first_image[0].find_element('class name', 'img-with-alt')
            first_image[0].click()
            time.sleep(2)

            html = driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.parser')
            biz_images = soup.find_all('img', class_="media-wrapper__media")

            time.sleep(2)

            first_image[0].click()

            html = driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.parser')
            biz_link = soup.find('a', class_='button _view_secondary-blue _ui _size_medium _link')
            biz_rate = soup.find('span', class_='business-rating-badge-view__rating-text')
            working_status = soup.find('div', class_='business-working-status-view')

            print(biz_link, biz_rate, working_status)

            if working_status is not None:
                working_status = working_status.text
            if biz_rate is not None:
                biz_rate = biz_rate.text
            if biz_link is not None:
                biz_link = biz_link.get('href')

            route_button = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                               '.button._view_primary._ui._size_medium')
            route_button.click()
            time.sleep(2)
            search_box = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                              'input.input__control')
            search_box[1].send_keys(f'{lat} {lon}')
            search_box[1].send_keys(selenium.webdriver.common.keys.Keys.ENTER)
            time.sleep(2)
            man_icon = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                           '.travel-modes-view__mode._mode_pedestrian')
            man_icon.click()
            time.sleep(2)
            driver.save_screenshot('route.png')

            print(biz_images)
            return [biz_images[0].get('src'), biz_images[1].get('src'), biz_images[2].get('src'),
                    str(working_status), str(biz_link), str(biz_rate), biz_images[0].get('alt')]

        else:
            biz_button = driver.find_element('class name', 'search-business-snippet-view__title')
            biz_button.click()
            time.sleep(2)

            html = driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.parser')
            biz_link = soup.find('a', class_='button _view_secondary-blue _ui _size_medium _link')
            biz_rate = soup.find('span', class_='business-rating-badge-view__rating-text')
            working_status = soup.find('div', class_='business-working-status-view')
            biz_name = soup.find('a', class_='card-title-view__title-link')
            if working_status is not None:
                working_status = working_status.text
            if biz_rate is not None:
                biz_rate = biz_rate.text
            if biz_link is not None:
                biz_link = biz_link.get('href')
            if biz_name is not None:
                biz_name = biz_name.text

            route_button = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                               '.button._view_primary._ui._size_medium')
            route_button.click()
            time.sleep(2)
            search_box = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                              'input.input__control')
            search_box[1].send_keys(f'{lat} {lon}')
            search_box[1].send_keys(selenium.webdriver.common.keys.Keys.ENTER)
            time.sleep(2)
            man_icon = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                           '.travel-modes-view__mode._mode_pedestrian')
            man_icon.click()
            time.sleep(2)
            driver.save_screenshot('route.png')

            biz_images = ['https://sun9-49.userapi.com/impg/bJKG4koWjGdYaTnVVPEeo34mIIZhdGUObZBOOQ/Nfy_CCG0Kaw.jpg?size=720x1280&quality=95&sign=5e1d139530ea9f3a51a5b077bd881b00&type=album',
                          'https://sun9-30.userapi.com/impg/oL-PSrEHIclKnO-Hrvf5zpkXU89gUSVEiQLDgQ/s-epxZTtHng.jpg?size=719x1280&quality=95&sign=63f892ae34987862b52a5b6ee7f9d2ae&type=album',
                          'https://sun9-6.userapi.com/impg/m-uEifTpWnKY8Gx5V1H_3E6NJAc1ieMhetnyYA/1HNCyL4jdVM.jpg?size=1280x719&quality=96&sign=dbecfcc5117268a4e4e60430ddb1657b&type=album']

            return [biz_images[0], biz_images[1], biz_images[2],
                    str(working_status), str(biz_link), str(biz_rate), str(biz_name)]
