import allure
from selene import browser, have


@allure.feature('UI Tests')
@allure.story('Main Page')
class TestMainPage:
    
    @allure.title('Проверка основных элементов главной страницы')
    def test_main_page_elements(self, setup_browser, main_page):
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

    @allure.title('Проверка формы обратной связи')
    def test_contact_form_fields(self, setup_browser, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_contact_form()
        main_page.should_have_contact_form_fields()

    @allure.title('Проверка ссылки на вакансии в хедере')
    def test_correct_vacancies_link(self, setup_browser, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_vacancies_link()
        main_page.should_have_correct_vacancies_link() 

    @allure.title('Проверка наличия логотипа на главной странице')
    def test_logo_visibility(self, setup_browser, main_page):
        # WHEN
        main_page.open()
        
        # THEN
        main_page.should_have_logo()

    @allure.title('Переход в раздел Вакансии')
    def test_clicking_vacancies_link(self, setup_browser, main_page):
        # WHEN
        main_page.open()

        # THEN
        main_page.should_have_vacancies_link()
        main_page.go_to_vacancies()

        
        # Проверяем, что URL соответствует ожидаемому
        browser.should(have.url('https://nordclan.com/jobs'))
        
    allure.title('Проверка основных элементов страницы "Вакансии"')
    def test_vacancies_page_elements(self, setup_browser, vacancies_page):
        # WHEN
        vacancies_page.open()

        # THEN
        vacancies_page.should_be_opened()
        """
        Остальные элементы допишу по мере написания методов и разработки тест-кейсов
        """
    

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип')
    def test_logo_navigation(self, setup_browser, main_page, vacancies_page):
        # WHEN
        main_page.open()
        main_page.go_to_vacancies()
        vacancies_page.click_logo()
        
        # THEN
        main_page.should_have_correct_title()