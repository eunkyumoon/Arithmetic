"""
결과 포맷팅 모듈
SOLID 원칙 - Single Responsibility Principle (SRP) 적용
"""

from typing import Union


class ResultFormatter:
    """결과 포맷팅 클래스"""
    
    @staticmethod
    def format_result(value: Union[int, float]) -> str:
        """계산 결과를 문자열로 포맷팅
        
        Args:
            value: 계산 결과 (정수 또는 실수)
            
        Returns:
            포맷팅된 문자열
        """
        # 정수인 경우 소수점 없이 표시
        if isinstance(value, int):
            return str(value)
        
        # 실수인 경우 소수점 표시 (불필요한 .0 제거)
        if isinstance(value, float):
            # 정수로 표현 가능한 경우 정수로 표시
            if value.is_integer():
                return str(int(value))
            # 소수점이 있는 경우 표시
            return str(value)
        
        return str(value)
    
    @staticmethod
    def format_expression(a: int, operator: str, b: int) -> str:
        """계산식을 문자열로 포맷팅
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자
            b: 두 번째 피연산자
            
        Returns:
            포맷팅된 계산식 문자열
        """
        return f"{a} {operator} {b}"
    
    @staticmethod
    def format_full_result(a: int, operator: str, b: int, result: Union[int, float]) -> str:
        """전체 계산 결과를 문자열로 포맷팅
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자
            b: 두 번째 피연산자
            result: 계산 결과
            
        Returns:
            포맷팅된 전체 결과 문자열 (예: "5 + 3 = 8")
        """
        expression = ResultFormatter.format_expression(a, operator, b)
        formatted_result = ResultFormatter.format_result(result)
        return f"{expression} = {formatted_result}"

