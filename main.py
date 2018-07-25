import copy

from utils import INITIAL_ATTEMPTS, ATTEMPT_KEY, WORD_KEY, WORD_VISIBILITY_KEY, hide_invisible_words, display_state, \
    get_player_input
from words_source import WordsSource


def initialize_state(word):
    return {
        ATTEMPT_KEY: INITIAL_ATTEMPTS,
        WORD_KEY: word,
        WORD_VISIBILITY_KEY: [False] * len(word)
    }


def play(state, player_input):
    res_state = copy.deepcopy(state)
    res_state[ATTEMPT_KEY] = res_state[ATTEMPT_KEY] - 1

    if type(player_input) is str and len(player_input) > 1:
        return res_state, player_input.lower().strip() == state[WORD_KEY].lower().strip()

    guessed_letters = [
        x == player_input and not state[WORD_VISIBILITY_KEY][i]
        for (i, x) in enumerate(state[WORD_KEY])
    ]

    res_state[WORD_VISIBILITY_KEY] = [
        guessed_letters[i] or state[WORD_VISIBILITY_KEY][i]
        for i in range(len(guessed_letters))
    ]

    return res_state, all(res_state[WORD_VISIBILITY_KEY])


def run_game():
    word = WordsSource().random_word()

    state = initialize_state(word)
    right_guess = False

    while state[ATTEMPT_KEY] > 0 and not right_guess:
        display_state(state)
        player_input = get_player_input()
        state, right_guess = play(state, player_input)

    if right_guess:
        print 'Congratulations, you won by guessing the word: {} in {} attempts.'.format(
            state[WORD_KEY], INITIAL_ATTEMPTS - state[ATTEMPT_KEY]
        )

    else:
        print 'Sorry, but you lost, you ran out of attempts. You got to {}.'.format(
            hide_invisible_words(state)
        )


if __name__ == '__main__':
    run_game()
