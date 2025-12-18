"""
PyQt 계산기 애플리케이션 진입점
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
# 이 파일이 src/gui/main.py에 있으므로, 프로젝트 루트는 상위 2단계
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

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

