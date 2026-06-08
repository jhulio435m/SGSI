---
title: Procedimiento de Control de Documentos y Registros del SGSI-UNCP
code: P-SGSI-00
---

**Organización:** Universidad Nacional del Centro del Perú (UNCP)

**Código del Documento:** P-SGSI-00

**Versión:** 1.0

**Norma Base:** ISO/IEC 27001:2022 (Cláusula 7.5 — Información Documentada)

**Alineamiento:** D-SGSI-00 (Marco Terminológico), R-SGSI-00 (Lista Maestra), R.S. Nº 001-2017-PCM/SEGDI (Modelo de Gestión Documental), Ley N° 29733 (Protección de Datos Personales)

# Objetivo

Establecer las directrices para la creación, codificación, revisión, aprobación, distribución, almacenamiento y control de la información documentada (documentos y registros) del Sistema de Gestión de Seguridad de la Información (SGSI) de la UNCP, garantizando la integridad, disponibilidad, trazabilidad y confidencialidad de la documentación del sistema conforme a ISO/IEC 27001:2022.

# Alcance

Este procedimiento aplica a toda la información documentada del SGSI-UNCP, incluyendo:

- Políticas de seguridad (POL-SGSI)
- Procedimientos (P-SGSI)
- Documentos de referencia y directrices (D-SGSI)
- Registros y formatos (R-SGSI, F-SGSI)
- Actas y compromisos (ACT-SGSI)
- Documentos de origen externo (normas ISO, leyes peruanas, directivas PCM/SGTD)
- Versiones obsoletas y documentos retenidos para fines legales

Queda excluida la documentación del Sistema Integrado de Gestión de la Calidad (SIGC) no vinculada al SGSI, y la documentación técnica de infraestructura de la OTI que se rige por sus propios procedimientos operativos.

# Roles y Responsabilidades

| Rol | Responsabilidad Documental | Cargo |
|:---|---|:---|
| Elaborador | Redactar el documento, aplicar el formato y codificación establecidos, gestionar la revisión por pares | Oficial de Seguridad y Confianza Digital / Responsable de área |
| Revisor | Validar la coherencia técnica, aplicabilidad al contexto UNCP y alineación normativa | Comité de Gobierno Digital (CGTD-UNCP) / Jefe de OTI / Dueño de Proceso |
| Aprobador | Autorizar la entrada en vigor, asignar recursos para su implementación | Rectorado UNCP / DGA (según jerarquía del documento) |
| Custodio | Mantener el repositorio documental, controlar versiones, asegurar la accesibilidad | Oficial de Seguridad y Confianza Digital |
| Archivador | Conservar versiones obsoletas con fines legales y de auditoría | Oficina de Gestión de la Calidad (SIGC) |
| Usuario | Consultar, usar y custodiar la versión vigente del documento en su ámbito de competencia | Todo el personal UNCP alcanzado por el SGSI |

# Sistema de Codificación Documental

Todos los documentos del SGSI-UNCP se identifican mediante un código único conforme al siguiente formato:

**[TIPO]-SGSI-[NRO]**

## Tipos Documentales

| Tipo | Prefijo | Descripción | Ejemplos |
|:---|---|---|---|
| Documento de Referencia | D-SGSI | Documentos normativos, guías, marcos conceptuales, análisis | D-SGSI-00 (Marco Terminológico), D-SGSI-01 (Contexto Estratégico) |
| Procedimiento | P-SGSI | Procedimientos documentados obligatorios por ISO 27001 | P-SGSI-02 (Gestión de Incidentes), P-SGSI-03 (Control de Acceso) |
| Política | POL-SGSI | Políticas de seguridad de alto nivel aprobadas por Rectorado | POL-SGSI-01 (Desarrollo Seguro), POL-SGSI-06 (Contraseñas) |
| Registro / Lista Maestra | R-SGSI | Registros obligatorios, inventarios, matrices de riesgo | R-SGSI-00 (Lista Maestra), R-SGSI-01 (Inventario de Activos) |
| Formato / Plantilla | F-SGSI | Formatos de solicitud, actas, reportes, bitácoras | F-SGSI-01 (Solicitud de Acceso), F-SGSI-05 (Acta de Eliminación) |
| Acta / Acuerdo | ACT-SGSI | Actas de compromiso, reuniones del CGTD | ACT-SGSI-01 (Acta de Compromiso de Alta Dirección) |

