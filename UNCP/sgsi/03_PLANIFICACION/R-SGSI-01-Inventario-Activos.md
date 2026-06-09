---
title: Inventario de Activos de Información
code: R-SGSI-01
---

# Inventario de Activos de Información — UNCP

## Instrucciones

1. El responsable de cada unidad organizacional debe completar una fila por activo de información bajo su custodia.
2. Los niveles de clasificación (Confidencialidad, Integridad, Disponibilidad) se asignan según la tabla de criterios de la Sección 2.
3. El inventario consolidado debe entregarse a la Oficina de Tecnologías de la Información (OTI) para su registro y validación.
4. Actualizar semestralmente o ante cambios significativos (altas, bajas, modificaciones de activos).
5. Utilizar la codificación estándar: `[TIPO]-[###]` (ej. HW-001, SW-015, DT-042).

***

## Registro Maestro de Activos

### Datos Generales del Activo

| # | ID | Nombre | Descripción | Tipo | Propietario | Custodio |
|--:|:----|:-------|:------------|:----|:------------|:---------|
| 1 | HW-001 | Servidor ADESA | Servidor principal del sistema de gestión documental y administrativa | Hardware | OTI | OTI |
| 2 | HW-002 | Servidor Moodle | Servidor de la plataforma educativa virtual (Campus Virtual) | Hardware | OTI | OTI |
| 3 | HW-003 | Firewall Perimetral | Dispositivo de seguridad de red (Fortinet) | Hardware | OTI | OTI |
| 4 | HW-004 | Switch Core | Switch de capa 3 para la red LAN central | Hardware | OTI | OTI |
| 5 | HW-005 | Storage NAS | Almacenamiento centralizado de respaldos (4TB) | Hardware | OTI | OTI |
| 6 | SW-001 | Sistema GESDOC | Sistema de trámite documentario y mesa de partes | Software | OTI | OTI |
| 7 | SW-002 | ERP ADESA | Sistema de gestión administrativa, financiera y académica | Software | OTI | OTI |
| 8 | SW-003 | Microsoft 365 | Suite de ofimática, correo institucional y colaboración | Software | OTI | OTI |
| 9 | SW-004 | Moodle 4.1 | Plataforma de aprendizaje virtual (Campus Virtual) | Software | Académico | OTI |
| 10 | SW-005 | SIGA/SIAF | Sistema de gestión de recursos humanos y planillas | Software | RRHH | OTI |
| 11 | SW-006 | DSpace | Repositorio institucional de publicaciones y tesis | Software | Investigación | OTI |
| 12 | DT-001 | BD Matrícula | Base de datos de estudiantes matriculados (≈11,700 registros) | Dato | Académico | OTI |
| 13 | DT-002 | BD Notas | Base de datos de calificaciones y actas académicas | Dato | Académico | OTI |
| 14 | DT-003 | BD RRHH | Base de datos de personal docente y administrativo (≈1,700 registros) | Dato | RRHH | OTI |
| 15 | DT-004 | BD Grados | Base de datos de grados y títulos emitidos | Dato | Grados | OTI |
| 16 | DT-005 | Repositorio Tesis | Archivo digital de tesis y trabajos de investigación | Dato | Investigación | OTI |
| 17 | RD-001 | Red LAN | Red cableada del campus central (10.0.0.0/16) | Red | OTI | OTI |
| 18 | RD-002 | Red WiFi | Red inalámbrica institucional (estudiantes, docentes, invitados) | Red | OTI | OTI |
| 19 | RD-003 | VPN Corporativa | Acceso remoto seguro para personal administrativo | Red | OTI | OTI |
| 20 | PE-001 | Personal OTI | Equipo de administración de sistemas, redes y seguridad (11 profesionales + practicantes) | Persona | OTI | RRHH |
| 21 | PE-002 | Oficial de Seguridad | Responsable del SGSI y la confianza digital | Persona | CGD | RRHH |
| 22 | SV-001 | Huawei Cloud | Infraestructura cloud para servicios críticos (IaaS) | Servicio | OTI | Huawei |
| 23 | SV-002 | Internet Dedicado | Enlace de internet principal (fibra óptica) | Servicio | OTI | Proveedor |
| 24 | SV-003 | Energía Eléctrica UPS | Sistema de alimentación ininterrumpida del data center | Servicio | OTI | Proveedor |

