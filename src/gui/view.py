"""
PyQt 계산기 뷰
SOLID 원칙 - Single Responsibility Principle (SRP) 적용
"""

from dataclasses import dataclass
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from typing import Optional, Callable
from src.gui.controller import CalculatorController
from src.gui.constants import (
    UIConstants, DisplayConstants, ButtonText, ButtonType
)
from src.gui.button_styles import ButtonStyles


@dataclass
class ButtonConfig:
    """버튼 설정 데이터 클래스"""
    text: str
    row: int
    col: int
    button_type: str = ButtonType.NUMBER


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
        self.setFixedSize(UIConstants.WINDOW_WIDTH, UIConstants.WINDOW_HEIGHT)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self._create_display(main_layout)
        self._create_button_grid(main_layout)
    
    def _create_display(self, layout: QVBoxLayout):
        """디스플레이 생성"""
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont(UIConstants.FONT_FAMILY, UIConstants.DISPLAY_FONT_SIZE))
        self.display.setText(DisplayConstants.DEFAULT_VALUE)
        self.display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                background-color: #f5f5f5;
            }
        """)
        layout.addWidget(self.display)
    
    def _create_button_grid(self, layout: QVBoxLayout):
        """버튼 그리드 생성"""
        button_layout = QGridLayout()
        button_layout.setSpacing(UIConstants.BUTTON_SPACING)
        
        button_configs = self._get_button_configs()
        for config in button_configs:
            button = self._create_button_widget(config)
            self._apply_button_style(button, config.button_type)
            self._add_button_to_layout(button, config, button_layout)
        
        layout.addLayout(button_layout)
    
    def _get_button_configs(self) -> list[ButtonConfig]:
        """버튼 설정 목록 반환"""
        return [
            # 첫 번째 행: 7, 8, 9, ×
            ButtonConfig("7", 0, 0),
            ButtonConfig("8", 0, 1),
            ButtonConfig("9", 0, 2),
            ButtonConfig(ButtonText.MULTIPLY, 0, 3, ButtonType.OPERATOR),
            # 두 번째 행: 4, 5, 6, −
            ButtonConfig("4", 1, 0),
            ButtonConfig("5", 1, 1),
            ButtonConfig("6", 1, 2),
            ButtonConfig(ButtonText.SUBTRACT, 1, 3, ButtonType.OPERATOR),
            # 세 번째 행: 1, 2, 3, +
            ButtonConfig("1", 2, 0),
            ButtonConfig("2", 2, 1),
            ButtonConfig("3", 2, 2),
            ButtonConfig(ButtonText.ADD, 2, 3, ButtonType.OPERATOR),
            # 네 번째 행: +/-, 0, ., =
            ButtonConfig(ButtonText.TOGGLE_SIGN, 3, 0, ButtonType.SPECIAL),
            ButtonConfig("0", 3, 1),
            ButtonConfig(ButtonText.DECIMAL, 3, 2, ButtonType.SPECIAL),
            ButtonConfig(ButtonText.EQUALS, 3, 3, ButtonType.EQUALS),
            # 다섯 번째 행: C, ÷
            ButtonConfig(ButtonText.CLEAR, 4, 0, ButtonType.SPECIAL),
            ButtonConfig(ButtonText.DIVIDE, 4, 1, ButtonType.OPERATOR),
        ]
    
    def _create_button_widget(self, config: ButtonConfig) -> QPushButton:
        """버튼 위젯 생성"""
        button = QPushButton(config.text)
        button.setMinimumSize(UIConstants.BUTTON_SIZE, UIConstants.BUTTON_SIZE)
        button.setFont(QFont(UIConstants.FONT_FAMILY, UIConstants.BUTTON_FONT_SIZE))
        
        if config.button_type == ButtonType.EQUALS:
            button.setMinimumHeight(UIConstants.EQUALS_BUTTON_HEIGHT)
        
        return button
    
    def _apply_button_style(self, button: QPushButton, button_type: str):
        """버튼 스타일 적용"""
        style = ButtonStyles.get_style(button_type)
        button.setStyleSheet(style)
    
    def _add_button_to_layout(self, button: QPushButton, config: ButtonConfig, layout: QGridLayout):
        """버튼을 레이아웃에 추가"""
        layout.addWidget(button, config.row, config.col)
    
    def _connect_signals(self):
        """버튼 시그널 연결"""
        buttons = self.findChildren(QPushButton)
        
        for button in buttons:
            handler = self._get_button_handler(button.text())
            if handler:
                button.clicked.connect(handler)
    
    def _get_button_handler(self, text: str) -> Optional[Callable]:
        """버튼 텍스트에 따른 핸들러 반환"""
        # 연산자 매핑
        operator_map = {
            ButtonText.ADD: "+",
            ButtonText.SUBTRACT: "-",
            ButtonText.MULTIPLY: "×",
            ButtonText.DIVIDE: "÷"
        }
        
        # 핸들러 매핑
        if text.isdigit():
            return lambda checked, digit=text: self._on_digit_clicked(digit)
        elif text == ButtonText.EQUALS:
            return self._on_equals_clicked
        elif text == ButtonText.TOGGLE_SIGN:
            return self._on_toggle_sign_clicked
        elif text == ButtonText.CLEAR:
            return self._on_clear_clicked
        elif text == ButtonText.DECIMAL:
            return self._on_decimal_clicked
        elif text in operator_map:
            operator = operator_map[text]
            return lambda checked, op=operator: self._on_operator_clicked(op)
        
        return None
    
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
        pass
    
    def _update_display(self):
        """디스플레이 업데이트"""
        display_value = self.controller.get_display_value()
        self.display.setText(display_value)
