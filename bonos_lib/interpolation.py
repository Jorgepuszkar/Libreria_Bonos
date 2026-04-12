"""Interpolación de tasas en la yield curve."""

import numpy as np
import pandas as pd


class LinearInterpolator:
    """Realiza interpolación lineal en la yield curve."""

    def interpolate(self, yields_df: pd.DataFrame, days: float) -> float:
        """
        Interpola la tasa para un plazo específico.

        Parámetros:
        -----------
        yields_df : pd.DataFrame
            DataFrame con columnas 'dias' y 'yield'
        days : float
            Número de días

        Retorna:
        --------
        float
            Tasa interpolada
        """
        df = yields_df[['dias', 'yield']].copy()
        df = df.sort_values('dias').reset_index(drop=True)

        min_days = df['dias'].min()
        max_days = df['dias'].max()

        if days < min_days or days > max_days:
            raise ValueError(
                f"El plazo {days} está fuera del rango [{min_days}, {max_days}]"
            )

        if days in df['dias'].values:
            return df[df['dias'] == days]['yield'].values[0]

        idx = df[df['dias'] <= days]['dias'].idxmax()
        d1, y1 = df.loc[idx, 'dias'], df.loc[idx, 'yield']
        d2, y2 = df.loc[idx + 1, 'dias'], df.loc[idx + 1, 'yield']

        return y1 + (y2 - y1) * (days - d1) / (d2 - d1)

    def interpolate_multiple(self, yields_df: pd.DataFrame, days_list: list) -> dict:
        """Interpola tasas para múltiples plazos."""
        result = {}
        for days in days_list:
            try:
                result[days] = self.interpolate(yields_df, days)
            except ValueError as e:
                print(f"Advertencia para {days} días: {e}")
                result[days] = None
        return result

    def interpolate_range(
        self, yields_df: pd.DataFrame, min_days: float, max_days: float, step: float
    ) -> pd.DataFrame:
        """Crea una curva interpolada en un rango."""
        days_range = np.arange(min_days, max_days + step, step)
        rates = [self.interpolate(yields_df, d) for d in days_range]

        return pd.DataFrame({'dias': days_range, 'yield': rates})
