---
title: Análisis del Contexto Estratégico del SGSI-UNCP
code: D-SGSI-01
---

**Organización:** Universidad Nacional del Centro del Perú (UNCP)

**Referencia Normativa:** ISO/IEC 27001:2022 — Cláusula 4.1 (Comprensión de la organización y su contexto), 4.2 (Comprensión de las necesidades y expectativas de las partes interesadas), 4.3 (Determinación del alcance del SGSI)

**Documentos Relacionados:** D-SGSI-02 (Alcance del SGSI), D-SGSI-06 (Marco Conceptual), PEI 2024-2030, PGTD-UNCP 2026-2030, Mapa de Procesos Nivel 0 y Nivel 1 (R. 3524-R-2025, R. 3526-R-2025)

# Introducción

El presente documento desarrolla el análisis del contexto estratégico de la UNCP como requisito de la Cláusula 4 de la norma ISO/IEC 27001:2022. Comprende la determinación de las cuestiones internas y externas que afectan la capacidad de la organización para alcanzar los resultados previstos de su Sistema de Gestión de Seguridad de la Información (SGSI).

La UNCP, fundada en 1959, cuenta con aproximadamente 10,000 estudiantes, 1,200 docentes y 500 trabajadores administrativos distribuidos en 4 sedes (Huancayo, Mantaro, Satipo, Tarma), 38 carreras profesionales, 46 programas de maestría y 7 doctorados. Su presupuesto anual de tecnologías de la información asciende a S/ 1,900,000, equivalente al 1.2% del presupuesto institucional total.

# Análisis del Entorno Externo

## Análisis PESTEL

