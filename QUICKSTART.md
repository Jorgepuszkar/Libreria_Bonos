# Quick Start - bonos-lib

## Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/usuario/bonos-lib.git
cd bonos-lib

# Instalar en modo desarrollo
pip install -e .

# Instalar dependencias de desarrollo
pip install -r requirements.txt pytest
```

## Uso Básico

### 1. Cargar datos de bonos

```python
import pandas as pd
from bonos_lib import YieldCurveCalculator

# CSV con columnas: dias, precio
bonos = pd.read_csv('ejemplos/sample_bonds.csv')

# O crear manualmente:
bonos = pd.DataFrame({
    'dias': [30, 60, 90, 180, 360],
    'precio': [99.25, 98.50, 97.75, 96.00, 92.00]
})
```

### 2. Calcular yields

```python
calc = YieldCurveCalculator(nominal=100)
yields = calc.calculate_yields(bonos)
print(yields)
```

### 3. Hacer bootstrapping

```python
forwards = calc.bootstrap(yields)
print(forwards)
```

### 4. Interpolar tasas

```python
# Una tasa
tasa_45 = calc.interpolate(yields, 45)
print(f"Tasa a 45 días: {tasa_45*100:.4f}%")

# Múltiples tasas
tasas = calc.interpolate_multiple(yields, [30, 45, 60, 90])
print(tasas)
```

## Ejecutar Tests

```bash
pytest tests/ -v
```

## Ejecutar Demo

```bash
python examples/demo.py
```

## Estructura de Archivos

```
├── bonos_lib/              # Librería (instalable)
├── tests/                  # Tests (pytest)
├── examples/
│   ├── sample_bonds.csv   # Datos de ejemplo
│   └── demo.py            # Script demostrativo
├── docs/                   # Documentación
├── notebook/
│   └── tutorial.ipynb     # Tutorial para Colab
├── setup.py               # Config para pip
└── README.md              # Documentación principal
```

## Próximos Pasos

1. **Para usar localmente**: `pip install -e .`
2. **Para publicar en PyPI**: Ver [PUBLISHING.md](PUBLISHING.md)
3. **Para entender la teoría**: Ver [docs/THEORY.md](docs/THEORY.md)
4. **Para documentación API**: Ver [docs/API.md](docs/API.md)

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'bonos_lib'"

Asegúrate de estar en el directorio correcto:
```bash
cd /path/to/bonos-lib
pip install -e .
```

### Error: "No module named 'pandas'"

Instala las dependencias:
```bash
pip install pandas numpy
```

### Tests fallando

Verifica que pytest esté instalado:
```bash
pip install pytest
pytest tests/ -v
```

## Requisitos

- Python 3.8+
- pandas >= 1.0.0
- numpy >= 1.19.0

Para desarrollo:
- pytest >= 6.0
