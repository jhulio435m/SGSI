---
title: Mapa de Procesos del Sistema de Gestión de Seguridad de la Información
code: D-SGSI-07
---

**Organización:** Universidad Nacional del Centro del Perú (UNCP)

**Referencia Normativa:** ISO/IEC 27001:2022 — Cláusula 4.4 (Sistema de Gestión y sus Procesos), Cláusula 4.1 (Comprensión de la organización)

**Documentos Relacionados:** D-SGSI-01 (Contexto Estratégico), D-SGSI-02 (Alcance del SGSI), D-SGSI-06 (Marco Conceptual), R-SGSI-01 (Inventario de Activos), R-SGSI-02 (Matriz de Riesgos)

**Mapa de Procesos Institucional:** Resoluciones R. N° 3524-R-2025 (Nivel 0) y R. N° 3526-R-2025 (Nivel 1)

![Mapa de Procesos Nivel 0 de la UNCP](../imagenes/mapa-procesos-nivel-0.png)

![Mapa de Procesos Nivel 1 de la UNCP](../imagenes/mapa-procesos-nivel-1.png)

# Introducción

El presente documento describe los procesos institucionales de la UNCP desde la perspectiva del Sistema de Gestión de Seguridad de la Información. Cada proceso se analiza identificando los activos de información críticos que gestiona, los riesgos de seguridad asociados, los sistemas que lo soportan y los controles aplicables según ISO/IEC 27001:2022.

El mapa de procesos constituye la base para la identificación de activos de información (R-SGSI-01), la evaluación de riesgos (R-SGSI-02) y la determinación del alcance del SGSI (D-SGSI-02). La meta del PGTD-UNCP es incorporar el 90% de los procesos institucionales al SGSI al año 2028.

# Clasificación de Procesos para la Seguridad

## Procesos Estratégicos

Los procesos estratégicos definen la dirección, las políticas y la supervisión del SGSI. Su afectación compromete la gobernabilidad de la UNCP y la continuidad del sistema.

| Proceso | Descripción | Activo de Información Clave | Sistema Asociado | Riesgo de Seguridad | Control ISO 27001 |
|:--------|:------------|:----------------------------|:-----------------|:--------------------|:------------------|
| Gobierno Digital | Liderazgo del Comité de Gobierno Digital (CGD), aprobación de políticas, supervisión del PGTD y del SGSI | Actas del CGD, resoluciones rectorales, políticas de seguridad, informes de avance | Gestor documental, Microsoft 365 | Alto — retraso en la toma de decisiones, pérdida de trazabilidad de acuerdos | A.5.1, A.5.2, A.5.4 |
| Planeamiento Estratégico | Alineamiento del SGSI con el PEI 2024-2030, PGTD 2026-2030 y presupuesto institucional | PEI, PGTD, informes de avance de proyectos, matriz de indicadores | Gestor documental, Microsoft 365 | Alto — desalineación estratégica, incumplimiento de metas PGTD | A.5.8, A.5.11 |
| Gestión de Riesgos Institucionales | Aplicación de ISO 31000, identificación y tratamiento de riesgos institucionales, definición del apetito de riesgo | Matriz de riesgos institucionales, Declaración de Aplicabilidad (SoA), planes de tratamiento | R-SGSI-02, D-SGSI-04, D-SGSI-05 | Alto — riesgos no mitigados, pérdida de activos críticos | A.5.6, A.5.7 |
| Gestión de Calidad y Mejora Continua | Auditorías internas del SGSI, revisión por la dirección, acciones correctivas y preventivas | Informes de auditoría, actas de revisión por la dirección, RAC, plan de mejora | P-SGSI-09, R-SGSI-04, F-SGSI-04 | Medio — pérdida de trazabilidad de no conformidades, estancamiento del SGSI | A.5.25, A.5.36 |
| Gestión de Cumplimiento Normativo | Seguimiento de obligaciones legales (Ley N° 29733, D.L. N° 1412, Marco de Confianza Digital), atención a entes de control (CGR) | Matriz de requisitos legales, informes a la CGR, registro de sanciones | Gestor documental, Microsoft 365 | Alto — sanciones administrativas, multas por incumplimiento de protección de datos | A.5.31, A.5.32 |

## Procesos Misionales

Los procesos misionales generan valor directo a la sociedad. Su interrupción afecta la formación de más de 10,000 estudiantes, la investigación científica y la responsabilidad social universitaria.

