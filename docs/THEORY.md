# Teoría de Yield Curves

## Conceptos Básicos

### Bonos Cupón Cero
- Sin pagos periódicos (cupones)
- Se venden con descuento
- Pagan valor nominal al vencimiento

### Tasa de Rendimiento (Yield)

**Fórmula:**
```
Precio = Valor Nominal / (1 + y)^(t/360)
```

Despejando y:
```
y = (Valor Nominal / Precio)^(360/t) - 1
```

### Tasa Spot vs Forward

**Tasa Spot (z_t):**
- Rendimiento actual para un plazo específico
- Se obtiene del precio del bono

**Tasa Forward (f_{t0,t1}):**
- Tasa implícita para período futuro
- Se calcula mediante bootstrapping

**Relación:**
```
(1 + z_t1)^t1 = (1 + z_t0)^t0 × (1 + f_{t0,t1})^(t1-t0)
```

## Bootstrapping

Técnica para calcular tasas forward a partir de tasas spot.

**Fórmula:**
```
f_{t0,t1} = [(1 + z_t1)^t1 / (1 + z_t0)^t0]^(1/(t1-t0)) - 1
```

## Interpolación Lineal

Supone que la curva es lineal entre dos puntos.

**Fórmula:**
```
y = y1 + (y2 - y1) × (x - x1) / (x2 - x1)
```

## Aplicaciones

1. **Valuación de bonos**
2. **Gestión de riesgo**
3. **Análisis de spreads**
4. **Arbitraje**
