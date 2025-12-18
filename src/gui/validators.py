"""
입력 검증 모듈
SOLID 원칙 - Single Responsibility Principle (SRP) 적용
"""

from typing import Optional


class InputValidator:
    """입력 검증 클래스"""
    
    @staticmethod
    def validate_number(value: str) -> Optional[int]:
        """문자열을 정수로 변환하고 검증
        
        Args:
            value: 입력 문자열
            
        Returns:
            변환된 정수 또는 None (유효하지 않은 입력)
        """
        try:
            return int(value)
        except ValueError:
            return None
    
    @staticmethod
    def is_valid_number(value: str) -> bool:
        """입력 문자열이 유효한 정수인지 확인
        
        Args:
            value: 입력 문자열
            
        Returns:
            유효 여부
        """
        return InputValidator.validate_number(value) is not None
    
    @staticmethod
    def validate_operator(operator: str) -> bool:
        """연산자가 유효한지 확인
        
        Args:
            operator: 연산자 문자열
            
        Returns:
            유효 여부
        """
        from src.arithmetic.operation_factory import OperationFactory
        return OperationFactory.is_supported(operator)

