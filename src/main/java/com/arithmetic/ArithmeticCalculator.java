package com.arithmetic;

/**
 * 사칙연산 계산기 클래스
 * TDD GREEN 단계: 최소 단위 구현
 * 
 * @author 홍길동
 * @version 1.0
 * @since 2020-09-01
 */
public class ArithmeticCalculator {
    
    /**
     * 덧셈 연산
     * Step 1-2: 실제 구현으로 변경 (TC-001, TC-002 통과)
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return 덧셈 결과
     */
    public int add(int a, int b) {
        return a + b;
    }
    
    /**
     * 뺄셈 연산
     * Step 1-3: TC-004 통과
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return 뺄셈 결과
     */
    public int subtract(int a, int b) {
        return a - b;
    }
    
    /**
     * 정수 나눗셈 연산
     * Step 1-4: TC-007 통과 (소수점 버림)
     * Step 1-6: TC-009, TC-010 통과 (예외 처리 추가)
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return 나눗셈 결과 (정수)
     * @throws ArithmeticException b가 0인 경우
     */
    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("0으로 나눌 수 없습니다.");
        }
        return a / b;
    }
}

