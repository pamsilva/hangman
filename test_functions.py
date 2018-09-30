from main import play
from utils import ATTEMPT_KEY, WORD_KEY, WORD_VISIBILITY_KEY, hide_invisible_letters


def test_hide_invisible_words():
    initial_state = {
        ATTEMPT_KEY: 7,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    expected = '_o_a__'

    assert hide_invisible_letters(initial_state) == expected


def test_play_iterative():
    initial_state = {
        ATTEMPT_KEY: 7,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    player_input = 'p'

    expected_state = {
        ATTEMPT_KEY: 6,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            True, True, False, True, False, False
        ],
    }
    expected_right_guess = False

    res_state, res_right_guess = play(initial_state, player_input)

    assert expected_right_guess == res_right_guess
    assert expected_state == res_state


def test_play_whole_word():
    initial_state = {
        ATTEMPT_KEY: 7,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    player_input = 'potato'

    expected_state = {
        ATTEMPT_KEY: 6,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    expected_right_guess = True

    res_state, res_right_guess = play(initial_state, player_input)

    assert expected_right_guess == res_right_guess
    assert expected_state == res_state


def test_play_failed_attempt():
    initial_state = {
        ATTEMPT_KEY: 7,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    player_input = 'x'

    expected_state = {
        ATTEMPT_KEY: 6,
        WORD_KEY: 'potato',
        WORD_VISIBILITY_KEY: [
            False, True, False, True, False, False
        ],
    }
    expected_right_guess = False

    res_state, res_right_guess = play(initial_state, player_input)

    assert expected_right_guess == res_right_guess
    assert expected_state == res_state