### Ubicación y Soporte

| ID | Ubicación Física | Ubicación Lógica | Soporte | Usuarios |
|:---|:-----------------|:------------------|:--------|:---------|
| HW-001 | Data Center — Pabellón Central | 192.168.10.10:8080 | Servidor físico | Administrativos, OTI |
| HW-002 | Data Center — Pabellón Central | 192.168.10.20:443 | Servidor físico | Estudiantes, docentes |
| HW-003 | Data Center — Rack Seguridad | 10.0.0.1 | Aparato de red | OTI |
| HW-004 | Data Center — Rack Principal | N/A (Capa 2/3) | Aparato de red | OTI |
| HW-005 | Data Center — Rack Storage | 192.168.10.30 | Storage NAS | OTI |
| SW-001 | Servidor ADESA | gesdoc.uncp.edu.pe | Aplicación web | Comunidad UNCP |
| SW-002 | Servidor ADESA | erp.uncp.edu.pe | Aplicación web | Administrativos |
| SW-003 | Microsoft Cloud (Azure) | outlook.office.com / uncp.edu.sharepoint.com | SaaS | Comunidad UNCP |
| SW-004 | Servidor Moodle | campus.uncp.edu.pe | Aplicación web | Estudiantes, docentes |
| SW-005 | Servidor SIGA | siga.uncp.edu.pe | Aplicación web | RRHH, Administrativos |
| SW-006 | Servidor DSpace | repositorio.uncp.edu.pe | Aplicación web | Investigadores, público |
| DT-001 | Servidor BD | db.uncp.edu.pe:3306 | Base de datos | Académica, OTI |
| DT-002 | Servidor BD | db.uncp.edu.pe:3307 | Base de datos | Académica, OTI |
| DT-003 | Servidor BD | db.uncp.edu.pe:3308 | Base de datos | RRHH, OTI |
| DT-004 | Servidor BD | db.uncp.edu.pe:3309 | Base de datos | Grados, OTI |
| DT-005 | Servidor DSpace | repositorio.uncp.edu.pe/files | Sistema de archivos | Investigación, OTI |
| RD-001 | Campus Central | 10.0.0.0/16 | Físico — Red | Sede Central |
| RD-002 | Campus Central y sedes | 10.1.0.0/16 | Inalámbrico | Comunidad UNCP |
| RD-003 | Acceso remoto | vpn.uncp.edu.pe | VPN SSL | Personal autorizado |
| PE-001 | Oficina OTI — Pabellón Central | N/A | Humano | N/A |
| PE-002 | Oficina DGA — Pabellón Central | N/A | Humano | N/A |
| SV-001 | Cloud (Lima, Perú) | console.huaweicloud.com | IaaS | OTI |
| SV-002 | CPD principal | N/A | Enlace físico | Comunidad UNCP |
| SV-003 | Data Center | N/A | Infraestructura | OTI |

## Clasificación de Seguridad (CID)

### Criterios de Clasificación

| Nivel | Confidencialidad | Integridad | Disponibilidad |
|:-----:|:-----------------|:-----------|:---------------|
| 3 (Alta) | Información sujeta a Ley N.° 29733 (datos personales, salud) o secreto institucional | Alteración no autorizada causaría impacto severo a la misión institucional | Servicio crítico sin alternativas; indisponibilidad > 4 hrs inaceptable |
| 2 (Media) | Información de uso interno no pública | Alteración causaría impacto moderado en procesos | Servicio importante con alternativas parciales |
| 1 (Baja) | Información pública o de divulgación autorizada | Alteración sin impacto significativo | Servicio no crítico; puede interrumpirse sin consecuencias mayores |

### Clasificación por Activo

