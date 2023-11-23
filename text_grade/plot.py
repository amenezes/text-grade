from typing import Any, Iterator

import pandas as pd

from text_grade._logger import logger
from text_grade.document import Document

try:
    import seaborn as sns
except ModuleNotFoundError:
    logger.warning("seaborn package not found!")


def _execute(func, *args, **kwargs) -> Any:
    try:
        return func(*args, **kwargs)
    except NameError as err:
        logger.error("seaborn package not found!")
        raise err


def characters_x_words(documents: Iterator[Document]):
    return _execute(
        sns.scatterplot,
        data=pd.concat([doc.to_df() for doc in documents]),
        x="n_words",
        y="n_characters",
    )


def characters_boxplot(documents: Iterator[Document]):
    return _execute(
        sns.boxplot,
        data=pd.DataFrame(
            [doc.characters() for doc in documents], columns=["characters"]
        ),
    )


def words_boxplot(documents: Iterator[Document]):
    return _execute(
        sns.boxplot,
        data=pd.DataFrame([doc.characters() for doc in documents], columns=["words"]),
    )


def sentences_boxplot(documents: Iterator[Document]):
    return _execute(
        sns.boxplot,
        data=pd.DataFrame(
            [doc.characters() for doc in documents], columns=["sentences"]
        ),
    )


def sentences_x_words(documents: Iterator[Document]):
    return _execute(
        sns.relplot,
        data=pd.concat([doc.to_df() for doc in documents]),
        x="n_sentences",
        y="n_words",
    )


def words_x_characters(documents: Iterator[Document]):
    return _execute(
        sns.relplot,
        data=pd.concat([doc.to_df() for doc in documents]),
        x="n_words",
        y="n_characters",
    )


def words_x_sentences(documents: Iterator[Document]):
    return _execute(
        sns.scatterplot,
        data=pd.concat([doc.to_df() for doc in documents]),
        x="n_sentences",
        y="n_words",
    )


def syllables_x_words(documents: Iterator[Document]):
    return _execute(
        sns.scatterplot,
        data=pd.concat([doc.to_df() for doc in documents]),
        x="n_words",
        y="syllables",
    )


def unique_words_distribution(documents: Iterator[Document]):
    raise NotImplementedError


def score_count(documents: Iterator[Document], formula):
    return _execute(
        sns.countplot,
        data=pd.DataFrame(
            [
                (score.value, str(score.grade))
                for score in [formula(doc) for doc in documents]
            ],
            columns=["value", "score"],
        ),
        x="score",
    )


def score_stripplot(documents: Iterator[Document], formula):
    return _execute(
        sns.stripplot,
        data=pd.DataFrame(
            [
                (score.value, str(score.grade))
                for score in [formula(doc) for doc in documents]
            ],
            columns=["value", "score"],
        ),
        x="score",
        y="value",
    )


def score_boxplot(documents: Iterator[Document], formula):
    return _execute(
        sns.boxplot,
        data=pd.DataFrame(
            [
                (score.value, str(score.grade))
                for score in [formula(doc) for doc in documents]
            ],
            columns=["value", "score"],
        ),
        x="score",
        y="value",
    )
