import time
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename="checkers_test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def navigate_to_checkers_game(driver):
    url = "https://www.gamesforthebrain.com/game/checkers/"
    driver.get(url)

def confirm_site_is_up(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Checkers"))
        logging.info("Step 2: Site is up and running.")
    except Exception as e:
        logging.error("Step 2: Site is not accessible.")
        logging.error(str(e))
        driver.quit()

def make_five_moves_as_orange(driver):
    for move in range(5):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "board")))

        orange_pieces = driver.find_elements(By.CSS_SELECTOR, "div.piece.orange")
        valid_moves = driver.find_elements(By.CSS_SELECTOR, "div.highlight.valid")
        
        if not orange_pieces or not valid_moves:
            logging.info("No valid moves left.")
            break
        
        #Perform a move
        orange_piece = orange_pieces[0]
        target_move = valid_moves[0]
        orange_piece.click()
        time.sleep(1)  #Wait for animation
        target_move.click()
        time.sleep(1)

        #Confirm the move
        make_move_button = driver.find_element(By.ID, "make-move")
        make_move_button.click()
        time.sleep(1)

def restart_game(driver):
    try:
        restart_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/p[2]/a[1]")
        restart_button.click()
        time.sleep(1)
        logging.info("Step 3c: Game restarted.")
    except Exception as e:
        logging.error("Step 3c: Failed to restart the game.")
        logging.error(str(e))

def confirm_restart(driver):
    orange_pieces_after_restart = driver.find_elements(By.CSS_SELECTOR, "div.piece.orange")
    if not orange_pieces_after_restart:
        logging.info("Step 3d: Game restarted successfully.")
    else:
        logging.error("Step 3d: Game restart failed.")

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    log_file_handler = logging.FileHandler("checkers_test.log")

    console_handler = logging.StreamHandler()

    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    log_file_handler.setFormatter(log_formatter)
    console_handler.setFormatter(log_formatter)

    logger.addHandler(log_file_handler)
    logger.addHandler(console_handler)