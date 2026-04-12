#!/bin/bash
# Run bonos-lib with Docker Compose

COMMAND=${1:-jupyter}

case $COMMAND in
    jupyter)
        echo "🚀 Starting Jupyter Lab on http://localhost:8888"
        docker-compose up
        ;;
    tests)
        echo "🧪 Running tests..."
        docker-compose --profile test up bonos-tests
        ;;
    shell)
        echo "🐚 Opening interactive shell..."
        docker-compose --profile shell run --rm bonos-shell
        ;;
    demo)
        echo "📊 Running demo..."
        docker-compose run --rm bonos-lib python examples/demo.py
        ;;
    *)
        echo "Usage: ./scripts/docker-run.sh [command]"
        echo ""
        echo "Commands:"
        echo "  jupyter  - Start Jupyter Lab (default)"
        echo "  tests    - Run test suite"
        echo "  shell    - Open interactive shell"
        echo "  demo     - Run demo script"
        exit 1
        ;;
esac
