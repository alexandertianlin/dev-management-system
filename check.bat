@echo off
echo === Dev Governance: Compliance Check ===
python scripts/enforce_check.py
if errorlevel 1 (
    echo.
    echo [FAILED] Compliance check failed.
    echo Re-run with: python scripts/enforce_check.py --pass-n 3 --heal
    pause
    exit /b 1
)
echo [PASSED] All checks passed.
pause
