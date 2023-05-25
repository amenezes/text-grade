import pytest
import spacy

from text_grade import Document

TEXT = """
PREÂMBULO

Nós, representantes do povo brasileiro, reunidos em Assembléia Nacional Constituinte para instituir um Estado Democrático, destinado a assegurar o exercício dos direitos sociais e individuais, a liberdade, a segurança, o bem-estar, o desenvolvimento, a igualdade e a justiça como valores supremos de uma sociedade fraterna, pluralista e sem preconceitos, fundada na harmonia social e comprometida, na ordem interna e internacional, com a solução pacífica das controvérsias, promulgamos, sob a proteção de Deus, a seguinte CONSTITUIÇÃO DA REPÚBLICA FEDERATIVA DO BRASIL.
"""


@pytest.fixture(scope="module")
def nlp():
    nlp = spacy.load("pt_core_news_sm")
    return nlp


@pytest.fixture(scope="module")
def document(nlp):
    return Document(nlp(TEXT))
