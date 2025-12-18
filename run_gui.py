#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GUI 계산기 실행 스크립트
프로젝트 루트에서 실행: python run_gui.py
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 현재 작업 디렉토리를 프로젝트 루트로 설정
os.chdir(project_root)

try:
    from src.gui.main import main
    
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"Import 오류: {e}")
    print(f"프로젝트 루트: {project_root}")
    print(f"Python 경로: {sys.path[:3]}")
    sys.exit(1)

