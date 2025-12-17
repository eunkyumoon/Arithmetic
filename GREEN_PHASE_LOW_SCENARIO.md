# GREEN 단계 낮음 우선순위 최소 단위 구현 시나리오

## 목표
README.md의 낮음 우선순위 작업을 TDD 방식으로 최소 단위로 구현합니다.

## 구현 범위
- **곱셈 연산 확장 (`multiply`)**: TC-006 (0 곱셈)

## 현재 상태
- ✅ `multiply` 메서드: 이미 구현됨 (`a * b`)
- ✅ TC-005: `multiply(-5, -3) = 15` 통과 확인 완료
- ⏳ TC-006: `multiply(0, 10) = 0` 테스트 통과 확인 필요

## 구현 전략
`multiply` 메서드가 이미 구현되어 있으므로, 추가 구현 없이 테스트만 실행하여 통과를 확인합니다.

---

## 시나리오: Python 버전 구현

### Step 1: 0 곱셈 테스트 통과 확인 (TC-006)
**목표**: `multiply(0, 10) = 0` 테스트 통과 확인

1. **현재 상태 확인**: 
   - `multiply` 메서드는 이미 `return a * b`로 구현되어 있음
   - 수학적으로 `0 * 10 = 0`이므로 추가 구현 불필요

2. **테스트 실행**: 
   ```bash
   pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiplication_2 -v
   ```

3. **예상 결과**: ✅ TC-006 통과 (추가 구현 불필요)

---

### Step 2: 전체 테스트 통과 확인
**목표**: 모든 테스트 케이스 통과 확인

1. **전체 테스트 실행**: 
   ```bash
   pytest tests/test_arithmetic_calculator.py -v
   ```

2. **예상 결과**: 
   - ✅ TC-001 ~ TC-010: 모든 테스트 통과 (10개)
   - 특히 TC-006 (test_multiplication_2) 통과 확인

---

### Step 3: 데모 출력 업데이트 (선택사항)
**목표**: `if __name__ == "__main__":` 블록에 0 곱셈 예시 추가

1. **데모 출력에 추가**:
   - 곱셈 연산 섹션에 `0 * 10 = 0` 예시 추가

2. **실행 확인**: 
   ```bash
   python src\arithmetic\arithmetic_calculator.py
   ```

3. **예상 결과**: 0 곱셈 결과가 출력됨

---

## 구현 순서 요약

1. ✅ TC-006 테스트 통과 확인 (추가 구현 불필요)
2. 전체 테스트 통과 확인
3. (선택) 데모 출력 업데이트

---

## 주의사항

1. **추가 구현 불필요**: `multiply` 메서드가 이미 `a * b`로 구현되어 있어 추가 작업 없음
2. **테스트 확인만**: 테스트 실행하여 통과 확인만 하면 됨
3. **Python만 작업**: Java 버전은 작성하지 않음

---

## 최종 검증

### Python 버전
```bash
pytest tests/test_arithmetic_calculator.py -v
```
**예상 결과**: 모든 테스트 케이스 통과 (10개)
- 특히 TC-006 (test_multiplication_2) 통과 확인

### 직접 실행 (선택)
```bash
python src\arithmetic\arithmetic_calculator.py
```
**예상 결과**: 모든 연산 결과가 출력됨 (0 곱셈 포함)

---

## 예상 소요 시간
- 매우 짧음 (약 1-2분)
- 테스트 실행 및 확인만 필요

---

**시나리오 작성일**: 2025-12-16  
**승인 대기**: 사용자 승인 후 구현 진행

