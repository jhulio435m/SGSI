---
title: Acta de Eliminación Segura de Activos / Información
code: F-SGSI-05
---

# Acta de Eliminación Segura de Activos / Información

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Referencia:** P-SGSI-07 (Eliminación Segura) / NIST SP 800-88
**ID de Acta:** ELIM-2026-001
**Fecha:** 30/06/2026
**Lugar:** Data Center UNCP -- Piso 3
**Solicitante:** Ing. Marco Antonio Quispe Laura -- Jefe de OTI

---

## Autorización de Eliminación

### Justificación

[ ] Fin del ciclo de vida del activo
[x] Actualización tecnológica
[ ] Daño irreparable del dispositivo
[x] Baja patrimonial programada
[ ] Cambio de proveedor de servicio cloud
[ ] Cumplimiento normativo (retención legal cumplida)
[ ] Otro: [Especificar]

### Autorización Previa

**Jefe de OTI:** Ing. Marco Antonio Quispe Laura -- **Fecha:** 15/06/2026
**Oficial de Seguridad:** Ing. Luis Castillo Gutierrez -- **Fecha:** 16/06/2026
**Control Patrimonial (V°B°):** CPC. María Elena Rojas Huamán -- **Fecha:** 16/06/2026

---

## Descripción de los Elementos a Eliminar

| # | Tipo | Descripción del Activo | Marca -- Modelo | Serie -- Patrim. | Clasif. | Nivel NIST | Método de Eliminación | Cantidad |
|:---|:---|:---|:---|:---|:---|:---|:---|:---:|
| 1 | Digital | Disco Duro HDD | Seagate 1TB | UNCP-HDD-045 | Confidencial | Purge | Desmagnetización | 4 |
| 2 | Digital | SSD | Samsung 256GB | UNCP-SSD-012 | Confidencial | Destroy | Trituración física | 3 |
| 3 | Físico | Actas académicas 2018 | -- | Caja N.° 10 a 15 | Confidencial | Destroy | Trituración industrial (P-5) | 6 cajas |
| 4 | Digital | USB Kingston | 32 GB | UNCP-USB-008 | Uso Interno | Destroy | Trituración física | 10 |
| 5 | Físico | CD/DVD respaldo | Varios | -- | Uso Interno | Destroy | Trituración física | 40 |
| 6 | Digital | Servidor HP DL380 (HDD) | HP ProLiant | UNCP-SRV-018 | Confidencial | Destroy | Perforación + trituración | 4 HDD |

### Niveles NIST SP 800-88

- **Clear:** Sobrescritura con software (datos no confidenciales)
- **Purge:** Desmagnetización o borrado criptográfico (datos confidenciales)
- **Destroy:** Destrucción física (datos de alto impacto / secreto)

## Método de Eliminación Aplicado

### Para Medios Digitales (HDD, SSD, USB)

[x] **Desmagnetización** -- Equipo: Degausser SD-825 -- Fecha: 30/06/2026
[x] **Trituración física** -- Equipo: Trituradora industrial HSM SECURIO -- Fecha: 30/06/2026
[x] **Perforación** (discos duros) -- Equipo: Taladro industrial -- Fecha: 30/06/2026
[ ] **Incineración controlada** -- Empresa: [Nombre] -- Fecha: [Fecha]
[ ] **Borrado criptográfico** -- Método: [AES-256 / otro] -- Fecha: [Fecha]
[ ] **Sobrescritura (Clear)** -- Estándar: [DoD 5220.22-M / NIST 800-88] -- Fecha: [Fecha]

### Para Medios Físicos (papel, actas)

[x] **Trituración industrial (corte cruzado)** -- Nivel de seguridad: P-5
[ ] **Incineración controlada**
[ ] **Empresa externa certificada:** [Nombre de la empresa] -- Certificado N.°: [Nro]

## Verificación Post-Eliminación (NIST SP 800-88)

### Verificación Visual

[x] Se verificó visualmente que los medios han sido destruidos/alterados irreversiblemente
[x] Fotografías de evidencia adjuntas: Sí

### Verificación Técnica (para Clear/Purge)

[ ] Muestreo de verificación realizado (para sobrescritura)
[ ] Software de verificación utilizado: [Nombre]
[ ] Resultado: [Pasó / No pasó]

## Declaración de Cumplimiento

Certificamos que los activos y la información descritos anteriormente han sido eliminados siguiendo los protocolos establecidos en el procedimiento **P-SGSI-07** (Eliminación Segura de Información y Activos) y los estándares **NIST SP 800-88 Rev. 1**, garantizando que la información contenida es ahora irreconstruible e ilegible.

## Responsables de la Supervisión

| Rol | Nombre | Firma | Fecha |
|:---|:---|:---|:---:|
| **Ejecutor (OTI)** | Ing. Miguel Ángel Paredes Torres | | 30/06/2026 |
| **Control Patrimonial** | CPC. María Elena Rojas Huamán | | 30/06/2026 |
| **Oficial de Seguridad (Veedor)** | Ing. Luis Castillo Gutierrez | | 30/06/2026 |

## Eliminación de Información en Cloud (si aplica)

[ ] Bucket OBS eliminado: [Nombre del bucket] -- [Fecha]
[ ] Instantáneas/snapshots eliminadas: [Fecha]
[ ] Confirmación de proveedor cloud recibida: [Sí / No] -- [ID del ticket]

---

**Nota:** Archivar este acta durante el período mínimo de retención (3 años) según POL-SGSI-03. Para activos con clasificación "Confidencial", el período de retención es de 5 años.