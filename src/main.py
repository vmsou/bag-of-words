from typing import List

from vocabulary import Vocabulary


def main() -> None:
    sentences: List[str] = [
        "A carteira colocou a carteira na carteira",
        "O carteiro não tem carteira",
        "O carteiro comprou uma carteira nova"
    ]

    vocabulary: Vocabulary[str] = Vocabulary.texts_to_vocabulary(sentences)
    print(vocabulary)

    for sentence in sentences:
        print(vocabulary.vectorize(sentence))


if __name__ == "__main__":
    main()
