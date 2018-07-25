INITIAL_ATTEMPTS = 9
ATTEMPT_KEY = 'attempts'
WORD_KEY = 'word'
WORD_VISIBILITY_KEY = 'word_visibiliy'


def hide_invisible_words(state):

    res = ['_'] * len(state[WORD_KEY])
    for i, v in enumerate(state[WORD_VISIBILITY_KEY]):
        if v:
            res[i] = state[WORD_KEY][i]

    return ''.join(res)


def display_state(state):
    print 'You still have {} attempts to guess.\n' \
              '{}\n'.format(state[ATTEMPT_KEY], hide_invisible_words(state))


def get_player_input():
    return raw_input(
        'Please insert your letter or attempt to guess the word. '
        'Then press enter:\n'
    )
