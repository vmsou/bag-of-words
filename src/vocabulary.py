from __future__ import annotations
from typing import Set, List, Generic, TypeVar, Iterable, Dict

import pandas as pd

_T = TypeVar("_T")


def text_to_words(text: str) -> list[str]:
    """ TODO: Better word separator. """
    return text.split()


class Vocabulary(Generic[_T], Iterable):
    def __init__(self):
        self.data: List[_T] = []
        self.unique: Set[_T] = set()
        self.position: Dict[_T, int] = dict()

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def index(self, item: _T): return self.position[item]

    def add(self, __o: _T) -> None:
        """ Appends an unique element to list. """
        if __o in self.unique: return
        self.position[__o] = len(self.data)
        self.unique.add(__o)
        self.data.append(__o)

    def union(self, vec: Iterable[_T]) -> None:
        """ Adds all elements from vec to self. """
        for element in vec:
            self.add(element)

    def vectorize(self, text: str) -> list[int]:
        vector: list[int] = [0 for _ in range(len(self.data))]
        for word in text_to_words(text):
            print(word, end=' ')
            vector[self.index(word)] += 1
        print()
        return vector

    def to_matrix(self, sentences: list[str]) -> pd.DataFrame:
        """ Converts data to Document-term matrix. """
        matrix: pd.DataFrame = pd.DataFrame(columns=self.data)
        for i in range(len(sentences)):
            sentence: str = sentences[i]
            vector: List[int] = self.vectorize(sentence)
            matrix.loc[i + 1] = vector
        return matrix

    @staticmethod
    def text_to_vocabulary(text: str) -> 'Vocabulary'[_T]:
        """ Converts text to words. """
        words: Vocabulary[str] = Vocabulary()
        for word in text_to_words(text):
            words.add(word)
        return words

    @staticmethod
    def texts_to_vocabulary(sentences: List[str]) -> Vocabulary[_T]:
        words: Vocabulary[str] = Vocabulary()
        for sentence in sentences:
            words.union(Vocabulary.text_to_vocabulary(sentence))
        return words
