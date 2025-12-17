# Arithmetic Operations - 사칙연산 모듈

## 프로젝트 개요

사칙연산의 정확도를 검증하는 공통 모듈 프로젝트입니다.  
TDD(Test-Driven Development)의 RED-GREEN-REFACTOR 사이클을 따라 개발합니다.

## 프로젝트 정보

- **프로젝트명**: 인사관리 앱 시스템 구축 (정산 시스템)
- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈

## 테스트 환경

- **JDK 버전**: 17
- **IDE**: IntelliJ IDEA 2023.2
- **운영 체제**: Windows 10
- **빌드 도구**: Maven 또는 Gradle (선택)

## 테스트 목적

사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도와 예외 처리를 검증합니다.

## 테스트 케이스

### 기본 연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | ✅ |
| 덧셈 | 0 + 1 | 1 | 중요 | ✅ |
| 덧셈 | -1 + (-10) | -11 | 보통 | ✅ |
| 뺄셈 | 5 - 2 | 3 | 중요 | ✅ |
| 곱셈 | -5 * -3 | 15 | 보통 | ✅ |
| 곱셈 | 0 * 10 | 0 | 낮음 | ✅ |
| 정수 나눗셈 | 5 / 2 | 2 | 중요 | ✅ |
| 소수점 나눗셈 | 5 ÷ 2 (quotient) | 2.5 | 보통 | ✅ |
| 나눗셈 | -10 / 2 | -5 | 중요 | ✅ |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticException | 중요 | ✅ |

## TDD 개발 방식

이 프로젝트는 **RED-GREEN-REFACTOR** 사이클을 따릅니다:

1. **RED**: 실패하는 테스트 작성
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성
3. **REFACTOR**: 코드 개선 및 리팩토링

## 프로젝트 구조

```
Arithmetic/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── arithmetic/
│   │               └── ArithmeticCalculator.java
│   └── test/
│       └── java/
│           └── com/
│               └── arithmetic/
│                   └── ArithmeticCalculatorTest.java
├── README.md
└── pom.xml (또는 build.gradle)
```

## 실행 방법

### 테스트 실행

```bash
# Maven 사용 시
mvn test

# Gradle 사용 시
gradle test
```

### 컴파일

```bash
# Maven 사용 시
mvn compile

# Gradle 사용 시
gradle build
```

## 전제 조건

- 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다.
- 모든 종속성을 올바르게 설치하고 구성해야 합니다.

## 성공/실패 기준

- **성공**: 모든 테스트 사례가 예상한 결과를 생성합니다.
- **실패**: 테스트 케이스가 예상한 결과를 생성하지 않습니다.

## 특별 절차

- 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
- 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 개발 단계

1. ✅ README.md 작성
2. ✅ 테스트 클래스 작성 (RED)
3. ⏳ 구현 클래스 작성 (GREEN)
4. ⏳ 리팩토링 (REFACTOR)

---

## GREEN 단계 구현 작업 목록

### 🔴 높음 (High Priority) - 중요도: 중요

#### 1. 덧셈 연산 (`add`) 메서드 구현
- [ ] **TC-001**: 양수 덧셈 - `add(1, 10) = 11`
- [ ] **TC-002**: 0 포함 덧셈 - `add(0, 1) = 1`
- **구현 위치**: 
  - Java: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
  - Python: `src/arithmetic/arithmetic_calculator.py`

#### 2. 뺄셈 연산 (`subtract`) 메서드 구현
- [ ] **TC-004**: 기본 뺄셈 - `subtract(5, 2) = 3`
- **구현 위치**: 
  - Java: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
  - Python: `src/arithmetic/arithmetic_calculator.py`

#### 3. 정수 나눗셈 (`divide`) 메서드 구현
- [ ] **TC-007**: 정수 나눗셈 - `divide(5, 2) = 2` (소수점 버림)
- [ ] **TC-009**: 음수 나눗셈 - `divide(-10, 2) = -5`
- [ ] **TC-010**: 0으로 나누기 예외 처리 - `divide(0, 0)` → 예외 발생
  - Java: `ArithmeticException` 발생
  - Python: `ZeroDivisionError` 또는 `ArithmeticError` 발생
- **구현 위치**: 
  - Java: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
  - Python: `src/arithmetic/arithmetic_calculator.py`

---

### 🟡 중간 (Medium Priority) - 중요도: 보통

#### 4. 덧셈 연산 확장 (`add`)
- [ ] **TC-003**: 음수 덧셈 - `add(-1, -10) = -11`
- **참고**: `add` 메서드가 이미 구현되어 있다면 추가 테스트만 통과하면 됨

#### 5. 곱셈 연산 (`multiply`) 메서드 구현
- [ ] **TC-005**: 음수 곱셈 - `multiply(-5, -3) = 15`
- **구현 위치**: 
  - Java: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
  - Python: `src/arithmetic/arithmetic_calculator.py`

#### 6. 소수점 나눗셈 (`quotient`) 메서드 구현
- [ ] **TC-008**: 소수점 나눗셈 - `quotient(5, 2) = 2.5`
  - 허용 오차: 0.0001
  - Java: `double` 반환 타입
  - Python: `float` 반환 타입
- **구현 위치**: 
  - Java: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
  - Python: `src/arithmetic/arithmetic_calculator.py`

---

### 🟢 낮음 (Low Priority) - 중요도: 낮음

#### 7. 곱셈 연산 확장 (`multiply`)
- [ ] **TC-006**: 0 곱셈 - `multiply(0, 10) = 0`
- **참고**: `multiply` 메서드가 이미 구현되어 있다면 추가 테스트만 통과하면 됨

---

### 📋 구현 체크리스트

#### Java 버전
- [ ] `ArithmeticCalculator` 클래스 생성
- [ ] `add(int a, int b)` 메서드 구현
- [ ] `subtract(int a, int b)` 메서드 구현
- [ ] `multiply(int a, int b)` 메서드 구현
- [ ] `divide(int a, int b)` 메서드 구현 (예외 처리 포함)
- [ ] `quotient(int a, int b)` 메서드 구현
- [ ] 모든 테스트 통과 확인: `.\mvnw.cmd test`
- [ ] 코드 컴파일 확인: `.\mvnw.cmd compile test-compile`

#### Python 버전
- [ ] `ArithmeticCalculator` 클래스 생성
- [ ] `add(a: int, b: int) -> int` 메서드 구현
- [ ] `subtract(a: int, b: int) -> int` 메서드 구현
- [ ] `multiply(a: int, b: int) -> int` 메서드 구현
- [ ] `divide(a: int, b: int) -> int` 메서드 구현 (예외 처리 포함)
- [ ] `quotient(a: int, b: int) -> float` 메서드 구현
- [ ] 모든 테스트 통과 확인: `pytest -v`
- [ ] 코드 커버리지 확인: `pytest --cov=src/arithmetic --cov-report=html`

---

### 🎯 구현 완료 기준

- ✅ 모든 테스트 케이스 통과 (10개)
- ✅ 코드 커버리지 100% 달성
- ✅ 예외 처리 정상 동작 확인
- ✅ Java와 Python 두 언어 모두 구현 완료
- ✅ 컴파일/실행 오류 없음

## 라이선스

이 프로젝트는 내부 사용을 위한 것입니다.

