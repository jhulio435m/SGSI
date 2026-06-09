# SGSI-UNCP - Contexto del Proyecto

## Objetivo

Implementación de un Sistema de Gestión de Seguridad de la Información (SGSI) basado en ISO/IEC 27001 para la Universidad Nacional del Centro del Perú (UNCP), alineado al Plan de Gobierno y Transformación Digital (PGTD) 2026-2030 y la normativa peruana vigente.

## Estructura de Archivos

```
SGSI/
├── UNCP/
│   ├── pgtd/
│   │   ├── Plan de Gobierno y Transformación Digital - UNCP 2026-2030.md + .pdf
│   │   └── imagenes/
│   ├── sgsi/
│   │   ├── SGSI-UNCP-Marco-Conceptual.md + .pdf
│   │   ├── Alcance-SGSI-UNCP.md + .pdf
│   │   └── Plantilla-Inventario-Activos.md
│   ├── analisis/
│   │   └── Infraestructura-UNCP-Analisis.md + .pdf
│   └── Requerimiento-Informacion-PGTD.md + .pdf
├── Referencias/
│   ├── Externos/
│   │   ├── APCI - Plan de Gobierno Digital 2025-2027.md + .pdf
│   │   ├── BCRP - Plan de Gobierno Digital 2025-2027.md + .pdf
│   │   ├── Electro Puno - Plan de Gobierno Digital.md
│   │   ├── MINAM - Plan de Gobierno y Transformación Digital 2025-2027.md + .pdf
│   │   ├── Ministerio Público - Plan de Gobierno y Transformación Digital 2025-2027.md
│   │   ├── RENIEC - Plan de Gobierno y Transformación Digital 2025-2027.md + .pdf
│   │   └── SUNAT - Plan de Gobierno Digital 2025-2027.md
│   ├── Normativa/
│   │   ├── Anexo I - Lineamientos formulación PGTD.md + .pdf
│   │   ├── PNTD - Política Nacional de Transformación Digital al 2030.md + .pdf
│   │   ├── PNTD - Política Nacional de Transformación Digital al 2030 - Completo.pdf
│   │   └── R.S. N° 005-2018-PCM-SEGDI - Lineamientos PGTD.md + .pdf
│   └── PEDN/
│       ├── PEDN al 2050 - Documento completo.md
│       ├── PEDN al 2050 - Tomo I.pdf
│       └── PEDN al 2050 - Tomo II - Indicadores y Fichas Técnicas.md + .pdf
└── AGENTS.md
```

## Decisiones Tomadas

- Archivos separados y limpios (no fusión en uno solo)
- Documento PGTD-UNCP actualizado al periodo **2026-2030**
- Año actual establecido como **2026**
- Terminología actualizada de **SEGDI** a **SGTD** (Secretaría de Gobierno y Transformación Digital)
- Alineamiento con la **Política General de Gobierno 2025-2026** (D.S. N° 141-2025-PCM), citando la obligatoriedad del uso intensivo de tecnologías digitales y datos (Quinta Disposición Complementaria Final)
- Proveedor de correo estandarizado a **Microsoft 365**
- Presupuesto PGTD-01 (SGSI) estandarizado en **S/ 850,000**
- Información "No verificada" descartada o convertida en tareas pendientes proactivas
- Adopción de estándares de **Sostenibilidad y Eco-eficiencia Digital (Green IT)** inspirados en el MINAM para la modernización del Data Center
- Integración del sistema de investigación con redes nacionales de datos ambientales (**SINIA/REDIAM**) para fortalecer el impacto científico regional
- Documentos UNCP convertidos a formato **PDF** mediante Pandoc y XeLaTeX
- Repositorio oficial de resoluciones identificado:
  - Rectorales: `https://uncp.edu.pe/la-universidad/resoluciones-rectorales/` (iframe público `https://resoluciones.uncp.edu.pe/documentos/R-RE`)
  - Directorales: `https://uncp.edu.pe/la-universidad/resoluciones-directorales/` (iframe público `https://resoluciones.uncp.edu.pe/documentos/R-DR`)
