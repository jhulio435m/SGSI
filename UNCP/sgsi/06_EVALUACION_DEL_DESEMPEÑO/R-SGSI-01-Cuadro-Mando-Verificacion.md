# R-SGSI-01: Cuadro de Mando de Seguridad y Verificación Continua

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0 (Dashboard Dinámico)
**Norma:** ISO/IEC 27001:2022 (Cláusula 9.1)

***

## 1. Monitoreo del Desempeño (KPIs de Seguridad)
La UNCP mide la efectividad del SGSI mediante indicadores en tiempo real integrados en el SIEM.

| Indicador | Meta | Frecuencia | Fuente de Datos |
| :--- | :--- | :--- | :--- |
| **MTTR (Tiempo de Respuesta)** | < 24 horas | Diario | Sistema de Tickets / SIEM |
| **Uptime Servicios Críticos** | > 99.5% | Continuo | Monitoreo Cloud/NMS |
| **Parches Críticos Aplicados** | 100% (< 48h) | Semanal | Gestor de Vulnerabilidades |
| **Cumplimiento de Capacitación** | > 80% anual | Trimestral | Campus Virtual (Moodle) |
| **Intentos de Acceso Fallidos** | Alerta > 10/min | Tiempo Real | Keycloak / WAF |

## 2. Auditoría Interna Ágil
En lugar de una auditoría anual masiva, se realizarán **Micro-Auditorías trimestrales** enfocadas en procesos específicos:
*   **Q1:** Gestión de Accesos y Altas/Bajas.
*   **Q2:** Seguridad en el Desarrollo (ERP ADESA).
*   **Q3:** Resiliencia y Backups (Huawei Cloud).
*   **Q4:** Gestión de Incidentes y Cumplimiento Legal.

## 3. Revisión por la Dirección (Insights)
El Comité de Gobierno Digital recibirá un informe mensual automatizado con los hallazgos de las micro-auditorías y el estado de los riesgos, permitiendo una toma de decisiones basada en hechos recientes, no en reportes pasados.
