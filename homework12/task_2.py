# Авторизоваться на сайте
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from atf.ui import *
from atf import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from task_1 import AuthOnline, MainPnline


class Tasks(Region):
    """Реестр Задачи / Задачи на мне / Вкладка в Работе"""

    folders_cslt = CustomList(By.CSS_SELECTOR, '[data-qa="items-container"] .controls-Grid__row_master', 'Папки в реестре Задачи на мне')
    number_of_tasks_elm = Element(By.CSS_SELECTOR, '[data-qa="controls-EditorList__additionalCounter"]', 'Число задач в папке')
    table_tasks_elm = Element(By.CSS_SELECTOR, '[data-qa="controls-EditorList__mainCounter"]', 'Число задач')
    folder_num_cslt = CustomList(By.CSS_SELECTOR, '[data-qa="items-container"] .controls-Grid__cell_master', 'Папки')
    add_btn = Button(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"] .controls-BaseButton__wrapper', 'Кнопка +')
    create_folder_btn = Button(By.CSS_SELECTOR, '[key="list-render-folderItem"]', 'Кнопка Создать новую папку')
    name_input_field_inp = TextField(By.CSS_SELECTOR, '[templatename="EDWS3/Utils/userFolder:ConstructionDialog"] input', 'Поле ввода названия папки')
    save_btn = Button(By.CSS_SELECTOR, '[templatename="EDWS3/Utils/userFolder:ConstructionDialog"] .controls-BaseButton', 'Кнопка сохранить')
    mess_in_registry_elm = Element(By.CSS_SELECTOR, '.hint-EmptyView__title_l', 'Сообщение в реестре')
    settings_folder_cslt = CustomList(By.CSS_SELECTOR, '.controls-itemActionsV__action', 'Настройки папки')
    delete_folder_btn = Button(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Удалить папку')
    confirm_removal_btn = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Подтвердить удаление')


class Test(TestCaseUI):
    """Класс с выполнением теста"""

    def test(self):

        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Перейти на страницу авторизации')
        self.browser.should_be(UrlContains(''), TitleExact(self.config.get('SBIS_TITLE')))

        log('Авторизоваться на сайте')
        auth = AuthOnline(self.driver)
        login, password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth.login_inp.type_in(login + Keys.ENTER).should_be(ExactText(login))
        auth.password_inp.type_in(password + Keys.ENTER)

        log('Перейти в реестр Задачи на вкладку "В работе"')
        accord = MainPnline(self.driver)
        accord.registry_accor_cslt.item(contains_text='Задачи').click()
        accord.contacts_panel_elm.click()
        self.browser.should_be(UrlContains(''))

        log('Убедиться, что выделена папка "Входящие" и стоит маркер')
        tasks = Tasks(self.driver)
        tasks.folders_cslt.item(1).element('.controls-StickyBlock').element('[data-qa="marker"]')

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        tasks.table_tasks_elm.should_not_be(ExactText('0'))

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        tasks.folder_num_cslt.item(2).click().element('.controls-StickyBlock')
        tasks.folders_cslt.item(1).should_not_be(CssClass('.controls-StickyBlock'))

        log('Создать новую папку и перейти в неё')
        tasks.folder_num_cslt.item(1).click()
        tasks.add_btn.click()
        tasks.create_folder_btn.should_be(Visible).click()
        tasks.name_input_field_inp.type_in('это новая папка')
        tasks.save_btn.click()
        tasks.folder_num_cslt.item(3).should_be(Visible).click()

        log('Убедиться, что она пустая')
        tasks.mess_in_registry_elm.should_be(ExactText(self.config.get('MESSAGE_REGISTER')))

        log('Удалить новую папку, проверить, что её нет в списке папок')
        tasks.folder_num_cslt.item(3).mouse_over()
        tasks.settings_folder_cslt.item(2).should_be(Visible).click()
        tasks.delete_folder_btn.should_be(Visible).click()
        tasks.confirm_removal_btn.click()
        tasks.folder_num_cslt.item(3).should_not_be(Visible)
