"""
Arithmetic Calculator 클래스
TDD GREEN 단계: 최소 단위 구현 완료
"""


class ArithmeticCalculator:
    """사칙연산 계산기 클래스"""
    
    def add(self, a: int, b: int) -> int:
        """덧셈 연산
        Step 2-1, 2-2: TC-001, TC-002 통과
        """
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        """뺄셈 연산
        Step 2-3: TC-004 통과
        """
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        """곱셈 연산
        Step 3: 실제 구현으로 변경 (TC-005 통과)
        """
        return a * b
    
    def divide(self, a: int, b: int) -> int:
        """정수 나눗셈 연산
        Step 2-4: TC-007 통과 (소수점 버림)
        Step 2-6: TC-009, TC-010 통과 (예외 처리 추가)
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            나눗셈 결과 (정수)
            
        Raises:
            ZeroDivisionError: b가 0인 경우
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a // b
    
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


if __name__ == "__main__":
    """Direct execution demo output"""
    calculator = ArithmeticCalculator()
    
    print("=" * 50)
    print("Arithmetic Calculator - Execution Results")
    print("=" * 50)
    print()
    
    # Addition tests
    print("[Addition Operations]")
    print(f"  1 + 10 = {calculator.add(1, 10)}")
    print(f"  0 + 1 = {calculator.add(0, 1)}")
    print(f"  -1 + (-10) = {calculator.add(-1, -10)}")
    print()
    
    # Subtraction tests
    print("[Subtraction Operations]")
    print(f"  5 - 2 = {calculator.subtract(5, 2)}")
    print()
    
    # Multiplication tests
    print("[Multiplication Operations]")
    print(f"  -5 * -3 = {calculator.multiply(-5, -3)}")
    print(f"  0 * 10 = {calculator.multiply(0, 10)}")
    print()
    
    # Division tests
    print("[Integer Division Operations]")
    print(f"  5 / 2 = {calculator.divide(5, 2)}")
    print(f"  -10 / 2 = {calculator.divide(-10, 2)}")
    print()
    
    # Quotient tests
    print("[Quotient Operations (Float Division)]")
    print(f"  5 / 2 = {calculator.quotient(5, 2)}")
    print()
    
    # Exception handling test
    print("[Exception Handling Test]")
    try:
        result = calculator.divide(0, 0)
        print(f"  0 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"  0 / 0 -> Exception raised: {e}")
    print()
    
    print("=" * 50)
    print("[Complete] All tests completed!")
    print("=" * 50)

