import random
import requests
import Live


def get_money_interval(amount_before_convert):
    response = ''
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=4b2b892a350ba2fe7aa2"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as error:
        print("Error: ", error)

    amount_after_convert = response.json()['USD_ILS']
    t = int(amount_after_convert * amount_before_convert)
    return t-(5-Live.difficulty), t+(5-Live.difficulty)


def get_guess_from_user(amount_before_convert):
    return int(input(f"How much is {amount_before_convert} USD in ILS ? : "))


def play():
    amount_before_convert = random.randint(1, 100)
    min_amount, max_amount = get_money_interval(amount_before_convert)
    user_guess = get_guess_from_user(amount_before_convert)
    if (max_amount >= user_guess) and (min_amount <= user_guess):
       return True
    return False

