---
title: Procedimiento de Eliminación Segura de Información y Activos
code: P-SGSI-07
---

# Procedimiento de Eliminación Segura de Información y Activos

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Aprobado por:** Oficial de Seguridad y Confianza Digital
**Norma:** ISO/IEC 27001:2022 (Controles A.8.10, A.8.11, A.7.14)
**Referencia Técnica:** NIST SP 800-88 Rev. 1 (Guidelines for Media Sanitization)
**Alineamiento:** POL-SGSI-03 (Clasificación de la Información), F-SGSI-05 (Acta de Eliminación Segura)

***

## Objetivo
Establecer los métodos y controles para la eliminación segura de información y activos de almacenamiento en la UNCP, garantizando que los datos institucionales no puedan ser recuperados o reconstruidos una vez finalizada su vida útil, mitigando el riesgo de fugas de información por disposición inadecuada.

## Alcance
Este procedimiento aplica a toda información y activos de almacenamiento de la UNCP, independientemente de su formato (físico o digital), incluyendo:

- Documentos en papel (actas, expedientes, contratos, resoluciones).
- Discos duros (HDD, SSD) de servidores, computadoras y laptops.
- Medios extraíbles (USB, CD/DVD, tarjetas SD, cintas magnéticas).
- Dispositivos móviles (smartphones, tablets) institucionales.
- Equipos de red y almacenamiento (NAS, SAN, switches con almacenamiento interno).
- Respaldos en cinta o discos externos.
- Información en la nube (buckets, volúmenes, snapshots).

## Niveles de Eliminación Segura

La UNCP adopta los tres niveles de sanitización definidos en **NIST SP 800-88 Rev. 1**:

| Nivel | Método | Descripción | Cuándo Aplicar |
|---|---|---|---|
| **Clear (Borrado Lógico)** | Sobrescritura con software especializado (1 o más pasadas con datos aleatorios o ceros) | El medio sigue siendo reutilizable internamente | Equipos que se reasignan a otra área o usuario dentro de la UNCP |
| **Purge (Purgado)** | Desmagnetización (Degaussing) para HDD, o borrado seguro criptográfico (Cryptographic Erase) para SSD | El medio queda inutilizable para cualquier propósito posterior | Equipos que se dan de baja definitiva para donación, venta o reciclaje |
| **Destroy (Destrucción Física)** | Trituración, pulverización, incineración o perforación del medio | Destrucción irreversible del medio físico | Medios dañados, clasificados como Confidenciales, o cuando el riesgo de fuga de datos es alto |

## Métodos Específicos por Tipo de Medio

### 4.1 Medios Físicos (Papel)

| Clasificación | Método Exigido | Estándar |
|---|---|---|
| **Pública** | Reciclaje convencional | N/A |
| **Uso Interno** | Trituración en partículas (corte cruzado, no tiras) | DIN 66399 Nivel P-4 o superior |
| **Confidencial** | Trituración en partículas finas (corte cruzado, partículas < 2x15 mm) | DIN 66399 Nivel P-5 o superior |

- Las trituradoras deben estar ubicadas en áreas accesibles al personal autorizado y recibir mantenimiento periódico.
- Para volúmenes masivos de documentos confidenciales, se puede contratar un servicio externo de destrucción certificada con emisión de certificado de destrucción.

### 4.2 Discos Duros HDD

| Destino | Método | Pasadas |
|---|---|---|
| Reasignación interna (Clear) | Sobrescritura con software (DBAN, Blanco·n·Cero o herramienta del fabricante) | 1 pasada con ceros |
| Baja/Donación (Purge) | Desmagnetización (Degausser) + verificación | N/A |
| Baja/Reciclaje (Destroy) | Perforación mecánica (al menos 3 agujeros atravesando los platos) o trituración industrial | N/A |

### 4.3 Unidades de Estado Sólido SSD

| Destino | Método |
|---|---|
| Reasignación interna | Cryptographic Erase (comando ATA SANITIZE o herramienta del fabricante que invalide la clave de cifrado) |
| Baja/Donación | Cryptographic Erase + verificación; si el SSD no soporta CE, destrucción física |
| Baja/Reciclaje | Destrucción física (trituración) |

