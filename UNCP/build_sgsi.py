import os
import re
import subprocess
from pathlib import Path

# Directorios
SGSI_DIR = Path('sgsi')

def clean_markdown(content):
    # Remover numeración manual en duro de encabezados (ej. "## 1. Objetivo" -> "## Objetivo")
    # para permitir que pandoc numere limpia y automáticamente sin duplicación.
    lines = content.splitlines()
    cleaned_lines = []
    for line in lines:
        line = re.sub(r'^(#+)\s+\d+(?:\.\d+)*\.?\s+', r'\1 ', line)
        cleaned_lines.append(line)
    content = '\n'.join(cleaned_lines)

    # Reemplazar *** por una línea horizontal LaTeX
    content = re.sub(r'^\*\*\*$', '\n\\\\vspace{0.3cm}\\\\hrule\\\\vspace{0.3cm}\n', content, flags=re.MULTILINE)
    # Reemplazar --- por una línea horizontal LaTeX (para evitar colisiones de YAML)
    content = re.sub(r'^---$', '\n\\\\vspace{0.3cm}\\\\hrule\\\\vspace{0.3cm}\n', content, flags=re.MULTILINE)
    
    # Permitir que los guiones bajos en nombres de carpetas se rompan
    # Reemplaza _ por _\hspace{0pt}
    # Pero solo si no están dentro de código o enlaces (simplificado aquí)
    content = content.replace('_', '_\\hspace{0pt}')
    
    # Mejorar checkboxes para PDF
    content = content.replace('[ ]', '$\\square$')
    content = content.replace('[x]', '$\\boxtimes$')
    
    # Corregir caracteres unicode que rompen pdflatex
    content = content.replace('≥', '$\\ge$')
    content = content.replace('≤', '$\\le$')
    content = content.replace('—', '---')
    content = content.replace('≈', '~')
    content = content.replace('🔴', '[Rojo]')
    content = content.replace('🟢', '[Verde]')
    content = content.replace('🟡', '[Amarillo]')
    
    return content

def extract_title(content):
    match = re.search(r'^#\s+(.+)$', content, flags=re.MULTILINE)
    if match:
        t = match.group(1).strip()
        # Limpiar cualquier residuo de \hspace
        t = t.replace('\\hspace{0pt}', '')
        return t.replace('"', '\\"')
    return "Documento SGSI"

def compile_pdf(md_path, pdf_path, title, subtitle=None):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer titulo antes de limpiar con escapes LaTeX
    raw_title = extract_title(content)
    
    # Remover frontmatter original para evitar duplicaciones y visualización textual en PDF
    if content.startswith('\ufeff'):
        content = content[1:]
    lines = content.splitlines()
    if len(lines) > 0 and lines[0].strip() == '---':
        try:
            end_idx = lines.index('---', 1)
            content = '\n'.join(lines[end_idx+1:])
        except ValueError:
            pass
            
    clean_cont = clean_markdown(content)
    # Remover el titulo original para que no se duplique en el PDF
    clean_cont = re.sub(r'^#\s+.+\n', '', clean_cont, count=1, flags=re.MULTILINE)
    
    yaml_subtitle = f'subtitle: "{subtitle}"' if subtitle else ""
    yaml_frontmatter = f"""---
title: "{raw_title}"
{yaml_subtitle}
author: "Universidad Nacional del Centro del Perú (UNCP)"
date: "SGSI ISO/IEC 27001:2022"
numbersections: true
...

"""
    new_content = yaml_frontmatter + clean_cont
    
    tmp_path = md_path.with_suffix('.tmp.md')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    cmd = [
        'pandoc',
        str(tmp_path),
        '-o', str(pdf_path),
        '-H', 'sgsi/sgsi_header.tex',
        '--pdf-engine=pdflatex',
        '--columns=80',
        '--quiet'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] Al compilar {md_path.name}: {result.stderr}")
        
    if tmp_path.exists():
        os.remove(tmp_path)

def compile_native_pdf(md_path, pdf_path, headertitle, header_file='header.tex', extra_args=[]):
    resource_dirs = [
        str(Path('.').resolve()),
        str(Path('pgtd').resolve()),
        str(Path('analisis').resolve()),
        str(Path('sgsi').resolve())
    ]
    resource_path = ':'.join(resource_dirs)
    
    cmd = [
        'pandoc',
        str(md_path),
        '-o', str(pdf_path),
        '--pdf-engine=xelatex',
        '-H', header_file,
        '-V', 'mainfont=Trebuchet MS',
        '-V', f'headertitle={headertitle}',
        f'--resource-path={resource_path}',
        '--columns=80',
        '--quiet'
    ] + extra_args
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] Al compilar nativo {md_path.name}: {result.stderr}")
    else:
        print(f"  -> Generado nativo: {pdf_path.name}")

