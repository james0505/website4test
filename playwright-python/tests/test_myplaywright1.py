import re
import os, pathlib
import pytest
from playwright.sync_api import Page, expect

work_directory = pathlib.Path(os.getcwd()).as_uri()
@pytest.fixture(autouse = True)
def run_browser(page: Page):
    page.goto(f"{work_directory}/website-codes/index.html")

def test_load_main_page(page: Page):
    #page.goto("file:///E:/VS-Code-Projects/website4test/index.html")
    expect(page).to_have_title(re.compile("Website for teast"))
    
def test_button_clickme(page: Page):
    #page.goto("file:///E:/VS-Code-Projects/website4test/index.html")
    b1 = page.get_by_text(r"Click Me")
    # navbar-container > ul > li:nth-child(2) > a /html/body/div[1]/ul/li[2]/a
    #clickme_locator.hover()
    #b1 = page.locator("button", has_text="Click Me")
    b1.hover()
    computed_style = b1.evaluate('b1 => getComputedStyle(b1)')
    #print(f"output: {computed_style['backgroundColor']}")
    assert r"rgb(0, 100, 0)" in computed_style['backgroundColor']
    b1.click()
    expect(page.get_by_text(r"has been clicked")).to_be_visible()
    
def test_about_page(page: Page):
    #page.goto("file:///E:/VS-Code-Projects/website4test/index.html")
    #page.locator('[href*="#about"]').click()
    expect(page.get_by_text("This is an about page")).to_be_visible()
