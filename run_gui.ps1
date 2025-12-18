# GUI 계산기 실행 PowerShell 스크립트
# 가상 환경을 자동으로 활성화하고 GUI를 실행합니다.

Write-Host "GUI 계산기 실행 중..." -ForegroundColor Green

# 프로젝트 루트로 이동
Set-Location $PSScriptRoot

# 가상 환경이 있는지 확인
if (Test-Path .venv\Scripts\Activate.ps1) {
    Write-Host "가상 환경 활성화 중..." -ForegroundColor Yellow
    & .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "가상 환경이 없습니다. 생성 중..." -ForegroundColor Yellow
    python -m venv .venv
    & .\.venv\Scripts\Activate.ps1
    Write-Host "PyQt6 설치 중..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
}

# PyQt6 설치 확인
$pyqt6Installed = python -c "import PyQt6; print('OK')" 2>$null
if (-not $pyqt6Installed) {
    Write-Host "PyQt6가 설치되지 않았습니다. 설치 중..." -ForegroundColor Yellow
    python -m pip install PyQt6>=6.6.0
}

# GUI 실행 (run_gui.py 사용 - 경로 문제 해결)
Write-Host "GUI 실행 중..." -ForegroundColor Green
python run_gui.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "오류가 발생했습니다." -ForegroundColor Red
    Read-Host "계속하려면 Enter를 누르세요"
}

