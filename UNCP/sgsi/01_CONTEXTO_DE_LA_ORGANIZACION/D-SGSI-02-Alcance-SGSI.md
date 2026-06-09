---
title: Alcance del Sistema de Gestión de Seguridad de la Información
code: D-SGSI-02
---

**Organización:** Universidad Nacional del Centro del Perú (UNCP)

**RUC:** 20172030258

**Domicilio Legal:** Av. Mariscal Ramón Castilla km. 5, N° 3809-4089, El Tambo, Huancayo

**Naturaleza:** Universidad pública peruana, con autonomía académica, normativa y económica (Ley Universitaria N° 30220)

**Referencia Normativa:** ISO/IEC 27001:2022 — Cláusula 4.3 (Determinación del alcance del SGSI), Cláusula 4.4 (Sistema de Gestión de Seguridad de la Información)

**Documentos Relacionados:** D-SGSI-01 (Contexto Estratégico), D-SGSI-06 (Marco Conceptual), PGTD-UNCP 2026-2030, R-SGSI-01 (Inventario de Activos), D-SGSI-05 (Declaración de Aplicabilidad)

# Organización

La Universidad Nacional del Centro del Perú (UNCP) es una institución educativa superior pública fundada en 1959, con sede central en Huancayo (Región Junín). Cuenta con aproximadamente 10,000 estudiantes, 1,200 docentes y 500 trabajadores administrativos distribuidos en 4 sedes académicas.

El SGSI se implementa bajo el proyecto PGTD-01 del Plan de Gobierno y Transformación Digital 2026-2030, con un presupuesto de S/ 850,000 y un horizonte de 30 meses, con la meta de incorporar el 90% de los procesos institucionales al sistema y obtener la certificación ISO/IEC 27001:2022.

# Alcance del SGSI

## Declaración de Alcance

El Sistema de Gestión de Seguridad de la Información (SGSI) de la UNCP abarca la protección de la información generada, procesada, almacenada y transmitida por los procesos académicos, administrativos y de investigación de la universidad, independientemente de su ubicación física o lógica, formato o método de acceso, aplicando controles basados en riesgo bajo el modelo Zero Trust y gestionando el ciclo de vida completo del dato.

## Ámbito Organizacional

| Macroproceso | Unidades y Procesos Incluidos | Activos Críticos Asociados |
|:-------------|:------------------------------|:---------------------------|
| **Gestión Académica** | Admisión, Matrícula, Registro de Notas, Grados y Títulos, Certificaciones, Biblioteca | ERP ADESA (23 módulos), DSpace (Repositorio), KOHA (Biblioteca), Moodle 4.1 (Campus Virtual) |
| **Investigación y Propiedad Intelectual** | Gestión de proyectos de investigación, Repositorio de tesis, Publicaciones científicas, 13 centros de investigación | Sistema de Investigación, DSpace, Laboratorios de investigación, Base de datos de patentes |
| **Gestión Administrativa y Financiera** | Planillas, Tesorería, Abastecimiento, Contabilidad, Recursos Humanos, Bienestar Universitario | SIGA, SIAF, ERP ADESA (módulos financieros), Sistema de Tesorería, Planillas |
| **Educación Digital y Colaboración** | Educación virtual, Comunicación institucional, Trabajo remoto | Microsoft 365 (Teams, SharePoint, Exchange Online), Moodle 4.1 |
| **Gestión de Salud Universitaria** | Centro Médico Universitario, Seguro Estudiantil | Historia Clínica Electrónica, Base de datos de pacientes |
| **Gestión de la Investigación Ambiental** | 13 centros de investigación: CENAA (agua), CEPREANDES (prevención de riesgos), IBIG (biotecnología), CIAM (alta montaña), CER (energías renovables), Nanotecnología, Biología Molecular, CIMMA (medicina de altura) | Datos de investigación ambiental, estaciones de monitoreo, SINIA/REDIAM |

## Ámbito Tecnológico

