"""
커스텀 위젯 모듈
필요시 재사용 가능한 커스텀 위젯을 정의합니다.
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from typing import Optional


class CalculatorButton(QPushButton):
    """계산기 전용 버튼 위젯
    
    재사용 가능한 커스텀 버튼 위젯입니다.
    필요시 스타일이나 동작을 확장할 수 있습니다.
    """
    
    def __init__(self, text: str, parent=None):
        """버튼 초기화
        
        Args:
            text: 버튼에 표시할 텍스트
            parent: 부모 위젯
        """
        super().__init__(text, parent)
        self.setMinimumSize(60, 60)
        self.setFont(QFont("Arial", 16))
        self._apply_default_style()
    
    def _apply_default_style(self):
        """기본 스타일 적용"""
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #f5f5f5;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
    
    def set_operator_style(self):
        """연산자 버튼 스타일 적용"""
        self.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)
    
    def set_equals_style(self):
        """등호 버튼 스타일 적용"""
        self.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: 1px solid #005a9e;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """)
    
    def set_special_style(self):
        """특수 버튼 스타일 적용"""
        self.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)


class CalculatorDisplay(QPushButton):
    """계산기 디스플레이 위젯 (향후 확장용)
    
    현재는 QLineEdit을 사용하지만, 필요시 커스텀 디스플레이 위젯으로 확장 가능합니다.
    """
    pass

