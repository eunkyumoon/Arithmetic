"""
PyQt 계산기 애플리케이션 진입점
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.arithmetic.arithmetic_calculator import ArithmeticCalculator
from src.gui.controller import CalculatorController
from src.gui.view import CalculatorView


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    
    # 의존성 주입: 계산기 인스턴스 생성
    calculator = ArithmeticCalculator()
    
    # 컨트롤러 생성
    controller = CalculatorController(calculator)
    
    # 뷰 생성 및 표시
    view = CalculatorView(controller)
    view.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

