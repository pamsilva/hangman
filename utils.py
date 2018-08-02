INITIAL_ATTEMPTS = 9
ATTEMPT_KEY = 'attempts'
WORD_KEY = 'word'
WORD_VISIBILITY_KEY = 'word_visibiliy'


def hide_invisible_letters(state):
    res = [state[WORD_KEY][i] if v else '_' for (i, v) in enumerate(state[WORD_VISIBILITY_KEY])]
    return ''.join(res)


def display_state(state):
    print 'You still have {} attempts to guess.\n' \
              '{}\n'.format(state[ATTEMPT_KEY], hide_invisible_letters(state))


def get_player_input():
    return raw_input(
        'Please insert your letter or attempt to guess the word. '
        'Then press enter:\n'
    )


def initialize_state(word):
    return {
        ATTEMPT_KEY: INITIAL_ATTEMPTS,
        WORD_KEY: word,
        WORD_VISIBILITY_KEY: [False] * len(word)
    }