from typing import Set, List


def sentence_to_words(sentence: str) -> Set[str]:
    words: Set[str] = set()
    for word in sentence.split():
        words.add(word)
    return words


def sentences_to_words(sentences: List[str]) -> Set[str]:
    words: Set[str] = set()
    for sentence in sentences:
        words = words.union(sentence_to_words(sentence))
    return words


def main() -> None:
    sentences: List[str] = [
        "A carteira colocou a carteira na carteira",
        "O carteiro não tem carteira",
        "O carteiro comprou uma carteira nova"
    ]

    vocabulario: Set[str] = sentences_to_words(sentences)
    print(vocabulario)


if __name__ == "__main__":
    main()
