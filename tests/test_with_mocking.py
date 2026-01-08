"""
이 테스트의 목적

1. jsonplaceholder에 POST 요청을 보내는 코드가 있다고 가정
2. 실제 네트워크 요청은 보내지 않는다
3. requests.post를 mock으로 가로채서
4. 우리가 정한 가짜 응답(mock data)을 반환하게 만든다
5. 코드가 '정상 동작하는지'만 검증한다

=> 외부 API, 네트워크 상태와 완전히 분리된 테스트
"""

import requests


def create_post(base_url, payload):
    """
    실제 서비스 코드라고 가정
    - jsonplaceholder에 POST 요청을 보냄
    """
    response = requests.post(f"{base_url}/posts", json=payload)
    return response.json()


def test_create_post_with_mock(mocker):
    # -----------------------------
    # 1️⃣ mock으로 돌려줄 가짜 응답 데이터
    # -----------------------------
    mock_response_data = {
        "userId": 1,
        "id": 101,
        "title": "mocked title",
        "body": "mocked body"
    }

    # -----------------------------
    # 2️⃣ requests.post를 mock으로 가로채기
    # -----------------------------
    # requests.post가 호출되면
    # 실제 HTTP 요청 ❌
    # 대신 mock 객체가 실행됨
    mock_post = mocker.patch("requests.post")

    # -----------------------------
    # 3️⃣ mock 객체의 동작 정의
    # -----------------------------
    # requests.post(...)의 반환값(response)을 흉내냄
    mock_post.return_value.json.return_value = mock_response_data
    mock_post.return_value.status_code = 201

    # -----------------------------
    # 4️⃣ 테스트 실행
    # -----------------------------
    base_url = "https://jsonplaceholder.typicode.com"

    payload = {
        "title": "real title",
        "body": "real body",
        "userId": 1
    }

    result = create_post(base_url, payload)

    # -----------------------------
    # 5️⃣ 결과 검증
    # -----------------------------
    # 실제 서버 응답이 아니라
    # 우리가 위에서 정의한 mock 데이터가 반환됨
    assert result["id"] == 101
    assert result["title"] == "mocked title"

    # -----------------------------
    # 6️⃣ requests.post가 호출됐는지 확인
    # -----------------------------
    mock_post.assert_called_once()

    # 어떤 URL과 payload로 호출됐는지도 확인 가능
    mock_post.assert_called_with(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
