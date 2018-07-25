from words_source import WordsSource

INITIAL_ATTEMPTS = 9

ATTEMPT_KEY = 'attempts'
WORD_KEY = 'word'
WORD_VISIBILITY_KEY = 'word_visibiliy'


def initialize_state(word):
    return {
        ATTEMPT_KEY: INITIAL_ATTEMPTS,
        WORD_KEY: word,
        WORD_VISIBILITY_KEY: [False] * len(word)
    }


def _hide_invisible_words(state):

    res = ['_'] * len(state[WORD_KEY])
    for i, v in enumerate(state[WORD_VISIBILITY_KEY]):
        if v:
            res[i] = state[WORD_KEY][i]

    return ''.join(res)


def display_state(state):
    print 'You still have {} attempts to guess.\n' \
              '{}\n'.format(state[ATTEMPT_KEY], _hide_invisible_words(state))


def get_player_input():
    return raw_input('Please insert your letter or attempt to guess the word. Then press enter.')


def play(state, player_input):
    if type(player_input) is str and len(player_input) > 1:
        return {
            ATTEMPT_KEY: state[ATTEMPT_KEY] - 1,
            WORD_KEY: state[WORD_KEY],
            WORD_VISIBILITY_KEY: [True] * len(state[WORD_KEY])
        }, player_input.lower().strip() == state[WORD_KEY].lower().strip()

    has_guessed = [
        x == player_input and not state[WORD_VISIBILITY_KEY][i]
        for (i, x) in enumerate(state[WORD_KEY])
    ]

    res_state = {
        ATTEMPT_KEY: state[ATTEMPT_KEY] - 1,
        WORD_KEY: state[WORD_KEY],
        WORD_VISIBILITY_KEY: [
            has_guessed[i] or state[WORD_VISIBILITY_KEY][i]
            for i in range(len(has_guessed))
        ]
    }

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
            state[WORD_KEY], state[ATTEMPT_KEY]
        )

    else:
        print 'Sorry, but you lost, you ran out of attempts. You got to {}'.format(
            _hide_invisible_words(state)
        )


if __name__ == '__main__':
    run_game()