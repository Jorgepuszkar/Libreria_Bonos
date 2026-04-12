# bonos-lib - Bond Yield Curve Analysis

Una librería Python para calcular, interpolar y hacer bootstrapping de curvas de rendimiento (yield curves) a partir de bonos cupón cero.

## Características

- ✅ **Cálculo de Yield Curve**: Extrae las tasas de rendimiento desde bonos cupón cero
- ✅ **Bootstrapping**: Construye tasas forward a partir de la curva de rendimiento
- ✅ **Interpolación Lineal**: Interpola tasas para plazos no disponibles
- ✅ **Análisis Completo**: Métricas y análisis integral de datos

## Instalación

```bash
pip install bonos-lib
```

## Uso Rápido

```python
import pandas as pd
from bonos_lib import YieldCurveCalculator

# Cargar datos de bonos cupón cero
df = pd.read_csv('bonos.csv')

# Crear y calcular
calc = YieldCurveCalculator(nominal=100)
yields = calc.calculate_yields(df)
forwards = calc.bootstrap(yields)
tasa_30_dias = calc.interpolate(yields, days=30)
```

## Formato CSV

```
dias,precio
30,99.25
60,98.50
90,97.75
180,96.00
360,92.00
```

## Tutorial

Abre el tutorial en Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/usuario/bonos-lib/blob/main/notebook/tutorial.ipynb)

## Documentación

- [API Reference](docs/API.md)
- [Teoría de Yield Curves](docs/THEORY.md)

## Licencia

MIT License
