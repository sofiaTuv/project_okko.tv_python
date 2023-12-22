from selene import browser, Element


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
