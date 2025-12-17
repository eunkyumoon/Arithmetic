# 테스트 케이스 작업 보고서

## 문서 정보

- **프로젝트명**: 인사관리 앱 시스템 구축 (정산 시스템)
- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2020-09-01
- **최종 업데이트**: 2025-12-16
- **버전**: v1.0
- **테스트 범위**: 공통 모듈 - 사칙연산 정확도 테스트

---

## 1. 테스트 케이스 개요

### 1.1 목적
사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도와 예외 처리를 검증하기 위한 테스트 케이스를 작성합니다.

### 1.2 테스트 전략
- **TDD 방식**: RED-GREEN-REFACTOR 사이클 적용
- **현재 단계**: RED (실패하는 테스트 작성 완료)
- **테스트 프레임워크**: 
  - Java: JUnit 5
  - Python: pytest

### 1.3 테스트 케이스 통계
- **총 테스트 케이스 수**: 10개
- **기본 연산 테스트**: 9개
- **예외 처리 테스트**: 1개
- **중요도 분포**:
  - 중요: 6개
  - 보통: 3개
  - 낮음: 1개

---

## 2. 테스트 케이스 상세

### 2.1 덧셈 연산 테스트

#### TC-001: 양수 덧셈 (1 + 10 = 11)
- **테스트 ID**: TC-001
- **테스트명**: 덧셈 테스트: 1 + 10 = 11
- **중요도**: 중요
- **입력값**: a = 1, b = 10
- **예상값**: 11
- **목적**: 기본적인 양수 덧셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("덧셈 테스트: 1 + 10 = 11")
void testAddition1() {
    int result = calculator.add(1, 10);
    assertEquals(11, result, "1 + 10은 11이어야 합니다.");
}
```

**Python 코드:**
```python
def test_addition_1(self, calculator):
    """덧셈 테스트: 1 + 10 = 11"""
    result = calculator.add(1, 10)
    assert result == 11, "1 + 10은 11이어야 합니다."
```

---

#### TC-002: 0 포함 덧셈 (0 + 1 = 1)
- **테스트 ID**: TC-002
- **테스트명**: 덧셈 테스트: 0 + 1 = 1
- **중요도**: 중요
- **입력값**: a = 0, b = 1
- **예상값**: 1
- **목적**: 0을 포함한 덧셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("덧셈 테스트: 0 + 1 = 1")
void testAddition2() {
    int result = calculator.add(0, 1);
    assertEquals(1, result, "0 + 1은 1이어야 합니다.");
}
```

**Python 코드:**
```python
def test_addition_2(self, calculator):
    """덧셈 테스트: 0 + 1 = 1"""
    result = calculator.add(0, 1)
    assert result == 1, "0 + 1은 1이어야 합니다."
```

---

#### TC-003: 음수 덧셈 (-1 + (-10) = -11)
- **테스트 ID**: TC-003
- **테스트명**: 덧셈 테스트: -1 + (-10) = -11
- **중요도**: 보통
- **입력값**: a = -1, b = -10
- **예상값**: -11
- **목적**: 음수 덧셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("덧셈 테스트: -1 + (-10) = -11")
void testAddition3() {
    int result = calculator.add(-1, -10);
    assertEquals(-11, result, "-1 + (-10)은 -11이어야 합니다.");
}
```

**Python 코드:**
```python
def test_addition_3(self, calculator):
    """덧셈 테스트: -1 + (-10) = -11"""
    result = calculator.add(-1, -10)
    assert result == -11, "-1 + (-10)은 -11이어야 합니다."
```

---

### 2.2 뺄셈 연산 테스트

#### TC-004: 기본 뺄셈 (5 - 2 = 3)
- **테스트 ID**: TC-004
- **테스트명**: 뺄셈 테스트: 5 - 2 = 3
- **중요도**: 중요
- **입력값**: a = 5, b = 2
- **예상값**: 3
- **목적**: 기본적인 뺄셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("뺄셈 테스트: 5 - 2 = 3")
void testSubtraction() {
    int result = calculator.subtract(5, 2);
    assertEquals(3, result, "5 - 2는 3이어야 합니다.");
}
```

**Python 코드:**
```python
def test_subtraction(self, calculator):
    """뺄셈 테스트: 5 - 2 = 3"""
    result = calculator.subtract(5, 2)
    assert result == 3, "5 - 2는 3이어야 합니다."
```

---

### 2.3 곱셈 연산 테스트