| ID Activo | Confidencialidad | Integridad | Disponibilidad | Criticidad General | Fecha de Registro |
|:----------|:----------------:|:----------:|:--------------:|:------------------:|:-----------------:|
| HW-001 | 2 (Interno) | 3 (Alta) | 3 (Alta) | Alta | 2026-06-03 |
| HW-002 | 2 (Interno) | 3 (Alta) | 3 (Alta) | Alta | 2026-06-03 |
| HW-003 | 2 (Interno) | 2 (Media) | 3 (Alta) | Alta | 2026-06-03 |
| HW-004 | 1 (Público) | 2 (Media) | 3 (Alta) | Alta | 2026-06-03 |
| HW-005 | 2 (Interno) | 3 (Alta) | 2 (Media) | Alta | 2026-06-03 |
| SW-001 | 2 (Interno) | 3 (Alta) | 2 (Media) | Alta | 2026-06-03 |
| SW-002 | 3 (Confidencial) | 3 (Alta) | 3 (Alta) | Crítico | 2026-06-03 |
| SW-003 | 2 (Interno) | 2 (Media) | 2 (Media) | Medio | 2026-06-03 |
| SW-004 | 2 (Interno) | 2 (Media) | 3 (Alta) | Alta | 2026-06-03 |
| SW-005 | 3 (Confidencial) | 3 (Alta) | 2 (Media) | Crítico | 2026-06-03 |
| SW-006 | 2 (Interno) | 2 (Media) | 2 (Media) | Medio | 2026-06-03 |
| DT-001 | 3 (Confidencial) | 3 (Alta) | 3 (Alta) | Crítico | 2026-06-03 |
| DT-002 | 3 (Confidencial) | 3 (Alta) | 2 (Media) | Crítico | 2026-06-03 |
| DT-003 | 3 (Confidencial) | 3 (Alta) | 2 (Media) | Crítico | 2026-06-03 |
| DT-004 | 3 (Confidencial) | 3 (Alta) | 2 (Media) | Crítico | 2026-06-03 |
| DT-005 | 2 (Interno) | 3 (Alta) | 2 (Media) | Alta | 2026-06-03 |
| RD-001 | 1 (Público) | 2 (Media) | 3 (Alta) | Alta | 2026-06-03 |
| RD-002 | 1 (Público) | 2 (Media) | 2 (Media) | Medio | 2026-06-03 |
| RD-003 | 3 (Confidencial) | 2 (Media) | 2 (Media) | Alta | 2026-06-03 |
| PE-001 | 2 (Interno) | 2 (Media) | 2 (Media) | Medio | 2026-06-03 |
| PE-002 | 2 (Interno) | 2 (Media) | 1 (Baja) | Medio | 2026-06-03 |
| SV-001 | 2 (Interno) | 2 (Media) | 3 (Alta) | Alta | 2026-06-03 |
| SV-002 | 1 (Público) | 1 (Baja) | 3 (Alta) | Alta | 2026-06-03 |
| SV-003 | 1 (Público) | 1 (Baja) | 3 (Alta) | Alta | 2026-06-03 |

## Controles Asociados (ISO 27001:2022)

| ID Activo | Controles Aplicables | Estado | Observaciones |
|:----------|:---------------------|:-------|:--------------|
| HW-001 | A.7.9, A.7.10, A.7.13, A.8.1 | Pendiente | Requiere control de acceso biométrico |
| HW-002 | A.7.9, A.7.10, A.7.13, A.8.1 | Pendiente | Misma sala de servidores que ADESA |
| HW-003 | A.8.20, A.8.22, A.8.33 | Implementado | Firewall Fortinet con reglas activas |
| HW-004 | A.8.20, A.8.22, A.8.33 | Implementado | VLANs configuradas |
| HW-005 | A.7.10, A.8.13 | Implementado | Backup diario automatizado |
| SW-001 | A.5.23, A.5.37, A.8.8, A.8.20 | Pendiente | Versión antigua, requiere actualización |
| SW-002 | A.5.23, A.5.37, A.8.8, A.8.15, A.8.24 | Pendiente | Requiere actualización y hardening |
| SW-003 | A.5.19, A.5.20, A.8.29, A.8.30 | Implementado | Cumplimiento Microsoft 365 |
| SW-004 | A.5.23, A.8.8, A.8.15, A.8.24 | Pendiente | SSL vigente, requiere actualización de plugins |
| SW-005 | A.5.15, A.8.2, A.8.3, A.8.24 | Pendiente | Acceso privilegiado no auditado |
| SW-006 | A.8.8, A.8.15, A.8.24 | Pendiente | SSL vigente |
| DT-001 | A.5.13, A.5.33, A.8.3, A.8.11, A.8.24 | Pendiente | Datos sensibles sin cifrado en reposo |
| DT-002 | A.5.13, A.5.33, A.8.3, A.8.11 | Pendiente | Datos críticos de estudiantes |
| DT-003 | A.5.13, A.5.33, A.8.3, A.8.11 | Pendiente | Datos personales con protección parcial |
| DT-004 | A.5.13, A.5.33, A.8.3, A.8.11 | Pendiente | Datos de egresados, reporte SUNEDU |
| DT-005 | A.5.32, A.5.33, A.8.3 | Pendiente | Control de acceso básico |
| RD-001 | A.8.20, A.8.22, A.8.33 | Implementado | Segmentación VLAN activa |
| RD-002 | A.8.20, A.8.22, A.8.33 | Implementado | Red invitados separada |
| RD-003 | A.8.5, A.8.20 | Implementado | VPN SSL con MFA planificado |
| PE-001 | A.6.1, A.6.3, A.6.5 | Pendiente | Capacitación en seguridad requerida |
| PE-002 | A.5.2, A.6.3 | Implementado | Rol designado formalmente |
| SV-001 | A.5.19, A.5.20, A.8.29 | En proceso | Contrato con cláusulas de seguridad |
| SV-002 | A.7.11, A.8.20 | Implementado | Enlace redundante |
| SV-003 | A.7.11 | Implementado | UPS con autonomía de 2 horas |

