import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.BoardApi import BoardApi

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    
    with allure.step("Закрыть браузер"):
        browser.quit()
        

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "61790ff29348904bc42217da/ATTSuG9eBENjDVWwfSBeZYy87yFvmtn3tzC5BZDqAp3grYKklpMHzlXdbU01zpzdRS9h83679F3F")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "")

@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi("https://api.trello.com/1", "61790ff29348904bc42217da/ATTSuG9eBENjDVWwfSBeZYy87yFvmtn3tzC5BZDqAp3grYKklpMHzlXdbU01zpzdRS9h83679F3F")
    resp = api.create_board("Board to be deleted").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary
    
    api = BoardApi("https://api.trello.com/1", "61790ff29348904bc42217da/ATTSuG9eBENjDVWwfSBeZYy87yFvmtn3tzC5BZDqAp3grYKklpMHzlXdbU01zpzdRS9h83679F3F")
    api.delete_board_by_id(dictionary.get("board_id"))