| Factor | Descripción y Diagnóstico | Impacto en SGSI |
|:-------|:--------------------------|:-----------------|
| **Político** | Mandato nacional de Transformación Digital (Ley N° 31814, D.L. N° 1412). La PCM/SGTD exige a todas las entidades públicas la implementación de un SGSI como parte del Marco de Confianza Digital (D.S. 126-2025-PCM). La Quinta Disposición Complementaria Final del D.S. N° 141-2025-PCM establece la obligatoriedad del uso intensivo de tecnologías digitales y datos en todas las entidades públicas. El PNTD al 2030 (D.S. N° 103-2023-PCM) fija 5 objetivos prioritarios que vinculan directamente a la UNCP. | **Crítico.** El SGSI no es optativo; su implementación responde a mandatos legales con plazos establecidos. El incumplimiento genera riesgos de sanción administrativa y afectación reputacional. |
| **Económico** | Presupuesto TI anual de S/ 1,900,000 (1.2% del presupuesto total). El proyecto PGTD-01 (SGSI) cuenta con S/ 850,000 asignados en un horizonte de 30 meses. El financiamiento proviene de Canon/RDR, sujeto a fluctuaciones anuales. La UNCP gestiona 8 fundos experimentales que generan ingresos propios. El subempleo de egresados universitarios (meta PEDN: 16.0% para 2027) impacta la demanda de carreras. | **Alto.** El presupuesto es suficiente para el SGSI basal pero no para acelerar la implementación. El riesgo de recorte presupuestal por factores macroeconómicos podría retrasar los proyectos de seguridad. Dependencia de Canon/RDR crea incertidumbre en la sostenibilidad plurianual. |
| **Social** | Comunidad universitaria de ~11,700 personas. Solo el 29% de peruanos mayores de 14 años sabe copiar o mover un archivo (PNTD). El 71% de estudiantes son nativos digitales con alta expectativa de disponibilidad 24/7. Cultura organizacional con resistencia al cambio digital (madurez dimensión D5: 1.175/5.0). La UNCP atiende a población de la región Junín con brecha digital significativa en zonas rurales. Las personas constituyen el activo más expuesto y vulnerable del SGSI por errores, phishing, ingeniería social, manejo inseguro de credenciales y baja cultura de reporte. | **Alto.** La baja cultura digital del personal administrativo incrementa el riesgo de errores humanos e incidentes de seguridad. Los estudiantes exigen servicios digitales seguros, móviles y disponibles permanentemente. La diversidad en competencias digitales obliga a programas de concientización segmentados, simulaciones de phishing, mensajes simples y mecanismos de reporte temprano sin enfoque punitivo. |
| **Tecnológico** | Madurez digital institucional: 1.569/5.0 (Nivel Inicial-Experimental, FONAFE). Infraestructura: 4 Gbps internet, Huawei Cloud (IaaS/PaaS), 8 servidores físicos, 3 virtualizados, 12 TB almacenamiento objeto, 4 TB backup. 9 firewalls con licencias vencidas, firewall perimetral obsoleto. 3,736 equipos de escritorio, 1,861 laptops, 143 APs, 137 PoE switches. Plataformas críticas: ERP ADESA (23 módulos), SIGA/SIAF, Moodle 4.1, DSpace, KOHA, Microsoft 365. Sin SIEM, sin SSO centralizado, sin integración PIDE. El auge de IA (D.S. N° 115-2025-PCM) exige nuevos controles. | **Crítico.** La infraestructura de seguridad presenta obsolescencia crítica (firewalls, segmentación). La ausencia de SIEM y monitoreo centralizado imposibilita la detección temprana de incidentes. La dependencia de Microsoft 365 y Huawei Cloud introduce riesgos de proveedor único. La falta de integración PIDE limita la interoperabilidad. La IA emergente requiere controles de auditoría de algoritmos. |
| **Ecológico** | Política Ambiental UNCP (R. N° 0835-R-2022) y Plan Ambiental 2023-2025. Comité de Gestión Ambiental formalizado. OGTD4 del PGTD-UNCP establece meta de reducción del 15% de consumo energético en Data Center. 13 centros de investigación ambiental (CENAA, IBIG, CIAM, CER, etc.) que generan datos científicos sensibles. Alineación con la ecoeficiencia del sector público (MINAM). SINIA y REDIAM como referentes. | **Medio.** El Green IT se integra como criterio de diseño en la modernización del Data Center. Los centros de investigación generan activos de información ambiental con requisitos específicos de integridad y disponibilidad. La reducción del consumo energético debe balancearse con los requisitos de alta disponibilidad del SGSI. |
| **Legal** | Siete nuevas normas en 2024-2025 que impactan directamente al SGSI: D.S. N° 016-2024-JUS (Reglamento Ley N° 29733 — Protección de Datos, vigente marzo 2025); D.S. N° 115-2025-PCM (Reglamento Ley N° 31814 — IA, auditoría de algoritmos); D.S. N° 098-2025-PCM (modifica D.S. N° 029-2021-PCM — identidad digital, interoperabilidad); R.SGTD N° 001-2025-PCM/SGTD (accesibilidad WCAG 2.2); Directiva N° 001-2025-PCM/SGTD (consumo seguro de servicios PIDE); D.S. 126-2025-PCM (Marco de Confianza Digital); Ley N° 29733 (Protección de Datos Personales). El PEDN al 2050 establece como objetivo prioritario la transformación digital del país (ON3). | **Crítico.** El volumen de nuevas obligaciones legales en 2024-2025 es sin precedentes. El D.S. N° 016-2024-JUS incrementa significativamente las sanciones por brechas de datos personales. El D.S. N° 115-2025-PCM exige auditorías de algoritmos para sistemas de IA que la UNCP ya utiliza o planea implementar. El Marco de Confianza Digital (D.S. 126-2025-PCM) establece requisitos específicos de seguridad que deben incorporarse al SGSI. |

## Análisis del Microentorno

