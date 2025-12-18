"""
입력 검증 모듈 테스트
리팩토링 검증을 위한 단위 테스트
"""

import pytest
from src.gui.validators import InputValidator


class TestInputValidator:
    """입력 검증 클래스 테스트"""
    
    @pytest.fixture
    def validator(self):
        """검증기 인스턴스 생성"""
        return InputValidator()
    
    def test_validate_number_positive_integers(self, validator):
        """양수 정수 검증 테스트"""
        assert validator.validate_number("123") == 123
        assert validator.validate_number("0") == 0
        assert validator.validate_number("999") == 999
    
    def test_validate_number_negative_integers(self, validator):
        """음수 정수 검증 테스트"""
        assert validator.validate_number("-123") == -123
        assert validator.validate_number("-1") == -1
    
    def test_validate_number_invalid_strings(self, validator):
        """유효하지 않은 문자열 검증 테스트"""
        assert validator.validate_number("abc") is None
        assert validator.validate_number("12.34") is None
        assert validator.validate_number("") is None
        assert validator.validate_number("12a") is None
    
    def test_validate_number_float_strings(self, validator):
        """소수점 문자열 검증 테스트 (정수만 지원)"""
        assert validator.validate_number("12.5") is None
        assert validator.validate_number("3.14") is None
    
    def test_is_valid_number_positive(self, validator):
        """유효한 숫자 확인 테스트 (양수)"""
        assert validator.is_valid_number("123") is True
        assert validator.is_valid_number("0") is True
        assert validator.is_valid_number("999") is True
    
    def test_is_valid_number_negative(self, validator):
        """유효한 숫자 확인 테스트 (음수)"""
        assert validator.is_valid_number("-123") is True
        assert validator.is_valid_number("-1") is True
    
    def test_is_valid_number_invalid(self, validator):
        """유효하지 않은 숫자 확인 테스트"""
        assert validator.is_valid_number("abc") is False
        assert validator.is_valid_number("12.34") is False
        assert validator.is_valid_number("") is False
        assert validator.is_valid_number("12a") is False
    
    def test_validate_operator_supported_operators(self, validator):
        """지원되는 연산자 검증 테스트"""
        assert validator.validate_operator("+") is True
        assert validator.validate_operator("-") is True
        assert validator.validate_operator("×") is True
        assert validator.validate_operator("÷") is True
        assert validator.validate_operator("/") is True
    
    def test_validate_operator_unsupported_operators(self, validator):
        """지원하지 않는 연산자 검증 테스트"""
        assert validator.validate_operator("%") is False
        assert validator.validate_operator("**") is False
        assert validator.validate_operator("") is False
        assert validator.validate_operator("mod") is False
    
    def test_validate_operator_case_sensitive(self, validator):
        """연산자 대소문자 구분 테스트"""
        # 대소문자 구분하지 않지만, 현재 구현은 정확한 기호만 지원
        assert validator.validate_operator("+") is True
        assert validator.validate_operator("Plus") is False
    
    def test_static_methods(self, validator):
        """정적 메서드 동작 테스트"""
        # 정적 메서드이므로 인스턴스 없이도 호출 가능
        assert InputValidator.validate_number("123") == 123
        assert InputValidator.is_valid_number("123") is True
        assert InputValidator.validate_operator("+") is True

