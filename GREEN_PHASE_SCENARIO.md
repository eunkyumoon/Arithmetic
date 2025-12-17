# GREEN 단계 최소 단위 구현 시나리오

## 목표
README.md 126-149줄에 명시된 높음 우선순위 작업을 TDD 방식으로 최소 단위로 구현합니다.

## 구현 범위
- **덧셈 연산 (`add`)**: TC-001, TC-002
- **뺄셈 연산 (`subtract`)**: TC-004
- **정수 나눗셈 (`divide`)**: TC-007, TC-009, TC-010

## 구현 전략
TDD의 GREEN 단계 원칙에 따라 **하나의 테스트를 통과시키기 위한 최소한의 코드만** 작성합니다.

---

## 시나리오 1: Java 버전 구현

### Step 1-1: 클래스 생성 및 첫 번째 테스트 통과 (TC-001)
**목표**: `add(1, 10) = 11` 테스트 통과

1. **파일 생성**: `src/main/java/com/arithmetic/ArithmeticCalculator.java`
2. **최소 구현**:
   ```java
   package com.arithmetic;
   
   public class ArithmeticCalculator {
       public int add(int a, int b) {
           return 11;  // TC-001만 통과시키기 위한 하드코딩
       }
   }
   ```
3. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testAddition1`
4. **예상 결과**: ✅ TC-001 통과

---

### Step 1-2: 두 번째 테스트 통과 (TC-002)
**목표**: `add(0, 1) = 1` 테스트 통과

1. **코드 수정**:
   ```java
   public int add(int a, int b) {
       return a + b;  // 실제 구현으로 변경
   }
   ```
2. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testAddition2`
3. **예상 결과**: ✅ TC-001, TC-002 모두 통과

---

### Step 1-3: 뺄셈 연산 구현 (TC-004)
**목표**: `subtract(5, 2) = 3` 테스트 통과

1. **메서드 추가**:
   ```java
   public int subtract(int a, int b) {
       return a - b;
   }
   ```
2. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testSubtraction`
3. **예상 결과**: ✅ TC-004 통과

---

### Step 1-4: 정수 나눗셈 기본 구현 (TC-007)
**목표**: `divide(5, 2) = 2` 테스트 통과

1. **메서드 추가**:
   ```java
   public int divide(int a, int b) {
       return a / b;  // 정수 나눗셈 (소수점 버림)
   }
   ```
2. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testIntegerDivision`
3. **예상 결과**: ✅ TC-007 통과

---

### Step 1-5: 음수 나눗셈 테스트 통과 (TC-009)
**목표**: `divide(-10, 2) = -5` 테스트 통과

1. **코드 확인**: 이미 `a / b`로 구현되어 있으므로 추가 수정 불필요
2. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testDivision`
3. **예상 결과**: ✅ TC-009 통과

---

### Step 1-6: 0으로 나누기 예외 처리 (TC-010)
**목표**: `divide(0, 0)` → `ArithmeticException` 발생

1. **코드 수정**:
   ```java
   public int divide(int a, int b) {
       if (b == 0) {
           throw new ArithmeticException("0으로 나눌 수 없습니다.");
       }
       return a / b;
   }
   ```
2. **테스트 실행**: `.\mvnw.cmd test -Dtest=ArithmeticCalculatorTest#testDivisionByZero`
3. **예상 결과**: ✅ TC-010 통과

---

### Step 1-7: 전체 테스트 통과 확인
**목표**: 높음 우선순위 테스트 모두 통과

1. **전체 테스트 실행**: `.\mvnw.cmd test`
2. **예상 결과**: 
   - ✅ TC-001 (testAddition1) 통과
   - ✅ TC-002 (testAddition2) 통과
   - ✅ TC-004 (testSubtraction) 통과
   - ✅ TC-007 (testIntegerDivision) 통과
   - ✅ TC-009 (testDivision) 통과
   - ✅ TC-010 (testDivisionByZero) 통과

---

## 시나리오 2: Python 버전 구현

### Step 2-1: 클래스 생성 및 첫 번째 테스트 통과 (TC-001)
**목표**: `add(1, 10) = 11` 테스트 통과

1. **파일 수정**: `src/arithmetic/arithmetic_calculator.py`
2. **최소 구현**:
   ```python
   def add(self, a: int, b: int) -> int:
       """덧셈 연산"""
       return 11  # TC-001만 통과시키기 위한 하드코딩
   ```
3. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_addition_1 -v`
4. **예상 결과**: ✅ TC-001 통과

---

### Step 2-2: 두 번째 테스트 통과 (TC-002)
**목표**: `add(0, 1) = 1` 테스트 통과

1. **코드 수정**:
   ```python
   def add(self, a: int, b: int) -> int:
       """덧셈 연산"""
       return a + b  # 실제 구현으로 변경
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_addition_2 -v`
3. **예상 결과**: ✅ TC-001, TC-002 모두 통과

---

### Step 2-3: 뺄셈 연산 구현 (TC-004)
**목표**: `subtract(5, 2) = 3` 테스트 통과

1. **메서드 수정**:
   ```python
   def subtract(self, a: int, b: int) -> int:
       """뺄셈 연산"""
       return a - b
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_subtraction -v`
3. **예상 결과**: ✅ TC-004 통과

---

### Step 2-4: 정수 나눗셈 기본 구현 (TC-007)
**목표**: `divide(5, 2) = 2` 테스트 통과

1. **메서드 수정**:
   ```python
   def divide(self, a: int, b: int) -> int:
       """정수 나눗셈 연산"""
       return a // b  # 정수 나눗셈 (소수점 버림)
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_integer_division -v`
3. **예상 결과**: ✅ TC-007 통과

---

### Step 2-5: 음수 나눗셈 테스트 통과 (TC-009)
**목표**: `divide(-10, 2) = -5` 테스트 통과

1. **코드 확인**: 이미 `a // b`로 구현되어 있으므로 추가 수정 불필요
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_division -v`
3. **예상 결과**: ✅ TC-009 통과

---

### Step 2-6: 0으로 나누기 예외 처리 (TC-010)
**목표**: `divide(0, 0)` → `ZeroDivisionError` 또는 `ArithmeticError` 발생

1. **코드 수정**:
   ```python
   def divide(self, a: int, b: int) -> int:
       """정수 나눗셈 연산"""
       if b == 0:
           raise ZeroDivisionError("0으로 나눌 수 없습니다.")
       return a // b
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_division_by_zero -v`
3. **예상 결과**: ✅ TC-010 통과

---

### Step 2-7: 전체 테스트 통과 확인
**목표**: 높음 우선순위 테스트 모두 통과

1. **전체 테스트 실행**: `pytest tests/test_arithmetic_calculator.py -v`
2. **예상 결과**: 
   - ✅ TC-001 (test_addition_1) 통과
   - ✅ TC-002 (test_addition_2) 통과
   - ✅ TC-004 (test_subtraction) 통과
   - ✅ TC-007 (test_integer_division) 통과
   - ✅ TC-009 (test_division) 통과
   - ✅ TC-010 (test_division_by_zero) 통과

---

## 최종 검증

### Java 버전
```bash
.\mvnw.cmd test
```
**예상 결과**: 높음 우선순위 테스트 6개 모두 통과

### Python 버전
```bash
pytest tests/test_arithmetic_calculator.py -v
```
**예상 결과**: 높음 우선순위 테스트 6개 모두 통과

---

## 구현 순서 요약

### Java
1. 클래스 생성 + `add` 하드코딩 (TC-001)
2. `add` 실제 구현 (TC-001, TC-002)
3. `subtract` 구현 (TC-004)
4. `divide` 기본 구현 (TC-007)
5. `divide` 예외 처리 추가 (TC-009, TC-010)

### Python
1. `add` 하드코딩 제거 + 실제 구현 (TC-001, TC-002)
2. `subtract` 구현 (TC-004)
3. `divide` 기본 구현 (TC-007)
4. `divide` 예외 처리 추가 (TC-009, TC-010)

---

## 주의사항

1. **최소 단위 원칙**: 각 단계마다 하나의 테스트만 통과시키기 위한 최소한의 코드만 작성
2. **하드코딩 허용**: 첫 번째 테스트 통과를 위해 하드코딩 허용 (Step 1-1, 2-1)
3. **점진적 리팩토링**: 하드코딩된 값을 다음 단계에서 실제 구현으로 변경
4. **테스트 우선**: 각 단계마다 테스트 실행하여 통과 확인 필수

---

**시나리오 작성일**: 2025-12-16  
**승인 대기**: 사용자 승인 후 구현 진행