| Fuerza | Diagnóstico | Implicancia para el SGSI |
|:-------|:------------|:-------------------------|
| **Rivalidad entre competidores** | 42 universidades licenciadas por SUNEDU. Las universidades privadas invierten agresivamente en plataformas digitales y certificaciones de seguridad. La UNCP compite por prestigio académico, investigación y acreditación. La seguridad de la información es un diferenciador de calidad en rankings y licenciamiento. | **Alta.** El SGSI y la eventual certificación ISO 27001:2022 constituyen una ventaja competitiva frente a universidades que no priorizan la seguridad. La confianza digital se convierte en un factor de atracción de estudiantes e investigadores. |
| **Poder de negociación de proveedores** | Alta dependencia de Huawei Cloud (IaaS/PaaS) como único proveedor cloud. Contrato Microsoft 365 con condiciones estándar. Proveedor de internet con 4 Gbps (contrato plurianual). 9 firewalls sin renovación de licencias. El ERP ADESA es un sistema Propietario con dependencia del proveedor para actualizaciones y soporte. | **Alta.** La dependencia de proveedores únicos (Huawei, Microsoft, ADESA) crea riesgos de concentración que deben gestionarse mediante cláusulas contractuales de seguridad (A.15 ISO 27002) y planes de contingencia. La falta de renovación de licencias de firewall representa un riesgo operativo inminente. |
| **Amenaza de nuevos competidores** | Programas de educación virtual global (Coursera, edX, plataformas internacionales). Nuevas universidades privadas con modelos 100% digitales. La SUNEDU exige condiciones mínimas de infraestructura tecnológica para el licenciamiento. | **Media.** La UNCP debe proteger el valor oficial de sus grados y títulos mediante la integridad y disponibilidad de sus registros académicos. La educación virtual global compite directamente con la oferta de pregrado y posgrado. |
| **Amenaza de productos sustitutos** | Certificaciones técnicas cortas, microcredenciales, bootcamps de programación. Cursos MOOC masivos. Plataformas de educación continua que no requieren infraestructura universitaria tradicional. | **Media.** La propuesta de valor de la UNCP debe incluir la seguridad y confianza como atributos diferenciadores frente a opciones no formales. Los registros académicos digitales deben contar con integridad garantizada para mantener su validez oficial. |
| **Poder de negociación de los estudiantes** | 10,000 estudiantes con expectativas crecientes de servicios digitales: matriculación en línea, acceso a notas, emisión de certificados, biblioteca virtual, aulas híbridas. Encuestas de satisfacción vinculadas a la evaluación institucional. Acceso a redes sociales como canal de reclamos públicos. | **Alta.** Los estudiantes son el grupo de interés más sensible a la disponibilidad y privacidad de los servicios digitales. Una brecha de seguridad con exposición de datos personales generaría daño reputacional severo y posible fuga de matrícula. La protección de datos personales (Ley N° 29733) es un derecho exigible. |

# Análisis del Entorno Interno

## Descripción de la Organización

La UNCP está organizada en 4 sedes académicas, 38 carreras profesionales, 46 maestrías y 7 doctorados. Su estructura de gobierno digital incluye un Comité de Gobierno Digital formalizado por R. N° 1862-R-2023, la Mg. Rocio Rosanna Damian Alvarado integrada al CGD como Oficial de Seguridad de la Informacion por R. N° 2143-R-2023, y una Oficina de Tecnologías de la Información (OTI) con solo 2 profesionales para atender a ~11,700 miembros de la comunidad universitaria.

La gestión de procesos se formaliza mediante el Mapa de Procesos Nivel 0 y Nivel 1 (R. 3524-R-2025, R. 3526-R-2025). El Plan Estratégico Institucional (PEI 2024-2030) y el Plan de Gobierno y Transformación Digital (PGTD 2026-2030) constituyen los instrumentos de gestión que enmarcan el SGSI.

## Valoración de la Madurez Digital Institucional

| Dimensión | Puntaje (1-5) | Interpretación |
|:----------|:--------------|:---------------|
| D1: Estrategia y Organización | 2.175 | Nivel 2 — En desarrollo. CGD formalizado pero sin reuniones periódicas. |
| D2: Habilitadores de Gestión | 1.800 | Nivel 1 — Inicial. Procesos digitalizados de forma aislada, sin integración. |
| D3: Habilitadores Tecnológicos | 1.475 | Nivel 1 — Inicial. Infraestructura con obsolescencia crítica (firewalls, licencias). |
| D4: Servicios al Ciudadano | 1.350 | Nivel 1 — Inicial. Pocos servicios digitales integrales. Sin PIDE. |
| D5: Cultura Digital | 1.175 | Nivel 1 — Inicial. Resistencia al cambio, baja adopción de herramientas digitales. |
| **Índice Global** | **1.569** | **Nivel 1-2: Inicial-Experimental** |
| Meta 2027 | 2.500 | Nivel 2 — En desarrollo |
| Meta 2028 | 3.500 | Nivel 3 — Integrado |

## Inventario de Activos Críticos Identificados

| Activo | Tipo | Riesgo Principal |
|:-------|:-----|:-----------------|
| ERP ADESA (23 módulos) | Software / Base de datos | Integridad y disponibilidad comprometidas. Sin plan de contingencia documentado. |
| Sistema de Tesorería / Recaudación | Software | Fraude financiero. Control de acceso débil. |
| Microsoft 365 (Correo, Teams, SharePoint) | Servicio Cloud | Phishing, fuga de información. Sin DLP implementado. |
| Moodle 4.1 (Campus Virtual) | Software | Interrupción del servicio. Sin redundancia. |
| DSpace / KOHA (Biblioteca) | Software | Pérdida de propiedad intelectual. Disponibilidad limitada. |
| Historias Clínicas (Centro Médico) | Base de datos | Acceso no autorizado a datos sensibles de salud (categoría especial Ley N° 29733). |
| Sistema de Investigación / Tesis | Software / Base de datos | Fuga de propiedad intelectual. Sin respaldo off-site. |
| Huawei Cloud (IaaS/PaaS) | Infraestructura | Dependencia de proveedor único. Sin plan de salida. |

