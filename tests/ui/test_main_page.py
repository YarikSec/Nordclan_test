import allure
from allure_commons.types import Severity
from selene import browser, have

@allure.epic('Главная страница Nordclan')
@allure.label('owner', 'Yaroslav Slipchishin')
@allure.feature('UI Tests')
@allure.story('Main Page')
class TestMainPage:

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка основных элементов главной страницы')
    def test_main_page_elements(self, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_be_opened()
        main_page.should_have_correct_title()
        main_page.should_have_contact_form()
        main_page.should_have_services_section()
        main_page.should_have_about_section()
        main_page.should_have_projects_section()
        main_page.should_have_reviews_section()
        main_page.should_have_articles_section()
        main_page.should_have_footer()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка формы обратной связи')
    def test_contact_form_fields(self, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_contact_form()
        main_page.should_have_contact_form_fields()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка ссылки на вакансии в хедере')
    def test_correct_vacancies_link(self, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_vacancies_link()
        main_page.should_have_correct_vacancies_link()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка наличия логотипа на главной странице')
    def test_logo_visibility(self, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_logo()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.title('Переход в раздел Вакансии')
    def test_clicking_vacancies_link(self, main_page):
        # WHEN
        main_page.open()

        # THEN
        main_page.should_have_vacancies_link()
        main_page.go_to_vacancies()

        
        # Проверяем, что URL соответствует ожидаемому
        browser.should(have.url('https://nordclan.com/jobs'))