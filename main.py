"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Svobodová
email: stavby.hlavac@seznam.cz
"""
import random
import time

def generate_secret_number(): # vygeneruje čmísté číslo 
    digits = list("123456789")         # první číslice nesmí být nula
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    digits.append("0")                 # nula může být použita
    remaining_digits = random.sample(digits, 3)
    return first_digit + ''.join(remaining_digits)

def is_valid_guess(guess): # ověří platný tip
    if not guess.isdigit():
        print("Chyba: Vstup musí obsahovat pouze číslice.")
        return False
    if len(guess) != 4:
        print("Chyba: Číslo musí mít přesně 4 číslice.")
        return False
    if guess[0] == "0":
        print("Chyba: Číslo nesmí začínat nulou.")
        return False
    if len(set(guess)) != 4:
        print("Chyba: Číslice se nesmí opakovat.")
        return False
    return True

def count_bulls_and_cows(secret, guess): # spočítá počet bulls a crows
    bulls = sum(a == b for a, b in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def format_result(word, number): # vrátí správný tvar
  return f"{number} {word}" if number == 1 else f"{number} {word}s"

def play_game():
    # Úvodní přivítání a instrukce
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()  # Tajné číslo
    attempts = 0                              # Počet pokusů
    start_time = time.time()                  # Čas zahájení

    # Hlavní herní smyčka
    while True:
        guess = input(">>> ")
        if not is_valid_guess(guess):
            continue  # Pokud vstup není platný, pokračuj od začátku

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret_number, guess)

        if bulls == 4:
            # Hráč uhodl celé číslo správně
            elapsed_time = int(time.time() - start_time)
            print("-----------------------------------------------")
            print(f"Correct, you've guessed the right number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            print(f"Time taken: {elapsed_time} seconds.")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        else:
            # hráč hádal špatně, vypiš počet bulls a cows
            print(f"{format_result('bull', bulls)}, {format_result('cow', cows)}")
            print("-----------------------------------------------")

# spuštění hry
if __name__ == "__main__":
    play_game()