# Matriz de Evaluación de Factores Internos

| Fortaleza o Debilidad | Peso | Calificación | Ponderado |
|:----------------------|:-----|:-------------|:----------|
| **F1:** Comité de Gobierno Digital formalizado (R. N° 1862-R-2023) con representación de todas las sedes. | 0.08 | 4 | 0.32 |
| **F2:** Oficial de Seguridad de la Informacion integrado al CGD por R. N° 2143-R-2023. | 0.07 | 4 | 0.28 |
| **F3:** Infraestructura Cloud Huawei Cloud operativa con IaaS, PaaS, WAF y Anti-DDoS. | 0.10 | 4 | 0.40 |
| **F4:** Equipo de respuesta a emergencias y 13 centros de investigación ambiental. | 0.04 | 3 | 0.12 |
| **F5:** Microsoft 365 implantado con capacidades de seguridad nativas (MFA, Conditional Access). | 0.06 | 3 | 0.18 |
| **D1:** Nivel de madurez digital inicial (1.569/5.0) — lejos de la meta 2028 (3.500). | 0.12 | 1 | 0.12 |
| **D2:** Personal de OTI insuficiente (2 profesionales) para ~11,700 usuarios. | 0.12 | 1 | 0.12 |
| **D3:** Resistencia al cambio cultural en personal docente y administrativo (D5: 1.175). | 0.10 | 2 | 0.20 |
| **D4:** Firewall perimetral obsoleto y 9 firewalls sin licencias vigentes. | 0.12 | 1 | 0.12 |
| **D5:** Ausencia de SIEM, monitoreo centralizado e integración PIDE. | 0.10 | 1 | 0.10 |
| **D6:** Segmentación de red limitada entre facultades y sedes (sin SD-WAN). | 0.09 | 1 | 0.09 |
| **TOTAL** | **1.00** | — | **2.05** |

Interpretación: El puntaje ponderado de 2.05 (por debajo de 2.50) indica una posición interna débil. Las debilidades en madurez digital, capacidad del personal OTI y obsolescencia de infraestructura de seguridad contrarrestan las fortalezas en gobernanza formal y disponibilidad de Cloud.

# Matriz de Evaluación de Factores Externos

| Oportunidad o Amenaza | Peso | Calificación | Ponderado |
|:----------------------|:-----|:-------------|:----------|
| **O1:** Presupuesto asignado al PGTD-01 (SGSI) por S/ 850,000 en 30 meses. | 0.10 | 4 | 0.40 |
| **O2:** Apoyo técnico de la PCM/SGTD para interoperabilidad (Directiva N° 001-2025-PCM/SGTD, PIDE). | 0.08 | 3 | 0.24 |
| **O3:** Marco normativo favorable: D.S. 126-2025-PCM (Marco de Confianza Digital) impulsa la seguridad desde la alta dirección. | 0.07 | 3 | 0.21 |
| **O4:** Meta PEDN al 2050 de transformación digital del país (ON3) — respaldo político al más alto nivel. | 0.05 | 3 | 0.15 |
| **O5:** Alineación con la ecoeficiencia MINAM — posibilidad de cofinanciamiento para Green IT. | 0.04 | 2 | 0.08 |
| **O6:** Network Readiness Index (NRI) meta 63.22 para Perú en 2026 — incentiva la inversión en infraestructura digital. | 0.04 | 2 | 0.08 |
| **A1:** Incremento de ciberataques: Perú registró 96 ataques por minuto en 2021 (3.er país más atacado de Latinoamérica), con crecimiento del 71%. Ransomware dirigido a universidades. | 0.18 | 1 | 0.18 |
| **A2:** Nuevas exigencias legales: D.S. N° 016-2024-JUS incrementa sanciones por brechas de datos personales. D.S. N° 115-2025-PCM exige auditoría de algoritmos de IA. | 0.15 | 2 | 0.30 |
| **A3:** Restricciones presupuestales del sector público: el TI representa solo el 1.2% del presupuesto institucional. La regla fiscal puede contraer el Canon. | 0.12 | 2 | 0.24 |
| **A4:** Fuga de talento digital del sector público al privado — la OTI con 2 personas no es sostenible. | 0.10 | 1 | 0.10 |
| **A5:** Obsolescencia normativa no actualizada: el Plan de Continuidad Operativa 2024 requiere alineación con ISO 27001. | 0.07 | 2 | 0.14 |
| **TOTAL** | **1.00** | — | **2.12** |

