import requests

def test_local_get_hello(base_url_local):
    """
    로컬 API(/hello) GET 테스트
    """
    url = f"{base_url_local}/hello"

    response = requests.get(url)

    assert response.status_code == 200

    # /hello 는 문자열만 내려준다고 가정 
    # assert response.text == "hello"