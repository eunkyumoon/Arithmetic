"""
연산 전략 구현
SOLID 원칙 - Open/Closed Principle (OCP) 적용
Strategy Pattern 구현
"""

from typing import Union
from src.arithmetic.interfaces import IOperationStrategy


class AddOperation(IOperationStrategy):
    """덧셈 연산 전략"""
    
    def execute(self, a: int, b: int) -> int:
        """덧셈 수행"""
        return a + b
    
    def get_symbol(self) -> str:
        """덧셈 기호 반환"""
        return "+"


class SubtractOperation(IOperationStrategy):
    """뺄셈 연산 전략"""
    
    def execute(self, a: int, b: int) -> int:
        """뺄셈 수행"""
        return a - b
    
    def get_symbol(self) -> str:
        """뺄셈 기호 반환"""
        return "-"


class MultiplyOperation(IOperationStrategy):
    """곱셈 연산 전략"""
    
    def execute(self, a: int, b: int) -> int:
        """곱셈 수행"""
        return a * b
    
    def get_symbol(self) -> str:
        """곱셈 기호 반환"""
        return "×"


class DivideOperation(IOperationStrategy):
    """정수 나눗셈 연산 전략"""
    
    def execute(self, a: int, b: int) -> int:
        """정수 나눗셈 수행"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a // b
    
    def get_symbol(self) -> str:
        """나눗셈 기호 반환"""
        return "÷"


class QuotientOperation(IOperationStrategy):
    """소수점 나눗셈 연산 전략"""
    
    def execute(self, a: int, b: int) -> float:
        """소수점 나눗셈 수행"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    
    def get_symbol(self) -> str:
        """나눗셈 기호 반환"""
        return "/"

