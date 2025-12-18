"""
GUI 상수 정의
Magic Numbers/Strings 제거를 위한 상수 모듈
"""


class UIConstants:
    """UI 관련 상수"""
    # 창 크기
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 400
    
    # 버튼 크기
    BUTTON_SIZE = 60
    EQUALS_BUTTON_HEIGHT = 130
    
    # 간격
    BUTTON_SPACING = 5
    
    # 폰트
    FONT_FAMILY = "Arial"
    DISPLAY_FONT_SIZE = 20
    BUTTON_FONT_SIZE = 16


class DisplayConstants:
    """디스플레이 관련 상수"""
    DEFAULT_VALUE = "0"
    ERROR_MESSAGE = "Error"


class ButtonText:
    """버튼 텍스트 상수"""
    EQUALS = "="
    TOGGLE_SIGN = "+/-"
    CLEAR = "C"
    DECIMAL = "."
    
    # 연산자
    ADD = "+"
    SUBTRACT = "−"
    MULTIPLY = "×"
    DIVIDE = "÷"
    
    # 숫자
    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # 연산자 목록
    OPERATORS = [ADD, SUBTRACT, MULTIPLY, DIVIDE]


class ButtonType:
    """버튼 타입 상수"""
    NUMBER = "number"
    OPERATOR = "operator"
    EQUALS = "equals"
    SPECIAL = "special"

