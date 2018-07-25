from random import randint


class WordsSource(object):
    WORD_LIST = [
        'potato',
        'pizza',
        'pasta',
        'pomegranate',
        'apple'
    ]

    def random_word(self):
        return self.WORD_LIST[
            randint(0, len(self.WORD_LIST))
        ]
