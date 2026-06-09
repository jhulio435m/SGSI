---
title: Plantilla de Acta de Revisión del SGSI por la Dirección
code: R-SGSI-06
---

# Plantilla de Acta de Revisión del SGSI por la Dirección

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Referencia:** ISO/IEC 27001:2022 (Cláusula 9.3)
**ID de Revisión:** REV-SGSI-2026-001
**Fecha:** 31/07/2026
**Lugar:** Sala de Consejo Universitario -- Piso 2
**Convocante:** Rectorado (Presidente del Comité de Gobierno Digital)
**Participantes:** Comité de Gobierno Digital (Rector, DGA, OTI, Oficial de Seguridad y Confianza Digital, Asesoría Jurídica, RRHH, Jefe de Planeamiento)

***

## Entradas de la Revisión (Cl. 9.3.2)

De acuerdo con la Cláusula 9.3 de ISO 27001:2022, se revisan los siguientes puntos:

| # | Punto a Revisar | Documento / Referencia | Resumen del Análisis |
|:---|:---|:---|:---|
| 1 | Estado de acciones de revisiones anteriores | No aplica (primera revisión) | -- |
| 2 | Cambios en cuestiones externas e internas | D-SGSI-01 (Contexto Estratégico), D-SGSI-02 (Alcance) | No se identificaron cambios significativos en el contexto desde la implementación inicial. Se mantienen los factores PESTEL y partes interesadas definidos. |
| 3 | Retroalimentación del desempeño del SGSI | R-SGSI-03 (Cuadro de Mando KPIs), P-SGSI-02 (Incidentes) | KPIs en proceso de consolidación; 3 incidentes gestionados en 2026 (1 phishing, 1 caída de servicio, 1 fuga de datos menor). Tiempo medio de respuesta: 3.2 horas. |
| 4 | Resultados de auditorías internas | AUD-2026-001, P-SGSI-09 | Primera auditoría interna completada (mayo 2026): 11 hallazgos (2 NC mayores, 4 NC menores, 2 fortalezas, 3 OM). Dictamen: Favorable con observaciones. |
| 5 | Cumplimiento de objetivos de seguridad | D-SGSI-05 (SoA), D-SGSI-03 (Política General) | 5 objetivos definidos; 2 en cumplimiento (concienciación, controles SoA), 3 en progreso (madurez 1.569/5.0, riesgos residuales, monitoreo continuo). |
| 6 | Resultados de la evaluación de riesgos | R-SGSI-02 (Matriz de Riesgos) | 15 riesgos evaluados; 5 altos con planes de tratamiento en ejecución; 10 medios monitoreados. Riesgo residual aceptable dentro del apetito definido. |
| 7 | Oportunidades de mejora continua | F-SGSI-04 (RAC), Propuestas del Comité | 3 OM identificadas en auditoría: cifrado de BD, propiedad intelectual en contratos, sensores de inundación. |

## Información Clave Presentada

### KPIs y Tendencias

| Indicador | Meta | Resultado | Semáforo |
|:---|:---:|:---:|:---:|
| % Personal capacitado en seguridad | 95 % | 62 % | 🔴 |
| Tiempo medio de respuesta a incidentes | < 4 h | 3.2 h | 🟢 |
| % Sistemas con respaldo verificado | 100 % | 100 % | 🟢 |
| Disponibilidad de servicios críticos | 99.5 % | 99.2 % | 🟡 |
| Hallazgos de auditoría cerrados a tiempo | 90 % | 0 % (en plazo) | 🟡 |

### Incidentes Relevantes del Período

- **INC-2026-001 (15/02/2026):** Caída del servicio de matrícula por falla de hardware en storage del Data Center. Tiempo de interrupción: 45 min. Causa raíz: disco SAS defectuoso. Acción correctiva: reemplazo de disco y configuración de RAID 6.
- **INC-2026-002 (10/04/2026):** Campaña de phishing dirigida a 12 correos institucionales de la DGA. 2 usuarios hicieron clic en el enlace malicioso. Contención inmediata, cambio de credenciales. Lección aprendida: reforzar simulacros de phishing.
- **INC-2026-003 (22/05/2026):** Fuga de datos menor: listado de correos electrónicos de estudiantes expuesto en un formulario público de Google Forms. Corrección: retiro del formulario y notificación a los afectados según Ley N° 29733.

### Estado de Auditorías Realizadas

- **AUD-2026-001 (20--22/05/2026):** Primera auditoría interna. 11 hallazgos. Plan de acciones correctivas aprobado con cierre programado para el 30/09/2026.

## Discusión y Análisis

### Puntos Críticos Discutidos

