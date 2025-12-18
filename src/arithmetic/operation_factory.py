"""
연산 전략 팩토리
SOLID 원칙 - Open/Closed Principle (OCP) 적용
Factory Pattern 구현
"""

from typing import Optional
from src.arithmetic.interfaces import IOperationStrategy
from src.arithmetic.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    QuotientOperation
)


class OperationFactory:
    """연산 전략을 생성하는 팩토리 클래스"""
    
    # 매직 스트링 제거: 상수로 정의
    OPERATOR_ADD = "+"
    OPERATOR_SUBTRACT = "-"
    OPERATOR_MULTIPLY = "×"
    OPERATOR_DIVIDE = "÷"
    OPERATOR_QUOTIENT = "/"
    
    # 지원되는 연산자 목록
    SUPPORTED_OPERATORS = {
        OPERATOR_ADD,
        OPERATOR_SUBTRACT,
        OPERATOR_MULTIPLY,
        OPERATOR_DIVIDE,
        OPERATOR_QUOTIENT
    }
    
    @staticmethod
    def create(operator: str) -> Optional[IOperationStrategy]:
        """연산자 문자열로부터 연산 전략 인스턴스를 생성
        
        Args:
            operator: 연산자 문자열 (+, -, ×, ÷, /)
            
        Returns:
            IOperationStrategy 인스턴스 또는 None (지원하지 않는 연산자)
        """
        operator_map = {
            OperationFactory.OPERATOR_ADD: AddOperation,
            OperationFactory.OPERATOR_SUBTRACT: SubtractOperation,
            OperationFactory.OPERATOR_MULTIPLY: MultiplyOperation,
            OperationFactory.OPERATOR_DIVIDE: DivideOperation,
            OperationFactory.OPERATOR_QUOTIENT: QuotientOperation,
        }
        
        operation_class = operator_map.get(operator)
        if operation_class:
            return operation_class()
        return None
    
    @staticmethod
    def is_supported(operator: str) -> bool:
        """연산자가 지원되는지 확인
        
        Args:
            operator: 연산자 문자열
            
        Returns:
            지원 여부
        """
        return operator in OperationFactory.SUPPORTED_OPERATORS