| Proceso | Descripción | Activo de Información Clave | Sistema Asociado | Flujo de Datos Crítico |
|:--------|:------------|:----------------------------|:-----------------|:-----------------------|
| Gestión de Admisión | Proceso de admisión, inscripción de postulantes, aplicación de examen de admisión, publicación de resultados | Bases de datos de postulantes, resultados de examen, cuadros de mérito | ERP ADESA, Portal web, Sistema de admisión | Postulante → inscripción → examen → calificación → publicación |
| Gestión de Matrícula | Registro de matrícula, asignación de asignaturas, generación de horarios, registro de estudiantes | Registros de matrícula, fichas de estudiante, horarios, silabos | ERP ADESA, Portal del Estudiante | Postulante admitido → registro → asignación de cursos → horario |
| Gestión de Formación y Notas | Registro de notas, control de asistencia, gestión de planes de estudio, evaluaciones | Actas de notas, registros de asistencia, planes de estudio, silabos | ERP ADESA, Moodle 4.1, Microsoft Teams | Docente → registro de notas → actas → validación → cierre |
| Gestión de Grados y Títulos | Emisión de grados y títulos, registro de egresados, trámite ante SUNEDU | Expedientes de grados, resoluciones de otorgamiento, diplomas, registros SUNEDU | ERP ADESA, Repositorio DSpace, Portal SUNEDU | Egresado → solicitud → validación académica → resolución → SUNEDU |
| Gestión de Investigación | Desarrollo de tesis, proyectos de investigación, patentes, publicaciones científicas | Tesis, papers, datos de investigación, patentes, registros de proyectos | DSpace, Sistema de investigación, Microsoft 365 | Investigador → proyecto → recolección de datos → análisis → publicación → repositorio |
| Gestión de Responsabilidad Social | Proyección social, extensión universitaria, voluntariado, convenios institucionales | Convenios, informes de proyección social, registros de beneficiarios | Portal web, Gestor documental | Comunidad → proyecto → ejecución → informe → rendición de cuentas |
| Servicios Estudiantiles | Comedor universitario, Centro Médico, bienestar universitario, actividades culturales y deportivas, becas | Historias clínicas, registros de becas, fichas socioeconómicas, registros de beneficiarios | Sistema de bienestar universitario | Estudiante → solicitud → evaluación → beneficio → seguimiento |

### Flujo de Datos del Proceso Misional Crítico: Gestión Académica

El flujo de datos del proceso misional principal (Gestión Académica) se compone de las siguientes etapas secuenciales:

| Etapa | Descripción | Datos Críticos | Sistema | Control de Seguridad Aplicable |
|:------|:------------|:---------------|:--------|:-------------------------------|
| 1. Admisión | Inscripción de postulantes, aplicación del examen, publicación de resultados | Datos personales de postulantes (nombres, DNI, domicilio), resultados de examen, cuadro de méritos | Portal web, ERP ADESA | A.9.4 (Restricción de acceso), A.10.1 (Cifrado en tránsito), A.8.24 (Cifrado en reposo) |
| 2. Matrícula | Registro del estudiante admitido, asignación de asignaturas, generación de horarios | Ficha de estudiante, registro de matrícula, asignaturas inscritas | ERP ADESA, Portal del Estudiante | A.9.2 (Gestión de acceso), A.9.3 (Responsabilidades de acceso), A.8.13 (Respaldos) |
| 3. Formación y Notas | Registro de notas parciales y finales, control de asistencia, evaluación docente | Actas de notas, registros de asistencia, evaluaciones parciales y finales | ERP ADESA, Moodle 4.1 | A.8.13 (Integridad de respaldos), A.8.2 (Privilegios de acceso), A.12.4 (Registro de eventos) |
| 4. Grados y Títulos | Validación de egreso, emisión de grados, registro ante SUNEDU | Expediente de grado, acta de sustentación, resolución de otorgamiento, diploma | ERP ADESA, SUNEDU | A.5.32 (Propiedad intelectual), A.8.2 (Privilegios), A.13.1 (Seguridad de red) |
| 5. Archivo y Custodia | Archivamiento de expedientes físicos y digitales, custodia de actas y resoluciones | Actas originales, expedientes, resoluciones (físicas y digitales) | Archivo central, DSpace | A.11.1 (Seguridad física), A.11.2.7 (Eliminación segura), A.8.3 (Manejo de medios) |

**Nota:** El sistema ERP ADESA (23 módulos) es el habilitador tecnológico transversal del flujo académico. Su disponibilidad es crítica: una interrupción prolongada detiene los procesos de matrícula, registro de notas y emisión de grados, con impacto directo en más de 10,000 estudiantes.

## Procesos de Apoyo

Los procesos de apoyo son necesarios para que los procesos misionales funcionen de forma segura y eficiente.

