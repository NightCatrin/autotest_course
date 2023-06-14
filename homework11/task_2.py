# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep


sbis_site = 'https://fix-online.sbis.ru/'
tensor_site = 'https://tensor.ru/'
driver = webdriver.Chrome()
action = ActionChains(driver)
employee = 'Тестовый Клиент'
message = 'Привет'

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(5)
    assert driver.current_url == 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/', 'Не открылась страница авторизации'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('', Keys.ENTER)
    assert login.get_attribute('value') == '', 'Неправильно введен логин'
    sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('', Keys.ENTER)
    sleep(5)
    assert driver.current_url == sbis_site, 'Не смогли авторизоваться'
    sleep(7)
    contacts = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')[0].click()
    sleep(2)
    contacts_panel = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    assert contacts_panel.text == 'Контакты'
    contacts_panel.click()
    assert driver.current_url == (sbis_site + f'page/dialogs'), 'Не смогли перейти в реестр Контакты'
    sleep(10)
    add_message = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]').click()
    sleep(3)
    search_field = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content_wrapper .controls-Field')
    search_field.send_keys(employee)
    assert search_field.get_attribute('value') == employee, 'Не правильно введен пользователь'
    sleep(3)
    employee_name = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert employee_name.text == employee, 'Пользователь не найден'
    employee_name.click()
    sleep(3)
    text_input_field = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    text_input_field.send_keys(message)
    sleep(3)
    send_mess_btn = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]').click()
    sleep(3)
    mess_in_register = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
    assert mess_in_register[0].text == message, 'Сообщение не появилось в реестре'
    action.move_to_element(mess_in_register[0]).perform()
    sleep(1)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"] > div:nth-child(1)  [title="Перенести в удаленные"]')
    assert delete_btn.is_displayed(), 'Кнопка "Удалить сообщение" не отображается'
    delete_btn.click()
    assert mess_in_register[0] != message, 'Сообщение не удалено'
    sleep(5)
finally:
    driver.quit()