#### TC-005: 음수 곱셈 (-5 * -3 = 15)
- **테스트 ID**: TC-005
- **테스트명**: 곱셈 테스트: -5 * -3 = 15
- **중요도**: 보통
- **입력값**: a = -5, b = -3
- **예상값**: 15
- **목적**: 음수 곱셈 연산의 정확도 검증 (음수 × 음수 = 양수)

**Java 코드:**
```java
@Test
@DisplayName("곱셈 테스트: -5 * -3 = 15")
void testMultiplication1() {
    int result = calculator.multiply(-5, -3);
    assertEquals(15, result, "-5 * -3은 15이어야 합니다.");
}
```

**Python 코드:**
```python
def test_multiplication_1(self, calculator):
    """곱셈 테스트: -5 * -3 = 15"""
    result = calculator.multiply(-5, -3)
    assert result == 15, "-5 * -3은 15이어야 합니다."
```

---

#### TC-006: 0 곱셈 (0 * 10 = 0)
- **테스트 ID**: TC-006
- **테스트명**: 곱셈 테스트: 0 * 10 = 0
- **중요도**: 낮음
- **입력값**: a = 0, b = 10
- **예상값**: 0
- **목적**: 0을 포함한 곱셈 연산의 정확도 검증 (0 × 어떤 수 = 0)

**Java 코드:**
```java
@Test
@DisplayName("곱셈 테스트: 0 * 10 = 0")
void testMultiplication2() {
    int result = calculator.multiply(0, 10);
    assertEquals(0, result, "0 * 10은 0이어야 합니다.");
}
```

**Python 코드:**
```python
def test_multiplication_2(self, calculator):
    """곱셈 테스트: 0 * 10 = 0"""
    result = calculator.multiply(0, 10)
    assert result == 0, "0 * 10은 0이어야 합니다."
```

---

### 2.4 나눗셈 연산 테스트

#### TC-007: 정수 나눗셈 (5 / 2 = 2)
- **테스트 ID**: TC-007
- **테스트명**: 정수 나눗셈 테스트: 5 / 2 = 2
- **중요도**: 중요
- **입력값**: a = 5, b = 2
- **예상값**: 2 (정수 나눗셈)
- **목적**: 정수 나눗셈 연산의 정확도 검증 (소수점 버림)

**Java 코드:**
```java
@Test
@DisplayName("정수 나눗셈 테스트: 5 / 2 = 2")
void testIntegerDivision() {
    int result = calculator.divide(5, 2);
    assertEquals(2, result, "5 / 2는 2이어야 합니다 (정수 나눗셈).");
}
```

**Python 코드:**
```python
def test_integer_division(self, calculator):
    """정수 나눗셈 테스트: 5 / 2 = 2"""
    result = calculator.divide(5, 2)
    assert result == 2, "5 / 2는 2이어야 합니다 (정수 나눗셈)."
```

---

#### TC-008: 소수점 나눗셈 (5 ÷ 2 = 2.5)
- **테스트 ID**: TC-008
- **테스트명**: 소수점 나눗셈 테스트: 5 ÷ 2 = 2.5
- **중요도**: 보통
- **입력값**: a = 5, b = 2
- **예상값**: 2.5 (소수점 포함)
- **목적**: 소수점을 포함한 나눗셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("소수점 나눗셈 테스트: 5 ÷ 2 = 2.5")
void testQuotient() {
    double result = calculator.quotient(5, 2);
    assertEquals(2.5, result, 0.0001, "5 ÷ 2는 2.5이어야 합니다.");
}
```

**Python 코드:**
```python
def test_quotient(self, calculator):
    """소수점 나눗셈 테스트: 5 ÷ 2 = 2.5"""
    result = calculator.quotient(5, 2)
    assert abs(result - 2.5) < 0.0001, "5 ÷ 2는 2.5이어야 합니다."
```

**참고**: 
- Java에서는 `assertEquals`의 세 번째 매개변수로 허용 오차(0.0001)를 지정
- Python에서는 `abs(result - 2.5) < 0.0001`로 부동소수점 오차를 처리

---

#### TC-009: 음수 나눗셈 (-10 / 2 = -5)
- **테스트 ID**: TC-009
- **테스트명**: 나눗셈 테스트: -10 / 2 = -5
- **중요도**: 중요
- **입력값**: a = -10, b = 2
- **예상값**: -5
- **목적**: 음수를 포함한 나눗셈 연산의 정확도 검증

**Java 코드:**
```java
@Test
@DisplayName("나눗셈 테스트: -10 / 2 = -5")
void testDivision() {
    int result = calculator.divide(-10, 2);
    assertEquals(-5, result, "-10 / 2는 -5이어야 합니다.");
}
```

**Python 코드:**
```python
def test_division(self, calculator):
    """나눗셈 테스트: -10 / 2 = -5"""
    result = calculator.divide(-10, 2)
    assert result == -5, "-10 / 2는 -5이어야 합니다."
