from selenium import webdriver
import time
import math


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector(
        "button.btn-add-to-basket"), "Кнопки добавления в корзину нет"


if __name__ == "__main__":
    pytest.main()
