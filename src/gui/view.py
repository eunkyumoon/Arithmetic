"""
PyQt 계산기 뷰
SOLID 원칙 - Single Responsibility Principle (SRP) 적용
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from typing import Optional
from src.gui.controller import CalculatorController


class CalculatorView(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self, controller: CalculatorController):
        """뷰 초기화
        
        Args:
            controller: 계산기 컨트롤러 인스턴스
        """
        super().__init__()
        self.controller = controller
        self._init_ui()
        self._connect_signals()
    
    def _init_ui(self):
        """UI 초기화"""
        self.setWindowTitle("Arithmetic Calculator")
        self.setFixedSize(300, 400)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이 (결과 표시 영역)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 20))
        self.display.setText("0")
        self.display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                background-color: #f5f5f5;
            }
        """)
        main_layout.addWidget(self.display)
        
        # 버튼 그리드 레이아웃
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        
        # 버튼 생성 및 배치
        # 첫 번째 행: 7, 8, 9, ×
        self._create_button("7", 0, 0, button_layout)
        self._create_button("8", 0, 1, button_layout)
        self._create_button("9", 0, 2, button_layout)
        self._create_button("×", 0, 3, button_layout, is_operator=True)
        
        # 두 번째 행: 4, 5, 6, −
        self._create_button("4", 1, 0, button_layout)
        self._create_button("5", 1, 1, button_layout)
        self._create_button("6", 1, 2, button_layout)
        self._create_button("−", 1, 3, button_layout, is_operator=True)
        
        # 세 번째 행: 1, 2, 3, +
        self._create_button("1", 2, 0, button_layout)
        self._create_button("2", 2, 1, button_layout)
        self._create_button("3", 2, 2, button_layout)
        self._create_button("+", 2, 3, button_layout, is_operator=True)
        
        # 네 번째 행: +/-, 0, ., = (= 버튼은 더블 높이)
        self._create_button("+/-", 3, 0, button_layout, is_special=True)
        self._create_button("0", 3, 1, button_layout)
        self._create_button(".", 3, 2, button_layout, is_special=True)
        equals_button = self._create_button("=", 3, 3, button_layout, is_equals=True)
        equals_button.setMinimumHeight(130)  # = 버튼을 더블 높이로 (2행 + 간격)
        
        # 다섯 번째 행: C (Clear), ÷ (나눗셈)
        self._create_button("C", 4, 0, button_layout, is_special=True)
        self._create_button("÷", 4, 1, button_layout, is_operator=True)
        
        main_layout.addLayout(button_layout)
    
    def _create_button(self, text: str, row: int, col: int, layout: QGridLayout,
                      is_operator: bool = False, is_equals: bool = False,
                      is_special: bool = False) -> QPushButton:
        """버튼 생성 및 스타일 설정
        
        Args:
            text: 버튼 텍스트
            row: 그리드 행 위치
            col: 그리드 열 위치
            layout: 그리드 레이아웃
            is_operator: 연산자 버튼 여부
            is_equals: 등호 버튼 여부
            is_special: 특수 버튼 여부
            
        Returns:
            생성된 버튼
        """
        button = QPushButton(text)
        button.setMinimumSize(60, 60)
        button.setFont(QFont("Arial", 16))
        
        # 버튼 스타일 설정
        if is_equals:
            # 등호 버튼: 파란색 배경
            button.setStyleSheet("""
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
        elif is_operator:
            # 연산자 버튼: 회색 배경
            button.setStyleSheet("""
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
        elif is_special:
            # 특수 버튼: 연한 회색 배경
            button.setStyleSheet("""
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
        else:
            # 숫자 버튼: 흰색 배경
            button.setStyleSheet("""
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
        
        layout.addWidget(button, row, col)
        return button
    
    def _connect_signals(self):
        """버튼 시그널 연결"""
        # 모든 버튼 찾기
        buttons = self.findChildren(QPushButton)
        
        for button in buttons:
            text = button.text()
            
            if text.isdigit():
                # 숫자 버튼
                button.clicked.connect(lambda checked, digit=text: self._on_digit_clicked(digit))
            elif text == "=":
                # 등호 버튼
                button.clicked.connect(self._on_equals_clicked)
            elif text == "+/-":
                # 부호 변경 버튼
                button.clicked.connect(self._on_toggle_sign_clicked)
            elif text == "C":
                # 클리어 버튼
                button.clicked.connect(self._on_clear_clicked)
            elif text == ".":
                # 소수점 버튼 (현재는 정수만 지원하므로 무시)
                button.clicked.connect(self._on_decimal_clicked)
            elif text in ["+", "−", "×", "÷"]:
                # 연산자 버튼
                operator_map = {
                    "+": "+",
                    "−": "-",
                    "×": "×",
                    "÷": "÷"
                }
                operator = operator_map[text]
                button.clicked.connect(lambda checked, op=operator: self._on_operator_clicked(op))
    
    def _on_digit_clicked(self, digit: str):
        """숫자 버튼 클릭 핸들러"""
        if self.controller.input_digit(digit):
            self._update_display()
    
    def _on_operator_clicked(self, operator: str):
        """연산자 버튼 클릭 핸들러"""
        if self.controller.set_operator(operator):
            self._update_display()
    
    def _on_equals_clicked(self):
        """등호 버튼 클릭 핸들러"""
        if self.controller.calculate():
            self._update_display()
    
    def _on_toggle_sign_clicked(self):
        """부호 변경 버튼 클릭 핸들러"""
        self.controller.toggle_sign()
        self._update_display()
    
    def _on_clear_clicked(self):
        """클리어 버튼 클릭 핸들러"""
        self.controller.clear()
        self._update_display()
    
    def _on_decimal_clicked(self):
        """소수점 버튼 클릭 핸들러 (현재 미구현)"""
        # 정수만 지원하므로 무시
        pass
    
    def _update_display(self):
        """디스플레이 업데이트"""
        display_value = self.controller.get_display_value()
        self.display.setText(display_value)

