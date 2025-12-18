"""
계산기 컨트롤러
SOLID 원칙 - Single Responsibility Principle (SRP) 적용
의존성 주입을 통한 Dependency Inversion Principle (DIP) 적용
"""

from typing import Optional, Union, Callable
from src.arithmetic.interfaces import ICalculator, IOperationStrategy
from src.arithmetic.operation_factory import OperationFactory
from src.gui.validators import InputValidator
from src.gui.formatters import ResultFormatter
from src.gui.constants import DisplayConstants


class CalculatorController:
    """계산기 컨트롤러 클래스
    
    UI와 비즈니스 로직 사이의 중재자 역할을 수행합니다.
    """
    
    def __init__(self, calculator: ICalculator):
        """컨트롤러 초기화
        
        Args:
            calculator: 계산기 인스턴스 (의존성 주입)
        """
        self.calculator = calculator
        self.validator = InputValidator()
        self.formatter = ResultFormatter()
        
        # 계산 상태 관리
        self.first_operand: Optional[int] = None
        self.pending_operator: Optional[str] = None
        self.display_value: str = DisplayConstants.DEFAULT_VALUE
        self.waiting_for_operand: bool = True
    
    def input_digit(self, digit: str) -> bool:
        """숫자 입력 처리 (0-9)
        
        Args:
            digit: 입력된 숫자 문자열 (0-9)
            
        Returns:
            입력 성공 여부
        """
        if not digit.isdigit():
            return False
        
        if self.waiting_for_operand:
            self.display_value = digit
            self.waiting_for_operand = False
        else:
            if self.display_value == DisplayConstants.DEFAULT_VALUE:
                self.display_value = digit
            else:
                self.display_value += digit
        
        return True
    
    def input_number(self, number: int):
        """숫자 직접 설정 (내부 사용)
        
        Args:
            number: 설정할 숫자
        """
        self.display_value = self.formatter.format_result(number)
        self.waiting_for_operand = False
    
    def set_operator(self, operator: str) -> bool:
        """연산자 설정
        
        Args:
            operator: 연산자 문자열
            
        Returns:
            설정 성공 여부
        """
        if not self.validator.validate_operator(operator):
            return False
        
        # 현재 표시된 값을 첫 번째 피연산자로 저장
        current = self._get_current_value()
        if current is None:
            return False
        
        # 이전 연산이 있으면 먼저 수행
        if self.pending_operator is not None and self.first_operand is not None:
            try:
                result = self.perform_operation(
                    self.first_operand,
                    self.pending_operator,
                    current
                )
                self.first_operand = int(result) if isinstance(result, int) else None
                self.display_value = self.formatter.format_result(result)
            except ZeroDivisionError:
                return self._handle_division_error()
        
        self.first_operand = current
        self.pending_operator = operator
        self.waiting_for_operand = True
        return True
    
    def calculate(self) -> bool:
        """계산 수행 (= 버튼)
        
        Returns:
            계산 성공 여부
        """
        if self.pending_operator is None or self.first_operand is None:
            return False
        
        current = self._get_current_value()
        if current is None:
            return False
        
        try:
            result = self.perform_operation(
                self.first_operand,
                self.pending_operator,
                current
            )
            self.display_value = self.formatter.format_result(result)
            self.first_operand = None
            self.pending_operator = None
            self.waiting_for_operand = True
            return True
        except ZeroDivisionError:
            return self._handle_division_error()
    
    def _handle_division_error(self) -> bool:
        """0으로 나누기 오류 처리
        
        Returns:
            항상 False (오류 발생)
        """
        self.display_value = DisplayConstants.ERROR_MESSAGE
        self.clear()
        return False
    
    def _get_current_value(self) -> Optional[int]:
        """현재 표시 값을 정수로 변환
        
        Returns:
            현재 값 또는 None
        """
        if self.display_value == DisplayConstants.ERROR_MESSAGE:
            return None
        return self.validator.validate_number(self.display_value)
    
    def clear(self):
        """계산기 상태 초기화"""
        self.first_operand = None
        self.pending_operator = None
        self.display_value = DisplayConstants.DEFAULT_VALUE
        self.waiting_for_operand = True
    
    def toggle_sign(self):
        """부호 변경 (+/- 버튼)"""
        current = self._get_current_value()
        if current is not None:
            self.display_value = self.formatter.format_result(-current)
    
    def get_display_value(self) -> str:
        """현재 표시할 값을 반환
        
        Returns:
            포맷팅된 현재 값 문자열
        """
        return self.display_value
    
    def perform_operation(self, a: int, operator: str, b: int) -> Union[int, float]:
        """두 숫자와 연산자를 받아 계산 수행
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자
            b: 두 번째 피연산자
            
        Returns:
            계산 결과
            
        Raises:
            ZeroDivisionError: 0으로 나누는 경우
            ValueError: 지원하지 않는 연산자인 경우
        """
        operation = OperationFactory.create(operator)
        if operation is None:
            raise ValueError(f"Unsupported operator: {operator}")
        
        return operation.execute(a, b)