## Reglas de Codificación

- El código se asigna correlativamente dentro de cada tipo, según el orden de creación.
- No se reutilizan códigos de documentos dados de baja.
- Los documentos en borrador no reciben código hasta su aprobación.
- Los documentos externos (normas ISO, leyes) se referencian por su identificador oficial, no reciben código SGSI.
- Las versiones mantienen el mismo código; solo cambia el número de versión.

# Estructura de Documentos

## Encabezado (Metadatos Obligatorios)

Todo documento oficial del SGSI-UNCP debe incluir al inicio:

| Campo | Descripción | Ejemplo |
|:---|---|:---|
| Título | Nombre completo del documento | Procedimiento de Gestión de Cambios en TI |
| Código | Código único según Sección 4 | P-SGSI-04 |
| Versión | Versión actual según Sección 6 | 2.0 |
| Organización | Nombre institucional | Universidad Nacional del Centro del Perú (UNCP) |
| Norma Base | Cláusula ISO 27001 o control aplicable | ISO/IEC 27001:2022 (Control A.8.32) |
| Alineamiento | Otros documentos SGSI relacionados | P-SGSI-02, P-SGSI-05 |

## Estructura Recomendada

1. **Objetivo** — Propósito del documento (qué problema resuelve)
2. **Alcance** — Límites de aplicación (qué incluye y qué excluye)
3. **Roles y Responsabilidades** — Tabla de roles con responsabilidades específicas
4. **Desarrollo** — Contenido sustantivo del documento (procedimiento, política, directriz)
5. **Referencias** — Documentos relacionados y normas aplicables
6. **Control de Cambios** — Historial de versiones

## Formato

- Fuente: Palatino (serif) para cuerpo, Helvética (sans-serif) para títulos.
- Alineación: Texto justificado a la izquierda (RaggedRight) para facilitar la lectura en pantalla.
- Tablas: Uso de `booktabs` con cabeceras alineadas y texto fluido.
- Código: Letra Courier para rutas, comandos y referencias técnicas.
- Numeración: Automática mediante LaTeX (pandoc).

# Control de Versiones

## Esquema de Versionado

| Componente | Cambio | Ejemplo |
|:---|---|---|
| Versión Mayor (X.0) | Cambios sustanciales en el contenido, nuevos requisitos normativos, reestructuración completa | 1.0 → 2.0 |
| Versión Menor (X.Y) | Cambios parciales, adición de secciones, actualización de referencias | 1.0 → 1.1 |
| Revisión (X.Y.Z) | Correcciones ortográficas, ajustes de formato, erratas | 1.0 → 1.0.1 |

## Historial de Cambios

Todo documento debe incluir una tabla de control de cambios al final:

| Versión | Fecha | Descripción del Cambio | Elaborador | Revisor | Aprobador |
|:---|---|---|---|---|---|
| 1.0 | 2026-06-07 | Versión inicial | Oficial de Seguridad | CGTD-UNCP | Rectorado |

# Ciclo de Vida del Documento

## Diagrama del Ciclo de Vida

| Fase | Secuencia |
|:---|:---|
| Creación → Revisión → Aprobación → Publicación | Flujo principal de incorporación de documentos |
| Distribución → Uso → Revisión Periódica | Flujo de operación y mantenimiento |
| Obsoleto → Archivo (Retención) | Flujo de disposición al terminar la vigencia |

## Etapas

| Etapa | Acción | Responsable | Tiempo Máximo |
|:---|---|---|---|
| 1. Creación | Redactar el documento según el formato y codificación establecidos | Elaborador | 15 días hábiles |
| 2. Revisión Técnica | Validar contenido, referencias y aplicabilidad | Revisor (CGTD / Jefe OTI / Dueño de Proceso) | 7 días hábiles |
| 3. Revisión Normativa | Verificar alineación con ISO 27001, normativa peruana y PGTD | Oficial de Seguridad | 5 días hábiles |
| 4. Aprobación | Autorizar la entrada en vigor mediante resolución o acta | Aprobador (Rector / DGA) | 7 días hábiles |
| 5. Publicación | Asignar código, registrar en R-SGSI-00, subir al repositorio | Custodio | 2 días hábiles |
| 6. Distribución | Notificar a los usuarios alcanzados, publicar en intranet | Custodio | 1 día hábil |
| 7. Uso | Consultar, aplicar y custodiar la versión vigente | Usuario | Permanente |
| 8. Revisión Periódica | Evaluar vigencia y actualización necesaria | Custodio + Revisor | Anual (enero) |
| 9. Obsoleto | Marcar como versión obsoleta, retirar de circulación | Custodio | Inmediato tras nueva versión |
| 10. Archivo | Conservar versión obsoleta con fines legales y de auditoría | Archivador | Según tabla de retención |

