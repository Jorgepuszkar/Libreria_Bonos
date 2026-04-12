#!/bin/bash
# Build Docker image for bonos-lib

echo "🐳 Building bonos-lib Docker image..."
docker build -t bonos-lib:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo ""
    echo "Usage examples:"
    echo "  Run Jupyter Lab:     docker run -p 8888:8888 bonos-lib"
    echo "  Run tests:           docker run bonos-lib pytest tests/ -v"
    echo "  Interactive shell:   docker run -it bonos-lib bash"
    echo "  Run demo:            docker run bonos-lib python examples/demo.py"
else
    echo "❌ Docker build failed!"
    exit 1
fi
