# Plantilla: Plan de Auditoría Interna del SGSI

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Referencia:** ISO/IEC 27001:2022 (Cláusula 9.2) / P-SGSI-09 (Metodología de Auditoría Basada en Riesgos)
**ID de Auditoría:** AUD-[Año]-[Nro]
**Tipo de Auditoría:** [ ] Interna [ ] Externa [ ] Pre-certificación [ ] Certificación
**Nivel de Riesgo de la Auditoría:** [ ] Alto [ ] Medio [ ] Bajo

***

## 1. Objetivos de la Auditoría
*   Verificar el cumplimiento del SGSI con los requisitos de la norma ISO/IEC 27001:2022.
*   Evaluar la eficacia y madurez de los controles implementados según la Declaración de Aplicabilidad (SoA).
*   Identificar no conformidades, observaciones y oportunidades de mejora.
*   Determinar la capacidad del SGSI para prepararse para la certificación (cuando aplique).
*   Verificar la implementación de acciones correctivas de auditorías previas.

## 2. Alcance de la Auditoría

### 2.1 Procesos y Unidades a Auditar
[Definir si es una auditoría total o parcial. Ejemplo: Todos los procesos del SGSI en la sede central de la UNCP, incluyendo los procesos misionales de Admisión, Matrícula, Grados y Títulos, y los procesos de soporte de la OTI y DGA].

### 2.2 Exclusiones (si aplica)
[Listar procesos, áreas o ubicaciones excluidas y justificar].

### 2.3 Período Cubierto
[Ejemplo: Desde la última auditoría interna (DD/MM/AAAA) hasta la fecha actual].

## 3. Criterios de Auditoría
*   Norma ISO/IEC 27001:2022 (Cláusulas 4–10).
*   Controles del Anexo A según la Declaración de Aplicabilidad (D-SGSI-05).
*   Políticas y procedimientos internos del SGSI-UNCP.
*   Ley N° 29733 (Protección de Datos Personales) y su reglamento D.S. 016-2024-JUS.
*   Decreto Legislativo N° 1412 (Gobierno Digital) y normas complementarias.
*   Norma NIST SP 800-63B (Autenticación) y NIST SP 800-88 (Eliminación segura) — según aplique.

## 4. Metodología de Auditoría (según P-SGSI-09)

### 4.1 Técnicas de Recolección
| Técnica | Aplica en |
| :--- | :--- |
| [ ] Entrevistas | [Detallar áreas] |
| [ ] Revisión documental | [Detallar documentos] |
| [ ] Observación directa | [Detallar procesos] |
| [ ] Análisis técnico | [Detallar sistemas] |
| [ ] Muestreo estadístico | [Detallar población] |
| [ ] Recorrido (Walkthrough) | [Detallar procesos] |
| [ ] Simulación/Prueba | [Detallar controles] |

### 4.2 Tamaño de Muestra
| Población | Tamaño | Método de Muestreo |
| :--- | :--- | :--- |
| [Ej: Solicitudes de acceso] | [Ej: 25] | [Ej: Aleatorio estratificado] |
| [Ej: Incidentes reportados] | [Ej: 10] | [Ej: Por juicio (críticos)] |

## 5. Equipo Auditor
| Rol | Nombre | Certificaciones |
| :--- | :--- | :--- |
| **Auditor Líder** | [Nombre] | [Ej: ISO 27001 LA, CISA] |
| **Auditor Técnico** | [Nombre] | [Ej: CISSP, CEH] |
| **Auditor de Soporte** | [Nombre] | [Ej: ISO 27001 IA] |
| **Observadores/Expertos** | [Nombre] | [Ej: Especialista en Cloud] |

## 6. Cronograma de Actividades (Agenda)

| Día | Hora | Proceso / Área | Cláusulas / Controles | Auditado (Responsable) | Auditor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Día 1 | 08:30 - 09:00 | Reunión de Apertura | — | Comité de Gobierno Digital | Equipo |
| Día 1 | 09:00 - 11:00 | Contexto y Liderazgo | Cl. 4, 5 | Rectorado / DGA | Líder |
| Día 1 | 11:00 - 13:00 | Planificación y Riesgos | Cl. 6, D-SGSI-04, R-SGSI-02 | Oficial de Seguridad | Líder |
| Día 1 | 14:00 - 16:00 | Soporte y Operaciones | Cl. 7, P-SGSI-03, P-SGSI-04, P-SGSI-06, P-SGSI-07 | OTI | Técnico |
| Día 1 | 16:00 - 17:00 | Evaluación y Mejora | Cl. 9, 10, P-SGSI-09, R-SGSI-03 | Oficial de Seguridad | Líder |
| Día 1 | 17:00 - 17:30 | Reunión de Cierre (Día 1) | — | Comité | Equipo |
| Día 2 | 08:30 - 12:00 | Controles Técnicos (Anexo A) | A.5.15, A.5.16, A.5.17, A.5.24, A.8.25, A.8.26 | OTI (Infraestructura/Desarrollo) | Técnico |
| Día 2 | 12:00 - 13:00 | Seguridad Física | A.7.1–A.7.14, POL-SGSI-07 | OTI / DGA | Técnico |
| Día 2 | 14:00 - 15:00 | Proveedores y Terceros | A.5.19–A.5.23, POL-SGSI-04, P-SGSI-06 | DGA / Logística | Líder |
| Día 2 | 15:00 - 16:00 | Revisión de Hallazgos (Equipo Auditor) | — | N/A | Equipo |
| Día 2 | 16:00 - 17:00 | Reunión de Cierre y Presentación de Hallazgos | — | Comité de Gobierno Digital | Equipo |

## 7. Recursos Necesarios
*   Acceso a la documentación del SGSI (carpeta compartida o repositorio documental).
*   Acceso a evidencias técnicas (logs de firewall, consola Huawei Cloud, Active Directory, listas de acceso).
*   Sala de reuniones o plataforma de videoconferencia.
*   Equipo de cómputo portátil (uno por auditor).
*   Acceso a las instalaciones físicas (Datacenter, oficinas administrativas).

## 8. Confidencialidad e Independencia
Los miembros del equipo auditor declaran su independencia respecto a las áreas auditadas y se comprometen a mantener la confidencialidad de la información obtenida durante el proceso.

***
**Elaborado por:**
[Nombre del Auditor Líder]

**Aprobado por:**
[Nombre y Firma del Oficial de Seguridad / Comité]

**Fecha de Aprobación:**
[Fecha]
