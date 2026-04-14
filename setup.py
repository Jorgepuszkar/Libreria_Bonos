from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bonos-lib",
    version="0.1.1",
    author="Tu Nombre",
    author_email="jpuszkar@itam.mx",
    description="Librería para yield curves de bonos cupón cero",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jorgepuszkar/Libreria_Bonos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "pytest-cov>=2.10.0"],
    },
)
