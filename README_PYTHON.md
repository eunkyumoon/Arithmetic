# Arithmetic Operations - Python 버전

## 프로젝트 개요

Java 버전을 Python으로 변환한 사칙연산 정확도 검증 프로젝트입니다.  
TDD(Test-Driven Development)의 RED-GREEN-REFACTOR 사이클을 따라 개발합니다.

## 프로젝트 구조

```
Arithmetic/
├── src/
│   └── arithmetic/
│       ├── __init__.py
│       └── arithmetic_calculator.py  # 구현 클래스 (아직 미구현)
├── tests/
│   └── test_arithmetic_calculator.py  # 테스트 파일
├── requirements.txt                   # Python 의존성
├── pyproject.toml                     # 프로젝트 설정
└── README_PYTHON.md                   # 이 파일
```

## Java → Python 변환 내용

### 테스트 프레임워크
- **Java**: JUnit 5
- **Python**: pytest

### 주요 변환 사항

| Java | Python |
|------|--------|
| `@Test` | `def test_*()` |
| `@DisplayName` | docstring |
| `@BeforeEach` | `@pytest.fixture` |
| `assertEquals(expected, actual, message)` | `assert actual == expected, message` |
| `assertThrows(ArithmeticException.class, ...)` | `pytest.raises(ZeroDivisionError, ...)` |
| `int`, `double` | `int`, `float` (자동 처리) |

## 설치 및 실행

### 1. 가상 환경 생성 (권장)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 테스트 실행
```bash
pytest
```

또는 상세 출력:
```bash
pytest -v
```

### 4. 테스트 커버리지 확인
```bash
pytest --cov=src/arithmetic --cov-report=html
```

## 현재 상태

### RED 단계 완료
- ✅ 테스트 클래스 작성 완료
- ✅ 구현 클래스 미작성 (의도된 상태)
- ⏳ 테스트 실행 시 실패 예상

## 테스트 케이스

Java 버전과 동일한 테스트 케이스를 포함합니다:

1. 덧셈: 1+10, 0+1, -1+(-10)
2. 뺄셈: 5-2
3. 곱셈: -5*(-3), 0*10
4. 정수 나눗셈: 5/2
5. 소수점 나눗셈: 5÷2 (quotient)
6. 나눗셈: -10/2
7. 예외 처리: 0/0 → ZeroDivisionError

## 다음 단계

1. **GREEN 단계**: `ArithmeticCalculator` 클래스 구현
2. **REFACTOR 단계**: 코드 개선 및 리팩토링

