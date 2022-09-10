import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from QuestionPage import Question_Program, Main_Page, Form_Order, About_Rent, YandexButton
from selenium.webdriver.common.by import By


# Создаем тестовый класс и методы
class TestProgram:
    @allure.title('Тест первого вопроса')
    @allure.feature('First question')
    @allure.story('Проверяем первый вопрос')
    def test_first_question(self, browser):
        first_question = Question_Program(browser)  # Создаем экземпляр класса first_question
        first_question.go_to_site()  # Запускаем сайт, это делается только один раз!
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")  # Здесь пришлось делать скрипт, для того чтобы
        # страница скроллилась вниз, иначе все это не работает!!
        first_question.do_first_question()  # Запускаем первый метод на проверку
        label = browser.find_element(By.CSS_SELECTOR,
                                     "#accordion__panel-0")  # это тоже больше костыль конечно, но он нужен чтобы
        # считывать текст с label'ов
        assert label.text == "Сутки — 400 рублей. Оплата курьеру — наличными или " \
                             "картой."

    # Ну в принципе тут методы все фактически одинаковые, единственно что фикстуры allure разные
    @allure.title('Тест второго вопроса')
    @allure.feature('Second question')
    @allure.story('Проверяем второй вопрос')
    def test_second_question(self, browser):
        second_question = Question_Program(browser)
        second_question.do_second_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-1")
        assert label.text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, " \
                             "можете просто сделать несколько заказов — один за другим."

    @allure.title('Тест третьего вопроса')
    @allure.feature('Third question')
    @allure.story('Проверяем третий вопрос')
    def test_third_question(self, browser):
        third_question = Question_Program(browser)
        third_question.do_third_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-2")
        assert label.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                             "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                             "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Тест четвертого вопроса')
    @allure.feature('Fourth question')
    @allure.story('Проверяем четвертый вопрос')
    def test_fourth_question(self, browser):
        fourth_question = Question_Program(browser)
        fourth_question.do_fourth_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-3")
        assert label.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Тест пятого вопроса')
    @allure.feature('Fifth question')
    @allure.story('Проверяем пятый вопрос')
    def test_fifth_question(self, browser):
        fifth_question = Question_Program(browser)
        fifth_question.do_fifth_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-4")
        assert label.text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по " \
                             "красивому номеру 1010."

    @allure.title('Тест шестого вопроса')
    @allure.feature('Sixth question')
    @allure.story('Проверяем шестой вопрос')
    def test_sixth_question(self, browser):
        sixth_question = Question_Program(browser)
        sixth_question.do_sixth_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-5")
        assert label.text == "Самокат приезжает к вам с полной зарядкой. " \
                             "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
                             "Зарядка не понадобится."

    @allure.title('Тест седьмого вопроса')
    @allure.feature('Seventh question')
    @allure.story('Проверяем седьмой вопрос')
    def test_seventh_question(self, browser):
        seventh_question = Question_Program(browser)
        seventh_question.do_seventh_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-6")
        assert label.text == "Да, пока самокат не привезли. " \
                             "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Тест восьмого вопроса')
    @allure.feature('Eighth question')
    @allure.story('Проверяем восьмой вопрос')
    def test_eighth_question(self, browser):
        eighth_question = Question_Program(browser)
        eighth_question.do_eighth_question()
        label = browser.find_element(By.CSS_SELECTOR, "#accordion__panel-7")
        assert label.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @allure.title('Тест кнопки заказать')
    @allure.feature('Test button')
    @allure.story('Проверяем кнопку заказать')
    def test_click_button_top(self, browser):
        main = Main_Page(browser)  # Создаем экземпляр класса main.
        browser.refresh()
        main.click_to_order_top()  # Нажимаем на кнопку заказать.

    @allure.title('Заполнение имени')
    @allure.feature('Filling out name')
    @allure.story('Заполняем имя и фамилию')
    def test_fill_out_name(self, browser):
        write_in_name = Form_Order(browser)  # Создаем экземпляр класса write_in_name.
        write_in_name.fill_name()  # Заполняем данным методом имя и фамилию.

    @allure.title('Заполнение адреса')
    @allure.feature('Filling out address')
    @allure.story('Заполняем адрес')
    def test_fill_out_address(self, browser):
        write_in_address = Form_Order(browser)  # Создаем экземпляр класса write_in_address.
        write_in_address.fill_address()  # Заполняем данным методом адрес и метро.

    @allure.title('Заполнение телефона')
    @allure.feature('Filling out phone number')
    @allure.story('Заполняем номер телефона')
    def test_fill_out_phone(self, browser):
        write_in_phone = Form_Order(browser)  # Создаем экземпляр класса write_in_phone.
        write_in_phone.fill_phone()  # Заполняем данным методом телефон, нажимаем на кнопку.

    @allure.title('Проверка заполнения данных')
    @allure.feature('Checking the filling of data')
    @allure.story('Проверяем, что заполнили данные')
    def test_check_order(self, browser):
        test = browser.find_element(By.CLASS_NAME,
                                    "Order_Header__BZXOb")  # В данном методе проверяем, что мы перешли в следующее
        # окно (Про Аренду).
        assert test.text == "Про аренду"

    @allure.title('Заполнение "про аренду"')
    @allure.feature('Fill "about rent"')
    @allure.story('Заполняем "про аренду"')
    def test_fill_rent(self, browser):
        write_in_rent = About_Rent(browser)  # Создаем экземпляр класса write_in_rent.
        write_in_rent.fill_date()  # Заполняем данным методом дату.
        write_in_rent.fill_other()  # Заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.

    @allure.title('Проверка оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)  # Создаем экземпляр класса check.
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")  # Ищу
        # кнопку, так как текст динамичен, и номер заказа не предугадать.
        assert test.text == "Посмотреть статус"  # Проверяем по тексту с кнопки.
        check.check_status()  # Нажимаем на кнопку "Проверить статус".

    @allure.title('Проверка кнопок Яндекса')
    @allure.feature('Check Yandex buttons')
    @allure.story('Проверяем кнопки Яндекса"')
    def test_yandex_buttons(self, browser):
        click = YandexButton(browser)  # Создаем экземпляр класса click.
        click.click_on_scooter_button()  # Нажимаем на кнопку "Самокаты".
        url = browser.current_url  # Берем текущий url, чтобы сверить, верно ли все произошло.
        assert url == 'https://qa-scooter.praktikum-services.ru/'  # Сравниваем url'ы.
        click.click_on_yandex_button()  # Нажимаем на кнопку "Яндекс".
        browser.switch_to.window(browser.window_handles[1])  # Переключаемся на страницу "Яндекса".
        WebDriverWait(browser, 15).until(ec.url_changes("about:blank"))
        url = browser.current_url  # Берем текущий url, чтобы сверить, верно ли все произошло.
        browser.close()  # Закрываем окно "Яндекс".
        assert url == 'https://yandex.ru/'  # Сравниваем url'ы.
        browser.switch_to.window(browser.window_handles[0])  # Переходим обратно в "основное" окно.

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем кнопку заказ(нижняя)"')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)  # Создаем экземпляр класса order_form.
        element = browser.find_element(By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")  #
        # Кнопка "Заказать" нижняя.
        browser.execute_script("arguments[0].scrollIntoView();", element)  # Здесь пришлось делать скрипт, для того
        # чтобы страница скроллилась вниз, до нашего элемента!
        order_form.click_to_order_down()  # Нажимаем на кнопку заказать.
        fill_form = Form_Order(browser)  # Создаем экземпляр класса fill_form
        fill_form.fill_name()  # Заполняем данным методом имя и фамилию.
        fill_form.fill_address()  # Заполняем данным методом адрес и метро.
        fill_form.fill_phone()  # Заполняем данным методом телефон, нажимаем на кнопку.
        test = browser.find_element(By.CLASS_NAME, "Order_Header__BZXOb")  # Проверяем, что мы перешли в следующее
        # окно (Про Аренду).
        assert test.text == "Про аренду"

    @allure.title('Проверка оформления заказа(нижняя кнопка) ')
    @allure.feature('Fill "for rent"(down)')
    @allure.story('Проверяем оформление заказа(нижняя кнопка)"')
    def test_about_rent_down(self, browser):
        write_in_rent = About_Rent(browser)  # Создаем экземпляр класса write_in_rent.
        write_in_rent.fill_date()  # Заполняем данным методом дату.
        write_in_rent.fill_other()  # Заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.
        check = About_Rent(browser)  # Создаем экземпляр класса check.
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")  # Ищу
        # кнопку, так как текст динамичен, и номер заказа не предугадать.
        assert test.text == "Посмотреть статус"  # Проверяем по тексту с кнопки.
        check.check_status()  # Нажимаем на кнопку "Проверить статус".
