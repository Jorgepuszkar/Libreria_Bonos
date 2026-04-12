#!/usr/bin/env python3
"""Demo script showing bonos-lib functionality."""

import sys
import pandas as pd
from bonos_lib import YieldCurveCalculator

def main():
    print("\n" + "="*60)
    print("bonos-lib Demo - Yield Curve Analysis")
    print("="*60 + "\n")

    # Create sample data
    print("1️⃣  Creating sample bond data...")
    bonos = pd.DataFrame({
        'dias': [30, 60, 90, 180, 360],
        'precio': [99.25, 98.50, 97.75, 96.00, 92.00]
    })
    print(bonos)
    print()

    # Initialize calculator
    calc = YieldCurveCalculator(nominal=100)

    # Calculate yields
    print("2️⃣  Calculating yield curve...")
    yields = calc.calculate_yields(bonos)
    print(yields[['dias', 'precio', 'yield']])
    print()

    # Bootstrapping
    print("3️⃣  Bootstrapping forward rates...")
    forwards = calc.bootstrap(yields)
    print(forwards)
    print()

    # Interpolation
    print("4️⃣  Interpolating rates for intermediate periods...")
    plazos = [45, 120, 270]
    for plazo in plazos:
        tasa = calc.interpolate(yields, plazo)
        print(f"   {plazo:3d} days: {tasa*100:.4f}%")
    print()

    # Complete analysis
    print("5️⃣  Complete analysis...")
    analysis = calc.analyze(bonos)
    print(f"   Min yield: {analysis['min_yield']*100:.4f}%")
    print(f"   Max yield: {analysis['max_yield']*100:.4f}%")
    print(f"   Avg yield: {analysis['avg_yield']*100:.4f}%")
    print(f"   Maturity range: {analysis['min_days']:.0f} - {analysis['max_days']:.0f} days")
    print()

    print("✅ Demo completed successfully!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
