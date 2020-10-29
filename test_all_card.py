import pytest
from selenium import webdriver

pytest.driver = webdriver.Chrome('D:/driver/chromedriver.exe')  # Optional argument, if not specified will search path.


def testing():
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('http://petfriends1.herokuapp.com/login')






def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


# находим фото, имя и возраст
pytest.driver.implicitly_wait(5)
images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
pytest.driver.implicitly_wait(5)
names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
pytest.driver.implicitly_wait(5)
descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')


def test_check_elements():
    # Проверяем что поля не пустые и есть фотографии
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


    pytest.driver.quit()