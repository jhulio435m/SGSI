# P-SGSI-05: Procedimiento de Gestión de Cambios en TI

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0 (Enfoque Ágil)
**Norma:** ISO/IEC 27001:2022 (Control A.8.32)

***

## 1. Objetivo
Asegurar que los cambios en los sistemas de información e infraestructura de la UNCP se realicen de forma controlada, minimizando el impacto en la disponibilidad y seguridad.

## 2. Tipos de Cambio
1.  **Cambio Estándar:** Cambios de bajo riesgo, rutinarios y pre-aprobados (ej. parches de seguridad mensuales).
2.  **Cambio Normal:** Requiere evaluación por el Comité de Cambios (CAB) o el Jefe de la OTI (ej. actualización de versión del ERP ADESA).
3.  **Cambio de Emergencia:** Requiere implementación inmediata ante un incidente crítico (ej. caída de base de datos).

## 3. Flujo del Cambio
1.  **Solicitud:** Se registra el requerimiento en el sistema de tickets.
2.  **Evaluación de Impacto:** Se analiza el riesgo, los recursos necesarios y el plan de retroceso (rollback).
3.  **Aprobación:** Según el tipo de cambio.
4.  **Implementación:** Se realiza en el horario de menor impacto (ventana de mantenimiento).
5.  **Pruebas de Aceptación:** Se valida que el cambio no afectó la seguridad ni la funcionalidad.
6.  **Cierre y Registro:** Documentación del resultado.

***
# P-SGSI-07: Procedimiento de Gestión de Seguridad con Proveedores

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0
**Norma:** ISO/IEC 27001:2022 (Controles A.5.19 - A.5.23)

***

## 1. Alcance
Aplica a todos los proveedores con acceso a información o infraestructura de la UNCP (ej. Huawei Cloud, ISPs, soporte de software).

## 2. Requisitos de Seguridad
*   **Contratos:** Deben incluir cláusulas de confidencialidad y cumplimiento del SGSI.
*   **SLA de Seguridad:** Se deben definir tiempos de respuesta ante incidentes detectados en la plataforma del proveedor.
*   **Derecho a Auditoría:** La UNCP se reserva el derecho de solicitar reportes de seguridad (SOC2 u otros) al proveedor.

## 3. Monitoreo y Revisión
*   Revisión anual del desempeño de seguridad del proveedor.
*   Cierre de accesos inmediato al finalizar la vigencia del contrato.
