#!/usr/bin/env python3
"""
Benchmark: Measure enforce_check.py execution performance.
Measures: scan time, violation detection rate, auto-heal speed.
"""

import time
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

def measure_enforce():
    """Measure basic enforce_check.py execution time."""
    from enforce_check import run_checks, print_header
    
    print("=== Benchmark: enforce_check.py ===")
    
    # Warm-up
    run_checks()
    
    # Measure 5 runs
    times = []
    for i in range(5):
        start = time.time()
        v = run_checks()
        elapsed = time.time() - start
        times.append(elapsed)
        print(f"  Run {i+1}: {elapsed*1000:.1f}ms ({len(v)} violations)")
    
    avg = sum(times) / len(times)
    print(f"\n  Average: {avg*1000:.1f}ms")
    print(f"  Min: {min(times)*1000:.1f}ms")
    print(f"  Max: {max(times)*1000:.1f}ms")
    
    # Measure auto-heal
    try:
        from auto_heal import auto_heal
        start = time.time()
        fixed, failed, msgs = auto_heal(v, dry_run=True)
        elapsed = time.time() - start
        print(f"\n  Auto-heal (dry-run): {elapsed*1000:.1f}ms ({fixed} fixable)")
    except ImportError:
        print("\n  auto_heal.py not available")

if __name__ == "__main__":
    measure_enforce()
