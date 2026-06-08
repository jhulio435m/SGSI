---
title: Plantilla de Informe de No Conformidad y Acción Correctiva (RAC)
code: F-SGSI-04
---

# Plantilla de Informe de No Conformidad y Acción Correctiva (RAC)

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**ID de RAC:** RAC-2026-001
**ID de Auditoría (si aplica):** AUD-2026-001

---

## Descripción de la No Conformidad

**Fecha de Detección:** 22/05/2026
**Detectado por:** Mg. Carlos Ramos Quispe (Auditor Líder)
**Fuente:** Auditoría Interna AUD-2026-001

**Descripción Detallada:**

En la inspección a la sala de servidores de la Facultad de Ingeniería de Sistemas se encontraron 3 equipos (2 switches Cisco Catalyst 2960, 1 servidor HP ProLiant DL380) no registrados en el inventario de activos R-SGSI-01. No tienen código de activo ni custodio asignado. Esta situación incumple el control A.7.8 de ISO 27001:2022 ("Los equipos deben ser inventariados") y la política POL-SGSI-07.

---

## Análisis de Causa Raíz

**Método Utilizado:** 5 Porqués
**Resultado del Análisis:**

1. ¿Por qué los equipos no están inventariados? Porque no se incluyeron en el levantamiento inicial de activos.
2. ¿Por qué no se incluyeron? Porque la sala de servidores de la FIIS no fue considerada en el alcance del inventario.
3. ¿Por qué no fue considerada? Porque el procedimiento R-SGSI-01 no especificaba claramente las ubicaciones a cubrir.
4. ¿Por qué no se especificaron? Porque el responsable del inventario asumió que solo el Data Center principal alberga servidores.
5. ¿Por qué asumió eso? Porque no existía una lista completa de ubicaciones con infraestructura TI ni un procedimiento de verificación cruzada.

**Causa Raíz:** Ausencia de un censo completo de ubicaciones con infraestructura TI al momento de elaborar el inventario, y falta de verificación cruzada con registros de compras y redes.

---

## Plan de Acción (Corrección y Acción Correctiva)

- **Corrección (Acción inmediata):** Registrar los 3 equipos encontrados en el inventario R-SGSI-01 con código de activo, custodio asignado (Jefe de la FIIS) y clasificación correspondiente. Realizar etiquetado físico de los equipos.
- **Acción Correctiva (Para evitar recurrencia):** Realizar un censo físico completo de todas las salas de servidores y gabinetes de telecomunicaciones en todas las facultades y dependencias de la UNCP. Actualizar el procedimiento R-SGSI-01 para incluir la verificación cruzada con registros de compras (DGA), redes (OTI) y planos de infraestructura.

**Responsable:** Ing. Marco Antonio Quispe Laura (Jefe de OTI)
**Fecha Límite:** 30/06/2026

---

## Verificación de la Eficacia

**Fecha de Verificación:** 15/07/2026
**Verificado por:** Ing. Luis Castillo Gutierrez (Oficial de Seguridad)

**Resultado:**

- [x] Eficaz (Se cierra el RAC)
- [ ] No Eficaz (Se requiere nuevo análisis de causa)

**Evidencia de Verificación:**

Se realizó una inspección conjunta OTI-Oficial de Seguridad el 10/07/2026. Los 3 equipos están registrados en R-SGSI-01 con códigos UNCP-SRV-025, UNCP-SW-047 y UNCP-SW-048. Se verificó el etiquetado físico en la sala FIIS. Adicionalmente, se completó el censo de 12 ubicaciones adicionales (facultades), identificando 5 equipos más que fueron incorporados al inventario. El procedimiento R-SGSI-01 fue actualizado (versión 2.1) incluyendo el paso de verificación cruzada con DGA y OTI Redes.

---

**Firmas:**

___________________________
**Ing. Marco Antonio Quispe Laura**
Responsable del Área (OTI)

___________________________
**Ing. Luis Castillo Gutierrez**
Oficial de Seguridad y Confianza Digital