## Documentos de Origen Externo

Los documentos externos (normas ISO, leyes, directivas PCM/SGTD, resoluciones) se controlan mediante:

- Identificación en la Lista Maestra (R-SGSI-00) como referencias externas.
- Verificación semestral de vigencia por el Oficial de Seguridad.
- Notificación al CGTD cuando una norma externa sufra modificaciones que impacten el SGSI.
- Las versiones descargadas para consulta interna se marcan con la fecha de descarga y la advertencia: "Documento externo — Verificar vigencia en la fuente oficial".

# Distribución y Acceso

## Repositorio Oficial

El repositorio documental del SGSI-UNCP está estructurado por cláusulas ISO 27001:

| Carpeta | Contenido |
|:---|---|
| 00_CONTROL_DOCUMENTAL | Marco terminológico, procedimiento de control documental, lista maestra |
| 01_CONTEXTO_DE_LA_ORGANIZACION | Análisis de contexto, alcance, mapa de procesos, marco conceptual |
| 02_LIDERAZGO | Política general, acta de compromiso |
| 03_PLANIFICACION | Metodología de riesgos, SoA, inventario de activos, matriz de riesgos |
| 04_SOPORTE | Plan de capacitación y concientización |
| 05_OPERACION | Procedimientos de incidentes, acceso, cambios, continuidad, proveedores, eliminación |
| 06_EVALUACION_DEL_DESEMPEÑO | KPIs, programa de auditoría, metodología, plantillas |
| 07_MEJORA_CONTINUA | No conformidades, acciones correctivas |
| 09_POLITICAS_Y_PROCEDIMIENTOS | Políticas de seguridad (desarrollo, uso aceptable, clasificación, etc.) |
| 10_FORMATOS | Formatos y plantillas (solicitudes, actas, bitácoras) |

## Niveles de Acceso

| Clasificación | Descripción | Medio | Permiso |
|:---|---|:---|:---|
| Público Interno | Documentos de consulta general (políticas, procedimientos aprobados) | Intranet UNCP / Repositorio SGSI | Lectura para todo el personal UNCP |
| Restringido | Documentos con información sensible (inventario de activos, matriz de riesgos, SoA) | Repositorio SGSI (controlado) | Lectura: CGTD, OTI, auditores. Edición: Oficial de Seguridad |
| Confidencial | Documentos de auditoría, incidentes críticos, data personal | Repositorio SGSI (cifrado) | Solo Oficial de Seguridad y CGTD |

## Control de Copias

- La copia oficial es la versión electrónica publicada en el repositorio SGSI.
- Las copias impresas se consideran copias no controladas.
- Cuando se emite una copia controlada impresa (para auditorías externas, reuniones del CGTD), se marca con sello de "Copia Controlada", número de copia y responsable.
- El usuario debe verificar que está utilizando la versión vigente antes de referenciar o aplicar el documento.

# Control de Registros

## Identificación

Los registros (evidencias) se identifican mediante su código de formato (F-SGSI) más la fecha de generación:

**Formato:** `[CÓDIGO-FORMATO]_[DESCRIPCIÓN]_[YYYY-MM-DD].[ext]`

**Ejemplo:** `F-SGSI-01_Solicitud-Acceso_Juan-Perez_2026-06-07.pdf`

## Almacenamiento

| Tipo | Medio | Ubicación |
|:---|---|:---|
| Digital (preferido) | Repositorio documental SGSI (cifrado en reposo) | Servidor UNCPro / Huawei Cloud OBS |
| Físico (excepcional) | Archivador con llave, folder por código de documento | Archivo Central UNCP (Oficina de Gestión de la Calidad - SIGC) |

## Protección contra Alteraciones