| Proceso | Descripción | Activo de Información Clave | Sistema Asociado | Dependencia Crítica |
|:--------|:------------|:----------------------------|:-----------------|:--------------------|
| Tecnologías de la Información (OTI) | Gestión de infraestructura TI, redes, cloud, seguridad, CSIRT, soporte técnico. Cuenta con 11 profesionales permanentes más soporte de practicantes para ~11,700 usuarios | Configuraciones de red, credenciales de administración, logs de seguridad, inventario de activos | Microsoft 365 Admin, Huawei Cloud Console | Crítica — todos los procesos dependen de TI |
| Gestión de Recursos Humanos | Contratación, capacitación, evaluación de desempeño, desvinculación, planillas | Expedientes de personal, planillas, contratos, evaluaciones, declaraciones juradas | SIGA/SIAF — Módulo RRHH | Alta — fuga de datos personales de ~1,700 trabajadores |
| Gestión Financiera y Abastecimiento | Contabilidad, tesorería, presupuesto, adquisiciones, proveedores | Registros contables, órdenes de compra, facturas, contratos, PAC | SIGA/SIAF, ERP ADESA (módulos financieros) | Crítica — fraude financiero, indisponibilidad de pagos |
| Gestión Documentaria | Mesa de partes, archivo central, gestión de expedientes digitales y notificaciones | Documentos recibidos y emitidos, resoluciones, memorandos, TUPA | Sistema de trámite documentario (GESDOC) | Alta — pérdida de trazabilidad documental |
| Asesoría Jurídica | Cumplimiento legal, protección de datos personales, contratos, defensa institucional | Contratos, resoluciones, directivas, informes legales, procesos judiciales | Gestor documental | Alta — responsabilidad legal por incumplimiento normativo |
| Comunicaciones e Imagen | Gestión de comunicación, portal web, redes sociales y atención al ciudadano | Contenido web, comunicados oficiales, cuentas de redes sociales | Portal web, gestor de contenidos | Media — suplantación de identidad institucional, desinformación |

# Matriz de Dependencias entre Procesos

| Proceso | Depende de (Entrada) | Provee a (Salida) | Sistema Transversal | Impacto de Indisponibilidad |
|:--------|:--------------------|:------------------|:--------------------|:---------------------------|
| Admisión | RRHH (convocatoria de personal), Abastecimiento (bienes y servicios) | Matrícula, SUNEDU (registro de ingresantes) | ERP ADESA, Portal web | Retraso del ciclo de admisión anual |
| Matrícula | Admisión, Servicios Estudiantiles (becas), Tesorería (pagos) | Formación (listas de clase), Tesorería (cobros) | ERP ADESA | Imposibilidad de iniciar el semestre académico |
| Formación y Notas | Matrícula, RRHH (asignación docente) | Grados y Títulos (egreso), Archivo (actas) | ERP ADESA, Moodle 4.1 | Pérdida de registros de notas, imposibilidad de emitir grados |
| Grados y Títulos | Formación y Notas, Asesoría Jurídica (legalidad del egreso) | SUNEDU (registro de egresados), Archivo Central | ERP ADESA, DSpace | Imposibilidad de emitir diplomas, incumplimiento SUNEDU |
| Investigación | RRHH, Abastecimiento | Repositorio DSpace, Publicaciones científicas | DSpace, Laboratorios | Pérdida de propiedad intelectual, retraso en publicaciones |
| Tesorería | Matrícula (pagos), Abastecimiento (proveedores), RRHH (planillas) | Contabilidad, SUNAT | SIGA/SIAF | Imposibilidad de pagar planillas y proveedores |
| OTI | Abastecimiento (hardware, licencias, servicios cloud) | Todos los procesos (conectividad, sistemas, seguridad) | Microsoft 365, Huawei Cloud, Red de datos | Detención de todos los procesos institucionales |

**Impacto transversal:** El proceso de OTI es el habilitador crítico de todos los demás procesos. La OTI cuenta con 11 profesionales permanentes y equipo de practicantes, lo que permite operar adecuadamente el SGSI en todas las sedes periféricas de la universidad.

# Controles de Seguridad por Nivel de Proceso

