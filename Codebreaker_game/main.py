import game_logic
CODE_LEN = 4
MAX_ATTEMPTS = 10
possible_digits = [str(i) for i in range(10)]

def guess_code(attempts):
    while True:
        guess_str = input(f"Attempt {attempts}/{MAX_ATTEMPTS} - Enter your {CODE_LEN}-digit number: ")
        if len(guess_str) != CODE_LEN:
            print("Invalid length of the number.")
            continue
        if not guess_str.isdigit():
            print("Please enter only digits")
        valid_digit = True
        for digit in guess_str:
            if digit not in possible_digits:
                print(f"Invalid digit: '{digit}'.Only use digits from {possible_digits[0]}{possible_digits[-1]}")
                valid_digit = False
                break
        if not valid_digit:
            continue
        
        return list(guess_str)
def play_game():
    secret_code = game_logic.gen_code()
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        play_guess = guess_code(attempts + 1)
        attempts += 1
        if play_guess == secret_code:
            print(f"Congratulations You Won !!! in {attempts}-attempts")
            return
        bulls,cows = game_logic.number_guess_feedback(secret_code, play_guess)
        print(f"Bulls = {bulls}, Cows = {cows}")
        
    print("Game over !! You ran out of attempts.")
    print(f"The secret code was {secret_code}.")
    
if __name__ == "__main__":
    play_game()