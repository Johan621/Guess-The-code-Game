import random
def gen_code():
    """
    Generates a secret code based on settings in config.py.
    Duplicates are allowed as per the original example.
    Returns a list of strings (digits).
    """
    code = ''
    for _ in range(4):
        code += str(random.randint(0,9))
    return code



def number_guess_feedback(secret_code, player_guess):
    """
    Calculates the number of bulls and cows for a given guess.
    - secret_code: The list of strings representing the secret code.
    - player_guess: The list of strings representing the player's guess.
    Returns a tuple: (bulls, cows)
    """
#Hera bulls indicates that if guessed number has any one or more digit same and in correct position
# then bulls count increases and if it has correct digit but in wrong place or location then cows increases
    bulls = 0
    cows = 0
    unmatched_secret = []
    unmatched_guess = []
    for i in range(4):
        if player_guess[i] == secret_code[i]:
            bulls += 1
        else:
            unmatched_guess.append(player_guess[i])
            unmatched_secret.append(secret_code[i])
    for i in unmatched_guess:
        if i in unmatched_secret:
            cows += 1
            unmatched_secret.remove(i)

    return bulls, cows