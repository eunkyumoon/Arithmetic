# PyQt GUI 리팩토링 가이드

## 개요

콘솔 기반 계산기를 PyQt6를 사용한 GUI 애플리케이션으로 리팩토링한 결과입니다.

## 리팩토링 결과 요약

### ✅ 완료된 작업

1. **인터페이스 정의** (`src/arithmetic/interfaces.py`)
   - `ICalculator`: 계산기 인터페이스
   - `IOperationStrategy`: 연산 전략 인터페이스

2. **Strategy Pattern 구현** (`src/arithmetic/operations.py`, `src/arithmetic/operation_factory.py`)
   - 각 연산을 독립적인 전략 클래스로 분리
   - Factory Pattern으로 연산자 생성

3. **컨트롤러 레이어** (`src/gui/controller.py`)
   - UI와 비즈니스 로직 분리
   - 의존성 주입 적용

4. **입력 검증 및 포맷팅** (`src/gui/validators.py`, `src/gui/formatters.py`)
   - 단일 책임 원칙 적용

5. **PyQt GUI 구현** (`src/gui/view.py`, `src/gui/main.py`)
   - 이미지와 동일한 레이아웃
   - 이벤트 기반 처리

### 📊 코드 품질 개선

#### Before (콘솔 버전)
- 순환 복잡도: 7 (`calculate()` 메서드)
- 결합도: 높음 (UI와 비즈니스 로직 결합)
- 코드 스멜: Long Method, Magic Strings, Feature Envy

#### After (GUI 버전)
- 순환 복잡도: 3 이하 (각 메서드)
- 결합도: 낮음 (인터페이스 기반 의존성)
- SOLID 원칙 준수:
  - ✅ SRP: 각 클래스가 단일 책임
  - ✅ OCP: Strategy Pattern으로 확장 용이
  - ✅ LSP: 인터페이스 기반 구현
  - ✅ ISP: 작은 인터페이스로 분리
  - ✅ DIP: 추상화에 의존

## 아키텍처 구조

```
┌─────────────────────────────────────────┐
│         GUI Layer (PyQt)                │
│  ┌───────────────────────────────────┐  │
│  │      CalculatorView               │  │
│  │  (UI 렌더링 및 이벤트 처리)        │  │
│  └──────────────┬────────────────────┘  │
└─────────────────┼───────────────────────┘
                  │ uses
┌─────────────────┼───────────────────────┐
│         Controller Layer                 │
│  ┌───────────────────────────────────┐  │
│  │   CalculatorController             │  │
│  │   InputValidator                   │  │
│  │   ResultFormatter                  │  │
│  └──────────────┬────────────────────┘  │
└─────────────────┼───────────────────────┘
                  │ uses
┌─────────────────┼───────────────────────┐
│      Business Logic Layer                │
│  ┌───────────────────────────────────┐  │
│  │   ArithmeticCalculator             │  │
│  │   OperationStrategy (Strategy)     │  │
│  │   OperationFactory (Factory)       │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## 디렉토리 구조

```
src/
├── arithmetic/                    # 비즈니스 로직 레이어
│   ├── __init__.py
│   ├── arithmetic_calculator.py  # 기존 (유지)
│   ├── interfaces.py             # 새로 추가
│   ├── operations.py              # 새로 추가 (Strategy Pattern)
│   └── operation_factory.py       # 새로 추가 (Factory Pattern)
│
├── gui/                          # GUI 레이어 (새로 추가)
│   ├── __init__.py
│   ├── controller.py             # 컨트롤러
│   ├── view.py                   # PyQt 메인 윈도우
│   ├── validators.py             # 입력 검증
│   ├── formatters.py             # 결과 포맷팅
│   └── main.py                   # 애플리케이션 진입점
│
└── console/                      # 콘솔 UI (기존 유지)
    ├── __init__.py
    └── console_calculator.py     # 기존 (리팩토링 가능)
