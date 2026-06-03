import os
import re
import subprocess
from pathlib import Path

# Directorios
SGSI_DIR = Path('sgsi')

def clean_markdown(content):
    # Reemplazar *** por una línea horizontal LaTeX
    content = re.sub(r'^\*\*\*$', '\n\\\\vspace{0.3cm}\\\\hrule\\\\vspace{0.3cm}\n', content, flags=re.MULTILINE)
    
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
    
    clean_cont = clean_markdown(content)
    # Remover el titulo original para que no se duplique en el PDF
    clean_cont = re.sub(r'^#\s+.+\n', '', clean_cont, count=1, flags=re.MULTILINE)
    
    yaml_subtitle = f'subtitle: "{subtitle}"' if subtitle else ""
    yaml_frontmatter = f"""---
title: "{raw_title}"
{yaml_subtitle}
author: "Universidad Nacional del Centro del Perú (UNCP)"
date: "SGSI ISO/IEC 27001:2022"
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

# 1. Generar PDFs individuales
print("🚀 Iniciando generación de documentos individuales...")
md_files = []
for root, dirs, files in os.walk(SGSI_DIR):
    for file in files:
        if file.endswith('.md'):
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

print("\n✨ ¡Proceso completado exitosamente!")
