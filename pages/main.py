import allure
from selene import be, have

from pages.helpers import Helpers


class MainPage(Helpers):

    def select_category(self, category_name):
        with allure.step(f'Выбрать из категорий: "{category_name}"'):
            self.click_on(f'//article[@test-id="rail_tab"]//span[text()="{category_name}"]/ancestor::a')

    def search_for(self, film_name):
        with allure.step('На главной странице okko.tv нажать на кнопку поиск'):
            self.click_on('[test-id=nav_search]')
            self.element("//input[@type='search']").should(be.visible)
        with allure.step(f'Ввести в строку поиска: "{film_name}"'):
            self.element("input[type='search']").set_value(film_name).press_enter()
            self.element('//h1').should(have.text('Результаты поиска'))