```

---

### 2.5 예외 처리 테스트

#### TC-010: 0으로 나누기 (0 / 0)
- **테스트 ID**: TC-010
- **테스트명**: 예외 처리 테스트: 0 / 0
- **중요도**: 중요
- **입력값**: a = 0, b = 0
- **예상값**: 예외 발생
  - Java: `ArithmeticException`
  - Python: `ZeroDivisionError` 또는 `ArithmeticError`
- **목적**: 0으로 나누기 시 예외 처리가 올바르게 동작하는지 검증

**Java 코드:**
```java
@Test
@DisplayName("예외 처리 테스트: 0 / 0는 ArithmeticException 발생")
void testDivisionByZero() {
    assertThrows(ArithmeticException.class, () -> {
        calculator.divide(0, 0);
    }, "0 / 0는 ArithmeticException을 발생시켜야 합니다.");
}
```

**Python 코드:**
```python
def test_division_by_zero(self, calculator):
    """예외 처리 테스트: 0 / 0는 ZeroDivisionError 또는 ArithmeticError 발생"""
    with pytest.raises((ZeroDivisionError, ArithmeticError)):
        calculator.divide(0, 0)
```

**참고**: 
- Java에서는 `ArithmeticException`을 사용
- Python에서는 `ZeroDivisionError` 또는 `ArithmeticError`를 사용 (둘 다 허용)

---

## 3. 테스트 케이스 요약표

| 테스트 ID | 테스트명 | 연산 | 입력값 | 예상값 | 중요도 | Java | Python |
|----------|---------|------|--------|--------|--------|------|--------|
| TC-001 | 덧셈: 1 + 10 | add | 1, 10 | 11 | 중요 | ✅ | ✅ |
| TC-002 | 덧셈: 0 + 1 | add | 0, 1 | 1 | 중요 | ✅ | ✅ |
| TC-003 | 덧셈: -1 + (-10) | add | -1, -10 | -11 | 보통 | ✅ | ✅ |
| TC-004 | 뺄셈: 5 - 2 | subtract | 5, 2 | 3 | 중요 | ✅ | ✅ |
| TC-005 | 곱셈: -5 * -3 | multiply | -5, -3 | 15 | 보통 | ✅ | ✅ |
| TC-006 | 곱셈: 0 * 10 | multiply | 0, 10 | 0 | 낮음 | ✅ | ✅ |
| TC-007 | 정수 나눗셈: 5 / 2 | divide | 5, 2 | 2 | 중요 | ✅ | ✅ |
| TC-008 | 소수점 나눗셈: 5 ÷ 2 | quotient | 5, 2 | 2.5 | 보통 | ✅ | ✅ |
| TC-009 | 나눗셈: -10 / 2 | divide | -10, 2 | -5 | 중요 | ✅ | ✅ |
| TC-010 | 예외: 0 / 0 | divide | 0, 0 | Exception | 중요 | ✅ | ✅ |

---

## 4. Java와 Python 버전 비교

### 4.1 테스트 프레임워크 비교

| 항목 | Java | Python |
|------|------|--------|
| 프레임워크 | JUnit 5 | pytest |
| 테스트 클래스 | `@DisplayName` 어노테이션 | docstring |
| 테스트 메서드 | `@Test` 어노테이션 | `test_*` 메서드명 |
| 테스트 설정 | `@BeforeEach` | `@pytest.fixture` |
| Assertion | `assertEquals(expected, actual, message)` | `assert actual == expected, message` |
| 예외 테스트 | `assertThrows(Exception.class, ...)` | `pytest.raises(Exception)` |
| 부동소수점 비교 | `assertEquals(expected, actual, delta)` | `abs(actual - expected) < delta` |

### 4.2 코드 구조 비교

**Java 구조:**
```java
@DisplayName("사칙연산 정확도 테스트")
class ArithmeticCalculatorTest {
    private ArithmeticCalculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new ArithmeticCalculator();
    }
    
    @Test
    @DisplayName("덧셈 테스트: 1 + 10 = 11")
    void testAddition1() {
        int result = calculator.add(1, 10);
        assertEquals(11, result, "1 + 10은 11이어야 합니다.");
    }
}
```

**Python 구조:**
```python
class TestArithmeticCalculator:
    """사칙연산 정확도 테스트"""
    
    @pytest.fixture
    def calculator(self):
        """테스트용 계산기 인스턴스 생성"""
        return ArithmeticCalculator()
    
    def test_addition_1(self, calculator):
        """덧셈 테스트: 1 + 10 = 11"""
        result = calculator.add(1, 10)
        assert result == 11, "1 + 10은 11이어야 합니다."
