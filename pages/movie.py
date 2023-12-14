from typing import List

import allure
from selene import be, browser
from pages.helpers import Helpers


class MoviePage(Helpers):

    def is_visible(self, film_name):
        with (allure.step(f'Страница {film_name} открыта')):
            e = self.element(f'//*[@test-id="content_title"]//img[@alt="{film_name}"]')
            e.should(be.visible)

    def is_genre(self, expectedGenres: list[str]):
        with allure.step('Проверка фильма на соответствующий жанр'):
            errors: List[Exception] = []
            for expectedGenre in expectedGenres:
                try:
                    p = f"//div[contains(text(), 'Жанр')]/parent::div//a[contains(text(),'{expectedGenre}')]"
                    browser.element(p).should(be.visible)
                    return
                except Exception as e:
                    errors.append(e)

            raise AssertionError('; '.join(map(str, errors)))