1. **Baja cobertura de capacitación (62 %):** El Rector instruyó a RRHH y OTI a implementar un plan intensivo de concientización para el personal administrativo de facultades, con metas mensuales y reporte al CGD.
2. **Monitoreo insuficiente de servicios cloud (NC-02):** La OTI reportó que la configuración de alertas en Huawei Cloud CBR está en progreso y se completará antes del 30/06/2026.
3. **Cifrado de dispositivos móviles:** Se detectaron 2 laptops de docentes extraviadas sin cifrado. El Oficial de Seguridad propuso activar BitLocker mediante GPO en todos los equipos Windows antes del 31/08/2026.
4. **Presupuesto PGTD-01:** Se confirmó la ejecución del 40 % del presupuesto asignado (S/ 340,000 de S/ 850,000) al corte de julio 2026, sin desviaciones significativas.

### Riesgos y Oportunidades Identificados

- **Nuevo riesgo:** Incremento de ataques de ransomware en universidades peruanas (CERT.PE reportó 3 casos en junio 2026). Se acordó adelantar el simulacro de ransomware a agosto 2026.
- **Oportunidad:** La implementación del SIEM (Wazuh) permitirá automatizar el monitoreo de seguridad y mejorar el KPI de disponibilidad.

## Salidas de la Revisión (Cl. 9.3.3)

### Decisiones y Acuerdos

| ID | Acuerdo / Decisión | Responsable | Fecha Límite | Estado |
|:---|:---|:---|:---:|:---:|
| A01 | Aprobar el plan de acciones correctivas de la auditoría interna AUD-2026-001 | Oficial de Seguridad | 15/06/2026 | Pendiente |
| A02 | Activar BitLocker mediante GPO en todos los equipos Windows corporativos | Jefe de OTI | 31/08/2026 | Pendiente |
| A03 | Realizar simulacro de ransomware antes del 31/08/2026 | CSIRT + OTI | 31/08/2026 | Pendiente |
| A04 | Implementar programa intensivo de concientización para administrativos (meta: 90 % al 31/12/2026) | RRHH + OTI | 31/12/2026 | Pendiente |
| A05 | Adquirir sensores de humedad y detección de inundación para salas de servidores | DGA + OTI | 30/09/2026 | Pendiente |

### Oportunidades de Mejora

- Incluir cláusula estándar de propiedad intelectual en todos los contratos de desarrollo de software (derivado de OM-01).
- Evaluar e implementar cifrado a nivel de columna (AES-256) para datos personales en GESDOC (derivado de OM-02).
- Formalizar el programa de simulacros de seguridad (phishing + ransomware) como actividad recurrente del P-SGSI-08.

### Recursos Asignados

- Se aprueba S/ 45,000 adicionales para la adquisición de sensores de inundación, actualización de licencias de BitLocker y contratación de servicio de simulación de phishing.
- Se asigna un practicante profesional de la Facultad de Ingeniería de Sistemas para apoyar en la implementación del SIEM Wazuh.

## Conclusión de la Alta Dirección

La Alta Dirección, en uso de sus atribuciones, declara que el SGSI de la UNCP es:

| Atributo | Evaluación |
|:---|:---|
| **Adecuación** (¿Los recursos son suficientes?) | [x] Adecuado [ ] Parcialmente adecuado [ ] Inadecuado |
| **Conveniencia** (¿El alcance y los objetivos son apropiados?) | [x] Conveniente [ ] Parcialmente conveniente [ ] No conveniente |
| **Eficacia** (¿Se logran los objetivos de seguridad?) | [ ] Eficaz [x] Parcialmente eficaz [ ] Ineficaz |

**Observaciones adicionales de la Alta Dirección:**

Pendiente de completar con el acta real de revisión por la dirección. La versión final debe consignar fecha de sesión, participantes, acuerdos, recursos aprobados, responsables y plazos, anexando el acta del CGD o documento equivalente.

## Próxima Revisión Programada

**Fecha:** 31/01/2027 (a los 6 meses, dado el estado parcialmente eficaz del SGSI)

***

**Firmas de los Asistentes:**

| Nombre | Cargo | Firma |
|:---|:---|:---|
| Dr. Amador Godofredo Vilcatoma Sánchez | Rector (Presidente) | |
| Econ. Cesar Orlando Canahualpa Tovar | Director General de Administración | |
| Ing. Marco Antonio Quispe Laura | Jefe de la OTI | |
| Ing. Luis Castillo Gutierrez | Oficial de Seguridad y Confianza Digital | |
| Abog. Rosa Mercedes Paredes Rojas | Representante de Asesoría Jurídica | |
| CPC. Patricia Lourdes Huamán Meza | Jefa de RRHH | |
| Mg. Juan Carlos Quispe Solórzano | Jefe de Planeamiento | |
