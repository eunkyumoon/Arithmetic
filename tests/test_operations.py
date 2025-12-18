"""
연산 전략 및 팩토리 테스트
리팩토링 검증을 위한 단위 테스트
"""

import pytest
from src.arithmetic.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    QuotientOperation
)
from src.arithmetic.operation_factory import OperationFactory


class TestAddOperation:
    """덧셈 연산 전략 테스트"""
    
    @pytest.fixture
    def operation(self):
        """덧셈 연산 인스턴스 생성"""
        return AddOperation()
    
    def test_execute_positive_numbers(self, operation):
        """양수 덧셈 테스트"""
        assert operation.execute(1, 10) == 11
        assert operation.execute(5, 3) == 8
    
    def test_execute_with_zero(self, operation):
        """0 포함 덧셈 테스트"""
        assert operation.execute(0, 1) == 1
        assert operation.execute(5, 0) == 5
    
    def test_execute_negative_numbers(self, operation):
        """음수 덧셈 테스트"""
        assert operation.execute(-1, -10) == -11
        assert operation.execute(-5, 3) == -2
    
    def test_get_symbol(self, operation):
        """덧셈 기호 반환 테스트"""
        assert operation.get_symbol() == "+"


class TestSubtractOperation:
    """뺄셈 연산 전략 테스트"""
    
    @pytest.fixture
    def operation(self):
        """뺄셈 연산 인스턴스 생성"""
        return SubtractOperation()
    
    def test_execute_basic(self, operation):
        """기본 뺄셈 테스트"""
        assert operation.execute(5, 2) == 3
        assert operation.execute(10, 5) == 5
    
    def test_execute_negative_result(self, operation):
        """음수 결과 테스트"""
        assert operation.execute(2, 5) == -3
    
    def test_execute_with_zero(self, operation):
        """0 포함 뺄셈 테스트"""
        assert operation.execute(5, 0) == 5
        assert operation.execute(0, 5) == -5
    
    def test_get_symbol(self, operation):
        """뺄셈 기호 반환 테스트"""
        assert operation.get_symbol() == "-"


class TestMultiplyOperation:
    """곱셈 연산 전략 테스트"""
    
    @pytest.fixture
    def operation(self):
        """곱셈 연산 인스턴스 생성"""
        return MultiplyOperation()
    
    def test_execute_positive_numbers(self, operation):
        """양수 곱셈 테스트"""
        assert operation.execute(5, 3) == 15
        assert operation.execute(2, 4) == 8
    
    def test_execute_negative_numbers(self, operation):
        """음수 곱셈 테스트"""
        assert operation.execute(-5, -3) == 15
        assert operation.execute(-2, 3) == -6
    
    def test_execute_with_zero(self, operation):
        """0 곱셈 테스트"""
        assert operation.execute(0, 10) == 0
        assert operation.execute(5, 0) == 0
    
    def test_get_symbol(self, operation):
        """곱셈 기호 반환 테스트"""
        assert operation.get_symbol() == "×"


class TestDivideOperation:
    """정수 나눗셈 연산 전략 테스트"""
    
    @pytest.fixture
    def operation(self):
        """정수 나눗셈 연산 인스턴스 생성"""
        return DivideOperation()
    
    def test_execute_basic(self, operation):
        """기본 정수 나눗셈 테스트"""
        assert operation.execute(5, 2) == 2
        assert operation.execute(10, 2) == 5
    
    def test_execute_negative_numbers(self, operation):
        """음수 나눗셈 테스트"""
        assert operation.execute(-10, 2) == -5
        assert operation.execute(10, -2) == -5
    
    def test_execute_division_by_zero(self, operation):
        """0으로 나누기 예외 테스트"""
        with pytest.raises(ZeroDivisionError):
            operation.execute(5, 0)
        with pytest.raises(ZeroDivisionError):
            operation.execute(0, 0)
    
    def test_get_symbol(self, operation):
        """나눗셈 기호 반환 테스트"""
        assert operation.get_symbol() == "÷"


class TestQuotientOperation:
    """소수점 나눗셈 연산 전략 테스트"""
    
    @pytest.fixture
    def operation(self):
        """소수점 나눗셈 연산 인스턴스 생성"""
        return QuotientOperation()
    
    def test_execute_basic(self, operation):
        """기본 소수점 나눗셈 테스트"""
        result = operation.execute(5, 2)
        assert abs(result - 2.5) < 0.0001
    
    def test_execute_exact_division(self, operation):
        """정확히 나누어떨어지는 경우 테스트"""
        result = operation.execute(10, 2)
        assert abs(result - 5.0) < 0.0001
    
    def test_execute_division_by_zero(self, operation):
        """0으로 나누기 예외 테스트"""
        with pytest.raises(ZeroDivisionError):
            operation.execute(5, 0)
    
    def test_get_symbol(self, operation):
        """나눗셈 기호 반환 테스트"""
        assert operation.get_symbol() == "/"


class TestOperationFactory:
    """연산 팩토리 테스트"""
    
    def test_create_add_operation(self):
        """덧셈 연산 생성 테스트"""
        operation = OperationFactory.create("+")
        assert operation is not None
        assert isinstance(operation, AddOperation)
        assert operation.execute(1, 2) == 3
    
    def test_create_subtract_operation(self):
        """뺄셈 연산 생성 테스트"""
        operation = OperationFactory.create("-")
        assert operation is not None
        assert isinstance(operation, SubtractOperation)
        assert operation.execute(5, 2) == 3
    
    def test_create_multiply_operation(self):
        """곱셈 연산 생성 테스트"""
        operation = OperationFactory.create("×")
        assert operation is not None
        assert isinstance(operation, MultiplyOperation)
        assert operation.execute(3, 4) == 12
    
    def test_create_divide_operation(self):
        """정수 나눗셈 연산 생성 테스트"""
        operation = OperationFactory.create("÷")
        assert operation is not None
        assert isinstance(operation, DivideOperation)
        assert operation.execute(10, 2) == 5
    
    def test_create_quotient_operation(self):
        """소수점 나눗셈 연산 생성 테스트"""
        operation = OperationFactory.create("/")
        assert operation is not None
        assert isinstance(operation, QuotientOperation)
        result = operation.execute(5, 2)
        assert abs(result - 2.5) < 0.0001
    
    def test_create_unsupported_operator(self):
        """지원하지 않는 연산자 테스트"""
        operation = OperationFactory.create("%")
        assert operation is None
    
    def test_is_supported_valid_operators(self):
        """지원되는 연산자 확인 테스트"""
        assert OperationFactory.is_supported("+") is True
        assert OperationFactory.is_supported("-") is True
        assert OperationFactory.is_supported("×") is True
        assert OperationFactory.is_supported("÷") is True
        assert OperationFactory.is_supported("/") is True
    
    def test_is_supported_invalid_operators(self):
        """지원하지 않는 연산자 확인 테스트"""
        assert OperationFactory.is_supported("%") is False
        assert OperationFactory.is_supported("**") is False
        assert OperationFactory.is_supported("") is False
    
    def test_supported_operators_set(self):
        """지원되는 연산자 집합 테스트"""
        expected_operators = {"+", "-", "×", "÷", "/"}
        assert OperationFactory.SUPPORTED_OPERATORS == expected_operators