| Nivel de Proceso | Controles Prioritarios (ISO 27002) | Enfoque de Seguridad |
|:-----------------|:-----------------------------------|:--------------------|
| **Estratégico** | A.5.1 (Políticas de seguridad), A.5.2 (Roles y responsabilidades), A.5.4 (Responsabilidades de la dirección), A.5.8 (Gestión de proyectos), A.5.24 (Gestión de incidentes), A.5.25 (Requisitos legales) | Gobernanza, cumplimiento normativo, supervisión estratégica, continuidad del programa SGSI |
| **Misional** | A.8.2 (Privilegios de acceso), A.8.13 (Respaldos), A.8.20 (Seguridad de redes), A.8.24 (Cifrado), A.5.30 (Continuidad), A.5.32 (Propiedad intelectual) | Disponibilidad e integridad de datos críticos, protección de propiedad intelectual, continuidad operativa |
| **Apoyo** | A.8.8 (Gestión de vulnerabilidades), A.8.16 (Monitoreo), A.8.17 (Servicios de TI), A.5.19 (Proveedores), A.7.1 (Seguridad física), A.5.23 (Seguridad cloud) | Operatividad de infraestructura, protección de servicios compartidos, gestión de proveedores |

# Responsables de Procesos

| Proceso | Dueño del Proceso | Unidad | Rol en el SGSI |
|:--------|:------------------|:-------|:---------------|
| Gestión Académica | Vicerrector Académico | Vicerrectorado Académico | Clasificar y proteger la información académica, autorizar accesos a sistemas académicos, validar integridad de registros |
| Gestión de Investigación | Vicerrector de Investigación | Vicerrectorado de Investigación | Proteger la propiedad intelectual, gestionar acceso al repositorio DSpace, autorizar publicaciones |
| Tecnologías de la Información | Jefe de la OTI | Oficina de Tecnologías de la Información | Implementar y operar los controles técnicos del SGSI, administrar infraestructura de seguridad, gestionar incidentes |
| Gestión Financiera | Director de Administración | Dirección de Administración | Asegurar confidencialidad e integridad de información financiera, autorizar transacciones críticas |
| Recursos Humanos | Jefe de RRHH | Oficina de Recursos Humanos | Gestionar confidencialidad de datos personales del personal, controlar accesos al módulo de planillas |
| Gestión Documentaria | Jefe del Archivo Central | Archivo Central | Custodiar documentos físicos y digitales, gestionar eliminación segura, controlar acceso a archivos históricos |
| Asesoría Jurídica | Jefe de Asesoría Jurídica | Oficina de Asesoría Jurídica | Asegurar cumplimiento legal del SGSI, gestionar protección de datos personales, revisar contratos de TI |

# Mapa de Interacción del SGSI

| Componente SGSI | Procesos Relacionados | Documento SGSI | Tipo de Interacción |
|:----------------|:---------------------|:---------------|:-------------------|
| Política de Seguridad | Todos los procesos estratégicos | D-SGSI-03 | Define los principios y responsabilidades de seguridad aplicables a todos los procesos |
| Evaluación de Riesgos | Todos los procesos misionales y de apoyo | D-SGSI-04, R-SGSI-02 | Identifica riesgos específicos por proceso y define tratamientos |
| Control de Acceso | Gestión Académica, Investigación, RRHH, Tesorería | P-SGSI-03 | Regula quién puede acceder a qué sistemas y datos según su rol |
| Gestión de Incidentes | OTI, todos los procesos (reporte) | P-SGSI-02 | Canaliza la detección, reporte y respuesta a incidentes de seguridad |
| Continuidad | Gestión Académica, Investigación, Tesorería | P-SGSI-05 | Asegura la continuidad de los procesos críticos ante interrupciones |
| Gestión de Cambios | Todos los procesos (cambios en sistemas, personal, normativa) | P-SGSI-04 | Controla los cambios que puedan afectar la seguridad de la información |
| Capacitación | RRHH, todos los procesos (concientización) | P-SGSI-08 | Desarrolla competencias de seguridad en todos los niveles |
| Auditoría Interna | Todos los procesos (evaluación periódica) | P-SGSI-09 | Verifica la eficacia de los controles en cada proceso |
| Eliminación Segura | Archivo Central, OTI, todos los procesos | P-SGSI-07 | Gestiona la destrucción segura de información cuando pierde vigencia |

# Documentos Relacionados

| Código | Nombre | Relación con el Mapa de Procesos |
|:-------|:-------|:---------------------------------|
| D-SGSI-01 | Análisis del Contexto Estratégico | Identifica factores externos e internos que afectan los procesos |
| D-SGSI-02 | Alcance del SGSI | Define qué procesos están dentro del alcance del SGSI |
| D-SGSI-06 | Marco Conceptual del SGSI | Establece el modelo conceptual y ciclo PHVA que rige los procesos |
| R-SGSI-01 | Inventario de Activos de Información | Cataloga los activos de información identificados por proceso |
| R-SGSI-02 | Matriz de Evaluación y Tratamiento de Riesgos | Documenta los riesgos asociados a cada proceso y sus controles |
| P-SGSI-00 | Control de Documentos y Registros | Regula la documentación de los procesos del SGSI |
