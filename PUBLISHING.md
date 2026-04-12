# Guía de Publicación a PyPI

## Pasos para Publicar bonos-lib en PyPI

### 1. Configurar tu cuenta en PyPI

1. Crear cuenta en [pypi.org](https://pypi.org) si no tienes una
2. Generar un token API en tu perfil de PyPI
3. Guardar el token en un lugar seguro (usarás `__token__` como usuario)

### 2. Crear un release en GitHub

La forma recomendada es usar las **GitHub Releases** que automáticamente publica a PyPI.

#### Opción A: Desde la CLI de GitHub

```bash
# Crear un tag
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# Crear release desde CLI
gh release create v0.1.0 --title "Version 0.1.0" --notes "Initial release"
```

#### Opción B: Desde la interfaz de GitHub

1. Ve a tu repositorio
2. Click en "Releases" → "Create a new release"
3. Tag version: `v0.1.0`
4. Release title: `Version 0.1.0`
5. Describe tu cambios
6. Click "Publish release"

### 3. Configurar el secreto de GitHub

Para que el workflow `publish.yml` funcione:

1. Ve a Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: (tu token de PyPI)

### 4. Verificar la publicación

Una vez que el workflow termine:

```bash
pip install bonos-lib --upgrade
```

### 5. Actualizar versión para próximas releases

Antes de hacer un nuevo release:

1. Actualizar `version` en `setup.py` y `pyproject.toml`
2. Crear commit: `git commit -am "Bump version to X.X.X"`
3. Crear tag y release como se describe arriba

## Publicación Manual (sin GitHub Actions)

Si prefieres hacerlo manualmente:

```bash
# Instalar herramientas
pip install build twine

# Construir distribuciones
python -m build

# Verificar
twine check dist/*

# Publicar (necesitas tu token de PyPI)
twine upload dist/* -u __token__ -p tu_token_aqui
```

## Verificación después de publicación

```bash
# Ver la librería en PyPI
pip search bonos-lib

# Instalar desde PyPI
pip install bonos-lib

# Verificar que funciona
python -c "from bonos_lib import YieldCurveCalculator; print('✓ bonos-lib instalado correctamente')"
```

## Estructura de versiones (SemVer)

- `MAJOR.MINOR.PATCH` (e.g., `0.1.0`)
- **MAJOR**: cambios incompatibles
- **MINOR**: nuevas features compatibles
- **PATCH**: bug fixes

Ejemplo de progresión:
- `0.1.0` → `0.2.0` (nueva interpolación spline)
- `0.2.0` → `0.2.1` (fix de bug)
- `1.0.0` → `2.0.0` (cambio de API)
