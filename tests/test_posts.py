import pytest

def test_get_allposts(client):
    resp = client.get('/posts')
    assert resp.status_code == 200
    assert len(resp.json()) == 100

@pytest.mark.smoke
def test_get_single_post(client):
    resp = client.get('/posts/1')
    assert resp.status_code == 200
    body = resp.json()
    assert body['title'] == 1
    assert "title" in body

def test_create_post(client):
    resp = client.post('/posts',json={'title':'qa','body':'x','userId': 1})
    assert resp.status_code == 201


