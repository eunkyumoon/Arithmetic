"""
사칙연산 정확도 테스트 클래스
TDD RED 단계: 실패하는 테스트 작성

@author 홍길동
@version 1.0
@since 2020-09-01
"""

import pytest
from arithmetic.arithmetic_calculator import ArithmeticCalculator


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
    
    def test_addition_2(self, calculator):
        """덧셈 테스트: 0 + 1 = 1"""
        result = calculator.add(0, 1)
        assert result == 1, "0 + 1은 1이어야 합니다."
    
    def test_addition_3(self, calculator):
        """덧셈 테스트: -1 + (-10) = -11"""
        result = calculator.add(-1, -10)
        assert result == -11, "-1 + (-10)은 -11이어야 합니다."
    
    def test_subtraction(self, calculator):
        """뺄셈 테스트: 5 - 2 = 3"""
        result = calculator.subtract(5, 2)
        assert result == 3, "5 - 2는 3이어야 합니다."
    
    def test_multiplication_1(self, calculator):
        """곱셈 테스트: -5 * -3 = 15"""
        result = calculator.multiply(-5, -3)
        assert result == 15, "-5 * -3은 15이어야 합니다."
    
    def test_multiplication_2(self, calculator):
        """곱셈 테스트: 0 * 10 = 0"""
        result = calculator.multiply(0, 10)
        assert result == 0, "0 * 10은 0이어야 합니다."
    
    def test_integer_division(self, calculator):
        """정수 나눗셈 테스트: 5 / 2 = 2"""
        result = calculator.divide(5, 2)
        assert result == 2, "5 / 2는 2이어야 합니다 (정수 나눗셈)."
    
    def test_quotient(self, calculator):
        """소수점 나눗셈 테스트: 5 ÷ 2 = 2.5"""
        result = calculator.quotient(5, 2)
        assert abs(result - 2.5) < 0.0001, "5 ÷ 2는 2.5이어야 합니다."
    
    def test_division(self, calculator):
        """나눗셈 테스트: -10 / 2 = -5"""
        result = calculator.divide(-10, 2)
        assert result == -5, "-10 / 2는 -5이어야 합니다."
    
    def test_division_by_zero(self, calculator):
        """예외 처리 테스트: 0 / 0는 ZeroDivisionError 또는 ArithmeticError 발생"""
        with pytest.raises((ZeroDivisionError, ArithmeticError)):
            calculator.divide(0, 0)

