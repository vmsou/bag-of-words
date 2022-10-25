from typing import Set, List, Generic, TypeVar, Iterable

_T = TypeVar("_T")


class UniqueList(Generic[_T], Iterable):
    def __init__(self):
        self.data: List[_T] = []
        self.unique: Set[_T] = set()

    def __str__(self): return str(self.data)

    def __len__(self): return len(self.data)

    def __iter__(self): return iter(self.data)

    def add(self, __o: _T) -> None:
        if __o in self.unique: return
        self.unique.add(__o)
        self.data.append(__o)

    def union(self, vec: Iterable[_T]) -> None:
        for element in vec:
            self.add(element)


def sentence_to_words(sentence: str) -> UniqueList[str]:
    words: UniqueList[str] = UniqueList()
    for word in sentence.split():
        words.add(word)
    return words


def sentences_to_words(sentences: List[str]) -> UniqueList[str]:
    words: UniqueList[str] = UniqueList()
    for sentence in sentences:
        words.union(sentence_to_words(sentence))
    return words


def main() -> None:
    sentences: List[str] = [
        "A carteira colocou a carteira na carteira",
        "O carteiro não tem carteira",
        "O carteiro comprou uma carteira nova"
    ]

    vocabulary: UniqueList[str] = sentences_to_words(sentences)
    print(vocabulary)


if __name__ == "__main__":
    main()
