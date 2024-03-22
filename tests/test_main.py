from app.main import obtenir_citation

def test_obtenir_citation():
    citation = obtenir_citation()
    assert citation is not None
    assert type(citation) == str
