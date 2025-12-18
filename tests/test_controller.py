"""
계산기 컨트롤러 테스트
리팩토링 검증을 위한 단위 테스트 및 통합 테스트
"""

import pytest
from src.arithmetic.arithmetic_calculator import ArithmeticCalculator
from src.gui.controller import CalculatorController


class TestCalculatorController:
    """계산기 컨트롤러 테스트"""
    
    @pytest.fixture
    def calculator(self):
        """계산기 인스턴스 생성"""
        return ArithmeticCalculator()
    
    @pytest.fixture
    def controller(self, calculator):
        """컨트롤러 인스턴스 생성"""
        return CalculatorController(calculator)
    
    # 초기화 테스트
    def test_initialization(self, controller):
        """컨트롤러 초기화 테스트"""
        assert controller.display_value == "0"
        assert controller.first_operand is None
        assert controller.pending_operator is None
        assert controller.waiting_for_operand is True
    
    # 숫자 입력 테스트
    def test_input_digit_single(self, controller):
        """단일 숫자 입력 테스트"""
        assert controller.input_digit("5") is True
        assert controller.get_display_value() == "5"
        assert controller.waiting_for_operand is False
    
    def test_input_digit_multiple(self, controller):
        """여러 숫자 입력 테스트"""
        controller.input_digit("1")
        controller.input_digit("2")
        controller.input_digit("3")
        assert controller.get_display_value() == "123"
    
    def test_input_digit_invalid(self, controller):
        """유효하지 않은 숫자 입력 테스트"""
        assert controller.input_digit("a") is False
        assert controller.input_digit("") is False
        assert controller.get_display_value() == "0"
    
    def test_input_digit_after_operator(self, controller):
        """연산자 입력 후 숫자 입력 테스트"""
        controller.input_digit("5")
        controller.set_operator("+")
        controller.input_digit("3")
        assert controller.get_display_value() == "3"
    
    # 연산자 설정 테스트
    def test_set_operator_valid(self, controller):
        """유효한 연산자 설정 테스트"""
        controller.input_digit("5")
        assert controller.set_operator("+") is True
        assert controller.pending_operator == "+"
        assert controller.first_operand == 5
        assert controller.waiting_for_operand is True
    
    def test_set_operator_invalid(self, controller):
        """유효하지 않은 연산자 설정 테스트"""
        controller.input_digit("5")
        assert controller.set_operator("%") is False
        assert controller.pending_operator is None
    
    def test_set_operator_without_number(self, controller):
        """숫자 없이 연산자 설정 테스트 (기본값 0 사용)"""
        # 초기 상태에서 display_value가 "0"이므로 연산자 설정 가능
        assert controller.set_operator("+") is True
        assert controller.first_operand == 0
    
    # 계산 테스트
    def test_calculate_addition(self, controller):
        """덧셈 계산 테스트"""
        controller.input_digit("5")
        controller.set_operator("+")
        controller.input_digit("3")
        assert controller.calculate() is True
        assert controller.get_display_value() == "8"
    
    def test_calculate_subtraction(self, controller):
        """뺄셈 계산 테스트"""
        controller.input_digit("10")
        controller.set_operator("-")
        controller.input_digit("3")
        assert controller.calculate() is True
        assert controller.get_display_value() == "7"
    
    def test_calculate_multiplication(self, controller):
        """곱셈 계산 테스트"""
        controller.input_digit("5")
        controller.set_operator("×")
        controller.input_digit("3")
        assert controller.calculate() is True
        assert controller.get_display_value() == "15"
    
    def test_calculate_division(self, controller):
        """나눗셈 계산 테스트"""
        controller.input_digit("10")
        controller.set_operator("÷")
        controller.input_digit("2")
        assert controller.calculate() is True
        assert controller.get_display_value() == "5"
    
    def test_calculate_quotient(self, controller):
        """소수점 나눗셈 계산 테스트"""
        controller.input_digit("5")
        controller.set_operator("/")
        controller.input_digit("2")
        assert controller.calculate() is True
        result = float(controller.get_display_value())
        assert abs(result - 2.5) < 0.0001
    
    def test_calculate_division_by_zero(self, controller):
        """0으로 나누기 테스트"""
        controller.input_digit("5")
        controller.set_operator("÷")
        controller.input_digit("0")
        # calculate()에서 ZeroDivisionError 발생 시 clear()가 호출되어 "0"으로 리셋됨
        assert controller.calculate() is False
        assert controller.get_display_value() == "0"
        assert controller.first_operand is None
        assert controller.pending_operator is None
    
    def test_calculate_without_operator(self, controller):
        """연산자 없이 계산 테스트"""
        controller.input_digit("5")
        assert controller.calculate() is False
    
    def test_calculate_chain_operations(self, controller):
        """연속 연산 테스트"""
        # 5 + 3 = 8
        controller.input_digit("5")
        controller.set_operator("+")
        controller.input_digit("3")
        controller.calculate()
        assert controller.get_display_value() == "8"
        
        # 8 * 2 = 16
        controller.set_operator("×")
        controller.input_digit("2")
        controller.calculate()
        assert controller.get_display_value() == "16"
    
    # 부호 변경 테스트
    def test_toggle_sign_positive(self, controller):
        """양수 부호 변경 테스트"""
        controller.input_digit("5")
        controller.toggle_sign()
        assert controller.get_display_value() == "-5"
    
    def test_toggle_sign_negative(self, controller):
        """음수 부호 변경 테스트"""
        controller.input_digit("5")
        controller.toggle_sign()
        controller.toggle_sign()
        assert controller.get_display_value() == "5"
    
    def test_toggle_sign_zero(self, controller):
        """0 부호 변경 테스트"""
        controller.toggle_sign()
        assert controller.get_display_value() == "0"
    
    # 초기화 테스트
    def test_clear(self, controller):
        """초기화 테스트"""
        controller.input_digit("123")
        controller.set_operator("+")
        controller.clear()
        assert controller.get_display_value() == "0"
        assert controller.first_operand is None
        assert controller.pending_operator is None
        assert controller.waiting_for_operand is True
    
    # 디스플레이 값 테스트
    def test_get_display_value(self, controller):
        """디스플레이 값 반환 테스트"""
        assert controller.get_display_value() == "0"
        controller.input_digit("42")
        assert controller.get_display_value() == "42"
    
    # perform_operation 테스트
    def test_perform_operation_addition(self, controller):
        """직접 연산 수행 테스트 - 덧셈"""
        result = controller.perform_operation(5, "+", 3)
        assert result == 8
    
    def test_perform_operation_subtraction(self, controller):
        """직접 연산 수행 테스트 - 뺄셈"""
        result = controller.perform_operation(10, "-", 3)
        assert result == 7
    
    def test_perform_operation_multiplication(self, controller):
        """직접 연산 수행 테스트 - 곱셈"""
        result = controller.perform_operation(5, "×", 3)
        assert result == 15
    
    def test_perform_operation_division(self, controller):
        """직접 연산 수행 테스트 - 나눗셈"""
        result = controller.perform_operation(10, "÷", 2)
        assert result == 5
    
    def test_perform_operation_quotient(self, controller):
        """직접 연산 수행 테스트 - 소수점 나눗셈"""
        result = controller.perform_operation(5, "/", 2)
        assert abs(result - 2.5) < 0.0001
    
    def test_perform_operation_division_by_zero(self, controller):
        """직접 연산 수행 테스트 - 0으로 나누기"""
        with pytest.raises(ZeroDivisionError):
            controller.perform_operation(5, "÷", 0)
    
    def test_perform_operation_unsupported_operator(self, controller):
        """직접 연산 수행 테스트 - 지원하지 않는 연산자"""
        with pytest.raises(ValueError):
            controller.perform_operation(5, "%", 3)
    
    # 통합 테스트 시나리오
    def test_integration_scenario_1(self, controller):
        """통합 테스트 시나리오 1: 간단한 계산"""
        # 5 + 3 = 8
        controller.input_digit("5")
        controller.set_operator("+")
        controller.input_digit("3")
        controller.calculate()
        assert controller.get_display_value() == "8"
    
    def test_integration_scenario_2(self, controller):
        """통합 테스트 시나리오 2: 연속 계산"""
        # 10 - 4 = 6, 그 다음 6 * 2 = 12
        controller.input_digit("10")
        controller.set_operator("-")
        controller.input_digit("4")
        controller.calculate()
        assert controller.get_display_value() == "6"
        
        controller.set_operator("×")
        controller.input_digit("2")
        controller.calculate()
        assert controller.get_display_value() == "12"
    
    def test_integration_scenario_3(self, controller):
        """통합 테스트 시나리오 3: 부호 변경 후 계산"""
        # -5 + 3 = -2
        controller.input_digit("5")
        controller.toggle_sign()
        assert controller.get_display_value() == "-5"
        controller.set_operator("+")
        controller.input_digit("3")
        controller.calculate()
        assert controller.get_display_value() == "-2"
    
    def test_integration_scenario_4(self, controller):
        """통합 테스트 시나리오 4: 오류 후 재시작"""
        # 5 / 0 = Error (clear()가 자동 호출되어 "0"으로 리셋됨)
        controller.input_digit("5")
        controller.set_operator("÷")
        controller.input_digit("0")
        controller.calculate()
        # calculate()에서 ZeroDivisionError 발생 시 clear()가 호출되어 "0"으로 리셋됨
        assert controller.get_display_value() == "0"
        assert controller.first_operand is None
        assert controller.pending_operator is None
        
        # 이미 clear된 상태이므로 바로 새 계산 가능
        controller.input_digit("10")
        controller.set_operator("+")
        controller.input_digit("5")
        controller.calculate()
        assert controller.get_display_value() == "15"

