"""Tests para YieldCurveCalculator."""

import pytest
from bonos_lib import YieldCurveCalculator
import pandas as pd


@pytest.fixture
def sample_bonds():
    """Datos de ejemplo."""
    return pd.DataFrame({
        'dias': [30, 60, 90, 180, 360],
        'precio': [99.25, 98.50, 97.75, 96.00, 92.00]
    })


def test_calculate_yields(sample_bonds):
    """Prueba el cálculo de yields."""
    calc = YieldCurveCalculator(nominal=100)
    yields = calc.calculate_yields(sample_bonds)

    assert 'yield' in yields.columns
    assert len(yields) == len(sample_bonds)
    assert all(yields['yield'] > 0)


def test_calculate_yields_validation():
    """Prueba validación."""
    calc = YieldCurveCalculator()

    with pytest.raises(TypeError):
        calc.calculate_yields([1, 2, 3])

    df_bad = pd.DataFrame({'dias': [30, 60]})
    with pytest.raises(ValueError):
        calc.calculate_yields(df_bad)


def test_interpolate(sample_bonds):
    """Prueba interpolación."""
    calc = YieldCurveCalculator(nominal=100)
    yields = calc.calculate_yields(sample_bonds)

    tasa_45 = calc.interpolate(yields, 45)
    assert 0 < tasa_45 < 1


def test_interpolate_out_of_range(sample_bonds):
    """Prueba interpolación fuera de rango."""
    calc = YieldCurveCalculator(nominal=100)
    yields = calc.calculate_yields(sample_bonds)

    with pytest.raises(ValueError):
        calc.interpolate(yields, 20)

    with pytest.raises(ValueError):
        calc.interpolate(yields, 400)


def test_bootstrap(sample_bonds):
    """Prueba bootstrapping."""
    calc = YieldCurveCalculator(nominal=100)
    yields = calc.calculate_yields(sample_bonds)
    forwards = calc.bootstrap(yields)

    assert 'forward_rate' in forwards.columns
    assert 'spot_rate' in forwards.columns


def test_analyze(sample_bonds):
    """Prueba análisis."""
    calc = YieldCurveCalculator(nominal=100)
    analysis = calc.analyze(sample_bonds)

    assert 'yields_df' in analysis
    assert 'forwards_df' in analysis
    assert 'avg_yield' in analysis
