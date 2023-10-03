import requests
import logging

#Logging
logging.basicConfig(filename='card_game.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def log_and_print(message):
    logging.info(message)
    print(message)

def check_response(response):
    if response.status_code == 200:
        log_and_print(f"Response status code: {response.status_code} (OK)")
        return response.json()
    else:
        log_and_print(f"Response status code: {response.status_code} (Failed)")
        raise requests.exceptions.RequestException(f"Request failed with status code {response.status_code}")

try:
    #Step 1: Navigate to https://deckofcardsapi.com/
    log_and_print("Step 1: Navigating to https://deckofcardsapi.com/")

    #Step 3: Get a new deck
    new_deck_url = "https://deckofcardsapi.com/api/deck/new/"
    response = requests.get(new_deck_url)
    data = check_response(response)
    deck_id = data["deck_id"]
    log_and_print(f"Step 3: Got a new deck with ID: {deck_id}")

    #Step 4: Shuffle the deck
    shuffle_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
    response = requests.get(shuffle_url)
    data = check_response(response)
    log_and_print(f"Step 4: Shuffled the deck: {data['shuffled']}")

    #Step 5: Deal three cards to each of two players
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=6"
    response = requests.get(draw_url)
    data = check_response(response)
    cards = data["cards"]
    log_and_print(f"Step 5: Dealt cards - Player 1 Cards: {[card['code'] for card in cards[:3]]}")
    log_and_print(f"                  Player 2 Cards: {[card['code'] for card in cards[3:]]}")

    #Step 6: Check whether either has blackjack
    blackjack = False
    for player_cards in [cards[:3], cards[3:]]:
        values = [card["value"] for card in player_cards]
        if "ACE" in values and any(value in ["KING", "QUEEN", "JACK", "10"] for value in values):
            blackjack = True
            break

    #Step 7: If either has blackjack, write out which one does
    if blackjack:
        if "ACE" in values[:3]:
            log_and_print("Step 7: Player 1 has blackjack!")
        else:
            log_and_print("Step 7: Player 2 has blackjack!")
    else:
        log_and_print("Step 7: No one has blackjack.")

except requests.exceptions.RequestException as e:
    log_and_print(f"An error occurred during API request: {e}")

except Exception as e:
    log_and_print(f"An unexpected error occurred: {e}")
