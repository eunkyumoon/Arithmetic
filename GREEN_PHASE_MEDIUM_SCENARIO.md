# GREEN 단계 중간 우선순위 최소 단위 구현 시나리오

## 목표
README.md의 중간 우선순위 작업을 TDD 방식으로 최소 단위로 구현합니다.

## 구현 범위
- **덧셈 연산 확장 (`add`)**: TC-003 (이미 구현되어 있으므로 테스트만 통과 확인)
- **곱셈 연산 (`multiply`)**: TC-005
- **소수점 나눗셈 (`quotient`)**: TC-008

## 현재 상태
- ✅ `add` 메서드: 이미 구현됨 (`a + b`)
- ❌ `multiply` 메서드: `NotImplementedError` 발생
- ❌ `quotient` 메서드: `NotImplementedError` 발생

## 구현 전략
TDD의 GREEN 단계 원칙에 따라 **하나의 테스트를 통과시키기 위한 최소한의 코드만** 작성합니다.

---

## 시나리오: Python 버전 구현

### Step 1: 음수 덧셈 테스트 통과 확인 (TC-003)
**목표**: `add(-1, -10) = -11` 테스트 통과 확인

1. **현재 상태 확인**: `add` 메서드는 이미 `a + b`로 구현되어 있음
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_addition_3 -v`
3. **예상 결과**: ✅ TC-003 통과 (추가 구현 불필요)

---

### Step 2: 곱셈 연산 첫 번째 테스트 통과 (TC-005)
**목표**: `multiply(-5, -3) = 15` 테스트 통과

1. **최소 구현**:
   ```python
   def multiply(self, a: int, b: int) -> int:
       """곱셈 연산
       Step 2: TC-005만 통과시키기 위한 하드코딩
       """
       return 15  # TC-005만 통과시키기 위한 하드코딩
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiplication_1 -v`
3. **예상 결과**: ✅ TC-005 통과

---

### Step 3: 곱셈 연산 실제 구현 (TC-005)
**목표**: 하드코딩을 실제 구현으로 변경

1. **코드 수정**:
   ```python
   def multiply(self, a: int, b: int) -> int:
       """곱셈 연산
       Step 3: 실제 구현으로 변경 (TC-005 통과)
       """
       return a * b
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiplication_1 -v`
3. **예상 결과**: ✅ TC-005 통과

**참고**: TC-006 (0 곱셈)도 자동으로 통과할 것으로 예상되지만, 이는 낮음 우선순위이므로 여기서는 확인만 함

---

### Step 4: 소수점 나눗셈 첫 번째 테스트 통과 (TC-008)
**목표**: `quotient(5, 2) = 2.5` 테스트 통과 (허용 오차: 0.0001)

1. **최소 구현**:
   ```python
   def quotient(self, a: int, b: int) -> float:
       """소수점 나눗셈 연산
       Step 4: TC-008만 통과시키기 위한 하드코딩
       """
       return 2.5  # TC-008만 통과시키기 위한 하드코딩
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_quotient -v`
3. **예상 결과**: ✅ TC-008 통과

---

### Step 5: 소수점 나눗셈 실제 구현 (TC-008)
**목표**: 하드코딩을 실제 구현으로 변경

1. **코드 수정**:
   ```python
   def quotient(self, a: int, b: int) -> float:
       """소수점 나눗셈 연산
       Step 5: 실제 구현으로 변경 (TC-008 통과)
       
       Args:
           a: 첫 번째 정수
           b: 두 번째 정수
           
       Returns:
           나눗셈 결과 (소수점 포함)
       """
       return a / b  # Python의 일반 나눗셈 (float 반환)
   ```
2. **테스트 실행**: `pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_quotient -v`
3. **예상 결과**: ✅ TC-008 통과

**참고**: 
- Python에서 `5 / 2`는 자동으로 `2.5` (float)를 반환
- 허용 오차 0.0001은 테스트에서 `abs(result - 2.5) < 0.0001`로 검증

---

### Step 6: 전체 테스트 통과 확인
**목표**: 중간 우선순위 테스트 모두 통과

1. **전체 테스트 실행**: 
   ```bash
   pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_addition_3 \
            tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiplication_1 \
            tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_quotient -v
   ```
2. **예상 결과**: 
   - ✅ TC-003 (test_addition_3) 통과
   - ✅ TC-005 (test_multiplication_1) 통과
   - ✅ TC-008 (test_quotient) 통과

---

### Step 7: 데모 출력 업데이트
**목표**: `if __name__ == "__main__":` 블록에 새로 구현된 메서드 추가

1. **데모 출력에 추가**:
   - 음수 덧셈 예시
   - 곱셈 연산 예시
   - 소수점 나눗셈 예시
2. **실행 확인**: `python src\arithmetic\arithmetic_calculator.py`
3. **예상 결과**: 모든 연산 결과가 출력됨

---

## 구현 순서 요약

1. ✅ TC-003 테스트 통과 확인 (추가 구현 불필요)
2. `multiply` 하드코딩 (TC-005)
3. `multiply` 실제 구현 (TC-005)
4. `quotient` 하드코딩 (TC-008)
5. `quotient` 실제 구현 (TC-008)
6. 전체 테스트 통과 확인
7. 데모 출력 업데이트

---

## 주의사항

1. **최소 단위 원칙**: 각 단계마다 하나의 테스트만 통과시키기 위한 최소한의 코드만 작성
2. **하드코딩 허용**: 첫 번째 테스트 통과를 위해 하드코딩 허용 (Step 2, 4)
3. **점진적 리팩토링**: 하드코딩된 값을 다음 단계에서 실제 구현으로 변경
4. **테스트 우선**: 각 단계마다 테스트 실행하여 통과 확인 필수
5. **Python만 작업**: Java 버전은 작성하지 않음

---

## 최종 검증

### Python 버전
```bash
pytest tests/test_arithmetic_calculator.py -v
```
**예상 결과**: 중간 우선순위 테스트 3개 모두 통과

### 직접 실행
```bash
python src\arithmetic\arithmetic_calculator.py
```
**예상 결과**: 모든 연산 결과가 출력됨

---

**시나리오 작성일**: 2025-12-16  
**승인 대기**: 사용자 승인 후 구현 진행