- Los registros digitales se almacenan en formato no editable (PDF/A-2u) con firma digital del custodio.
- Los registros físicos se almacenan en folders con numeración correlativa de folios y sello de recepción.
- Cualquier modificación posterior a un registro debe realizarse mediante un nuevo registro que anule al anterior (no se permite sobrescritura ni edición directa).

## Tiempos de Retención

| Tipo de Registro | Plazo Mínimo | Fundamento Legal |
|:---|---|:---|
| Políticas y procedimientos (vigentes) | Vigencia + 5 años | ISO 27001:2022 Cláusula 7.5, Ley 29733 Art. 9 |
| Registros de capacitación | 5 años | Directiva SGSI-UNCP |
| Reportes de incidentes de seguridad | 5 años | ISO 27001:2022 Cláusula 10.1 |
| Auditorías internas y externas | 7 años | Ley Universitaria 30220, Estatuto UNCP |
| Matriz de riesgos y SoA | Vigencia + 5 años | ISO 27001:2022 Cláusula 6.1, 6.2 |
| Solicitudes de acceso y bajas | 2 años después de la desvinculación | Ley 29733 Art. 38, D.S. 016-2024-JUS |
| Datos personales (expedientes estudiantiles) | 10 años | Ley Universitaria 30220 Art. 103 |
| Actas de eliminación segura | 5 años | P-SGSI-07, NIST SP 800-88 Rev. 1 |

## Disposición Final

Al vencer el plazo de retención, el Oficial de Seguridad evalúa:

1. **Destrucción segura** del registro (según P-SGSI-07) si no tiene valor legal, histórico o de auditoría.
2. **Archivo histórico** si el registro tiene valor institucional (resoluciones rectorales, actas fundacionales, convenios marco).
3. **Transferencia al Archivo General de la UNCP** si corresponde según la Directiva de Archivo Universitario.

Toda disposición se documenta mediante el F-SGSI-05 (Acta de Eliminación Segura) o el documento de transferencia correspondiente.

# Revisión y Mantenimiento

## Revisión Periódica

| Tipo | Periodicidad | Responsable | Criterio |
|:---|---|---|---|
| Programada | Anual (enero) | Oficial de Seguridad | Verificar vigencia normativa, aplicabilidad y coherencia con otros documentos del SGSI |
| Extraordinaria | Cuando ocurra un cambio significativo | Oficial de Seguridad | Nueva versión de ISO 27001, nueva normativa nacional, cambio organizacional, incidente crítico |

## Indicadores de Eficacia (KPI)

| Indicador | Fórmula | Meta | Frecuencia |
|:---|---|---|---|
| Documentos con código asignado correctamente | (Documentos conforme / Total documentado) × 100 | ≥ 98% | Trimestral |
| Documentos aprobados dentro del plazo | (Aprobados dentro de 30 días / Total aprobados) × 100 | ≥ 90% | Trimestral |
| Lista Maestra actualizada | (Documentos listados / Total documentos oficiales) × 100 | 100% | Mensual |
| Registros con retención cumplida | (Registros eliminados al vencer / Total registros vencidos) × 100 | 100% | Anual |
| Personal que conoce el procedimiento documental | (Aprobados en evaluación / Total evaluados) × 100 | ≥ 85% | Anual |

# Referencias

| Código | Referencia |
|:---|---|
| ISO 27001 | ISO/IEC 27001:2022 — Cláusula 7.5 (Información Documentada), Anexo A Controles 5.9, 5.10, 5.13 |
| ISO 27002 | ISO/IEC 27002:2022 — Controles 5.9 (Inventario), 5.10 (Aceptación), 5.13 (Etiquetado) |
| NIST CSF 2.0 | Identify (ID.AM), Protect (PR.DS) |
| R.S. 001-2017-PCM | Modelo de Gestión Documental (MGD) — Secretaría de Gestión Pública |
| Ley 29733 | Ley de Protección de Datos Personales — Art. 9 (Seguridad), Art. 38 (Plazos de conservación) |
| D.S. 016-2024-JUS | Reglamento de la Ley 29733 |
| D.L. 1412 | Decreto Legislativo de Gobierno Digital — Art. 17 (Interoperabilidad) |
| P-SGSI-07 | Procedimiento de Eliminación Segura de Información y Activos |
| R-SGSI-00 | Lista Maestra de Documentos del SGSI |

