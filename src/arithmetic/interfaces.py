"""
계산기 인터페이스 정의
SOLID 원칙 - Dependency Inversion Principle (DIP) 적용
"""

from abc import ABC, abstractmethod
from typing import Union


class ICalculator(ABC):
    """계산기 인터페이스"""
    
    @abstractmethod
    def add(self, a: int, b: int) -> int:
        """덧셈 연산"""
        pass
    
    @abstractmethod
    def subtract(self, a: int, b: int) -> int:
        """뺄셈 연산"""
        pass
    
    @abstractmethod
    def multiply(self, a: int, b: int) -> int:
        """곱셈 연산"""
        pass
    
    @abstractmethod
    def divide(self, a: int, b: int) -> int:
        """정수 나눗셈 연산"""
        pass
    
    @abstractmethod
    def quotient(self, a: int, b: int) -> float:
        """소수점 나눗셈 연산"""
        pass


class IOperationStrategy(ABC):
    """연산 전략 인터페이스
    SOLID 원칙 - Open/Closed Principle (OCP) 적용
    """
    
    @abstractmethod
    def execute(self, a: int, b: int) -> Union[int, float]:
        """연산을 수행하고 결과를 반환"""
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """연산자 기호를 반환"""
        pass

