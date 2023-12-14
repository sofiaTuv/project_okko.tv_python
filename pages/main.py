import allure
from selene import browser, be, have

from pages.helpers import Helpers


class MainPage(Helpers):

    def select_category(self, category_name):
        with allure.step(f'Выбрать из категорий: {category_name}'):
            self.click_on(f'//article[@test-id="rail_tab"]//span[text()="{category_name}"]/ancestor::a')

    def search_for(self, film_name):
        with allure.step('На главной странице okko.tv нажать на кнопку поиск'):
            self.click_on('[test-id=nav_search]')
            browser.element("//input[@type='search']").should(be.visible)
        with allure.step('Ввести в строку поиска: ' + film_name):
            self.element('input[type=search]').set_value(film_name).press_enter()
            browser.element('//h1').should(have.text('Результаты поиска'))


#//a[text()='Все результаты']