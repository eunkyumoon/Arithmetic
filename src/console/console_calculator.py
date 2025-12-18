"""
간단한 사칙연산 콘솔 프로그램
사용자로부터 두 정수와 연산자를 입력받아 계산 결과를 출력합니다.
"""

import sys
import os

# 프로젝트 루트를 경로에 추가
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
sys.path.insert(0, project_root)

from src.arithmetic.arithmetic_calculator import ArithmeticCalculator


def get_integer_input(prompt: str) -> int:
    """정수 입력을 받는 함수"""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input() -> str:
    """연산자 입력을 받는 함수"""
    while True:
        operator = input("연산자 >>")
        if operator in ['+', '-', '*', '/', '//', '%']:
            return operator
        print("올바른 연산자를 입력해주세요. (+, -, *, /, //, %)")


def calculate(calculator: ArithmeticCalculator, a: int, operator: str, b: int):
    """계산을 수행하고 결과를 출력하는 함수"""
    # 연산자에 따른 계산
    if operator == '+':
        result = calculator.add(a, b)
        operator_display = '+'
    elif operator == '-':
        result = calculator.subtract(a, b)
        operator_display = '-'
    elif operator == '*':
        result = calculator.multiply(a, b)
        operator_display = '*'
    elif operator == '/':
        # 소수점 나눗셈
        result = calculator.quotient(a, b)
        operator_display = '/'
    elif operator == '//':
        # 정수 나눗셈
        result = calculator.divide(a, b)
        operator_display = '//'
    else:
        print("지원하지 않는 연산자입니다.")
        return
    
    # 결과 출력
    print("=" * 50)
    print(f"{a} {operator_display} {b}을 계산합니다.")
    print("=" * 50)
    
    # 소수점이 있는 경우와 없는 경우 구분
    if isinstance(result, float):
        print(f"{a}{operator_display}{b}={result}입니다.")
    else:
        print(f"{a}{operator_display}{b}={result}입니다.")


def main():
    """메인 함수"""
    calculator = ArithmeticCalculator()
    
    # 첫번째 정수 입력
    first_number = get_integer_input("첫번째 정수값>>")
    
    # 연산자 입력
    operator = get_operator_input()
    
    # 두번째 정수 입력
    second_number = get_integer_input("두번째 정수값>>")
    
    # 계산 및 결과 출력
    try:
        calculate(calculator, first_number, operator, second_number)
    except ZeroDivisionError as e:
        print("=" * 50)
        print(f"{first_number} {operator} {second_number}을 계산합니다.")
        print("=" * 50)
        print(f"오류: {e}")


if __name__ == "__main__":
    main()

