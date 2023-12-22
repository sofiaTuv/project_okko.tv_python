from time import sleep
import allure
from selene import be, by, browser
from pages.helpers import Helpers


class MoodRecommendationsPage(Helpers):

    def select_mood(self, mood: str):
        with (allure.step(f'Выбрать настроение: "{mood}"')):
            self.element("[test-id='mood_rekko']").should(be.visible)
            self.click_on('[test-id="mood_filter_mood_button"]')
            self.element("[id=okko-popup] div").should(be.visible)\
                .element(by.text(mood)).click()

    def select_company(self, company: str):
        with (allure.step(f'Выбрать компанию: "{company}"')):
            self.click_on('[test-id="mood_filter_companions_button"]')
            self.element("[id=okko-popup] div").should(be.visible)\
                .element(by.text(company)).click()

    def select_movie(self):
        with allure.step('Открываем страницу фильма'):
            sleep(3)
            self.click_on("//article[@test-id='mood_rekko']//a")
