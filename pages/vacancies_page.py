from selene import have, be
from selene.support.shared import browser
from selene.support import by
import allure

class VacanciesPage():
    def __init__(self):
        self.header = browser.element('.sc-lbOyJj')
        self.logo_header = browser.element('img[itemprop="logo"].sc-breuTD')

        self.description = browser.element('.sc-efBctP')
        self.life_at_nordclan = browser.element('.eWhjWy')

        self.title = browser.element('.sc-bczRLJ')
        self.vacancies_list = browser.all('.sc-iBkjds')  # список всех вакансий
        self.vacancy_titles = browser.all('.sc-gsnTZi')  # заголовки вакансий
        self.vacancy_departments = browser.all('.sc-cxabCf')  # отделы вакансий

    def open(self):
        with allure.step('Открываем страницу "Вакансии"'):
            browser.open('https://nordclan.com/jobs')
        return self


    def should_be_opened(self):
        with allure.step('Проверяем, что страница открылась'):
            self.header.should(be.visible)
            self.title.should(be.visible)
        return self
    
    def should_have_vacancies(self):
        with allure.step('Проверяем наличие списка вакансий'):
            self.vacancies_list.should(have.size_greater_than(0))
        return self

    def should_have_expected_vacancies(self, expected_vacancies):
        with allure.step(f'Проверяем наличие ожидаемых вакансий: {expected_vacancies}'):
            for vacancy in expected_vacancies:
                self.vacancy_titles.should(have.texts(vacancy))
            return self

    def should_have_expected_departments(self, expected_departments):
        with allure.step(f'Проверяем наличие ожидаемых отделов: {expected_departments}'):
            for department in expected_departments:
                self.vacancy_departments.should(have.texts(department))
            return self
        
    def should_have_department_filters(self):
        with allure.step('Проверяем наличие фильтров по отделам'):
            self.department_filters = browser.all('.department-filter')
            self.department_filters.should(be.visible)
            self.department_filters.should(have.size.greater_than(0))
            return self

    def filter_by_department(self, department):
        with allure.step(f'Фильтруем вакансии по отделу: {department}'):
            filter_button = browser.element(f'.department-filter[data-department="{department}"]')
            filter_button.click()
            return self

    def should_show_only_department_vacancies(self, department):
        with allure.step(f'Проверяем, что отображаются только вакансии отдела: {department}'):
            self.vacancy_departments.should(have.texts(department))
            return self
    
    def click_logo(self):
        with allure.step('Кликаем по логотипу в хедере'):
            self.logo_header.click()
        return self

    def should_have_send_resume_button(self):
        with allure.step('Проверяем наличие кнопки отправки резюме'):
            self.send_resume_button = browser.element('.sc-ftvSup')
            browser.execute_script("arguments[0].scrollIntoView(true);", self.send_resume_button())
            self.send_resume_button.should(be.visible)
            self.send_resume_button.should(have.text('ОТПРАВИТЬ РЕЗЮМЕ'))
            return self