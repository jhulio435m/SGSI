
import re
import sys

def clean_content(content):
    # 1. Remove specific headers at the start
    content = re.sub(r'### UNIVERSIDAD NACIONAL DEL CENTRO DEL PERU\n?', '', content)
    content = re.sub(r'### CÓDIGO : PGD\n?', '', content)
    content = re.sub(r'### VERSIÓN : 1\.\n?', '', content)

    # 2. Remove artifacts
    content = content.replace('(^)', '')
    content = content.replace('(A/R)', '')
    content = re.sub(r'\(Se\s*mana\s*s?\)', 'Semanas', content)
    # Remove things like ^5 or ^ 
    content = re.sub(r'\^(\d+)', r'\1', content)
    content = content.replace('^', '')

    # 3. Fix split words (common OCR errors)
    split_patterns = [
        (r'cronogra\s+ma', 'cronograma'),
        (r'actividade\s+s', 'actividades'),
        (r'informació\s+n', 'información'),
        (r'estratégic\s+o', 'estratégico'),
        (r'estratégic\s+a', 'estratégica'),
        (r'instituciona\s+l', 'institucional'),
        (r'identificació\s+n', 'identificación'),
        (r'tecnolog\s+ías', 'tecnologías'),
        (r'públic\s+a', 'pública'),
        (r'gestió\s+n', 'gestión'),
        (r'digitalizació\s+n', 'digitalización'),
        (r'comunicació\s+n', 'comunicación'),
        (r'interoperabilida\s+d', 'interoperabilidad'),
        (r'entida\s+d', 'entidad'),
        (r'Respons\s+ables', 'Responsables'),
        (r'transformació\s+n', 'transformación'),
        (r'modernizació\s+n', 'modernización'),
        (r'ejecució\s+n', 'ejecución'),
        (r'implementació\s+n', 'implementación'),
        (r'asigna\s+ción', 'asignación'),
        (r'evaluació\s+n', 'evaluación'),
        (r'documen\s+to', 'documento'),
        (r'consul\s+ta', 'consulta'),
        (r'infraestruct\s+ura', 'infraestructura'),
        (r'tecnológic\s+os', 'tecnológicos'),
        (r'tecnológic\s+a', 'tecnológica'),
        (r'formulació\s+n', 'formulación'),
        (r'orgánic\s+as', 'orgánicas'),
        (r'regula\s+ción', 'regulación'),
        (r'Secretari\s+o', 'Secretario'),
        (r'Técnico', 'Técnico'), # Sometimes split but here it's fine
    ]
    for pattern, replacement in split_patterns:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    # 4. Handle code blocks
    def replace_code_block(match):
        text = match.group(1).strip()
        if not text:
            return ''
        # If it starts with quote marks, make it a blockquote
        if text.startswith('“') or text.startswith('"') or text.startswith('«'):
            return '\n\n> ' + text.replace('\n', ' ') + '\n\n'
        # Otherwise just return the text
        return '\n\n' + text + '\n\n'

    content = re.sub(r'```(.*?)```', replace_code_block, content, flags=re.DOTALL)

    # 5. Fix header levels
    def fix_headers(match):
        hashes = match.group(1)
        numbering = match.group(2)
        dots = numbering.count('.')
        new_level = dots + 2
        return '#' * new_level + ' ' + numbering

    content = re.sub(r'^(##+)\s+(\d+(?:\.\d+)+)\.?', fix_headers, content, flags=re.MULTILINE)

    # 6. Join broken lines and handle excessive blank lines
    lines = content.split('\n')
    cleaned_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip excessive blank lines
        if not line:
            if cleaned_lines and cleaned_lines[-1] != '':
                cleaned_lines.append('')
            i += 1
            continue
        
        # If it's a header or list item or blockquote or table marker, keep it
        if line.startswith('#') or line.startswith('- ') or line.startswith('>') or line.startswith('|'):
            cleaned_lines.append(line)
            i += 1
            continue
            
        # Continuation logic: join with next line(s)
        while i + 1 < len(lines):
            next_line = lines[i+1].strip()
            
            # If next line is empty, decide whether to jump over it and join anyway
            if not next_line:
                # Look ahead for a third line
                if i + 2 < len(lines):
                    after_next = lines[i+2].strip()
                    if after_next and not any(after_next.startswith(m) for m in ['#', '-', '*', '>', '|', '1.', '2.', '3.']):
                        # If current line doesn't end with terminal, jump over blank line and join
                        if not line.endswith(('.', ':', ';', '!', '?', '”', '"')):
                            line += ' ' + after_next
                            i += 2
                            continue
                break
            
            # Don't join if next line is a special marker
            if any(next_line.startswith(m) for m in ['#', '-', '*', '>', '|', '1.', '2.', '3.', '4.', '5.']):
                break
            
            # If current line doesn't end with a sentence terminator, join it
            if not line.endswith(('.', ':', ';', '!', '?', '”', '"')):
                line += ' ' + next_line
                i += 1
            # Or if it's a very short line
            elif len(line) < 50 and not line.endswith('.'):
                line += ' ' + next_line
                i += 1
            else:
                break
        
        cleaned_lines.append(line)
        i += 1

    content = '\n'.join(cleaned_lines)
    
    # 7. Specific Table Fixes
    # Reconstruct the cronograma table if possible
    content = content.replace("Nombre de la Etapa Nombre de la Actividad Plazos por cada Actividad Semanas Duración de la Actividad (días) Fecha de Inicio Fecha de Fin Responsables de la Actividad Hitos / Entregable",
                              "\n| Etapa | Actividad | Plazos (Semanas) | Duración (días) | Inicio | Fin | Responsables | Hitos / Entregable |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n")

    # Fix tables that look like "Text ### X" or "Text (^) X"
    content = re.sub(r'\s+### X', ' | X', content)
    content = re.sub(r'\s+\(\s*\)\s+X', ' | X', content)
    
    # Final cleanup of excessive spaces and newlines
    content = re.sub(r' +', ' ', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_content(content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
