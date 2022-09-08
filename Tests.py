import allure

from QuestionPage import Question_Program


class TestProgram:
    @allure.title('Тест первого вопроса')
    @allure.feature('First question')
    @allure.story('Проверяем первый вопрос')
    def test_first_question(self, browser):
        first_question = Question_Program(browser)
        first_question.go_to_site()
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        first_question.do_first_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-0")
        assert counter.text == "Сутки — 400 рублей. Оплата курьеру — наличными или " \
                               "картой."

    @allure.title('Тест второго вопроса')
    @allure.feature('Second question')
    @allure.story('Проверяем второй вопрос')
    def test_second_question(self, browser):
        second_question = Question_Program(browser)
        second_question.do_second_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-1")
        assert counter.text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, " \
                               "можете просто сделать несколько заказов — один за другим."

    @allure.title('Тест третьего вопроса')
    @allure.feature('Third question')
    @allure.story('Проверяем третий вопрос')
    def test_third_question(self, browser):
        third_question = Question_Program(browser)
        third_question.do_third_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-2")
        assert counter.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                               "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Тест четвертого вопроса')
    @allure.feature('Fourth question')
    @allure.story('Проверяем четвертый вопрос')
    def test_third_question(self, browser):
        fourth_question = Question_Program(browser)
        fourth_question.do_fourth_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-3")
        assert counter.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Тест пятого вопроса')
    @allure.feature('Fifth question')
    @allure.story('Проверяем пятый вопрос')
    def test_fourth_question(self, browser):
        fifth_question = Question_Program(browser)
        fifth_question.do_fifth_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-4")
        assert counter.text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по " \
                               "красивому номеру 1010."

    @allure.title('Тест шестого вопроса')
    @allure.feature('Sixth question')
    @allure.story('Проверяем шестой вопрос')
    def test_sixth_question(self, browser):
        sixth_question = Question_Program(browser)
        sixth_question.do_sixth_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-5")
        assert counter.text == "Самокат приезжает к вам с полной зарядкой. " \
                               "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
                               "Зарядка не понадобится."

    @allure.title('Тест седьмого вопроса')
    @allure.feature('Seventh question')
    @allure.story('Проверяем седьмой вопрос')
    def test_seventh_question(self, browser):
        seventh_question = Question_Program(browser)
        seventh_question.do_seventh_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-6")
        assert counter.text == "Да, пока самокат не привезли. " \
                               "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Тест восьмого вопроса')
    @allure.feature('Eighth question')
    @allure.story('Проверяем восьмой вопрос')
    def test_eighth_question(self, browser):
        eighth_question = Question_Program(browser)
        eighth_question.do_eighth_question()
        counter = browser.find_element_by_css_selector("#accordion__panel-7")
        assert counter.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
