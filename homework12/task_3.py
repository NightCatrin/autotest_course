# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",
# где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from task_1 import AuthOnline, MainPnline


class Task(Region):
    """Задача в новой вкладке"""

    performer_elm = Element(By.CSS_SELECTOR, '.edws-StaffChooser__itemTpl-name', 'ФИ Исполнителя')
    data_and_num_task_cslt = CustomList(By.CSS_SELECTOR, '.controls-EditableArea__Text__inner', 'Номер и дата задачи')
    description_elm = Element(By.CSS_SELECTOR, '[name="editorWrapper"]', 'Описание задачи')
    author_task_elm = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'ФИ автора')


class Test(TestCaseUI):
    """Класс с выполнением теста"""

    def test(self):

        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Переходим на страницу авторизации')
        self.browser.should_be(UrlContains(''), TitleExact(self.config.get('SBIS_TITLE')))

        log('Авторизуемся на сайте')
        auth = AuthOnline(self.driver)
        login, password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth.login_inp.type_in(login + Keys.ENTER).should_be(ExactText(login))
        auth.password_inp.type_in(password + Keys.ENTER)

        log('Открываем эталонную задачу по прямой ссылке в новом окне')
        main_page = MainPnline(self.driver)
        main_page.dashboards_elm.should_be(Visible)
        self.browser.create_new_tab(self.config.get('TASK_LINK'))
        self.browser.switch_to_opened_window()

        log('Проверяем, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА"')
        assert_that(self.browser.current_title, equal_to(self.config.get('TITLE_TASK')), 'Открыта неправильная задача')

        log('Проверяем, что поле Исполнитель отображается с эталонными значениями')
        task = Task(self.driver)
        task.performer_elm.should_be(ExactText(self.config.get('HUMAN')))

        log('Проверяем поле Дата')
        task.data_and_num_task_cslt.item(1).should_be(ExactText(self.config.get('FIELD_DATA')))

        log('Проверяем поле Номер')
        task.data_and_num_task_cslt.item(2).should_be(ExactText(self.config.get('FIELD_NUMBER')))

        log('Проверяем поле Описание')
        task.description_elm.should_be(ExactText(self.config.get('FIELD_DESCRIPTION')))

        log('Проверяем поле Автор')
        task.author_task_elm.should_be(ExactText(self.config.get('HUMAN')))
