from typing import Set, List, Generic, TypeVar, Iterable

_T = TypeVar("_T")


class Vocabulary(Generic[_T], Iterable):
    def __init__(self):
        self.data: List[_T] = []
        self.unique: Set[_T] = set()

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def add(self, __o: _T) -> None:
        """ Appends an unique element to list. """
        if __o in self.unique: return
        self.unique.add(__o)
        self.data.append(__o)

    def union(self, vec: Iterable[_T]) -> None:
        """ Adds all elements from vec to self. """
        for element in vec:
            self.add(element)

    @staticmethod
    def text_to_words(text: str) -> 'Vocabulary'[_T]:
        """ Converts text to words. """
        words: Vocabulary[str] = Vocabulary()
        for word in text.split():
            words.add(word)
        return words

    @staticmethod
    def texts_to_words(sentences: List[str]) -> 'Vocabulary'[_T]:
        words: Vocabulary[str] = Vocabulary()
        for sentence in sentences:
            words.union(Vocabulary.text_to_words(sentence))
        return words
