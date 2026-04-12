"""Calcula yield curves de bonos cupón cero."""

import numpy as np
import pandas as pd
from .bootstrap import BootstrapCalculator
from .interpolation import LinearInterpolator


class YieldCurveCalculator:
    """
    Calcula y analiza curvas de rendimiento de bonos cupón cero.

    Parámetros:
    -----------
    nominal : float
        Valor nominal de los bonos (default: 100)
    days_year : int
        Número de días en el año (default: 360)
    """

    def __init__(self, nominal: float = 100, days_year: int = 360):
        self.nominal = nominal
        self.days_year = days_year
        self.bootstrap_calc = BootstrapCalculator(days_year=days_year)
        self.interpolator = LinearInterpolator()

    def calculate_yields(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula las tasas de rendimiento de los bonos.

        Parámetros:
        -----------
        df : pd.DataFrame
            DataFrame con columnas 'dias' y 'precio'

        Retorna:
        --------
        pd.DataFrame
            DataFrame con columnas 'dias', 'precio', 'yield'
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df debe ser un DataFrame de pandas")

        if 'dias' not in df.columns or 'precio' not in df.columns:
            raise ValueError("df debe contener columnas 'dias' y 'precio'")

        df = df.copy()
        df = df.sort_values('dias').reset_index(drop=True)

        df['yield'] = (self.nominal / df['precio']) ** (self.days_year / df['dias']) - 1

        return df

    def bootstrap(self, yields_df: pd.DataFrame) -> pd.DataFrame:
        """Realiza bootstrapping para calcular tasas forward."""
        return self.bootstrap_calc.bootstrap(yields_df)

    def interpolate(self, yields_df: pd.DataFrame, days: float) -> float:
        """Interpola la tasa para un plazo específico."""
        return self.interpolator.interpolate(yields_df, days)

    def interpolate_multiple(self, yields_df: pd.DataFrame, days_list: list) -> dict:
        """Interpola tasas para múltiples plazos."""
        result = {}
        for days in days_list:
            result[days] = self.interpolate(yields_df, days)
        return result

    def analyze(self, df: pd.DataFrame) -> dict:
        """Realiza análisis completo de los datos."""
        yields_df = self.calculate_yields(df)
        forwards = self.bootstrap(yields_df)

        stats = {
            'yields_df': yields_df,
            'forwards_df': forwards,
            'avg_yield': yields_df['yield'].mean(),
            'min_yield': yields_df['yield'].min(),
            'max_yield': yields_df['yield'].max(),
            'min_days': yields_df['dias'].min(),
            'max_days': yields_df['dias'].max(),
        }

        return stats
