from selene import have, be
from selene.support.shared import browser
from selene.support import by
import allure

class VacanciesPage():
    def __init__(self):
        self.header = browser.element('.sc-lbOyJj')
        self.logo_header = browser.element('img[itemprop="logo"].sc-breuTD')

        self.title = browser.element('.sc-bczRLJ')

    def open(self):
        with allure.step('Открываем страницу "Вакансии"'):
            browser.open('https://nordclan.com/jobs')
        return self


    def should_be_opened(self):
        with allure.step('Проверяем, что страница открылась'):
            self.header.should(be.visible)
            self.title.should(be.visible)
        return self
    
    def click_logo(self):
        with allure.step('Клмкаем по логотипу в хедере'):
            self.logo_header.click()
        return self