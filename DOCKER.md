# Docker Setup - bonos-lib

Usar Docker permite tener un entorno aislado y reproducible sin preocuparte por instalar Python o dependencias.

## Requisitos

- [Docker](https://www.docker.com/products/docker-desktop) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

## Uso Rápido

### 1. Ejecutar Jupyter Lab (Recomendado)

```bash
docker-compose up
```

Luego abre tu navegador en: **http://localhost:8888**

Puedes crear y ejecutar notebooks directamente, con bonos-lib ya instalada.

### 2. Ejecutar Tests

```bash
docker-compose --profile test up bonos-tests
```

O construir y ejecutar:
```bash
docker build -t bonos-lib .
docker run bonos-lib pytest tests/ -v
```

### 3. Abrirse una Shell Interactiva

```bash
docker-compose --profile shell run --rm bonos-shell
```

Dentro del contenedor:
```bash
# Ejecutar demo
python examples/demo.py

# Python interactivo
python
>>> from bonos_lib import YieldCurveCalculator
>>> # ... tu código
```

### 4. Ejecutar un Comando Específico

```bash
docker run --rm bonos-lib python examples/demo.py
```

## Opciones Avanzadas

### Build sin usar cache

```bash
docker build --no-cache -t bonos-lib .
```

### Ejecutar con volúmenes personalizados

```bash
docker run -it -v $(pwd):/app bonos-lib bash
```

### Especificar puerto diferente para Jupyter

```bash
docker run -p 9999:8888 bonos-lib
```

Luego abre: http://localhost:9999

## Estructura del Contenedor

```
/app
├── bonos_lib/          # Librería instalada
├── tests/              # Tests
├── examples/           # Scripts y datos
└── notebook/           # Notebooks
```

## Volúmenes en docker-compose.yml

- `./:/app` - Código del proyecto (sincronizado)
- `./notebooks:/workspace/notebooks` - Notebooks creados

## Usar en Producción

Para un entorno de producción, crea un Dockerfile optimizado:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bonos_lib/ ./bonos_lib/
COPY setup.py .
RUN pip install --no-cache-dir -e .

CMD ["python"]
```

Construir e ejecutar:
```bash
docker build -f Dockerfile.prod -t bonos-lib:prod .
docker run bonos-lib:prod python examples/demo.py
```

## Troubleshooting

### Error: "Cannot connect to Docker daemon"

Asegúrate de que Docker está corriendo:
```bash
docker --version
```

### Error: "Port 8888 already in use"

Cambia el puerto en docker-compose.yml:
```yaml
ports:
  - "9999:8888"  # Cambiar 8888 por otro puerto
```

### Los cambios en el código no se reflejan

Los volúmenes en docker-compose.yml mantienen sincronizado el código. Si no funciona:
```bash
docker-compose down
docker-compose up --build
```

## Limpiar

Detener contenedor:
```bash
docker-compose down
```

Eliminar imagen:
```bash
docker rmi bonos-lib
```

Eliminar todo (¡cuidado!):
```bash
docker-compose down -v
docker system prune -a
```
