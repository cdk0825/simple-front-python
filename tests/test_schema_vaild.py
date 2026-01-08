"""
이 테스트의 목적

1. 외부 API(jsonplaceholder)에 GET 요청을 보낸다
2. 응답을 JSON → Python 객체(dict)로 변환한다
3. 응답 데이터가 dict인지 1차 확인한다 (isinstance)
4. 응답 데이터가 우리가 기대한 구조(스키마)와
   정확히 일치하는지 검증한다 (jsonschema)

핵심 포인트
- isinstance : "형태만" 검사
- jsonschema : "내용 + 규칙" 검사
"""

import requests
from jsonschema import validate


def test_get_post_1_schema_validation():
    # -----------------------------
    # 1️⃣ API 요청
    # -----------------------------
    # jsonplaceholder의 1번 게시물 조회
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    # HTTP 요청이 정상적으로 성공했는지 확인
    # 200이 아니면 아래 로직은 의미가 없음
    assert response.status_code == 200

    # -----------------------------
    # 2️⃣ JSON 역직렬화
    # -----------------------------
    # response.json()
    # → 문자열(JSON)을 Python 객체로 변환
    data = response.json()

    # -----------------------------
    # 3️⃣ 1차 방어선: 타입 검사
    # -----------------------------
    # posts/1 응답은 "객체"여야 하므로 dict가 맞는지 확인
    # 이 단계에서는 키나 값 내용은 전혀 보지 않음
    assert isinstance(data, dict)

    # -----------------------------
    # 4️⃣ 기대하는 스키마 정의
    # -----------------------------
    # 이 API는 항상 아래 구조를 반환해야 한다는 "계약서"
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        # 반드시 존재해야 하는 필드들
        "required": ["userId", "id", "title", "body"]
    }

    # -----------------------------
    # 5️⃣ 스키마 검증 (핵심)
    # -----------------------------
    # data가 expected_schema 규칙을 하나라도 어기면
    # 여기서 바로 예외 발생 → 테스트 실패
    validate(instance=data, schema=expected_schema)

    # 여기까지 왔다는 건
    # - dict 타입 맞고
    # - 필수 키 다 있고
    # - 각 값의 타입도 전부 맞다는 뜻
