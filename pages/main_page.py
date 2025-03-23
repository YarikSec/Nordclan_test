from selene import have, be
from selene.support.shared import browser
from selene.support import by
import allure


class MainPage:
    def __init__(self):
        self.header = browser.element('.sc-lbOyJj')
        self.logo_header = browser.element('img[itemprop="logo"].sc-breuTD')
        self.vacancies_link = browser.element('.sc-fbPSWO')

        self.main_title = browser.element('.sc-bczRLJ')

        self.contact_form = browser.element('#feedback-form')
        self.name_input = browser.element('#feedback-form input[name="clientName"]')
        self.phone_input = browser.element('#feedback-form input[name="phone"]')
        self.company_input = browser.element('#feedback-form input[name="company"]')
        self.email_input = browser.element('#feedback-form input[name="email"]')
        self.message_input = browser.element('#feedback-form textarea[name="comments"]')
        self.submit_button = browser.element('#feedback-form button[type="submit"]')
        
        self.services_section = browser.element('.sc-iBkjds')
        self.about_section = browser.element('.sc-iBkjds')
        self.projects_section = browser.element('.sc-iBkjds')
        self.reviews_section = browser.element('.sc-bczRLJ')
        self.articles_section = browser.element('.sc-iBkjds')
        self.footer = browser.element('.sc-csvncw')

        

    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('https://nordclan.com')
        return self

    def should_be_opened(self):
        with allure.step('Проверяем, что страница открылась'):
            self.header.should(be.visible)
            self.main_title.should(be.visible)
        return self

    def should_have_correct_title(self):
        with allure.step('Проверяем заголовок страницы'):
            self.main_title.should(have.text('Создаем уникальное программное обеспечение и решения для финансового сектора, промышленностимедицины и корпоративных стартапов'))
        return self

    def should_have_contact_form(self):
        with allure.step('Проверяем наличие формы обратной связи'):
            self.contact_form.should(be.visible)
        return self

    def should_have_services_section(self):
        with allure.step('Проверяем наличие секции услуг'):
            self.services_section.should(be.visible)
        return self

    def should_have_about_section(self):
        with allure.step('Проверяем наличие секции о компании'):
            self.about_section.should(be.visible)
        return self

    def should_have_projects_section(self):
        with allure.step('Проверяем наличие секции проектов'):
            self.projects_section.should(be.visible)
        return self

    def should_have_reviews_section(self):
        with allure.step('Проверяем наличие секции отзывов'):
            self.reviews_section.should(be.visible)
        return self

    def should_have_articles_section(self):
        with allure.step('Проверяем наличие секции статей'):
            self.articles_section.should(be.visible)
        return self

    def should_have_footer(self):
        with allure.step('Проверяем наличие футера'):
            self.footer.should(be.visible)
        return self

    def should_have_contact_form_fields(self):
        with allure.step('Проверяем наличие полей формы'):
            self.contact_form.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.name_input.should(be.visible)
            self.company_input.should(be.visible)
            self.phone_input.should(be.visible)
            self.email_input.should(be.visible)
            self.message_input.should(be.visible)
            self.submit_button.should(be.visible)
        return self 
    
    def should_have_vacancies_link(self):
        with allure.step('Проверяем наличие ссылки на вакансии в хедере'):
            self.vacancies_link.should(be.visible)
        return self

    def should_have_correct_vacancies_link(self):
        with allure.step('Проверяем корректность ссылки на вакансии'):
            self.vacancies_link.should(have.attribute('href', 'https://nordclan.com/jobs'))
        return self
    
    def go_to_vacancies(self):
        with allure.step('Переходим в раздел Вакансии с главной страницы'):
            self.vacancies_link.click()
        return self

    def should_have_logo(self):
        with allure.step('Проверяем наличие логотипа'):
            self.logo_header.should(be.visible)
            return self

    def click_logo(self):
        with allure.step('Кликаем по логотипу в хедере'):
            self.logo_header.click()
        return self