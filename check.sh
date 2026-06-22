#!/bin/bash
echo "=== Dev Governance: Compliance Check ==="
python scripts/enforce_check.py
if [ $? -ne 0 ]; then
    echo ""
    echo "[FAILED] Compliance check failed."
    echo "Re-run with: python scripts/enforce_check.py --pass-n 3 --heal"
    exit 1
fi
echo "[PASSED] All checks passed."
