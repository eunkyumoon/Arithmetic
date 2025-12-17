# Report 폴더 안내

이 폴더에는 Arithmetic Operations 프로젝트의 종합 보고서가 포함되어 있습니다.

## 파일 목록

### 1. Project_Report.md

### 1. Project_Report.md
프로젝트 전체 진행 상황을 종합적으로 정리한 메인 보고서입니다.

**주요 내용:**
- 프로젝트 개요 및 목적
- 작업 진행 상황 및 타임라인
- 테스트 케이스 목록
- RED 단계 상세 결과 (Java & Python)
- 프로젝트 구조
- Git 저장소 관리 현황
- 다음 단계 계획

### 2. Test_Results.md
테스트 실행 결과를 상세히 기록한 보고서입니다.

**주요 내용:**
- Java 버전 컴파일 결과
- Python 버전 테스트 실행 결과
- 테스트 케이스별 상태
- 테스트 커버리지 현황
- 성능 테스트 계획

### 3. Test_Cases.md
테스트 케이스 작업에 대한 상세 보고서입니다.

**주요 내용:**
- 테스트 케이스 개요 및 통계
- 각 테스트 케이스 상세 설명 (10개)
- Java와 Python 버전 비교
- 테스트 실행 방법
- 테스트 결과 및 커버리지
- 다음 단계 계획

## 보고서 업데이트 주기

- **RED 단계**: 완료 ✅
- **GREEN 단계**: 진행 시 업데이트 예정
- **REFACTOR 단계**: 진행 시 업데이트 예정

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

## 보고서 작성 기준

각 단계(TDD 사이클)가 완료될 때마다 해당 보고서를 업데이트합니다.

---

**최종 업데이트**: 2025-12-16

