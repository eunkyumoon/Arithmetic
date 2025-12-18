# GUI 계산기 빠른 시작 가이드

## 🚀 가장 빠른 실행 방법

### Windows PowerShell 사용 시:
```powershell
.\run_gui.ps1
```

### Windows CMD 사용 시:
```cmd
run_gui.bat
```

### Python 직접 실행:
```bash
# 가상 환경 활성화 후
python run_gui.py
```

## ✅ 문제 해결

### ModuleNotFoundError: No module named 'src'

이 오류는 경로 문제입니다. 해결 방법:

1. **프로젝트 루트에서 실행**:
   ```bash
   cd C:\DEV\cursor_pro\Arithmetic
   python run_gui.py
   ```

2. **직접 실행 시**:
   ```bash
   python src\gui\main.py
   ```
   (이제 `main.py`가 자동으로 경로를 설정합니다)

## 📋 실행 전 체크리스트

- [ ] 가상 환경이 활성화되어 있는가? (`(.venv)` 표시 확인)
- [ ] PyQt6가 설치되어 있는가?
  ```bash
  pip list | findstr PyQt6
  ```
- [ ] 프로젝트 루트에서 실행하는가?
  ```bash
  # 현재 디렉토리 확인
  pwd  # 또는 PowerShell: Get-Location
  # Arithmetic 폴더에 있어야 함
  ```

## 🔧 수동 설치 (필요시)

```bash
# 1. 가상 환경 생성
python -m venv .venv

# 2. 가상 환경 활성화
# PowerShell:
.\.venv\Scripts\Activate.ps1
# CMD:
.venv\Scripts\activate.bat

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 실행
python run_gui.py
```

## 💡 팁

- **가장 안전한 실행 방법**: `run_gui.py` 사용
- **자동 스크립트 사용**: `run_gui.ps1` 또는 `run_gui.bat` 사용
- **직접 실행**: `src/gui/main.py`도 이제 경로를 자동으로 설정합니다

---

**작성일**: 2025-01-XX  
**버전**: 1.0

