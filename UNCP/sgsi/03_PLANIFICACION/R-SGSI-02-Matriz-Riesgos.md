# R-SGSI-02: Matriz de Evaluación y Plan de Tratamiento de Riesgos

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0 (Plantilla Operativa)
**Metodología:** D-SGSI-04 (O x I)

***

## 1. Evaluación de Riesgos (Muestra)

| ID | Activo | Amenaza | Vulnerabilidad | O | I | NR | Nivel | Tratamiento |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R01 | ERP ADESA (BD) | Inyección SQL | Código no auditado | 2 | 4 | 8 | **Medio** | Mitigar |
| R02 | Campus Virtual | Ransomware | Falta de backups inmutables | 2 | 4 | 8 | **Medio** | Mitigar |
| R03 | Centro Médico (HC) | Acceso no autorizado | Falta de MFA | 3 | 4 | 12 | **Alto** | Mitigar |
| R04 | Red de Facultades | Sniffing | Tráfico no cifrado | 3 | 3 | 9 | **Alto** | Mitigar |

## 2. Plan de Tratamiento de Riesgos (Acciones)

| ID Riesgo | Control ISO 27001 Seleccionado | Acción de Tratamiento | Responsable | Fecha Límite | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R01** | A.8.25 (Desarrollo Seguro) | Implementar SAST en el pipeline de desarrollo. | OTI (Desarrollo) | Q2-2026 | Pendiente |
| **R02** | A.8.13 (Copias de Seguridad) | Activar Cloud Backup inmutable en Huawei Cloud. | OTI (Sistemas) | Q1-2026 | En Proceso |
| **R03** | A.5.15 (Acceso) | Implementar MFA vía Keycloak para acceso a HC. | OTI (Seguridad) | Q1-2026 | Pendiente |
| **R04** | A.8.20 (Seguridad Redes) | Desplegar microsegmentación ZTNA y 802.1X. | OTI (Redes) | Q2-2026 | Pendiente |

***
**Nota:** El Nivel de Riesgo (NR) = Ocurrencia (O) x Impacto (I). NR >= 5 requiere tratamiento.