## Formulario de Auditoría por Unidad

### Identificación de la Unidad

| Campo | Información |
|:------|:------------|
| Unidad Organizacional | Oficina de Tecnologías de la Información (OTI) — Dependiente de la Dirección General de Administración (DGA) |
| Responsable del Inventario | Jefe de la Oficina de Tecnologías de la Información |
| Fecha de Registro | 03 de junio de 2026 |
| Sede / Campus | Ciudad Universitaria — Av. Mariscal Castilla N.° 3909, El Tambo, Huancayo |
| Teléfono / Anexo | (064) 481060 / Anexo 1234 |
| Correo Electrónico | oti@uncp.edu.pe |

### Detalle del Activo (completar por cada activo)

| Atributo | Registro (Ejemplo: Servidor ADESA — HW-001) |
|:---------|:---------------------------------------------|
| ID Activo | HW-001 |
| Nombre del Activo | Servidor ADESA (HP ProLiant DL380 Gen10) |
| Descripción | Servidor principal que aloja el sistema de gestión documental (GESDOC), el ERP ADESA y las bases de datos administrativas de la UNCP. Procesa las transacciones diarias de matrícula, planillas, contabilidad y trámite documentario. |
| Tipo | [X] Hardware [ ] Software [ ] Dato [ ] Red [ ] Persona [ ] Servicio |
| Ubicación Física | Data Center — Pabellón Central, Ciudad Universitaria, Av. Mariscal Castilla N.° 3909, El Tambo, Huancayo (Rack #01, posición 12U) |
| Ubicación Lógica | Dirección IP: 192.168.10.10 — Puerto 8080 (interfaz web) / 3306 (MySQL) / 1433 (MSSQL) — VLAN Servidores (VLAN 10) — Segmento: 192.168.10.0/24 |
| Propietario | Oficina de Tecnologías de la Información (OTI) — Jefatura OTI |
| Custodio | Administrador de Servidores — OTI (Responsable: Ing. Juan Pérez López) |
| Usuarios Autorizados | Administrativos (≈300 usuarios): Dirección General de Administración, Secretaría General, Facultades, Unidad de Grados y Títulos |
| Confidencialidad | [ ] 3 — Alta [X] 2 — Media [ ] 1 — Baja |
| Integridad | [X] 3 — Alta [ ] 2 — Media [ ] 1 — Baja |
| Disponibilidad | [X] 3 — Alta [ ] 2 — Media [ ] 1 — Baja |
| Controles Aplicables | A.7.9 (Equipo desatendido), A.7.10 (Pérdida de equipos), A.7.13 (Mantenimiento), A.8.1 (Dispositivos de usuario final), A.8.2 (Accesos privilegiados), A.8.8 (Vulnerabilidades), A.8.13 (Backup), A.8.15 (Registro de eventos) |
| Observaciones | Servidor con 5 años de antigüedad. Próximo a renovación según PGTD-04 (Modernización Data Center). Backup diario a Storage NAS (4TB) y replicación semanal a Huawei Cloud. Sin control de acceso biométrico en rack. Se recomienda implementar monitoreo de temperatura y humedad. |

***

*Este documento es propiedad de la Universidad Nacional del Centro del Perú. Su reproducción o distribución no autorizada está prohibida.*