if __name__ == '__main__':
    # 1. Generar PDFs individuales del SGSI
    print("🚀 Iniciando generación de documentos individuales de SGSI...")
    md_files = []
    for root, dirs, files in os.walk(SGSI_DIR):
        for file in files:
            if file.endswith('.md') and not file.endswith('.tmp.md'):
                md_files.append(Path(root) / file)

    md_files.sort()

    for filepath in md_files:
        pdf_name = filepath.stem + '.pdf'
        pdf_path = filepath.parent / pdf_name
        print(f"  -> Procesando: {filepath.name}")
        compile_pdf(filepath, pdf_path, None)

    # 2. Generar Manual Consolidado
    print("\n📚 Generando Manual Consolidado (Libro)...")
    manual_md = Path('MANUAL-SGSI-UNCP-MAESTRO.md')
    consolidated_content = """---
title: "Manual del Sistema de Gestión de Seguridad de la Información (SGSI)"
subtitle: "ISO/IEC 27001:2022"
author: "Universidad Nacional del Centro del Perú (UNCP)"
date: "Huancayo, 2026"
toc: true
toc-depth: 3
numbersections: true
...

\\newpage

"""

    folders = sorted([d for d in SGSI_DIR.iterdir() if d.is_dir()])

    for folder in folders:
        folder_display = folder.name.replace('_', ' ').strip().title()
        folder_display = re.sub(r'^\d+\s+', '', folder_display)
        consolidated_content += f"\n\\newpage\n# {folder_display}\n\n"
        
        files_in_folder = sorted(list(folder.glob('*.md')))
        for f in files_in_folder:
            content = f.read_text(encoding='utf-8')
            # Remover de forma robusta el frontmatter YAML al inicio de los archivos individuales para evitar fallas de pandoc en el consolidado
            if content.startswith('\ufeff'):
                content = content[1:]
            lines = content.splitlines()
            if len(lines) > 0 and lines[0].strip() == '---':
                try:
                    end_idx = lines.index('---', 1)
                    content = '\n'.join(lines[end_idx+1:])
                except ValueError:
                    pass
            content = clean_markdown(content)
            content = re.sub(r'^#', '##', content, flags=re.MULTILINE)
            consolidated_content += content + "\n\n"

    manual_md.write_text(consolidated_content, encoding='utf-8')

    print("  -> Compilando Manual...")
    cmd_manual = [
        'pandoc',
        str(manual_md),
        '-o', 'MANUAL-SGSI-UNCP-FINAL.pdf',
        '-H', 'sgsi/sgsi_header.tex',
        '--pdf-engine=pdflatex',
        '--columns=80',
        '--quiet'
    ]
    result_manual = subprocess.run(cmd_manual, capture_output=True, text=True)
    if result_manual.returncode != 0:
        print(f"  [ERROR] Al compilar Manual: {result_manual.stderr}")
    else:
        print("  -> Generado: MANUAL-SGSI-UNCP-FINAL.pdf")

    # 3. Compilar Informe Final
    print("  -> Compilando Informe Final Ejecutivo...")
    compile_pdf(Path('INFORME-FINAL-SGSI-UNCP.md'), Path('INFORME-FINAL-SGSI-UNCP.pdf'), None)

    # 4. Compilar Documentos Estratégicos Adicionales (PGTD, Cronograma, Análisis, RFI)
    print("\n💼 Compilando documentos estratégicos adicionales...")
    
    print("  -> Procesando: Plan de Gobierno y Transformación Digital - UNCP 2026-2030.md")
    # Para el PGTD usamos su header específico pgtd/header.tex y no pasamos --toc, --lof ni --lot a pandoc
    # dado que ya están declarados de forma explícita en el cuerpo de su Markdown.
    compile_native_pdf(
        Path('pgtd/Plan de Gobierno y Transformación Digital - UNCP 2026-2030.md'),
        Path('pgtd/Plan de Gobierno y Transformación Digital - UNCP 2026-2030.pdf'),
        headertitle="PGTD 2026-2030 - UNCP",
        header_file='pgtd/header.tex',
        extra_args=[]
    )
    
    print("  -> Procesando: Cronograma-PGTD-UNCP-2026-2030.md")
    compile_native_pdf(
        Path('pgtd/Cronograma-PGTD-UNCP-2026-2030.md'),
        Path('pgtd/Cronograma-PGTD-UNCP-2026-2030.pdf'),
        headertitle="Cronograma PGTD 2026-2030 - UNCP",
        header_file='pgtd/header.tex',
        extra_args=['--toc']
    )
    
    print("  -> Procesando: Infraestructura-UNCP-Analisis.md")
    compile_native_pdf(
        Path('analisis/Infraestructura-UNCP-Analisis.md'),
        Path('analisis/Infraestructura-UNCP-Analisis.pdf'),
        headertitle="Análisis Infraestructura - UNCP",
        header_file='header.tex',
        extra_args=['--toc']
    )
    
    print("  -> Procesando: Requerimiento-Informacion-PGTD.md")
    compile_native_pdf(
        Path('Requerimiento-Informacion-PGTD.md'),
        Path('Requerimiento-Informacion-PGTD.pdf'),
        headertitle="RFI PGTD - UNCP",
        header_file='header.tex',
        extra_args=['--toc']
    )

    print("  -> Procesando: RESUMEN-EJECUTIVO-OTI.md")
    compile_native_pdf(
        Path('RESUMEN-EJECUTIVO-OTI.md'),
        Path('RESUMEN-EJECUTIVO-OTI.pdf'),
        headertitle="Resumen Técnico OTI - SGSI UNCP",
        header_file='header.tex',
        extra_args=[]
    )

    print("  -> Procesando: RESUMEN-EJECUTIVO-DIRECTIVO.md")
    compile_native_pdf(
        Path('RESUMEN-EJECUTIVO-DIRECTIVO.md'),
        Path('RESUMEN-EJECUTIVO-DIRECTIVO.pdf'),
        headertitle="Resumen Ejecutivo - SGSI UNCP",
        header_file='header.tex',
        extra_args=[]
    )

    print("\n✨ ¡Proceso completado exitosamente!")

