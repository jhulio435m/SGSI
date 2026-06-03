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

## Sugerencias Normativas (Perú)

1. **Oficial de Seguridad y Confianza Digital:** Es imperativo designar formalmente este rol mediante resolución, conforme al D.S. N° 029-2021-PCM.
2. **Interoperabilidad (PIDE):** Se sugiere priorizar la integración con la PIDE para automatizar la verificación de identidad (RENIEC) y el registro de grados (SUNEDU).
3. **Política de Privacidad:** El sitio web institucional debe incluir una Política de Privacidad visible que detalle el tratamiento de datos personales (Ley N° 29733).

## Pendientes / Próximos Pasos

- [ ] Ejecutar auditoría inicial de activos (AS-IS) 2026
- [ ] Definir políticas de seguridad formales basadas en ISO 27001:2022
- [ ] Implementar proyecto PGTD-01 (SGSI)
- [ ] Actualizar la conformación del CGTD UNCP
- [ ] Designar Oficial de Seguridad y Confianza Digital


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

## Próximos Pasos Inmediatos

1. Actualizar AGENTS.md con compromisos no verificables ← **completado**
2. Preparar plantilla de inventario de activos y procedimiento de auditoría AS-IS ← **completado**
3. Verificar compromisos CGR pendientes con documentación interna ← **pendiente (usuario tiene acceso disponible más adelante)**
   - Datos Abiertos en PNDA (Compromiso 8)
   - Responsable de Software Público (Compromiso 13)
   - Plan de Transición a IPv6 (Compromiso 14)
   - Encuesta Nacional de Activos Digitales (Compromiso 17)
   - Oficial de Gobierno de Datos (Compromiso 20)
