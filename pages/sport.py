import allure
from selene import have
from pages.helpers import Helpers


class SportCategoryPage(Helpers):

    def select_subcategory(self, subcategory):
        with allure.step(f'Выбрать подкатегорию: {subcategory}'):
            self.click_on(f'//article[@test-id="rail_tab"]//span[text()="{subcategory}"]/ancestor::a')
            self.element("//h1").should(have.text(subcategory))

    def is_visible(self, name: str):
        with allure.step(f'Страница {name} открыта'):
            self.element("//h1").should(have.text(name))
