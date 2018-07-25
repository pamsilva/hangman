from random import randint


class WordsSource(object):
    def random_word(self):
        raise NotImplementedError('Abstract Class. Use a subclass instead.')


class WordsSourceMemory(WordsSource):
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
