# GUI 계산기 실행 가이드

## 문제 해결

### 문제: ModuleNotFoundError: No module named 'PyQt6'

이 오류는 가상 환경에 PyQt6가 설치되지 않아서 발생합니다.

## 해결 방법

### 방법 1: 자동 실행 스크립트 사용 (권장)

#### Windows PowerShell 사용 시:
```powershell
.\run_gui.ps1
```

#### Windows CMD 사용 시:
```cmd
run_gui.bat
```

이 스크립트들은 자동으로:
1. 가상 환경이 없으면 생성
2. 가상 환경 활성화
3. PyQt6 설치 확인 및 설치
4. GUI 실행

### 방법 2: 수동 실행

#### 1단계: 가상 환경 활성화

**PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**CMD:**
```cmd
.venv\Scripts\activate.bat
```

#### 2단계: PyQt6 설치 확인 및 설치

```bash
# 설치 확인
python -c "import PyQt6; print('PyQt6 설치됨')"

# 설치되지 않은 경우
pip install -r requirements.txt
# 또는
pip install PyQt6>=6.6.0
```

#### 3단계: GUI 실행

```bash
python src/gui/main.py
# 또는
python run_gui.py
```

## 가상 환경이 없는 경우

처음 실행하는 경우:

```bash
# 가상 환경 생성
python -m venv .venv

# 가상 환경 활성화 (PowerShell)
.\.venv\Scripts\Activate.ps1

# 의존성 설치
pip install --upgrade pip
pip install -r requirements.txt

# GUI 실행
python src/gui/main.py
```

## 확인 사항

### 1. 가상 환경 활성화 확인
프롬프트 앞에 `(.venv)`가 표시되어야 합니다:
```
(.venv) C:\DEV\cursor_pro\Arithmetic>
```

### 2. PyQt6 설치 확인
```bash
pip list | findstr PyQt6
```

다음과 같이 표시되어야 합니다:
```
PyQt6                     6.10.1
PyQt6-Qt6                 6.10.1
PyQt6-sip                 13.10.3
```

### 3. 모듈 import 테스트
```bash
python -c "from PyQt6.QtWidgets import QApplication; print('OK')"
```

## 문제 해결 체크리스트

- [ ] 가상 환경이 생성되어 있는가? (`Test-Path .venv`)
- [ ] 가상 환경이 활성화되어 있는가? (프롬프트에 `(.venv)` 표시)
- [ ] PyQt6가 설치되어 있는가? (`pip list | findstr PyQt6`)
- [ ] Python 경로가 올바른가? (`python -c "import sys; print(sys.executable)"`)

## 추가 도움말

문제가 계속되면:
1. 가상 환경을 삭제하고 재생성:
   ```bash
   Remove-Item -Recurse -Force .venv
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. 시스템 Python에 직접 설치 (권장하지 않음):
   ```bash
   pip install PyQt6>=6.6.0
   ```

---

**작성일**: 2025-01-XX  
**버전**: 1.0

