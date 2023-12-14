from typing import List
from selene import browser, Element
from selene.core.condition import Condition


class Helpers:

    @staticmethod
    def click_on(xpath_or_selector: str, element_number=0) -> None:
        if element_number == 0:
            browser.element(xpath_or_selector).click()
        else:
            browser.all(xpath_or_selector)[element_number].click()

    @staticmethod
    def element(path) -> Element:
        return browser.element(path)

    @staticmethod
    def element_assert(path: str, conditions: list[Condition[Element]]) -> None:
        element = browser.element(path)
        errors: List[Exception] = []
        for condition in conditions:
            try:
                element.should(condition)
                return
            except Exception as e:
                errors.append(e)
        raise AssertionError('; '.join(map(str, errors)))

