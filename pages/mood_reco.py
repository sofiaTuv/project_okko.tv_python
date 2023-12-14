from time import sleep

import allure
from selene import command, be, by, browser

from pages.helpers import Helpers


class MoodRecommendationsPage(Helpers):

    def select_mood(self, mood: str):
        with (allure.step('Выбрать настроение: ' + mood)):
            self.element("[test-id=mood_rekko]").perform(command.js.scroll_into_view)
            self.click_on('.//div/span[text() ="посмеяться"]')
            self.element("[id=okko-popup] div").should(be.visible) \
                .element(by.text(mood)).click()

    def select_company(self, company: str):
        with (allure.step('Выбрать компанию: ' + company)):
            self.click_on('.//div/span[text() ="наедине"]')
            self.element("[id=okko-popup] div").should(be.visible)\
            .element(by.text(company)).click()

    def select_movie(self):
        with allure.step('Открываем страницу фильма'):
            sleep(3)
            browser.element("//article[@test-id='mood_rekko']//a").click()
            #self.click_on("//article[@test-id='mood_rekko']//a")


'''def is_genre(self, genres: list[str]):
        with allure.step('Проверка фильма на соответствующий жанр'):
            conditions = list(map(lambda s: have.text(s), genres))
            self.element_assert('[test-id="meta_genre"]', conditions)'''