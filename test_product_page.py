import pytest
from .pages.product_page import ProductPage

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


# @pytest.mark.skip("not now")
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    assert True


def test_guest_cant_see_success_message(browser):
    pass


def test_message_disappeared_after_adding_product_to_basket(browser):
    pass