```

## 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. GUI 애플리케이션 실행

```bash
python src/gui/main.py
```

또는

```bash
python -m src.gui.main
```

### 3. 콘솔 버전 실행 (기존)

```bash
python src/arithmetic/console_calculator.py
```

## 사용 방법

### GUI 계산기 사용법

1. **숫자 입력**: 0-9 버튼 클릭
2. **연산자 선택**: +, −, ×, ÷ 버튼 클릭
3. **두 번째 숫자 입력**: 0-9 버튼 클릭
4. **계산 실행**: = 버튼 클릭
5. **부호 변경**: +/- 버튼 클릭
6. **초기화**: C 버튼 클릭

### 예제

1. `5` → `+` → `3` → `=` → 결과: `8`
2. `10` → `−` → `4` → `=` → 결과: `6`
3. `7` → `×` → `2` → `=` → 결과: `14`
4. `8` → `÷` → `2` → `=` → 결과: `4`

## 테스트

### 기존 테스트 실행

```bash
pytest tests/ -v
```

### 테스트 커버리지 확인

```bash
pytest --cov=src/arithmetic --cov-report=html
```

## 주요 개선 사항

### 1. 코드 스멜 제거

- ✅ **Long Method**: `calculate()` 메서드를 작은 메서드로 분리
- ✅ **Magic Strings**: `OperationFactory`에 상수로 정의
- ✅ **Feature Envy**: 컨트롤러를 통해 간접 접근
- ✅ **Duplicate Code**: 공통 로직을 메서드로 추출

### 2. SOLID 원칙 적용

#### Single Responsibility Principle (SRP)
- `CalculatorController`: 계산 흐름 제어만 담당
- `InputValidator`: 입력 검증만 담당
- `ResultFormatter`: 결과 포맷팅만 담당
- `CalculatorView`: UI 렌더링만 담당

#### Open/Closed Principle (OCP)
- 새로운 연산자 추가 시 `IOperationStrategy`를 구현하는 클래스만 추가
- 기존 코드 수정 불필요

#### Liskov Substitution Principle (LSP)
- 모든 연산 전략이 `IOperationStrategy` 인터페이스를 구현
- 서로 교체 가능

#### Interface Segregation Principle (ISP)
- 작은 인터페이스로 분리 (`ICalculator`, `IOperationStrategy`)

#### Dependency Inversion Principle (DIP)
- 컨트롤러가 `ICalculator` 인터페이스에 의존
- 구체적인 구현이 아닌 추상화에 의존

### 3. 디자인 패턴 적용

- **Strategy Pattern**: 연산 로직을 전략으로 분리
- **Factory Pattern**: 연산자에 따른 전략 생성
- **MVC Pattern**: Model-View-Controller 구조

## 확장 가능성

### 새로운 연산자 추가

1. `src/arithmetic/operations.py`에 새로운 전략 클래스 추가:
```python
class ModuloOperation(IOperationStrategy):
    def execute(self, a: int, b: int) -> int:
        return a % b
    
    def get_symbol(self) -> str:
        return "%"
```

2. `src/arithmetic/operation_factory.py`에 매핑 추가:
```python
OPERATOR_MODULO = "%"
SUPPORTED_OPERATORS.add(OPERATOR_MODULO)
operator_map[OPERATOR_MODULO] = ModuloOperation
```

3. `src/gui/view.py`에 버튼 추가

### 다른 UI 구현

인터페이스를 구현하여 다른 UI로 교체 가능:
- 웹 UI (Flask/Django)
- 모바일 UI (Kivy)
- CLI UI (기존 콘솔 버전)

## 문제 해결

### PyQt6 설치 오류

```bash
pip install --upgrade pip
pip install PyQt6
```

### Import 오류

프로젝트 루트에서 실행하거나 PYTHONPATH 설정:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## 참고 자료

- [PyQt6 공식 문서](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [SOLID 원칙](https://en.wikipedia.org/wiki/SOLID)
- [Design Patterns](https://refactoring.guru/design-patterns)

---

**작성일**: 2025-01-XX  
**버전**: 1.0

