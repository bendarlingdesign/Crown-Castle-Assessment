import pytest
import logging
from selenium import webdriver
from checkers_game_functions import navigate_to_checkers_game, confirm_site_is_up, make_five_moves_as_orange, restart_game, confirm_restart

logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

checkers_url = "https://www.gamesforthebrain.com/game/checkers/"

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_checkers_game(driver):
    logging.info("Test case 'test_checkers_game' started.")
    navigate_to_checkers_game(driver)
    confirm_site_is_up(driver)
    make_five_moves_as_orange(driver)
    restart_game(driver)
    confirm_restart(driver)
    logging.info("Test case 'test_checkers_game' completed.")

if __name__ == "__main__":
    pytest.main(["-v", "tests_checkers_game_ui.py"])
