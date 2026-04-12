# API Reference - bonos-lib

## YieldCurveCalculator

### Constructor

```python
YieldCurveCalculator(nominal=100, days_year=360)
```

### Métodos

#### calculate_yields(df)
Calcula yields de bonos.

```python
yields = calc.calculate_yields(bonos_df)
```

**Parámetros:**
- `df`: DataFrame con columnas 'dias' y 'precio'

**Retorna:** DataFrame con columna 'yield'

#### bootstrap(yields_df)
Calcula tasas forward.

```python
forwards = calc.bootstrap(yields)
```

#### interpolate(yields_df, days)
Interpola tasa para un plazo.

```python
tasa = calc.interpolate(yields, 45)
```

**Retorna:** float

#### interpolate_multiple(yields_df, days_list)
Interpola múltiples tasas.

#### analyze(df)
Análisis completo de datos.

## BootstrapCalculator

### bootstrap(yields_df)
Realiza bootstrapping.

### get_forward_rate(yields_df, t0, t1)
Obtiene tasa forward entre dos períodos.

## LinearInterpolator

### interpolate(yields_df, days)
Interpola tasa.

### interpolate_multiple(yields_df, days_list)
Interpola múltiples tasas.

### interpolate_range(yields_df, min_days, max_days, step)
Crea curva interpolada en un rango.
