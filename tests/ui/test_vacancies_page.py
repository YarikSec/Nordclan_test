import allure
from allure_commons.types import Severity
from selene import browser, have
import pytest

@allure.epic('Раздел "Вакансии" на сайте Nordclan')
@allure.label('owner', 'Yaroslav Slipchishin')
@allure.feature('UI Tests')
@allure.story('Vacancies Page')
class TestVacanciesPage:

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка основных элементов страницы "Вакансии"')
    def test_vacancies_page_elements(self, vacancies_page):
        # WHEN
        vacancies_page.open()

        # THEN
        vacancies_page.should_be_opened()
        """
        Остальные элементы допишу по мере написания методов и разработки тест-кейсов
        """

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка перехода на главную страницу при нажатии на логотип')
    def test_logo_navigation(self, main_page, vacancies_page):
        # WHEN
        main_page.open()
        main_page.go_to_vacancies()
        vacancies_page.click_logo()

        # THEN
        main_page.should_have_correct_title()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка списка вакансий')
    @pytest.mark.skip(reason='Тест в разработке - требуется обновление селекторов')
    def test_vacancies_list(self, vacancies_page):
        # WHEN
        vacancies_page.open()
        vacancies_page.should_be_opened()
    
        # THEN
        vacancies_page.should_have_vacancies()
        vacancies_page.should_have_expected_vacancies([
            '.Net',
            'QA Middle',
            'Middle Java',
            'IT Sales',
            'Senior Java',
            'Ведущий системный аналитик'
        ])
        vacancies_page.should_have_expected_departments([
            'Разработка',
            'Управление',
            'Отдел аналитики'
        ])

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка фильтрации вакансий по отделам')
    @pytest.mark.skip(reason='Тест в разработке - требуется обновление селекторов')
    def test_vacancy_department_filter(self, vacancies_page):
        # WHEN
        vacancies_page.open()
        vacancies_page.should_be_opened()
        
        # THEN
        vacancies_page.should_have_department_filters()
        vacancies_page.filter_by_department('Разработка')
        vacancies_page.should_show_only_department_vacancies('Разработка')

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка наличия кнопки отправки резюме')
    def test_send_resume_button(self, vacancies_page):
        # WHEN
        vacancies_page.open()
        vacancies_page.should_be_opened()
        
        # THEN
        vacancies_page.should_have_send_resume_button()