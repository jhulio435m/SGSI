#!/bin/bash

# Script de compilación automática para documentos UNCP
# Requiere: pandoc, xelatex y la fuente Trebuchet MS

set -e # Detener el script si hay algún error

echo "🚀 Iniciando compilación de documentos UNCP..."

# 1. Compilar PGTD y Cronograma
echo "📄 Generando Plan de Gobierno y Transformación Digital (PGTD)..."
cd UNCP/pgtd
pandoc "Plan de Gobierno y Transformación Digital - UNCP 2026-2030.md" \
    -o "Plan de Gobierno y Transformación Digital - UNCP 2026-2030.pdf" \
    --pdf-engine=xelatex \
    -H header.tex \
    -V papersize:a4 \
    -V geometry:margin=1in \
    --toc --lof --lot \
    -V mainfont="Trebuchet MS"

echo "📅 Generando Cronograma..."
pandoc "Cronograma-PGTD-UNCP-2026-2030.md" \
    -o "Cronograma-PGTD-UNCP-2026-2030.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V mainfont="Trebuchet MS"

# 2. Compilar documentos de Seguridad (SGSI)
echo "🛡️ Generando documentos de Seguridad (SGSI)..."
cd ../sgsi
pandoc "SGSI-UNCP-Marco-Conceptual.md" \
    -o "SGSI-UNCP-Marco-Conceptual.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V mainfont="Trebuchet MS"

pandoc "Alcance-SGSI-UNCP.md" \
    -o "Alcance-SGSI-UNCP.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V mainfont="Trebuchet MS"

# 3. Compilar Análisis de Infraestructura
echo "🏗️ Generando Análisis de Infraestructura..."
cd ../analisis
pandoc "Infraestructura-UNCP-Analisis.md" \
    -o "Infraestructura-UNCP-Analisis.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V mainfont="Trebuchet MS"

# 4. Compilar Requerimiento de Información (RFI)
echo "📋 Generando Requerimiento de Información..."
cd ..
pandoc "Requerimiento-Informacion-PGTD.md" \
    -o "Requerimiento-Informacion-PGTD.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V mainfont="Trebuchet MS"

echo "✅ ¡Compilación exitosa! Los archivos PDF están listos en sus respectivas carpetas."
