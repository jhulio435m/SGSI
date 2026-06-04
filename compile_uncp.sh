#!/bin/bash

# Script de compilación automática para documentos UNCP
# Requiere: pandoc, xelatex y la fuente Trebuchet MS

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"
echo "🚀 Iniciando compilación de documentos UNCP..."

PANDOC_OPTS=(
    --pdf-engine=xelatex
    -H "UNCP/header.tex"
    -V mainfont="Trebuchet MS"
    -V geometry:margin=1in
)

# 1. PGTD
echo "📄 Generando Plan de Gobierno y Transformación Digital (PGTD)..."
pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/pgtd/Plan de Gobierno y Transformación Digital - UNCP 2026-2030.md" \
    -o "UNCP/pgtd/Plan de Gobierno y Transformación Digital - UNCP 2026-2030.pdf" \
    -V headertitle="PGTD 2026-2030 - UNCP" \
    --toc --lof --lot

echo "📅 Generando Cronograma..."
pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/pgtd/Cronograma-PGTD-UNCP-2026-2030.md" \
    -o "UNCP/pgtd/Cronograma-PGTD-UNCP-2026-2030.pdf" \
    -V headertitle="Cronograma PGTD 2026-2030 - UNCP" \
    --toc

# 2. SGSI
echo "🛡️ Generando documentos de Seguridad (SGSI)..."
pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/sgsi/01_CONTEXTO_DE_LA_ORGANIZACION/D-SGSI-06-Marco-Conceptual.md" \
    -o "UNCP/sgsi/01_CONTEXTO_DE_LA_ORGANIZACION/D-SGSI-06-Marco-Conceptual.pdf" \
    -V headertitle="SGSI ISO/IEC 27001 - UNCP" \
    --toc

pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/sgsi/01_CONTEXTO_DE_LA_ORGANIZACION/D-SGSI-02-Alcance-SGSI.md" \
    -o "UNCP/sgsi/01_CONTEXTO_DE_LA_ORGANIZACION/D-SGSI-02-Alcance-SGSI.pdf" \
    -V headertitle="SGSI ISO/IEC 27001 - UNCP" \
    --toc

# 3. Análisis de Infraestructura
echo "🏗️ Generando Análisis de Infraestructura..."
pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/analisis/Infraestructura-UNCP-Analisis.md" \
    -o "UNCP/analisis/Infraestructura-UNCP-Analisis.pdf" \
    -V headertitle="Análisis Infraestructura - UNCP" \
    --toc

# 4. Requerimiento de Información
echo "📋 Generando Requerimiento de Información..."
pandoc "${PANDOC_OPTS[@]}" \
    "UNCP/Requerimiento-Informacion-PGTD.md" \
    -o "UNCP/Requerimiento-Informacion-PGTD.pdf" \
    -V headertitle="RFI PGTD - UNCP" \
    --toc

echo "✅ ¡Compilación exitosa! Los archivos PDF están listos en sus respectivas carpetas."