**Nota importante:** La sobrescritura tradicional no es efectiva en SSD debido al desgaste de celdas y la reserva de bloques internos. Siempre que sea posible, debe utilizarse Cryptographic Erase.

### 4.4 Medios Extraíbles (USB, CD/DVD, Tarjetas SD)
- Todos los medios extraíbles que hayan contenido información clasificada como **Confidencial** o **Uso Interno** deben ser destruidos físicamente al finalizar su vida útil.
- Método aceptado: Trituración mecánica, perforación o incineración controlada.
- No se acepta la reutilización de medios extraíbles que hayan contenido datos confidenciales.

### 4.5 Dispositivos Móviles (Smartphones, Tablets)
- **Android:** Restauración de fábrica + verificación de que el cifrado estaba activo (si no, destrucción física).
- **iOS:** Borrado de contenido y configuración (activa el Cryptographic Erase del chip de cifrado).
- **En caso de daño:** Destrucción física del dispositivo.

### 4.6 Información en la Nube
- Antes de dar de baja una suscripción cloud, la OTI debe:
  1. Verificar que todos los datos han sido migrados o respaldados según las políticas de retención.
  2. Eliminar todos los objetos (buckets, volúmenes, snapshots, bases de datos).
  3. Solicitar al proveedor la certificación de eliminación de los datos de sus servidores.
  4. Eliminar las cuentas de acceso asociadas.

## Verificación Post-Eliminación

Después de aplicar cualquier método de eliminación, se debe verificar:

| Medio | Método de Verificación |
|---|---|
| Papel triturado | Inspección visual de que las partículas cumplen el tamaño exigido |
| HDD sobrescrito | Lectura de verificación con la misma herramienta de sobrescritura |
| HDD desmagnetizado | Comprobación con un medidor de campo o verificación de que el disco no es reconocido por ningún sistema |
| SSD con Cryptographic Erase | Verificación de que la unidad aparece como "no inicializada" o sin particiones |
| Destrucción física | Inspección visual del daño irreversible |

## Cadena de Custodia para Eliminación

Para activos clasificados como **Confidenciales** o de alto valor, se debe mantener una cadena de custodia documentada:

1. **Responsable** del activo solicita la baja mediante **F-SGSI-03**.
2. **OTI** recibe el activo, registra el estado y aplica el método de eliminación correspondiente.
3. **Testigo** (Oficial de Seguridad o delegado) presencia la eliminación y firma el **F-SGSI-05 (Acta de Eliminación Segura)**.
4. **Acta** se archiva en el expediente del activo por un período mínimo de **5 años**.

## Proveedores Externos de Eliminación

Si se contrata a un tercero para la eliminación masiva de activos:

- El proveedor debe estar certificado (NAID AAA o equivalente).
- Debe emitir un **Certificado de Destrucción** por lote con fecha, método, cantidad y tipo de medio.
- La UNCP se reserva el derecho de realizar auditorías in situ al proceso del proveedor.
- Se debe firmar un acuerdo de confidencialidad previo a la entrega de los activos.

## Responsabilidades

| Rol | Responsabilidad |
|---|---|
| **Custodio del activo** | Solicitar la baja y entregar el activo a la OTI |
| **OTI** | Ejecutar o supervisar el método de eliminación; mantener los registros |
| **Oficial de Seguridad** | Aprobar el método según la clasificación; verificar la destrucción de activos Confidenciales |
| **Jefe de Área** | Autorizar la baja de activos de su unidad |

## Documentos Relacionados

| Código | Nombre |
|---|---|
| POL-SGSI-03 | Política de Clasificación de Información y Respaldos |
| F-SGSI-03 | Formato de Baja de Usuario y Devolución de Activos |
| F-SGSI-05 | Acta de Eliminación Segura de Activos |
| POL-SGSI-05 | Política de Seguridad para Dispositivos Móviles del Personal |
| D-SGSI-00 | Marco de Referencia Terminológico y Normativo |

***

**Elaborado por:**
Oficina de Tecnologías de la Información (OTI) — UNCP
