import allure
from allure_commons.types import Severity
from selene import browser, have

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