| Capa | Componentes Incluidos | Excluido del Alcance |
|:-----|:----------------------|:--------------------|
| **Infraestructura On-Premise** | Data Center Huancayo: 8 servidores físicos, 3 virtualizados, 12 TB almacenamiento objeto, 4 TB backup. Redes de facultades: 4 sedes (Huancayo, Mantaro, Satipo, Tarma), 143 APs, 137 PoE switches, 9 firewalls. **Se incluye de forma explícita el aseguramiento de todas las APIs y servicios locales expuestos en cualquiera de las sedes periféricas como fronteras críticas.** | Infraestructura civil (edificaciones, mobiliario) que no procesa ni almacena información |
| **Infraestructura Cloud** | Huawei Cloud (IaaS/PaaS): servidores virtuales, balanceadores, WAF, Anti-DDoS. Microsoft 365 (SaaS): Exchange Online, SharePoint, Teams, OneDrive | Servicios cloud personales no autorizados (Shadow IT no descubierto) |
| **Red y Conectividad** | 4 Gbps internet, VPN IPsec, SSL-VPN para acceso remoto (con obligatoriedad de cumplimiento de directivas de seguridad y validación de postura de red), segmentación de red actual (sin ZTNA aún). **Se incluyen las interfaces y endpoints de APIs que integran servicios externos.** | Redes de terceros no administradas por la UNCP (a excepción de las APIs y canales de comunicación desarrollados o controlados por la UNCP que actúan como integraciones) |
| **Dispositivos Finales** | 3,736 equipos de escritorio, 1,861 laptops, dispositivos móviles institucionales y BYOD voluntario autorizado para funciones laborales | Dispositivos personales de estudiantes y docentes usados para servicios académicos generales; se gestionan mediante concientización, MFA cuando esté disponible y condiciones de acceso por cuenta |
| **Seguridad Perimetral** | Firewalls existentes (con licencias vencidas — en proceso de renovación), WAF Huawei Cloud | — |
| **Monitoreo** | Sin SIEM al inicio del proyecto. Se implementará durante la ejecución del PGTD-01 | — |

## Ámbito Geográfico

| Sede | Ubicación | Procesos Principales | Tipo de Conexión |
|:-----|:-----------|:--------------------|:-----------------|
| **Sede Central Huancayo** | Av. Mariscal Ramón Castilla km. 5, El Tambo | Rectorado, OTI, Administración Central, Facultades | Fibra óptica 4 Gbps |
| **Sede Mantaro** | Distrito de El Mantaro, Jauja | Facultad de Ciencias Agrarias | Fibra óptica |
| **Sede Satipo** | Satipo, Junín | Facultad de Ciencias Agrarias — Satipo | Fibra óptica |
| **Sede Tarma** | Tarma, Junín | Facultad de Ciencias Agrarias — Tarma | Fibra óptica |
| **Acceso Remoto** | Domicilios de docentes y administrativos, trabajo de campo, sedes temporales | Todos los procesos con acceso remoto autorizado | VPN / Internet |

## Ámbito Temporal

El SGSI se implementa en fases progresivas conforme al cronograma del PGTD-01:

| Fase | Periodo | Hito |
|:-----|:--------|:-----|
| **Fase 0 — Diagnóstico AS-IS** | 2026 Q2-Q3 | Auditoría inicial de activos, definición de políticas, ratificación de roles y matriz RACI |
| **Fase 1 — Implementación Basal** | 2026 Q4 — 2027 Q2 | Controles críticos (A.5, A.6, A.7, A.8), SIEM básico, MFA obligatorio |
| **Fase 2 — Consolidación** | 2027 Q3 — 2028 Q1 | Segmentación ZTNA, integración PIDE, SOC básico, 50% procesos en SGSI |
| **Fase 3 — Certificación** | 2028 Q2-Q4 | Auditoría interna, auditoría de certificación ISO 27001:2022, 90% procesos en SGSI |

# Partes Interesadas y sus Requisitos

| Parte Interesada | Requisitos Clave para el SGSI | Expectativa |
|:-----------------|:------------------------------|:------------|
| **Estudiantes (~10,000)** | Disponibilidad 24/7 de servicios académicos, protección de datos personales (Ley N° 29733), privacidad de calificaciones | Confianza en la plataforma digital |
| **Docentes (~1,200)** | Acceso remoto seguro, integridad de investigaciones y publicaciones, protección de propiedad intelectual | Continuidad del trabajo académico |
| **Personal Administrativo (~500)** | Confidencialidad de datos financieros y de personal, disponibilidad de sistemas de gestión | Eficiencia operativa |
| **OTI (11 profesionales + equipo de soporte/practicantes)** | Herramientas de monitoreo y respuesta, procesos documentados, autonomía técnica, soporte de red y aseguramiento de APIs en todas las sedes | Capacidad de gestión de seguridad y resiliencia operativa |
| **Organismo Supervisor (SUNEDU)** | Licenciamiento institucional, calidad educativa, infraestructura tecnológica adecuada | Cumplimiento normativo |
| **PCM / SGTD** | Implementación del Marco de Confianza Digital (D.S. 126-2025-PCM), interoperabilidad PIDE, reporte de avance PGTD | Cumplimiento de política nacional |
| **Proveedores (Huawei, Microsoft)** | SLA de seguridad, continuidad del servicio, protección de datos en cloud | Cumplimiento contractual |
| **RENIEC / SUNEDU (PIDE)** | Interoperabilidad segura, autenticación de identidad, verificación de grados | Integración digital del Estado |
| **Sociedad / Región Junín** | Transparencia, protección de datos de exalumnos y postulantes, continuidad del servicio educativo | Confianza institucional |

# Límites del SGSI

## Inclusiones

Todas las cláusulas 4 a 10 de ISO/IEC 27001:2022 se incluyen sin exclusión, siendo indispensables para la conformidad del sistema:

