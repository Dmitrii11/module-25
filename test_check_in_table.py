import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytest.driver = webdriver.Chrome('D:/driver/chromedriver.exe')


def testing():
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Открываем сайт


def test_login():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Переходим на страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Ждем таблицу с животными
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))


    # Получаем количество животных в таблице
all_str = pytest.driver.find_elements_by_css_selector("div#all_my_pets > table > tbody > tr")
    # Получаем количество животных в карточке аккаунта
all_pets = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")
    # Получаем список имен из таблицы
names = pytest.driver.find_elements_by_css_selector("div#all_my_pets > table > tbody > tr > td:nth-of-type(1)")
    # Получаем список пород из таблицы
breeds = pytest.driver.find_elements_by_css_selector("div#all_my_pets > table > tbody > tr > td:nth-of-type(2)")
    # Получаем список возростов животных
age = pytest.driver.find_elements_by_css_selector("div#all_my_pets > table > tbody > tr > td:nth-of-type(3)")

images = pytest.driver.find_elements_by_css_selector("div#all_my_pets > table > tbody > tr > th > img")

def test_check_elements():

    # Проверяем что у всех животных есть имена, порода и возраст
    for i in range(len(all_str)):
        all_images = 0
        if images[i].get_attribute('src') !='':
            all_images += 1
        assert all_images >= len(all_str)/2
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert age[i].text != ''
        # Проверка что количество питомцев в списке равно числу в карточек аккаунта(не смог понять как вытащить от туда число)
        #assert len(all_str) == all_pets
    pytest.driver.quit()