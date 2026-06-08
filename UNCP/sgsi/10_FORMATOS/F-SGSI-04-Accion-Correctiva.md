---
title: Reporte de Acción Correctiva (RAC)
code: F-SGSI-04
---

# Reporte de Acción Correctiva (RAC)

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Referencia:** ISO/IEC 27001:2022 (Cl. 10.1)
**ID RAC:** RAC-2026-002
**Fecha de Apertura:** 22/05/2026
**Fecha de Cierre:** 15/07/2026

---

## Origen de la No Conformidad

[x] Auditoría Interna (AUD-2026-001)
[ ] Auditoría Externa / Certificación
[ ] Revisión por la Dirección (REV-ID)
[ ] Incidente de seguridad (INC-ID)
[ ] Queja / Reclamo de usuario
[ ] Monitoreo continuo (KPI por debajo del umbral)
[ ] Autoevaluación / Hallazgo interno

## Descripción de la No Conformidad / Hallazgo

### Descripción Detallada

Durante la auditoría interna AUD-2026-001 realizada el 20/05/2026, se identificó que la sala de servidores de la Facultad de Ingeniería de Sistemas (FIIS) alberga 3 equipos (2 switches Cisco Catalyst 2960, 1 servidor HP ProLiant DL380) no registrados en el inventario de activos R-SGSI-01. Los equipos no tienen código de activo, custodio asignado ni clasificación de seguridad. Esto incumple el control A.7.8 de ISO/IEC 27001:2022 (ubicación y protección de equipos) y la política POL-SGSI-07.

### Requisito Incumplido

- [x] Requisito de ISO/IEC 27001:2022 -- Control: A.7.8
- [ ] Control del Anexo A -- Control: __________
- [ ] Requisito legal (Ley 29733 / D.L. 1412 / otro): __________
- [x] Política / Procedimiento interno: POL-SGSI-07, R-SGSI-01

### Clasificación Inicial

[x] **No Conformidad Mayor** -- Impacto significativo en el SGSI
[ ] **No Conformidad Menor** -- Incumplimiento puntual y controlable
[ ] **Observación / Oportunidad de Mejora**

## Análisis de Causa Raíz

### Metodología Utilizada

[x] 5 Porqués
[ ] Diagrama de Ishikawa (Causa-Efecto)
[ ] Árbol de Problemas
[ ] Otra: __________

### Desarrollo del Análisis

1. ¿Por qué los equipos no están inventariados? -> Porque no se incluyeron en el levantamiento inicial de activos.
2. ¿Por qué no se incluyeron? -> Porque la sala de servidores de la FIIS no fue considerada en el alcance del inventario.
3. ¿Por qué no fue considerada? -> Porque el procedimiento R-SGSI-01 no especificaba claramente las ubicaciones a cubrir.
4. ¿Por qué no se especificaron las ubicaciones? -> Porque el responsable del inventario asumió que solo el Data Center principal alberga servidores.
5. ¿Por qué asumió eso? -> Porque no existía un censo completo de ubicaciones con infraestructura TI ni un procedimiento de verificación cruzada con registros de compras y redes.

### Causa Raíz Identificada

Ausencia de un censo completo de ubicaciones con infraestructura TI al momento de elaborar el inventario, y falta de verificación cruzada con registros de compras (DGA) y redes (OTI) para identificar todas las salas de servidores activas.

## Plan de Acción

### Acción de Corrección (Solución Inmediata -- Contención)

| Acción | Responsable | Fecha de Ejecución | Estado |
|:---|:---|:---:|:---:|
| Registrar los 3 equipos encontrados en R-SGSI-01 con código de activo y custodio asignado (Jefe FIIS) | Ing. Marco Quispe (OTI) | 25/05/2026 | [ ] Pendiente [x] Ejecutado |

### Acción Correctiva (Solución Permanente -- Evitar Recurrencia)

| Acción | Responsable | Fecha Límite | Recursos Necesarios | Estado |
|:---|:---|:---:|:---|:---:|
| Realizar censo físico completo de todas las salas de servidores y gabinetes de telecomunicaciones en todas las facultades | Ing. Marco Quispe (OTI) | 30/06/2026 | 1 técnico OTI, 2 semanas | [ ] Pendiente [x] Ejecutado |
| Actualizar el procedimiento R-SGSI-01 para incluir verificación cruzada con DGA (compras) y OTI Redes | Oficial de Seguridad | 30/06/2026 | 4 horas | [ ] Pendiente [x] Ejecutado |

### Acciones Preventivas Adicionales (Opcional)

Establecer una revisión trimestral del inventario de activos con cruce de información entre OTI (redes) y DGA (compras) para asegurar que todo equipo adquirido sea inventariado dentro de los 15 días hábiles posteriores a su recepción.

## Seguimiento y Cierre

### Verificación de Implementación

[x] Acciones correctivas implementadas según lo planificado
[x] Evidencia objetiva de implementación adjunta
[x] Personal relevante notificado / capacitado

### Validación de Eficacia (Oficial de Seguridad)

**¿La acción correctiva fue eficaz para eliminar la causa raíz y prevenir la recurrencia?**

[x] Sí [ ] Parcialmente [ ] No

**Observaciones:** El censo completo identificó 12 ubicaciones adicionales (facultades) con infraestructura TI, incorporando 5 equipos más al inventario. El procedimiento R-SGSI-01 fue actualizado a versión 2.1. Se programó la revisión trimestral cruzada para setiembre 2026.

**Nombre del Oficial de Seguridad:** Ing. Luis Castillo Gutierrez
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Fecha de Validación:** 15/07/2026

### Cierre Formal

**Aprobado por:** Ing. Luis Castillo Gutierrez -- Oficial de Seguridad
**Fecha de Cierre:** 15/07/2026