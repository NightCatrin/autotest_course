# Авторизоваться на сайте
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили1
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import log, info
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class AuthOnline(Region):
    """Страница авторизации"""

    login_inp = TextField(By.CSS_SELECTOR, '[name="Login"]', 'Поле ввода логина')
    password_inp = TextField(By.CSS_SELECTOR, '[name="Password"]', 'Поле ввода пароля')


class MainPnline(Region):
    """Главная страница"""

    registry_accor_cslt = CustomList(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]', 'Реестры аккордеона')
    contacts_panel_elm = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Контакты / Контакты')
    dashboards_elm = Element(By.CSS_SELECTOR, '[data-name="dashboard-View"]', 'дашборды')


class PageContacts(Region):
    """Страница Контакты/Контакты"""

    add_message_btn = Button(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"] .controls-BaseButton__wrapper', 'Кнопка создать новый диалог')
    search_field_inp = TextField(By.CSS_SELECTOR, '.controls-StackTemplate-content_wrapper .controls-Field', 'Поле ввода сотрудника')
    employee_elm = Element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]', 'Найденный сорудник')
    message_field_inp = Element(By.CSS_SELECTOR, '[role="textbox"]', 'Поле ввода сообщения')
    send_mess_btn = Button(By.CSS_SELECTOR, '[title="Отправить"]', 'Кнопка отправить сообщение')
    mess_in_register_cslt = CustomList(By.CSS_SELECTOR, '.msg-entity-text', 'Сообщения в реестре')
    delete_btn = Button(By.CSS_SELECTOR, '[data-qa="items-container"] > div:nth-child(1) [title="Перенести в удаленные"]', 'Кнопка удалить сообщение')


class Test(TestCaseUI):
    """"""
    def test(self):
        """Функция для авторизации"""

        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Перейти на страницу авторизации')
        self.browser.should_be(UrlContains(''), TitleExact(self.config.get('SBIS_TITLE')))

        log('Авторизоваться на сайте')
        auth = AuthOnline(self.driver)
        login, password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth.login_inp.type_in(login+Keys.ENTER).should_be(ExactText(login))
        auth.password_inp.type_in(password+Keys.ENTER)

        log('Перейти в реестр Контакты')
        main_online = MainPnline(self.driver)
        main_online.registry_accor_cslt.item(contains_text='Контакты').click()
        main_online.contacts_panel_elm.click()


        log('Отправить сообщение самому себе и проверить, что сообщение появилось в реестре')
        mess = PageContacts(self.driver)
        mess.add_message_btn.should_be(Visible, wait_time=5).click()
        mess.search_field_inp.type_in(self.config.get('EMPLOYEE'))
        mess.employee_elm.should_be(Visible).click()
        message = self.config.get('MESSAGE')
        mess.message_field_inp.type_in(message).should_be(ExactText(message))
        mess.send_mess_btn.click()
        mess.mess_in_register_cslt.item(contains_text=message).should_be(Visible).mouse_over()
        mess.delete_btn.click()
        mess.mess_in_register_cslt.item(contains_text=message).should_not_be(Visible)
