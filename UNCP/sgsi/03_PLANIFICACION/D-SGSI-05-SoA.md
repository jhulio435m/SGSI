---
title: Declaración de Aplicabilidad (Statement of Applicability — SoA)
code: D-SGSI-05
---

# Declaración de Aplicabilidad (Statement of Applicability — SoA)

**Organización:** Universidad Nacional del Centro del Perú (UNCP)  
**Norma:** ISO/IEC 27001:2022 (Cláusula 6.1.3 d)  

***

## 1. Introducción

Este documento define cuáles de los 93 controles de seguridad enumerados en el Anexo A de la norma ISO/IEC 27001:2022 aplican al Sistema de Gestión de Seguridad de la Información (SGSI) de la UNCP, la justificación de su inclusión y su estado actual de implementación.

La Declaración de Aplicabilidad (SoA) es el documento clave que vincula la evaluación de riesgos ([R-SGSI-02](file:///home/blink/Documentos/practicas/SGSI/UNCP/sgsi/03_PLANIFICACION/R-SGSI-02-Matriz-Riesgos.md)) con los controles seleccionados para mitigarlos, demostrando que la implementación del SGSI es completa, metodológicamente correcta y auditable.

## 2. Metodología de Selección

Dada la naturaleza de la UNCP como universidad pública que opera su propio Data Center físico, gestiona filiales desconcentradas, desarrolla software institucional (ERP ADESA), consume servicios críticos en la nube (Huawei Cloud e híbrido Microsoft 365) y trata datos personales sensibles (historias clínicas, matrícula y planillas), **el Comité de Gobierno Digital ha determinado que aplican el 100% (93) de los controles del Anexo A de la norma ISO/IEC 27001:2022**. No se realiza ninguna exclusión, asegurando la máxima robustez en la defensa del SGSI ante auditorías externas de SUNEDU, la Contraloría General de la República (CGR) y certificadoras internacionales.

## 3. Resumen de Aplicabilidad

| Categoría de Controles (ISO/IEC 27001:2022) | Total Controles | Aplican | No Aplican | % Aplicabilidad |
|:-------------------------------------------|:---------------:|:-------:|:----------:|:---------------:|
| 5. Controles Organizacionales              | 37              | 37      | 0          | 100%            |
| 6. Controles de Personas                   | 8               | 8       | 0          | 100%            |
| 7. Controles Físicos                       | 14              | 14      | 0          | 100%            |
| 8. Controles Tecnológicos                  | 34              | 34      | 0          | 100%            |
| **Total**                                  | **93**          | **93**  | **0**      | **100%**        |

---

## 4. Tabla Detallada de Controles (ISO/IEC 27001:2022)

### 4.1 Controles Organizacionales (Anexo A.5)

| Control | Nombre del Control | ¿Aplica? | Justificación de Inclusión | Estado Actual |
|:--------|:-------------------|:--------:|:---------------------------|:--------------|
| A.5.1 | Políticas para la seguridad de la información | Sí | Define el marco normativo interno de la UNCP. | Implementado ([D-SGSI-03](file:///home/blink/Documentos/practicas/SGSI/UNCP/sgsi/02_LIDERAZGO/D-SGSI-03-Politica-General-SGSI.md)) |
| A.5.2 | Roles y responsabilidades en seguridad de la información | Sí | Asigna responsabilidades claras. Comité de Gobierno Digital formalizado (R. N.° 1862-R-2023) y Oficial de Seguridad designado (R. N.° 2143-R-2023). | Parcial (falta RACI nominal y suplencia) |
| A.5.3 | Segregación de tareas | Sí | Previene fraudes y errores en procesos críticos (SIGA/SIAF y OTI). | En proceso |
| A.5.4 | Responsabilidades de la dirección | Sí | Asegura el compromiso y apoyo del Rectorado y la DGA. | Parcial |
| A.5.5 | Contacto con las autoridades | Sí | Permite coordinar incidentes con la SGTD-PCM, CGR, SUNEDU y la APDP. | Planificado |
| A.5.6 | Contacto con grupos de interés | Sí | Intercambio de alertas con el CSIRT Nacional y redes académicas. | En proceso |
| A.5.7 | Inteligencia de amenazas | Sí | Permite recibir, analizar y actuar frente a indicadores de compromiso de ransomware. | Planificado |
| A.5.8 | Seguridad de la información en la gestión de proyectos | Sí | Incorpora la seguridad desde el diseño en los proyectos del PGTD. | En proceso |
| A.5.9 | Inventario de información y otros activos asociados | Sí | Mapea y clasifica el ERP ADESA, bases de datos y hardware. | En proceso ([R-SGSI-01](file:///home/blink/Documentos/practicas/SGSI/UNCP/sgsi/03_PLANIFICACION/R-SGSI-01-Inventario-Activos.md)) |
| A.5.10 | Uso aceptable de la información y otros activos asociados | Sí | Regula el uso de recursos tecnológicos por personal y alumnos. | Planificado |
| A.5.11 | Retorno de activos | Sí | Procedimiento de entrega de equipos al cesar contratos. | Planificado |
| A.5.12 | Clasificación de la información | Sí | Protege los datos sensibles según su criticidad. | Planificado |
| A.5.13 | Etiquetado de la información | Sí | Identifica visual y lógicamente la información confidencial. | Planificado |
| A.5.14 | Transferencia de información | Sí | Asegura el envío de datos a SUNEDU, RENIEC (PIDE) y MINEDU. | En proceso |
| A.5.15 | Control de acceso | Sí | Restringe el acceso de usuarios a sistemas misionales. | En proceso ([P-SGSI-03](file:///home/blink/Documentos/practicas/SGSI/UNCP/sgsi/05_OPERACION/P-SGSI-03-Gestion-Accesos.md)) |
| A.5.16 | Gestión de identidades | Sí | Unifica cuentas a través del Identity Provider (IdP) del PGTD. | Planificado |
| A.5.17 | Información de autenticación | Sí | Establece la robustez de contraseñas y uso de MFA. | Planificado ([POL-SGSI-06](file:///home/blink/Documentos/practicas/SGSI/UNCP/sgsi/09_POLITICAS_Y_PROCEDIMIENTOS/POL-SGSI-06-Contrasenas.md)) |
| A.5.18 | Derechos de acceso | Sí | Controla la asignación, modificación y revocación de permisos. | En proceso |
| A.5.19 | Seguridad de la información en las relaciones con proveedores | Sí | Define requisitos para Huawei Cloud, Microsoft y contratistas. | Planificado |
| A.5.20 | Direccionamiento de la seguridad de la información en los acuerdos con proveedores | Sí | Cláusulas contractuales y SLAs de ciberseguridad. | Planificado |
| A.5.21 | Gestión de la seguridad de la información en la cadena de suministro de TIC | Sí | Evalúa el riesgo de proveedores de desarrollo y hardware. | Planificado |
| A.5.22 | Monitoreo, revisión y gestión de cambios de servicios de proveedores | Sí | Supervisión continua de los servicios cloud e infraestructura externa. | En proceso |
| A.5.23 | Seguridad de la información para el uso de servicios en la nube | Sí | Mitiga riesgos en Huawei Cloud (IaaS/PaaS) y M365 (SaaS). | En proceso |
| A.5.24 | Planificación y preparación para la gestión de incidentes de seguridad de la información | Sí | Planificación del flujo de respuesta a incidentes del CSIRT UNCP. | Planificado |
| A.5.25 | Evaluación y decisión sobre eventos de seguridad de la información | Sí | Clasifica eventos y descarta falsos positivos en el SIEM. | Planificado |
| A.5.26 | Respuesta a incidentes de seguridad de la información | Sí | Ejecución de acciones de mitigación, contención y erradicación. | Planificado |
| A.5.27 | Aprendizaje de los incidentes de seguridad de la información | Sí | Implementación de lecciones aprendidas tras un ataque. | Planificado |
| A.5.28 | Recopilación de evidencia | Sí | Asegura la cadena de custodia para procesos legales o administrativos. | Planificado |
| A.5.29 | Seguridad de la información durante la interrupción | Sí | Mantiene controles mínimos durante incidentes de continuidad. | Planificado |
| A.5.30 | Preparación de las TIC para la continuidad del negocio | Sí | Resiliencia y redundancia tecnológica del Data Center y nube. | Planificado |
| A.5.31 | Requisitos legales, estatutarios, regulatorios y contractuales | Sí | Asegura cumplimiento con Ley N.° 29733 y directivas de la SGTD. | En proceso |
| A.5.32 | Derechos de propiedad intelectual | Sí | Protege el repositorio de tesis DSpace y software propio. | En proceso |
| A.5.33 | Protección de registros | Sí | Protege las actas físicas y digitales del archivo central. | En proceso |
| A.5.34 | Privacidad y protección de información de identificación personal (PII) | Sí | Obligatorio por Ley N.° 29733 de Protección de Datos Personales. | En proceso |
| A.5.35 | Revisión independiente de la seguridad de la información | Sí | Auditorías externas periódicas y revisiones del SGSI. | Planificado |
| A.5.36 | Cumplimiento de políticas y normas para la seguridad de la información | Sí | Asegura que las áreas cumplan las políticas aprobadas. | Planificado |
| A.5.37 | Procedimientos operativos documentados | Sí | Documentación de manuales y procedimientos de la OTI. | En proceso |

### 4.2 Controles de Personas (Anexo A.6)

| Control | Nombre del Control | ¿Aplica? | Justificación de Inclusión | Estado Actual |
|:--------|:-------------------|:--------:|:---------------------------|:--------------|
| A.6.1 | Selección (Investigación de antecedentes) | Sí | Verificación de antecedentes de administradores de TI y RRHH. | En proceso |
| A.6.2 | Términos y condiciones del empleo | Sí | Obligaciones contractuales de seguridad para el personal. | En proceso |
| A.6.3 | Concienciación, educación y capacitación en seguridad de la información | Sí | Mitiga el riesgo de phishing e ingeniería social en usuarios. | Planificado |
| A.6.4 | Proceso disciplinario | Sí | Sanciona el incumplimiento de políticas de seguridad. | En proceso |
| A.6.5 | Responsabilidades después de la terminación o cambio de empleo | Sí | Revocación inmediata de accesos y entrega de activos. | Planificado |
| A.6.6 | Acuerdos de confidencialidad o no divulgación (NDA) | Sí | Firmados por empleados de planta, practicantes y terceros. | En proceso |
| A.6.7 | Trabajo a distancia | Sí | Asegura accesos de docentes y administrativos por teletrabajo. | Planificado |
| A.6.8 | Reporte de eventos de seguridad de la información | Sí | Obligación de reportar incidentes y sospechas para la comunidad. | En proceso |

### 4.3 Controles Físicos (Anexo A.7)

| Control | Nombre del Control | ¿Aplica? | Justificación de Inclusión | Estado Actual |
|:--------|:-------------------|:--------:|:---------------------------|:--------------|
| A.7.1 | Perímetros de seguridad física | Sí | Barreras en el Data Center central de Huancayo y filiales. | En proceso |
| A.7.2 | Controles de ingreso físico | Sí | Biometría y tarjetas de proximidad para el Data Center. | En proceso |
| A.7.3 | Aseguramiento de oficinas, salas e instalaciones | Sí | Protección física de la OTI y oficinas administrativas críticas. | Parcial |
| A.7.4 | Monitoreo de seguridad física | Sí | Sistemas de videovigilancia y alarmas contra intrusos. | En proceso |
| A.7.5 | Protección contra amenazas físicas y ambientales | Sí | Pararrayos, sistemas de extinción de incendios y sismorresistencia. | En proceso |
| A.7.6 | Trabajo en áreas seguras | Sí | Protocolos de ingreso y restricciones de conducta en salas de TI. | En proceso |
| A.7.7 | Escritorio limpio y pantalla limpia | Sí | Evita la exposición visual de información confidencial. | Planificado |
| A.7.8 | Ubicación y protección de equipos | Sí | Ubicación segura de servidores en racks bajo llave y UPS. | En proceso |
| A.7.9 | Seguridad de los activos fuera de las instalaciones | Sí | Control y protección de laptops de la UNCP en teletrabajo. | Planificado |
| A.7.10 | Medios de almacenamiento | Sí | Cifrado y control de soportes (discos, NAS de backup). | En proceso |
| A.7.11 | Servicios de soporte | Sí | Suministro eléctrico estable, climatización y UPS del Data Center. | En proceso |
| A.7.12 | Seguridad del cableado | Sí | Protección física de tendidos de red y fibra óptica. | Implementado |
| A.7.13 | Mantenimiento de equipos | Sí | Plan anual de mantenimiento de hardware de servidores. | En proceso |
| A.7.14 | Eliminación o reutilización segura de equipos | Sí | Borrado seguro (wipe) de discos antes de reasignación o descarte. | Planificado |

### 4.4 Controles Tecnológicos (Anexo A.8)

| Control | Nombre del Control | ¿Aplica? | Justificación de Inclusión | Estado Actual |
|:--------|:-------------------|:--------:|:---------------------------|:--------------|
| A.8.1 | Dispositivos de usuario final | Sí | Hardening de endpoints institucionales y control de BYOD. | En proceso |
| A.8.2 | Derechos de acceso privilegiado | Sí | Restringe y audita credenciales de administración (root/sa). | En proceso |
| A.8.3 | Restricción de acceso a la información | Sí | Control de accesos granular a bases de datos y archivos. | En proceso |
| A.8.4 | Acceso al código fuente | Sí | Protege el repositorio del ERP ADESA de accesos no autorizados. | En proceso |
| A.8.5 | Autenticación segura | Sí | Implementación de MFA obligatorio y contraseñas seguras. | Planificado |
| A.8.6 | Gestión de capacidad | Sí | Evita denegación de servicios por saturación de disco o RAM. | En proceso |
| A.8.7 | Protección contra malware | Sí | Antivirus/EDR en servidores, laptops y filtrado de correo. | Parcial |
| A.8.8 | Gestión de vulnerabilidades técnicas | Sí | Escaneo de vulnerabilidades del ERP, Moodle y servidores. | En proceso |
| A.8.9 | Gestión de configuraciones | Sí | Líneas base de configuración segura de SO y redes. | Planificado |
| A.8.10 | Eliminación de información | Sí | Destrucción lógica y física segura de datos confidenciales. | Planificado |
| A.8.11 | Enmascaramiento de datos | Sí | Uso de datos anonimizados para desarrollo y pruebas. | Planificado |
| A.8.12 | Prevención de fuga de datos | Sí | Implementación de DLP para flujos de datos sensibles. | Planificado |
| A.8.13 | Respaldos de información | Sí | Backups inmutables y automatizados con replicación cloud. | Parcial |
| A.8.14 | Redundancia de las instalaciones de procesamiento de información | Sí | Clusterización y redundancia de servicios de matrícula e identidad. | Planificado |
| A.8.15 | Registro de eventos (Logs) | Sí | Generación y almacenamiento seguro de trazas de auditoría. | En proceso |
| A.8.16 | Actividades de monitoreo | Sí | Correlación de logs en el SIEM y detección de ataques. | Planificado |
| A.8.17 | Sincronización de relojes | Sí | Sincronización NTP unificada para asegurar validez de logs. | Implementado |
| A.8.18 | Uso de programas utilitarios privilegiados | Sí | Restricción de herramientas administrativas en servidores. | Planificado |
| A.8.19 | Instalación de software en sistemas operativos en producción | Sí | Prohíbe la instalación de software no autorizado en producción. | Planificado |
| A.8.20 | Seguridad de redes | Sí | Firewalls, segmentación, e implementación de Zero Trust. | En proceso |
| A.8.21 | Seguridad de los servicios de red | Sí | Cifrado HTTPS/TLS y VPN robusta para acceso remoto. | En proceso |
| A.8.22 | Segregación de redes | Sí | Aislamiento lógico de redes administrativa, académica y de invitados. | En proceso |
| A.8.23 | Filtrado web | Sí | Restricción de acceso a sitios maliciosos desde el campus. | Planificado |
| A.8.24 | Uso de criptografía | Sí | Cifrado de bases de datos críticas y canales de APIs. | En proceso |
| A.8.25 | Ciclo de vida de desarrollo seguro | Sí | Metodología de desarrollo seguro para el ERP ADESA. | Planificado |
| A.8.26 | Requisitos de seguridad de las aplicaciones | Sí | Especificación de requisitos en desarrollo propio y compras. | Planificado |
| A.8.27 | Arquitectura de sistemas seguros y principios de ingeniería | Sí | Diseño seguro de servidores físicos y despliegues en Huawei Cloud. | Planificado |
| A.8.28 | Codificación segura | Sí | Uso de frameworks y OWASP Top 10 para evitar inyección SQL. | En proceso |
| A.8.29 | Pruebas de seguridad en el desarrollo y aceptación | Sí | Pruebas de penetración y escaneo antes de paso a producción. | Planificado |
| A.8.30 | Desarrollo subcontratado | Sí | Supervisión y estándares de seguridad para software de terceros. | Planificado |
| A.8.31 | Separación de entornos de desarrollo, prueba y producción | Sí | Evita pruebas con datos reales en el entorno de producción. | Planificado |
| A.8.32 | Seguridad de la información durante las pruebas | Sí | Uso de datos simulados y protección del entorno de testing. | Planificado |
| A.8.33 | Pruebas de seguridad de sistemas durante las auditorías | Sí | Auditoría técnica de sistemas sin interrumpir la operación. | Planificado |
| A.8.34 | Protección de las herramientas de auditoría de sistemas de información | Sí | Restringe el acceso a escáneres de vulnerabilidades y herramientas de red. | Planificado |

---

## 5. Estado General de Implementación

| Estado | Controles | Porcentaje |
|:-------|:---------:|:----------:|
| Implementado | 3 | 3.2% |
| Implementado parcialmente | 5 | 5.4% |
| En proceso | 32 | 34.4% |
| Planificado | 53 | 57.0% |
| **Total aplicables** | **93** | **100%** |

El estado de implementación refleja la línea base actual (AS-IS). El proyecto PGTD-01 (SGSI) tiene como objetivo alcanzar al menos el 80% de controles implementados o en proceso en un plazo de 18 meses, con el soporte del equipo ampliado de la OTI.

## 6. Aprobación y Vigencia

La presente Declaración de Aplicabilidad (SoA) ha sido revisada y aprobada por el Comité de Gobierno Digital de la UNCP. Tiene vigencia anual a partir de su aprobación y será actualizada ante cambios significativos en el mapa de riesgos o la infraestructura tecnológica.

\
\___________________________  
**Mg. Rocío Rosanna Damián Alvarado**  
Oficial de Seguridad de la Información (R. N.° 2143-R-2023)  
Jefa de la Oficina de Tecnologías de la Información  

\
\___________________________  
**Director(a) General de Administración**  
Líder de Gobierno y Transformación Digital  
UNCP  
