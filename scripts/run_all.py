#!/usr/bin/env python3
"""Regenerate every figure used in the manuscript.

Usage:
    python scripts/run_all.py [--outdir figures]

Writes exp1..exp6 PNGs to the output directory and prints the key numbers from
the quantitative experiments (5 and 6).
"""
import argparse
import os
import sys

# allow running from a checkout without installation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mcbalance.experiments import (  # noqa: E402
    exp1_regimes, exp2_jtc, exp3_pivot, exp4_corridor, exp5_indices, exp6_policy,
)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outdir", default="figures", help="directory for PNG output")
    args = ap.parse_args()

    print("Generating figures in:", os.path.abspath(args.outdir))
    for fn in (exp1_regimes, exp2_jtc, exp3_pivot, exp4_corridor, exp5_indices):
        print("  wrote", fn(args.outdir))

    path, stats = exp6_policy(args.outdir)
    print("  wrote", path)
    print("\nExperiment 6 numbers:")
    print(f"  corridor dwell  - sequential {stats['dwell_seq']:.2f} | balanced {stats['dwell_bal']:.2f}")
    print(f"  recovery time   - sequential {stats['rec_seq']:.1f} | balanced {stats['rec_bal']:.1f}")


if __name__ == "__main__":
    main()
