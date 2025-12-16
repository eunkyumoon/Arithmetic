package com.arithmetic;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * 사칙연산 정확도 테스트 클래스
 * TDD RED 단계: 실패하는 테스트 작성
 * 
 * @author 홍길동
 * @version 1.0
 * @since 2020-09-01
 */
@DisplayName("사칙연산 정확도 테스트")
class ArithmeticCalculatorTest {

    private ArithmeticCalculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new ArithmeticCalculator();
    }

    @Test
    @DisplayName("덧셈 테스트: 1 + 10 = 11")
    void testAddition1() {
        int result = calculator.add(1, 10);
        assertEquals(11, result, "1 + 10은 11이어야 합니다.");
    }

    @Test
    @DisplayName("덧셈 테스트: 0 + 1 = 1")
    void testAddition2() {
        int result = calculator.add(0, 1);
        assertEquals(1, result, "0 + 1은 1이어야 합니다.");
    }

    @Test
    @DisplayName("덧셈 테스트: -1 + (-10) = -11")
    void testAddition3() {
        int result = calculator.add(-1, -10);
        assertEquals(-11, result, "-1 + (-10)은 -11이어야 합니다.");
    }

    @Test
    @DisplayName("뺄셈 테스트: 5 - 2 = 3")
    void testSubtraction() {
        int result = calculator.subtract(5, 2);
        assertEquals(3, result, "5 - 2는 3이어야 합니다.");
    }

    @Test
    @DisplayName("곱셈 테스트: -5 * -3 = 15")
    void testMultiplication1() {
        int result = calculator.multiply(-5, -3);
        assertEquals(15, result, "-5 * -3은 15이어야 합니다.");
    }

    @Test
    @DisplayName("곱셈 테스트: 0 * 10 = 0")
    void testMultiplication2() {
        int result = calculator.multiply(0, 10);
        assertEquals(0, result, "0 * 10은 0이어야 합니다.");
    }

    @Test
    @DisplayName("정수 나눗셈 테스트: 5 / 2 = 2")
    void testIntegerDivision() {
        int result = calculator.divide(5, 2);
        assertEquals(2, result, "5 / 2는 2이어야 합니다 (정수 나눗셈).");
    }

    @Test
    @DisplayName("소수점 나눗셈 테스트: 5 ÷ 2 = 2.5")
    void testQuotient() {
        double result = calculator.quotient(5, 2);
        assertEquals(2.5, result, 0.0001, "5 ÷ 2는 2.5이어야 합니다.");
    }

    @Test
    @DisplayName("나눗셈 테스트: -10 / 2 = -5")
    void testDivision() {
        int result = calculator.divide(-10, 2);
        assertEquals(-5, result, "-10 / 2는 -5이어야 합니다.");
    }

    @Test
    @DisplayName("예외 처리 테스트: 0 / 0는 ArithmeticException 발생")
    void testDivisionByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(0, 0);
        }, "0 / 0는 ArithmeticException을 발생시켜야 합니다.");
    }
}

