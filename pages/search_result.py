import allure

from pages.helpers import Helpers


class SearchResultPage(Helpers):

    def select(self, film_name):
        with allure.step('В результатах поиска выбрать фильм ' + film_name):
            self.click_on(f".//a[@aria-label='{film_name}']")