- Comité de Gobierno Digital ya formalizado mediante **R. N.° 1862-R-2023**; no tratarlo como inexistente.
- **R. N.° 2143-R-2023** incorporada: integra al Comité de Gobierno Digital a la Mg. Rocío Rosanna Damián Alvarado, Jefa de la OTI, como Oficial de Seguridad de la Información.
- **R. N.° 2140-R-2023** incorporada: designa a la Mg. Rocío Rosanna Damián Alvarado como Funcionaria Responsable del Software Público.
- **R. N.° 3255-R-2024** incorporada: aprueba el Plan de Continuidad Operativa de la UNCP.
- **R. N.° 3524-R-2025** y **R. N.° 3526-R-2025** incorporadas como mapa de procesos Nivel 0 y Nivel 1; el Mermaid fue convertido a imagen PNG con Chromium.
- **PEI 2024-2030** incorporado: `Plan+Estratégico+Institucional+UNCP+2024-2030.md` contiene los OEI/AEI vigentes para el alineamiento PGTD/SGSI.

## Sugerencias Normativas (Perú)

1. **Oficial de Seguridad y Confianza Digital:** La **R. N.° 2143-R-2023** confirma la integración del Oficial de Seguridad de la Información al CGD; falta evidenciar suplencia, dedicación operativa, recursos y actas de seguimiento.
2. **Interoperabilidad (PIDE):** Se sugiere priorizar la integración con la PIDE para automatizar la verificación de identidad (RENIEC) y el registro de grados (SUNEDU).
3. **Política de Privacidad:** El sitio web institucional debe incluir una Política de Privacidad visible que detalle el tratamiento de datos personales (Ley N° 29733).

## Pendientes / Próximos Pasos

- [ ] Ejecutar auditoría inicial de activos (AS-IS) 2026
- [ ] Definir políticas de seguridad formales basadas en ISO 27001:2022
- [ ] Implementar proyecto PGTD-01 (SGSI)
- [ ] Validar directorio vigente del CGTD UNCP y evidencias de sesiones posteriores a la R. N.° 1862-R-2023
- [ ] Ratificar vigencia operativa, suplencia y carga de trabajo del Oficial de Seguridad de la Información integrado por R. N.° 2143-R-2023


## Bloqueado / Requiere Acceso Interno

Los siguientes compromisos CGR no pudieron verificarse sin acceso a sistemas internos:
- **Compromiso 8** - Datos Abiertos en PNDA (verificar si UNCP publica en datosabiertos.gob.pe)
- **Compromiso 13** - Responsable de Software Público (D.S. N° 051-2018-PCM)
- **Compromiso 14** - Plan de Transición a IPv6
- **Compromiso 17** - Encuesta Nacional de Activos Digitales (requiere coordinación con OTI)
- **Compromiso 20** - Oficial de Gobierno de Datos

Sin acceso a:
- PDFs del Mapa de Procesos (Nivel 0 y Nivel 01)
- Organigrama en imagen
- Servidores o sistemas internos para verificar controles de seguridad reales
- Texto resolutivo en Markdown de las resoluciones rectorales citadas como evidencia del PGTD/SGSI
- Actas, directorio vigente, suplencias, PIDE, IPv6, datos abiertos, ENAD, Oficial de Gobierno de Datos y Política de Privacidad no están accesibles en red; tratarlos como requerimientos formales a la universidad.

## Próximos Pasos Inmediatos

1. Actualizar AGENTS.md con compromisos no verificables ← **completado**
2. Preparar plantilla de inventario de activos y procedimiento de auditoría AS-IS ← **completado**
3. Verificar compromisos CGR pendientes con documentación interna ← **pendiente (usuario tiene acceso disponible más adelante)**
   - Datos Abiertos en PNDA (Compromiso 8)
   - Responsable de Software Público (Compromiso 13)
   - Plan de Transición a IPv6 (Compromiso 14)
   - Encuesta Nacional de Activos Digitales (Compromiso 17)
   - Oficial de Gobierno de Datos (Compromiso 20)
