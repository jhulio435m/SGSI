#!/bin/bash

# Script de compilación automática para documentos UNCP (Delegado a Python)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/UNCP"

echo "🚀 Ejecutando script de compilación unificado en Python..."
python3 build_sgsi.py
