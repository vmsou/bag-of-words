import pandas as pd
from typing import List

from vocabulary import Vocabulary


def main() -> None:
    sentences: List[str] = [
        "A carteira colocou a carteira na carteira.",
        "O carteiro não tem carteira.",
        "O carteiro comprou uma carteira nova."
    ]

    # Generate vocabulary from sentences
    vocabulary: Vocabulary[str] = Vocabulary.texts_to_vocabulary(sentences)

    # Generate Document-term matrix
    matrix: pd.DataFrame = vocabulary.to_matrix(sentences)

    print(matrix.head(3))


if __name__ == "__main__":
    main()
