#!/usr/bin/env python
"""
GUI 계산기 실행 스크립트
프로젝트 루트에서 실행: python run_gui.py
"""

import sys
import os

# 프로젝트 루트를 경로에 추가
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.gui.main import main

if __name__ == "__main__":
    main()

