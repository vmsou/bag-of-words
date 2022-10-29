import pandas as pd
from typing import List

from vocabulary import Vocabulary
from corpus.scraper import Article, sentences_from_site

DEFAULT_ARTICLES: List[Article] = [
    Article(
        title="Natural language processing: an introduction",
        link="https://academic.oup.com/jamia/article/18/5/544/829676?ref=https%3A%2F%2Fcodemonkey.link&login=false"
    ),
    Article(
        title="Your Guide to Natural Language Processing (NLP)",
        link="https://www.datasciencecentral.com/your-guide-to-natural-language-processing-nlp/"
    ),
    Article(
        title="Natural language processing: State of the art, current trends and challenges",
        link="https://link.springer.com/article/10.1007/s11042-022-13428-4"
    ),
    Article(
        title="Overview of Artificial Intelligence and Role of Natural Language Processing in Big Data",
        link="https://www.datasciencecentral.com/overview-of-artificial-intelligence-and-role-of-natural-language"
    ),
    Article(
        title="Natural Language Processing (NLP)",
        link="https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"
    )
]


def main() -> None:
    sentences: List[str] = [
        "A carteira colocou a carteira na carteira.",
        "O carteiro não tem carteira.",
        "O carteiro comprou uma carteira nova."
    ]

    articles: list[Article] = DEFAULT_ARTICLES.copy()

    print("[Articles]".center(80, '-'))
    for article in articles:
        print(f"{article.title}: {article.link}")
    print("".center(80, '-'))

    all_sentences: List[List[str]] = []

    for article in articles:
        url: str = article.link
        current_sentences: List[str] = sentences_from_site(url)
        print(f"{article.title}({article.link}): {len(current_sentences)} sentences.")
        start: int = len(current_sentences) // 4
        for report in current_sentences[start:start + 3]:
            print(f"> '{report}'")
        print("...\n")
        all_sentences.append(current_sentences)

    # Generate vocabulary from sentences
    vocabulary: Vocabulary[str] = Vocabulary.texts_to_vocabulary(sentences)

    # Generate Document-term matrix
    matrix: pd.DataFrame = vocabulary.to_matrix(sentences)

    print(matrix.head(3))


if __name__ == "__main__":
    main()
