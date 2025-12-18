"""
버튼 스타일 정의
중복 코드 제거를 위한 스타일 모듈
"""

from src.gui.constants import UIConstants, ButtonType


class ButtonStyles:
    """버튼 스타일 클래스"""
    
    @staticmethod
    def get_equals_style() -> str:
        """등호 버튼 스타일"""
        return f"""
            QPushButton {{
                background-color: #0078d4;
                color: white;
                border: 1px solid #005a9e;
                border-radius: 5px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #106ebe;
            }}
            QPushButton:pressed {{
                background-color: #005a9e;
            }}
        """
    
    @staticmethod
    def get_operator_style() -> str:
        """연산자 버튼 스타일"""
        return f"""
            QPushButton {{
                background-color: #e0e0e0;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #d0d0d0;
            }}
            QPushButton:pressed {{
                background-color: #c0c0c0;
            }}
        """
    
    @staticmethod
    def get_special_style() -> str:
        """특수 버튼 스타일"""
        return f"""
            QPushButton {{
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #e0e0e0;
            }}
            QPushButton:pressed {{
                background-color: #d0d0d0;
            }}
        """
    
    @staticmethod
    def get_number_style() -> str:
        """숫자 버튼 스타일"""
        return f"""
            QPushButton {{
                background-color: white;
                color: black;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #f5f5f5;
            }}
            QPushButton:pressed {{
                background-color: #e0e0e0;
            }}
        """
    
    @staticmethod
    def get_style(button_type: str) -> str:
        """버튼 타입에 따른 스타일 반환
        
        Args:
            button_type: 버튼 타입 (ButtonType 상수 사용)
            
        Returns:
            CSS 스타일 문자열
        """
        style_map = {
            ButtonType.EQUALS: ButtonStyles.get_equals_style,
            ButtonType.OPERATOR: ButtonStyles.get_operator_style,
            ButtonType.SPECIAL: ButtonStyles.get_special_style,
            ButtonType.NUMBER: ButtonStyles.get_number_style,
        }
        
        style_func = style_map.get(button_type, ButtonStyles.get_number_style)
        return style_func()