```

### 4.3 주요 차이점

1. **타입 선언**
   - Java: 명시적 타입 선언 (`int`, `double`)
   - Python: 타입 힌트 사용 (`int`, `float`)

2. **예외 처리**
   - Java: `ArithmeticException`
   - Python: `ZeroDivisionError` 또는 `ArithmeticError`

3. **부동소수점 비교**
   - Java: `assertEquals(2.5, result, 0.0001)`
   - Python: `abs(result - 2.5) < 0.0001`

---

## 5. 테스트 실행 방법

### 5.1 Java 버전

**컴파일:**
```bash
.\mvnw.cmd compile test-compile
```

**테스트 실행 (구현 후):**
```bash
.\mvnw.cmd test
```

**특정 테스트 실행:**
```bash
.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testAddition1
```

### 5.2 Python 버전

**의존성 설치:**
```bash
pip install -r requirements.txt
```

**전체 테스트 실행:**
```bash
pytest -v
```

**특정 테스트 실행:**
```bash
pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_addition_1 -v
```

**커버리지 포함 테스트:**
```bash
pytest --cov=src/arithmetic --cov-report=html
```

---

## 6. 테스트 결과

### 6.1 현재 상태 (RED 단계)

#### Java 버전
- **컴파일 상태**: ❌ 실패 (예상된 결과)
- **실패 원인**: `ArithmeticCalculator` 클래스 미존재
- **상태**: ✅ RED 단계 목표 달성

#### Python 버전
- **테스트 실행**: ❌ 실패 (예상된 결과)
- **실패 원인**: `NotImplementedError` 발생
- **상태**: ✅ RED 단계 목표 달성

### 6.2 예상 결과 (GREEN 단계)

모든 테스트 케이스가 통과할 것으로 예상됩니다:
- ✅ TC-001 ~ TC-009: 모든 연산 테스트 통과
- ✅ TC-010: 예외 처리 테스트 통과

---

## 7. 테스트 커버리지

### 7.1 현재 커버리지 (RED 단계)
- **코드 커버리지**: 0% (구현 클래스 미존재)
- **테스트 작성률**: 100% (10개 테스트 케이스)

### 7.2 예상 커버리지 (GREEN 단계)
- **코드 커버리지**: 100% (모든 메서드 테스트)
- **분기 커버리지**: 100% (모든 조건문 테스트)
- **예외 처리 커버리지**: 100% (0으로 나누기 예외)

---

## 8. 테스트 케이스 검증 기준

### 8.1 성공 기준
- 모든 테스트 케이스가 예상한 결과를 생성해야 함
- 예외 처리 테스트가 올바른 예외를 발생시켜야 함
- 코드 커버리지가 100% 이상이어야 함

### 8.2 실패 기준
- 테스트 케이스가 예상한 결과를 생성하지 않으면 실패
- 예외가 발생해야 하는 경우 예외가 발생하지 않으면 실패
- 예외가 발생하지 않아야 하는 경우 예외가 발생하면 실패

---

## 9. 다음 단계

### 9.1 GREEN 단계 계획
1. `ArithmeticCalculator` 클래스 구현
2. 모든 메서드 구현:
   - `add(int a, int b)`
   - `subtract(int a, int b)`
   - `multiply(int a, int b)`
   - `divide(int a, int b)`
   - `quotient(int a, int b)`
3. 예외 처리 구현 (0으로 나누기)
4. 모든 테스트 통과 확인

### 9.2 REFACTOR 단계 계획
1. 코드 리뷰 및 개선
2. 중복 코드 제거
3. 성능 최적화 (필요시)
4. 문서화 개선

---

## 10. 결론

현재 **10개의 테스트 케이스**를 Java와 Python 두 가지 언어로 작성 완료했습니다. 모든 테스트 케이스는 RED 단계에서 의도한 대로 실패하는 것을 확인했습니다.

다음 단계인 GREEN 단계에서는 실제 구현 클래스를 작성하여 모든 테스트를 통과시켜야 합니다.

---

**보고서 작성일**: 2025-12-16  
**작성자**: 홍길동  
**승인자**: 박문수  
**문서 버전**: v1.0