Interpretación: El puntaje ponderado de 2.12 indica que la UNCP está respondiendo por debajo del promedio a las amenazas externas. La velocidad del cambio normativo y el crecimiento exponencial de ciberataques superan la capacidad actual de respuesta institucional.

# Estrategia Proactiva

## Matriz CAME

| Estrategia | Acción Concreta | Código de Proyecto | Indicador de Éxito |
|:-----------|:----------------|:-------------------|:-------------------|
| **Corregir** debilidades internas aprovechando oportunidades | Ejecutar PGTD-01 (SGSI) para implementar controles ISO 27001:2022 priorizando: segmentación ZTNA (ZTNA), SIEM, y renovación de firewalls. | PGTD-01 + PGTD-04 | 90% de procesos incorporados al SGSI al 2028. |
| **Afrontar** amenazas externas con fortalezas internas | Utilizar la resiliencia de Huawei Cloud (backups inmutables, WAF, Anti-DDoS) para defenderse de ransomware y ataques DDoS. Implementar MFA obligatorio en Microsoft 365. | PGTD-01 / Control A.8.16 | Tiempo de respuesta a incidentes < 24 horas. |
| **Mantener** fortalezas para consolidar la posición | Fortalecer la gobernanza del Comité de Gobierno Digital con calendario formal de sesiones, auditorías internas trimestrales (P-SGSI-09), actas de seguimiento y reportes al rectorado. | P-SGSI-09 | 4 auditorías internas por año y actas CGTD trazables. |
| **Explotar** oportunidades externas para acelerar la transformación | Aprovechar los lineamientos de la SGTD, el Marco de Confianza Digital (D.S. 126-2025-PCM) y la Directiva PIDE para elevar el nivel de madurez digital de 1.569 a 2.500 al 2027. Integrar servicios con PIDE (RENIEC, SUNEDU). | PGTD-02 + PIDE | Madurez digital 2.500 al 2027. |

## Mapa de Acciones por Horizonte

| Horizonte | Acciones Clave | Meta de Madurez |
|:----------|:---------------|:-----------------|
| **Corto plazo** (2026) | Ratificar vigencia operativa, suplencia y recursos del Oficial de Seguridad de la Informacion integrado por R. N° 2143-R-2023. Iniciar auditoría AS-IS de activos. Renovar licencias de firewall. Implementar MFA obligatorio. Realizar primera campaña de concientización. | 1.800 |
| **Mediano plazo** (2027) | Implementar SIEM y SOC básico. Iniciar segmentación ZTNA. Integrar PIDE (RENIEC, SUNEDU). Certificar al personal OTI en ISO 27001. Alcanzar 50% de procesos en SGSI. | 2.500 |
| **Largo plazo** (2028) | Completar implementación del SGSI con 90% de procesos. Preparar auditoría de certificación ISO 27001:2022. Implementar Gobierno de Datos. Consolidar Centro de Operaciones de Seguridad (SOC). | 3.500 |

# Conclusión: Posicionamiento Estratégico

El análisis integrado de los factores internos y externos revela que la UNCP se encuentra en una **posición estratégica defensiva** con puntajes MEFI (2.05) y MEFE (2.12) por debajo del umbral de 2.50. Esto significa que las debilidades internas y las amenazas externas superan a las fortalezas y oportunidades, respectivamente.

La estrategia prioritaria es **corregir las debilidades internas críticas** (obsolescencia de infraestructura de seguridad, falta de personal OTI, madurez digital incipiente) antes de que las amenazas externas materialicen riesgos con consecuencias graves. El proyecto PGTD-01 (SGSI) constituye el vehículo principal para esta corrección, con un presupuesto de S/ 850,000 y un horizonte de 30 meses.

La ventana de oportunidad es estrecha: el aluvión normativo de 2024-2025 exige acciones inmediatas, y el crecimiento de ciberataques a universidades no se detendrá. Cada mes de retraso en la implementación del SGSI incrementa la exposición a riesgos legales, operativos y reputacionales.
