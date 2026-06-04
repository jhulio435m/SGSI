# F-SGSI-05: Acta de Eliminación Segura de Activos / Información

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Referencia:** P-SGSI-07 (Eliminación Segura de Información y Activos) / NIST SP 800-88
**ID de Acta:** ELIM-[Año]-[Nro]
**Fecha:** [Fecha]
**Lugar:** [Oficina/Sede]
**Solicitante:** [Nombre y Cargo]

***

## 1. Autorización de Eliminación

### 1.1 Justificación
[ ] Fin del ciclo de vida del activo
[ ] Actualización tecnológica
[ ] Daño irreparable del dispositivo
[ ] Baja patrimonial programada
[ ] Cambio de proveedor de servicio cloud
[ ] Cumplimiento normativo (retención legal cumplida)
[ ] Otro: [Especificar]

### 1.2 Autorización Previa
**Jefe de OTI:** [Nombre y Firma] — **Fecha:** [Fecha]
**Oficial de Seguridad:** [Nombre y Firma] — **Fecha:** [Fecha]
**Control Patrimonial (V°B°):** [Nombre y Firma] — **Fecha:** [Fecha]

***

## 2. Descripción de los Elementos a Eliminar

| # | Tipo | Descripción del Activo | Marca/Modelo | N° Serie / Patrimonial | Clasificación (POL-SGSI-03) | Nivel NIST SP 800-88 | Método de Eliminación | Cantidad |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Digital | Disco Duro | WD 500GB | S/N: WD-XXXXX | Confidencial | Purge | Desmagnetización | 2 |
| 2 | Digital | SSD | Samsung 256GB | S/N: SAM-XXXX | Confidencial | Destroy | Trituración física | 3 |
| 3 | Físico | Actas académicas | — | Caja N° 10-2020 | Confidencial | Destroy | Trituración industrial | 10 cajas |
| 4 | Digital | USB | Kingston 32GB | S/N: K-XXXX | Uso Interno | Destroy | Incineración controlada | 15 |
| 5 | Físico | CD/DVD | Varios | — | Uso Interno | Destroy | Trituración física | 50 |
| 6 | Digital | Servidor (HDD) | Dell PowerEdge | PAT-XXXXX | Confidencial | Destroy | Perforación + trituración | 4 |

### Niveles NIST SP 800-88:
- **Clear:** Sobrescritura con software (datos no confidenciales)
- **Purge:** Desmagnetización o borrado criptográfico (datos confidenciales)
- **Destroy:** Destrucción física (datos de alto impacto / secreto)

## 3. Método de Eliminación Aplicado

### 3.1 Para Medios Digitales (HDD, SSD, USB)
[ ] **Desmagnetización** — Equipo: [Modelo] — Fecha: [Fecha]
[ ] **Trituración física** — Equipo: [Modelo] — Fecha: [Fecha]
[ ] **Perforación** (discos duros) — Equipo: [Herramienta] — Fecha: [Fecha]
[ ] **Incineración controlada** — Empresa: [Nombre] — Fecha: [Fecha]
[ ] **Borrado criptográfico** — Método: [AES-256 / otro] — Fecha: [Fecha]
[ ] **Sobrescritura (Clear)** — Estándar: [DoD 5220.22-M / NIST 800-88] — Fecha: [Fecha]

### 3.2 Para Medios Físicos (papel, actas)
[ ] **Trituración industrial (corte cruzado)** — Nivel de seguridad: [P-4 / P-5 / P-6]
[ ] **Incineración controlada**
[ ] **Empresa externa certificada:** [Nombre de la empresa] — Certificado N°: [Nro]

## 4. Verificación Post-Eliminación (NIST SP 800-88)

### 4.1 Verificación Visual
[ ] Se verificó visualmente que los medios han sido destruidos/alterados irreversiblemente
[ ] Fotografías de evidencia adjuntas: [Sí / No]

### 4.2 Verificación Técnica (para Clear/Purge)
[ ] Muestreo de verificación realizado (para sobrescritura)
[ ] Software de verificación utilizado: [Nombre]
[ ] Resultado: [Pasó / No pasó]

## 5. Declaración de Cumplimiento
Certificamos que los activos y la información descritos anteriormente han sido eliminados siguiendo los protocolos establecidos en el procedimiento **P-SGSI-07** (Eliminación Segura de Información y Activos) y los estándares **NIST SP 800-88 Rev. 1**, garantizando que la información contenida es ahora irreconstruible e ilegible.

## 6. Responsables de la Supervisión

| Rol | Nombre | Firma | Fecha |
| :--- | :--- | :--- | :--- |
| **Ejecutor (OTI)** | | | |
| **Control Patrimonial** | | | |
| **Oficial de Seguridad (Veedor)** | | | |

## 7. Eliminación de Información en Cloud (si aplica)
[ ] Bucket OBS eliminado: [Nombre del bucket] — [Fecha]
[ ] Instantáneas/snapshots eliminadas: [Fecha]
[ ] Confirmación de proveedor cloud recibida: [Sí / No] — [ID del ticket]

---

**Nota:** Archivar este acta durante el período mínimo de retención (3 años) según POL-SGSI-03. Para activos con clasificación "Confidencial", el período de retención es de 5 años.
