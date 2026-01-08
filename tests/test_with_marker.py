import requests
import pytest

def test_get_posts(base_url):
    # GET 요청
    response = requests.get(f"{base_url}/posts")

    # 상태코드 체크
    assert response.status_code == 200

    # 역직렬화 (JSON → Python 객체)
    posts = response.json()

    # posts는 list
    assert isinstance(posts, list)

    # 리스트 출력
    for post in posts[:5]:  # 너무 많으니까 앞에 5개만
        print(post)

@pytest.mark.login
def test_sinmple1():
    assert 1+1 ==2
    
@pytest.mark.login
def test_sinmple2():
    assert 1+1 ==2
    
@pytest.mark.pika
def test_sinmple3():
    assert 1+1 ==2
