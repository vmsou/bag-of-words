"""
Aluno: Vinícius Marques da Silva de Oliveira

Sua tarefa será gerar a matriz termo documento, dos documentos recuperados da internet e
imprimir esta matriz na tela. Para tanto:

a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, onde cada item será uma das palavras da sentença.
b) Todos os vetores devem ser unidos em um corpus único formando uma lista de vetores, onde cada item será um lexema.
c) Este único corpus será usado para gerar o vocabulário.
d) O resultado esperado será uma matriz termo documento criada a partir da aplicação da técnica bag of Words em todo o corpus
"""

import pandas as pd
from typing import List

from vocabulary import Vocabulary
from corpus.scraper import Article, sentences_from_site

DEFAULT_ARTICLES: List[Article] = [
    Article(
        title="Your Guide to Natural Language Processing (NLP)",
        link="https://www.datasciencecentral.com/your-guide-to-natural-language-processing-nlp/"
    ),
    Article(
        title="Natural language processing: an introduction",
        link="https://academic.oup.com/jamia/article/18/5/544/829676?ref=https%3A%2F%2Fcodemonkey.link&login=false"
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


def sentences_from_articles(articles: List[Article]) -> List[List[str]]:
    articles_sentences: List[List[str]] = []
    for article in articles:
        url: str = article.link
        current_sentences: List[str] = sentences_from_site(url)
        print(f"{article.title}({article.link}): {len(current_sentences)} sentences.")
        start: int = len(current_sentences) // 4
        for report in current_sentences[start:start + 3]:
            print(f"> '{report}'")
        print("...\n")
        articles_sentences.append(current_sentences)
    return articles_sentences


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

    documents_sentences: List[List[str]] = sentences_from_articles(articles)
    if documents_sentences:
        # Flatten sentences
        sentences = [sentence for sentences in documents_sentences for sentence in sentences]

    # Generate vocabulary from sentences
    print("Generating vocabulary...", end=' ')
    vocabulary: Vocabulary[str] = Vocabulary.texts_to_vocabulary(sentences)
    print('Done.')

    # Generate Document-term matrix
    print("Generating Document-term matrix...", end=' ')
    matrix: pd.DataFrame = vocabulary.to_matrix(sentences)
    print("Done.")

    print(matrix.head(3))


if __name__ == "__main__":
    main()
