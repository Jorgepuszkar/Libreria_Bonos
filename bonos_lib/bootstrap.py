"""Bootstrapping de tasas forward."""

import numpy as np
import pandas as pd


class BootstrapCalculator:
    """Calcula tasas forward usando bootstrapping."""

    def __init__(self, days_year: int = 360):
        self.days_year = days_year

    def bootstrap(self, yields_df: pd.DataFrame) -> pd.DataFrame:
        """
        Realiza bootstrapping para calcular tasas forward.

        Parámetros:
        -----------
        yields_df : pd.DataFrame
            DataFrame con columnas 'dias' y 'yield'

        Retorna:
        --------
        pd.DataFrame
            DataFrame con columnas 'dias', 'spot_rate', 'forward_rate'
        """
        if 'dias' not in yields_df.columns or 'yield' not in yields_df.columns:
            raise ValueError("yields_df debe contener columnas 'dias' y 'yield'")

        df = yields_df[['dias', 'yield']].copy()
        df = df.sort_values('dias').reset_index(drop=True)
        df.rename(columns={'yield': 'spot_rate'}, inplace=True)

        df['forward_rate'] = np.nan

        # El primer período: forward = spot
        df.loc[0, 'forward_rate'] = df.loc[0, 'spot_rate']

        # Calcular forward rates
        for i in range(1, len(df)):
            t0 = df.loc[i - 1, 'dias']
            t1 = df.loc[i, 'dias']
            z_t0 = df.loc[i - 1, 'spot_rate']
            z_t1 = df.loc[i, 'spot_rate']

            t0_years = t0 / self.days_year
            t1_years = t1 / self.days_year
            delta_t = (t1 - t0) / self.days_year

            if delta_t > 0:
                forward_rate = (
                    ((1 + z_t1) ** t1_years) / ((1 + z_t0) ** t0_years)
                ) ** (1 / delta_t) - 1
            else:
                forward_rate = z_t1

            df.loc[i, 'forward_rate'] = forward_rate

        return df

    def get_forward_rate(self, yields_df: pd.DataFrame, t0: float, t1: float) -> float:
        """Obtiene la tasa forward entre dos períodos."""
        if t0 >= t1:
            raise ValueError("t1 debe ser mayor que t0")

        df = yields_df[['dias', 'yield']].copy()
        df = df.sort_values('dias').reset_index(drop=True)

        z_t0 = self._interpolate_yield(df, t0)
        z_t1 = self._interpolate_yield(df, t1)

        t0_years = t0 / self.days_year
        t1_years = t1 / self.days_year
        delta_t = (t1 - t0) / self.days_year

        forward_rate = (
            ((1 + z_t1) ** t1_years) / ((1 + z_t0) ** t0_years)
        ) ** (1 / delta_t) - 1

        return forward_rate

    def _interpolate_yield(self, df: pd.DataFrame, days: float) -> float:
        """Interpola linealmente la tasa."""
        if days <= df['dias'].min():
            return df.loc[df['dias'].idxmin(), 'yield']
        if days >= df['dias'].max():
            return df.loc[df['dias'].idxmax(), 'yield']

        idx = df[df['dias'] <= days]['dias'].idxmax()
        d1, y1 = df.loc[idx, 'dias'], df.loc[idx, 'yield']
        d2, y2 = df.loc[idx + 1, 'dias'], df.loc[idx + 1, 'yield']

        return y1 + (y2 - y1) * (days - d1) / (d2 - d1)
