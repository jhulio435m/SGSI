# R-SGSI-03: Cuadro de Mando de Seguridad y Verificación Continua

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 2.0 (Dashboard Dinámico)
**Norma:** ISO/IEC 27001:2022 (Cláusula 9.1 — Monitoreo, medición, análisis y evaluación)
**Alineamiento:** P-SGSI-09 (Metodología de Auditoría), R-SGSI-04 (Programa de Auditoría), D-SGSI-05 (SoA)

***

## 1. KPIs de Desempeño del SGSI

La UNCP mide la efectividad del SGSI mediante indicadores clasificados en 4 categorías. La información se consolida en un dashboard (SIEM / Power BI) actualizado en tiempo real.

### 1.1 KPIs de Seguridad Operacional

| # | Indicador | Descripción | Meta | Frecuencia | Fuente de Datos | Disparador de Alerta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| KPI-01 | **MTTR (Tiempo Medio de Respuesta)** | Tiempo desde la detección hasta la contención de incidentes | < 4h (críticos) / < 24h (medios) | Diario | SIEM / Sistema de Tickets | > 4h para críticos |
| KPI-02 | **Uptime Servicios Críticos** | Disponibilidad de ERP ADESA, Campus Virtual, Correo | > 99.5% | Continuo | Monitoreo Cloud / NMS | < 99.0% |
| KPI-03 | **Parches Críticos Aplicados** | % de parches de seguridad críticos aplicados dentro del SLA | 100% (< 48h) | Semanal | Gestor de Vulnerabilidades | Cualquier parche vencido |
| KPI-04 | **Intentos de Acceso Fallidos** | Número de autenticaciones fallidas por minuto | Alerta > 10/min | Tiempo Real | Keycloak / WAF / Azure AD | > 10/min sostenido |
| KPI-05 | **Cobertura Antimalware** | % de endpoints con protección activa y actualizada | > 98% | Diario | Consola EDR / AV Central | < 95% |

### 1.2 KPIs de Gestión de Accesos e Identidades

| # | Indicador | Descripción | Meta | Frecuencia | Fuente de Datos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KPI-06 | **Tiempo de Provisionamiento** | Tiempo entre solicitud de acceso y su habilitación | < 24h | Mensual | ITSM / P-SGSI-03 |
| KPI-07 | **Accesos Privilegiados** | % de accesos administrativos con PAM/JIT activado | 100% | Semanal | PAM / Consola Cloud |
| KPI-08 | **Offboarding Completo** | % de bajas ejecutadas dentro de las 24h del cese | 100% | Mensual | ITSM / RRHH |
| KPI-09 | **MFA en Sistemas Críticos** | % de usuarios en sistemas críticos con MFA habilitado | 100% | Mensual | Azure AD / Keycloak |

### 1.3 KPIs de Capacitación y Concientización

| # | Indicador | Descripción | Meta | Frecuencia | Fuente de Datos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KPI-10 | **Cobertura de Capacitación** | % del personal que completó el curso obligatorio anual | > 95% | Trimestral | Campus Virtual / Moodle |
| KPI-11 | **Tasa de Aprobación** | % de participantes que aprueban la evaluación | > 85% | Trimestral | Campus Virtual / Moodle |
| KPI-12 | **Phishing Simulado** | % de usuarios que fallan en simulación de phishing | < 5% | Trimestral | Plataforma de simulación |

### 1.4 KPIs de Auditoría y Cumplimiento

| # | Indicador | Descripción | Meta | Frecuencia | Fuente de Datos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KPI-13 | **Hallazgos Abiertos** | Cantidad de NC y OM sin cerrar después del plazo | 0 | Mensual | R-SGSI-04 / RACs |
| KPI-14 | **Tiempo de Cierre de NC** | Días promedio para cerrar una no conformidad | < 30 días | Mensual | F-SGSI-04 (RAC) |
| KPI-15 | **Cobertura de Auditoría** | % de procesos del alcance auditados en el ciclo anual | 100% | Anual | R-SGSI-04 |

## 2. Micro-Auditorías Trimestrales (Programa 2026)

En línea con P-SGSI-09 y R-SGSI-04, se ejecutan micro-auditorías focalizadas:

| Período | Enfoque | Controles / Cláusulas | Riesgo |
| :--- | :--- | :--- | :--- |
| **Q1 (Ene–Mar)** | Gestión de Accesos e Identidades | A.5.15, A.5.16, A.5.17, A.5.18, P-SGSI-03 | Crítico |
| **Q2 (Abr–Jun)** | Seguridad en Desarrollo y APIs | A.8.25, A.8.26, A.8.27, POL-SGSI-01 | Alto |
| **Q3 (Jul–Sep)** | Resiliencia, Respaldos y Continuidad | A.8.13, A.5.30, POL-SGSI-03, Huawei Cloud | Crítico |
| **Q4 (Oct–Dic)** | Incidentes, Privacidad y Cumplimiento Legal | A.5.24, Cl. 10, Ley 29733, D.L. 1412 | Alto |

## 3. Revisión por la Dirección (Cl. 9.3)

### 3.1 Reporte Mensual Automatizado
El dashboard genera automáticamente un informe ejecutivo para el Comité de Gobierno Digital que incluye:
- KPIs con semáforo (🟢 / 🟡 / 🔴)
- Top 5 incidentes del mes
- Estado de hallazgos abiertos y RACs
- Tendencia de riesgos (mapa de calor)

### 3.2 Revisión Formal Trimestral
Cada trimestre, el Oficial de Seguridad presenta el informe consolidado al Comité de Gobierno Digital, quien decide sobre:
- Asignación de recursos adicionales
- Aprobación de cambios mayores
- Actualización del apetito de riesgo
- Modificaciones al alcance o la SoA

## 4. Umbrales de Alerta y Escalamiento

| Semáforo | Rango | Acción |
| :--- | :--- | :--- |
| 🟢 **Verde** | Meta cumplida | Monitoreo normal |
| 🟡 **Amarillo** | Desviación < 10% de la meta | Plan de acción preventiva en 15 días |
| 🔴 **Rojo** | Desviación >= 10% de la meta | Acción correctiva inmediata (F-SGSI-04), escalar al CGD |

---
**Última actualización de KPIs:** [Fecha]
**Responsable de actualización:** Oficial de Seguridad y Confianza Digital
