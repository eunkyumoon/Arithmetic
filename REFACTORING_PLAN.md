# PyQt GUI 리팩토링 계획서

## 목차
1. [현재 코드 분석](#1-현재-코드-분석)
2. [코드 스멜 분석](#2-코드-스멜-분석)
3. [정적 분석](#3-정적-분석)
4. [SOLID 원칙 적용](#4-solid-원칙-적용)
5. [리팩토링 단계](#5-리팩토링-단계)
6. [구현 계획](#6-구현-계획)

---

## 1. 현재 코드 분석

### 1.1 아키텍처 구조
```
현재 구조:
┌─────────────────────────┐
│  console_calculator.py  │  ← UI 레이어 (콘솔)
├─────────────────────────┤
│ arithmetic_calculator.py │  ← 비즈니스 로직 레이어
└─────────────────────────┘
```

### 1.2 현재 코드의 강점
- ✅ 비즈니스 로직(`ArithmeticCalculator`)과 UI 로직(`console_calculator`)이 분리되어 있음
- ✅ 예외 처리가 명확함
- ✅ 타입 힌트가 일부 사용됨
- ✅ 단일 책임 원칙(SRP)이 부분적으로 준수됨

### 1.3 현재 코드의 약점
- ❌ UI와 비즈니스 로직이 완전히 분리되지 않음 (의존성 주입 없음)
- ❌ 콘솔 UI에 하드코딩된 로직 존재
- ❌ GUI로 전환 시 재사용 불가능한 구조

---

## 2. 코드 스멜 분석

### 2.1 발견된 코드 스멜

#### 🔴 Long Method (긴 메서드)
**위치**: `console_calculator.py::calculate()`
- **문제**: 하나의 메서드가 너무 많은 책임을 가짐
  - 연산자 매핑
  - 계산 수행
  - 결과 포맷팅
  - 출력 처리
- **영향**: 유지보수 어려움, 테스트 어려움

#### 🟡 Magic Numbers/Strings (매직 넘버/문자열)
**위치**: `console_calculator.py`
- **문제**: 하드코딩된 연산자 문자열 `['+', '-', '*', '/', '//', '%']`
- **영향**: 연산자 추가/변경 시 여러 곳 수정 필요

#### 🟡 Feature Envy (기능 질투)
**위치**: `console_calculator.py::calculate()`
- **문제**: `ArithmeticCalculator`의 메서드를 직접 호출하는 방식
- **영향**: UI 레이어가 비즈니스 로직에 과도하게 의존

#### 🟡 Duplicate Code (중복 코드)
**위치**: `console_calculator.py::calculate()`
- **문제**: 결과 출력 로직이 중복됨 (예외 처리와 정상 처리)
- **영향**: 코드 중복으로 인한 유지보수 비용 증가

#### 🟡 Primitive Obsession (원시 타입 집착)
**위치**: `console_calculator.py`
- **문제**: 연산자를 문자열로 표현
- **영향**: 타입 안정성 부족, 컴파일 타임 오류 감지 불가

---

## 3. 정적 분석

### 3.1 순환 복잡도 (Cyclomatic Complexity)

#### `console_calculator.py::calculate()`
- **현재 복잡도**: 7
- **권장 복잡도**: ≤ 5
- **문제점**: 
  - 다중 if-elif 분기
  - 예외 처리 분기
  - 결과 타입 분기

#### `console_calculator.py::get_operator_input()`
- **현재 복잡도**: 2
- **권장 복잡도**: ≤ 5
- **상태**: ✅ 양호

### 3.2 결합도 (Coupling)
- **현재 결합도**: 높음
  - `console_calculator`가 `ArithmeticCalculator`에 직접 의존
  - 연산자 매핑 로직이 UI 레이어에 존재

### 3.3 응집도 (Cohesion)
- **현재 응집도**: 중간
  - UI 관련 기능들이 한 파일에 모여있지만, 계산 로직도 포함됨

---

## 4. SOLID 원칙 적용

### 4.1 Single Responsibility Principle (SRP) - 단일 책임 원칙

#### 현재 문제점
- `console_calculator.py`가 다음 책임들을 모두 가짐:
  1. 사용자 입력 처리
  2. 입력 검증
  3. 연산자 매핑
  4. 계산 수행
  5. 결과 포맷팅
  6. 출력 처리

#### 개선 방안
```python
# 분리된 책임들:
1. CalculatorController: UI 이벤트 처리 및 흐름 제어
2. InputValidator: 입력 검증
3. OperationMapper: 연산자 매핑
4. ResultFormatter: 결과 포맷팅
5. CalculatorView: UI 렌더링 (PyQt)
```

### 4.2 Open/Closed Principle (OCP) - 개방/폐쇄 원칙

#### 현재 문제점
- 새로운 연산자 추가 시 `calculate()` 메서드 수정 필요
- UI 변경 시 비즈니스 로직 수정 필요

#### 개선 방안
```python
# Strategy Pattern 적용
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int):
        pass

class AddOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

# Factory Pattern으로 연산자 생성
class OperationFactory:
    @staticmethod
    def create(operator: str) -> OperationStrategy:
        ...
```

### 4.3 Liskov Substitution Principle (LSP) - 리스코프 치환 원칙

#### 현재 상태
- ✅ `ArithmeticCalculator`는 잘 설계되어 LSP 준수

#### 개선 방안
- UI 인터페이스 정의로 다양한 UI 구현체 교체 가능하도록 설계

### 4.4 Interface Segregation Principle (ISP) - 인터페이스 분리 원칙

#### 개선 방안
```python
# 큰 인터페이스를 작은 인터페이스로 분리
class IInputHandler(ABC):
    @abstractmethod
    def get_input(self) -> str:
        pass

class IOutputHandler(ABC):
    @abstractmethod
    def display_result(self, result: Any):
        pass

class ICalculatorView(ABC):
    @abstractmethod
    def render(self):
        pass
```

### 4.5 Dependency Inversion Principle (DIP) - 의존성 역전 원칙

#### 현재 문제점
- UI 레이어가 구체적인 `ArithmeticCalculator`에 직접 의존

#### 개선 방안
```python
# 추상화에 의존
class ICalculator(ABC):
    @abstractmethod
    def add(self, a: int, b: int) -> int:
        pass
    # ...

# 의존성 주입
class CalculatorController:
    def __init__(self, calculator: ICalculator, view: ICalculatorView):
        self.calculator = calculator
        self.view = view
```

---

## 5. 리팩토링 단계

### 단계 1: 아키텍처 설계 및 인터페이스 정의
**목표**: SOLID 원칙을 준수하는 아키텍처 설계

**작업 내용**:
1. 인터페이스 정의 (`ICalculator`, `ICalculatorView`, `IOperationStrategy`)
2. 디렉토리 구조 설계
3. 의존성 관계 다이어그램 작성

**예상 결과물**:
- `src/arithmetic/interfaces.py` (인터페이스 정의)
- `REFACTORING_ARCHITECTURE.md` (아키텍처 문서)

---

### 단계 2: 비즈니스 로직 레이어 개선
**목표**: Strategy Pattern 적용 및 연산자 매핑 로직 분리

**작업 내용**:
1. `OperationStrategy` 인터페이스 및 구현체 생성
2. `OperationFactory` 생성
3. `ArithmeticCalculator` 리팩토링 (필요시)

**예상 결과물**:
- `src/arithmetic/operations.py` (연산 전략)
- `src/arithmetic/operation_factory.py` (팩토리)

---

### 단계 3: 컨트롤러 레이어 생성
**목표**: UI와 비즈니스 로직 분리

**작업 내용**:
1. `CalculatorController` 생성
2. 입력 검증 로직 분리 (`InputValidator`)
3. 결과 포맷팅 로직 분리 (`ResultFormatter`)

**예상 결과물**:
- `src/gui/controller.py`
- `src/gui/validators.py`
- `src/gui/formatters.py`

---

### 단계 4: PyQt View 레이어 구현
**목표**: 이미지에 맞는 계산기 UI 구현

**작업 내용**:
1. PyQt6 설치 및 설정
2. 계산기 UI 디자인 (키패드 레이아웃)
3. 이벤트 핸들러 연결
4. 컨트롤러와 통합

**예상 결과물**:
- `src/gui/view.py` (PyQt 메인 윈도우)
- `src/gui/widgets.py` (커스텀 위젯)
- `src/gui/main.py` (애플리케이션 진입점)

---

### 단계 5: 테스트 작성 및 리팩토링 검증
**목표**: 리팩토링 후 기능 검증

**작업 내용**:
1. 단위 테스트 작성
2. 통합 테스트 작성
3. GUI 테스트 (선택사항)
4. 기존 테스트 통과 확인

**예상 결과물**:
- `tests/test_controller.py`
- `tests/test_operations.py`
- `tests/test_validators.py`

---

### 단계 6: 문서화 및 정리
**목표**: 리팩토링 결과 문서화

**작업 내용**:
1. 리팩토링 리포트 작성
2. 사용자 가이드 작성
3. 개발자 가이드 작성

**예상 결과물**:
- `REFACTORING_REPORT.md`
- `GUI_USER_GUIDE.md`

---

## 6. 구현 계획

### 6.1 새로운 디렉토리 구조

```
src/
├── arithmetic/                    # 비즈니스 로직 레이어
│   ├── __init__.py
│   ├── arithmetic_calculator.py  # 기존 (유지)
│   ├── interfaces.py             # 새로 추가
│   ├── operations.py             # 새로 추가
│   └── operation_factory.py      # 새로 추가
│
├── gui/                          # GUI 레이어 (새로 추가)
│   ├── __init__.py
│   ├── controller.py            # 컨트롤러
│   ├── view.py                  # PyQt 메인 윈도우
│   ├── widgets.py               # 커스텀 위젯
│   ├── validators.py            # 입력 검증
│   ├── formatters.py            # 결과 포맷팅
│   └── main.py                  # 애플리케이션 진입점
│
└── console/                      # 콘솔 UI (기존 유지)
    ├── __init__.py
    └── console_calculator.py     # 기존 (리팩토링)
```

### 6.2 의존성 추가

**requirements.txt**에 추가:
```
PyQt6>=6.6.0
PyQt6-Qt6>=6.6.0
```

### 6.3 클래스 다이어그램

```
┌─────────────────────┐
│  ICalculator        │ (인터페이스)
└─────────────────────┘
         ▲
         │ implements
         │
┌─────────────────────┐
│ ArithmeticCalculator│
└─────────────────────┘

┌─────────────────────┐
│ IOperationStrategy  │ (인터페이스)
└─────────────────────┘
         ▲
         │ implements
    ┌────┴────┬──────────┬──────────┐
    │         │          │          │
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ AddOp   │ │ SubOp   │ │ MulOp   │ │ DivOp   │
└─────────┘ └─────────┘ └─────────┘ └─────────┘

┌─────────────────────┐
│ OperationFactory    │
└─────────────────────┘

┌─────────────────────┐
│ CalculatorController │
│ - calculator         │───┐
│ - view              │───┤
│ - validator         │───┤
│ - formatter         │───┤
└─────────────────────┘   │
                          │ uses
┌─────────────────────┐   │
│ CalculatorView      │◄──┘
│ (PyQt QMainWindow)  │
└─────────────────────┘
```

### 6.4 구현 우선순위

1. **Phase 1**: 인터페이스 및 전략 패턴 구현
2. **Phase 2**: 컨트롤러 및 검증 로직 구현
3. **Phase 3**: PyQt UI 기본 구조 구현
4. **Phase 4**: UI 이벤트 처리 및 통합
5. **Phase 5**: 테스트 및 버그 수정

---

## 7. 예상 개선 효과

### 7.1 코드 품질
- ✅ 순환 복잡도 감소 (7 → 3 이하)
- ✅ 결합도 감소 (높음 → 낮음)
- ✅ 응집도 증가 (중간 → 높음)

### 7.2 유지보수성
- ✅ 새로운 연산자 추가 시 확장 용이
- ✅ UI 변경 시 비즈니스 로직 영향 없음
- ✅ 테스트 작성 용이

### 7.3 재사용성
- ✅ 비즈니스 로직 재사용 가능
- ✅ 다양한 UI 구현체 교체 가능 (콘솔, GUI, 웹 등)

---

## 8. 리스크 및 대응 방안

### 8.1 리스크
1. **PyQt 학습 곡선**: 개발자가 PyQt에 익숙하지 않을 수 있음
   - **대응**: 단계별 구현 및 문서화

2. **기존 테스트 실패**: 리팩토링 중 기존 테스트가 깨질 수 있음
   - **대응**: 리팩토링 전후 테스트 실행 및 비교

3. **성능 이슈**: GUI 추가로 인한 성능 저하 가능성
   - **대응**: 프로파일링 및 최적화

### 8.2 완료 기준
- ✅ 모든 기존 테스트 통과
- ✅ 새로운 단위 테스트 작성 및 통과
- ✅ GUI가 이미지와 동일하게 동작
- ✅ 코드 커버리지 90% 이상 유지
- ✅ 순환 복잡도 5 이하
- ✅ SOLID 원칙 준수 확인

---

**작성일**: 2025-01-XX  
**작성자**: AI Assistant  
**버전**: 1.0

