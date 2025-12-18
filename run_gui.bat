@echo off
REM GUI 계산기 실행 배치 파일 (Windows)
REM 가상 환경을 자동으로 활성화하고 GUI를 실행합니다.

echo GUI 계산기 실행 중...

REM 프로젝트 루트로 이동
cd /d "%~dp0"

REM 가상 환경이 있는지 확인
if exist .venv\Scripts\activate.bat (
    echo 가상 환경 활성화 중...
    call .venv\Scripts\activate.bat
) else (
    echo 가상 환경이 없습니다. 생성 중...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo PyQt6 설치 중...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
)

REM GUI 실행 (run_gui.py 사용 - 경로 문제 해결)
python run_gui.py

if errorlevel 1 (
    echo.
    echo 오류가 발생했습니다.
    pause
)

