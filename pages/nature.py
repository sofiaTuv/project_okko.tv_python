import allure
from selene import have

from pages.helpers import Helpers


class NatureCategoryPage(Helpers):

    def is_visible(self):
        with allure.step(f'Страница Природа открыта'):
            self.element("//h1").should(have.text('Природа'))

    def select_first_movie(self):
        with allure.step(f'Выбор первого фильма'):
            Helpers.click_on('//article[@test-id="grid"]//a', 0)
