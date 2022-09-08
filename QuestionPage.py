from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Создаем класс FireFoxLocators. Он будет только для хранения локаторов.
# В классе описываем локаторы:
class FireFoxLocators:
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    LOCATOR_FIRST_QUESTION_BUTTON = (By.ID, "accordion__heading-0")
    LOCATOR_SECOND_QUESTION_BUTTON = (By.ID, "accordion__heading-1")
    LOCATOR_THIRD_QUESTION_BUTTON = (By.ID, "accordion__heading-2")
    LOCATOR_FOURTH_QUESTION_BUTTON = (By.ID, "accordion__heading-3")
    LOCATOR_FIFTH_QUESTION_BUTTON = (By.ID, "accordion__heading-4")
    LOCATOR_SIXTH_QUESTION_BUTTON = (By.ID, "accordion__heading-5")
    LOCATOR_SEVENTH_QUESTION_BUTTON = (By.ID, "accordion__heading-6")
    LOCATOR_EIGHTH_QUESTION_BUTTON = (By.ID, "accordion__heading-7")


# Создаем класс Question_Program, наследуемся от BasePage.
class Question_Program(BasePage):
    def do_first_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_COOKIE_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_FIRST_QUESTION_BUTTON).click()

    # В данных методах реализуем нажатие на кнопки.
    # P.S. В первом методе больше кликов, потому что кнопка куки мешает для нажатия.
    def do_second_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SECOND_QUESTION_BUTTON).click()

    def do_third_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_THIRD_QUESTION_BUTTON).click()

    def do_fourth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_FOURTH_QUESTION_BUTTON).click()

    def do_fifth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_FIFTH_QUESTION_BUTTON).click()

    def do_sixth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SIXTH_QUESTION_BUTTON).click()

    def do_seventh_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SEVENTH_QUESTION_BUTTON).click()

    def do_eighth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_EIGHTH_QUESTION_BUTTON).click()