| Cláusula ISO 27001:2022 | Aplicación en UNCP |
|:------------------------|:-------------------|
| **4. Contexto de la organización** | Documentado en D-SGSI-01 (Análisis de Contexto Estratégico) y el presente documento |
| **5. Liderazgo** | Política de Seguridad (D-SGSI-03), Acta de Compromiso (ACT-SGSI-01), roles y responsabilidades |
| **6. Planificación** | Metodología de Gestión de Riesgos (D-SGSI-04), SoA (D-SGSI-05), objetivos de seguridad |
| **7. Soporte** | Recursos, competencias, concientización (P-SGSI-08), comunicación, información documentada (P-SGSI-00) |
| **8. Operación** | Planificación operativa, evaluación de riesgos, tratamiento de riesgos, controles A.5-A.8 |
| **9. Evaluación del desempeño** | Monitoreo, medición, auditoría interna (P-SGSI-09), revisión por la dirección |
| **10. Mejora** | No conformidades, acciones correctivas, mejora continua |

## Exclusiones

Se excluyen del alcance del SGSI los siguientes elementos, por no procesar ni almacenar información objeto de protección:

- Infraestructura civil (edificaciones, mobiliario, instalaciones eléctricas no asociadas a TI)
- Vehículos y activos de transporte
- Activos de consumo (material de oficina, suministros de limpieza)
- Sistemas de información de entidades externas sobre los cuales la UNCP no tenga control directo (sin embargo, los endpoints, APIs y canales de integración desarrollados o consumidos por la UNCP para interactuar con estos sistemas externos sí están incluidos en el alcance del SGSI para mitigar vectores de ataque externos)

No se excluye ningún requisito de las cláusulas 4 a 10 de la norma ISO/IEC 27001:2022.

# Justificación Basada en Riesgos

La delimitación del alcance responde a los riesgos críticos identificados en el análisis de contexto (D-SGSI-01) y la matriz de evaluación de riesgos (R-SGSI-02):

| Riesgo Crítico | Factor de Riesgo | Justificación de Inclusión en el Alcance |
|:----------------|:-----------------|:-----------------------------------------|
| Fuga de datos sensibles de estudiantes | Acceso remoto masivo, ausencia de DLP, MFA parcial | Se incluye el control de acceso remoto, la segmentación de red y la implementación de DLP progresivo |
| Alteración de registros académicos | APIs expuestas sin autenticación segura en sedes, vulnerabilidades de red periféricas, segmentación de red deficiente, ausencia de ZTNA | Se incluye la seguridad y auditoría de APIs en todas las sedes, la infraestructura de red de facultades y el proyecto de microsegmentación (ZTNA) |
| Indisponibilidad de servicios críticos | Dependencia de Huawei Cloud sin plan de salida, firewall obsoleto | Se incluye la gestión de continuidad del negocio y la resiliencia cloud |
| Incumplimiento normativo | 7 nuevas normas 2024-2025, sanciones por brecha de datos | Se incluye el cumplimiento legal como requisito transversal del SGSI |
| Fuga de propiedad intelectual | Repositorio DSpace sin controles de acceso granular, tesis sin respaldo off-site | Se incluye el sistema de investigación y el repositorio digital |
| Ataque de ransomware | 96 ataques/min en Perú, universidades como blanco prioritario | Se incluyen controles A.8.16 (backups inmutables) y A.8.7 (protección contra malware) |

# Mapa de Dependencias Críticas

| Proceso | Activo Crítico | Dependencia Tecnológica | Dependencia Humana |
|:--------|:---------------|:------------------------|:-------------------|
| Matrícula / Notas | Base de Datos ADESA | Huawei Cloud / Keycloak IdM | OTI (Equipo técnico y de desarrollo) |
| Gestión de Pagos | Sistema de Tesorería | SIAF / Pasarela de Pagos | Dirección de Finanzas |
| Educación Virtual | Moodle 4.1 | Huawei Cloud S3 / Contenedores | Equipo de Educación Virtual |
| Investigación | Repositorio DSpace | Red de Telemetría / Backup | Vicerrectorado de Investigación |
| Comunicación | Microsoft 365 | Exchange Online / Teams | OTI / Comunicaciones |
| Salud Universitaria | Historias Clínicas | Base de datos Centro Médico | Centro Médico Universitario |

# Declaración de Conformidad

El presente documento establece los límites y la aplicabilidad del SGSI-UNCP, alineado con los requisitos de la Cláusula 4.3 de ISO/IEC 27001:2022. El alcance definido ha sido determinado considerando las cuestiones internas y externas identificadas en el análisis de contexto (D-SGSI-01), las necesidades y expectativas de las partes interesadas, y los resultados de la evaluación de riesgos inicial.

El SGSI será objeto de revisión periódica durante las auditorías internas y las revisiones por la dirección, pudiendo ajustarse su alcance cuando ocurran cambios significativos en la organización, su contexto o sus activos de información.
