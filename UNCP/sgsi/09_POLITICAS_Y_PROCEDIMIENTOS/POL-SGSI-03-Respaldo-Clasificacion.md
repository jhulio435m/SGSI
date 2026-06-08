---
title: Política de Clasificación de la Información y Respaldos
code: POL-SGSI-03
---

# Política de Clasificación de la Información y Respaldos

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Aprobado por:** Comité de Gobierno y Transformación Digital
**Norma:** ISO/IEC 27001:2022 (Controles A.5.12, A.5.13, A.5.14, A.8.13)
**Alineamiento:** D-SGSI-02 (Alcance del SGSI), P-SGSI-07 (Eliminación Segura)

***

## Objetivo
Establecer el esquema de clasificación de la información institucional y las directrices para su etiquetado, manejo y respaldo, garantizando que cada activo de información reciba el nivel de protección adecuado según su valor y criticidad para la UNCP.

## Alcance
Esta política aplica a toda la información generada, procesada, almacenada o transmitida por la UNCP, independientemente de su formato (digital, físico, transmitido), soporte (servidores, nube, papel, dispositivos móviles) o ubicación (instalaciones UNCP, trabajo remoto, proveedores).

---

## PARTE I: CLASIFICACIÓN DE LA INFORMACIÓN

## Niveles de Clasificación

La UNCP clasifica su información en tres niveles, basándose en el impacto potencial sobre la Confidencialidad, Integridad y Disponibilidad (CID):

| Nivel | Definición | Impacto si se Compromete | Ejemplos UNCP |
|---|---|---|---|
| **Pública** | Información que puede ser divulgada sin restricción a cualquier persona, dentro o fuera de la UNCP | Sin impacto significativo | Portal web institucional, noticias, comunicados oficiales, oferta académica, calendario académico |
| **Uso Interno** | Información de acceso restringido al personal de la UNCP que no debe ser divulgada externamente sin autorización | Impacto moderado: podría afectar la imagen institucional o procesos internos | Manuales de procedimientos, memorandos internos, directivas, organigramas, información presupuestal agregada, resultados de evaluaciones internas |
| **Confidencial** | Información sensible cuya divulgación no autorizada podría causar daño significativo a la UNCP, a los miembros de su comunidad o a terceros | Impacto alto o crítico: sanciones legales, pérdida de confianza, daño reputacional severo | Datos personales de estudiantes y personal (Ley N° 29733), notas y actas académicas, planillas, historias clínicas del Centro Médico, contratos, resoluciones rectorales, credenciales de acceso, tesis en proceso de revisión, información financiera detallada |

## Etiquetado de la Información

### 4.1 Información Digital
Todo documento digital debe incluir una marca de clasificación visible:

| Nivel | Marca en Documento | Marca en Correo Electrónico |
|---|---|---|
| **Pública** | "[PÚBLICA]" o sin marca | Sin restricción |
| **Uso Interno** | "[USO INTERNO]" | "[USO INTERNO]" en el asunto |
| **Confidencial** | "[CONFIDENCIAL]" | "[CONFIDENCIAL]" en el asunto + cifrado del adjunto |

### 4.2 Información Física (Papel)
Los documentos impresos clasificados como **Confidenciales** deben llevar un sello o carátula con la leyenda "CONFIDENCIAL" en la portada y en cada página, si es posible.

### 4.3 Sistemas de Información
Los sistemas que almacenan o procesan información deben mostrar una advertencia de clasificación al iniciar sesión, indicando que la información contenida es de uso institucional y su acceso está restringido.

## Manejo Seguro según Clasificación

| Actividad | Pública | Uso Interno | Confidencial |
|---|---|---|---|
| **Almacenamiento** | Sin restricción | Servidores UNCP o nube autorizada | Servidores UNCP cifrados o nube con cifrado en reposo. No en dispositivos personales ni en servicios cloud personales |
| **Transmisión** | Sin restricción | Correo institucional con adjunto (sin cifrado adicional requerido) | Correo institucional con adjunto cifrado o mediante plataforma segura. Prohibido por WhatsApp, Telegram u otros mensajeros no corporativos |
| **Impresión** | Sin restricción | Impresoras de red de la unidad | Impresoras de red con autenticación (solo el usuario puede retirar la impresión). No en impresoras compartidas sin control |
| **Copias/Fotocopiado** | Sin restricción | Con autorización del área | Solo con autorización del dueño del proceso. Recoger inmediatamente de la bandeja |
| **Destrucción** | Reciclaje | Trituración (corte cruzado) | Trituración (partículas) o servicio de destrucción certificada |
| **Envío físico** | Sin restricción | Sobre cerrado | Sobre cerrado y lacrado, con acuse de recibo |
| **Acceso desde móvil** | Sin restricción | Permitido con PIN/bloqueo | Permitido solo con cifrado de dispositivo + VPN |

## Transferencia de Información a Terceros

- La transferencia de información clasificada como **Confidencial** a terceros (otras instituciones, entidades del Estado, investigadores externos) debe ser autorizada por escrito por el dueño del proceso y registrada.
- Cuando la transferencia sea masiva o periódica, debe formalizarse mediante un **Acuerdo de Confidencialidad** o **Convenio de Intercambio de Información**.
- Para información de **Uso Interno** enviada a terceros, debe agregarse la leyenda "USO INTERNO - NO DIVULGAR".

---

## PARTE II: POLÍTICA DE RESPALDOS

## Principios Generales de Respaldo

1. **Regla 3-2-1:** Mantener al menos **3 copias** de los datos críticos, en **2 soportes diferentes**, con **1 copia fuera del sitio principal**.
2. **Cifrado:** Todos los respaldos que contengan información **Confidencial** deben estar cifrados, tanto en tránsito como en reposo.
3. **Pruebas:** Todo respaldo debe ser restaurable. Se realizarán pruebas de restauración con la frecuencia indicada.
4. **Registro:** Todos los procesos de respaldo y restauración deben quedar registrados (logs).

## Frecuencia y Retención por Tipo de Información

| Tipo de Información | Sistema / Dato | Frecuencia de Respaldo | Tiempo de Retención | Ubicación |
|---|---|---|---|---|
| **Base de datos misional** | ERP ADESA (matrícula, notas, grados) | **Diaria** (full semanal + diferencial diaria) | 5 años fiscales | Huawei Cloud CBR + copia local cifrada |
| **Base de datos académica** | Moodle (campus virtual) | **Diaria** (backup automatizado) | 2 años + curso activo | Huawei Cloud CBR |
| **Correo institucional** | Microsoft 365 Exchange | **Continua** (retención por litigio) | Según política de retención Microsoft + 5 años para documentos oficiales | Microsoft 365 (SaaS) |
| **Archivos compartidos** | Carpetas de red, repositorio documental | **Semanal** | 3 años | Huawei Cloud CBR + NAS local |
| **Sistemas financieros** | SIGA, SIAF, planillas | **Diaria** (en periodo de cierre mensual) / **Semanal** (resto) | 10 años (legal) | Huawei Cloud CBR + copia local |
| **Bases de datos de investigación** | Repositorio DSpace (tesis) | **Semanal** | Permanente para tesis publicadas | Huawei Cloud CBR |
| **Historias clínicas** | Centro Médico UNCP | **Diaria** | 20 años según legislación sanitaria | Huawei Cloud CBR (cifrado) |
| **Configuración de red y sistemas** | Switches, firewalls, servidores | **Antes de cada cambio significativo** + mensual completo | 2 años | Copia local + cloud |

## Metodología de Respaldo

### 9.1 Infraestructura Local + Cloud (Híbrida)
- **Respaldos primarios:** Automatizados mediante **Huawei Cloud Backup & Recovery (CBR)**, con política de retención configurada por tipo de datos.
- **Respaldos locales:** Copia adicional en NAS institucional para recuperación rápida ante fallos de conectividad.
- **Inmutabilidad:** Los respaldos del ERP ADESA y bases de datos críticas deben ser **inmutables** (no modificables ni eliminables antes del período de retención) para protección contra ransomware.

### 9.2 Verificación de Integridad
- Cada respaldo debe generar un **hash (SHA-256)** del archivo de respaldo para verificar su integridad.
- El sistema de respaldo debe notificar automáticamente a la OTI ante cualquier fallo o corrupción.

## Pruebas de Restauración

| Tipo de Datos | Frecuencia de Prueba | Alcance | Responsable |
|---|---|---|---|
| Bases de datos críticas (ERP ADESA) | **Trimestral** | Restauración completa en entorno de pruebas + verificación de integridad de datos | OTI (Sistemas) |
| Archivos compartidos | **Semestral** | Restauración de una muestra de archivos de diferentes fechas | OTI (Sistemas) |
| Correo institucional | **Anual** | Restauración de un buzón de archivo muerto | OTI (Soporte) |
| Infraestructura completa (DRP) | **Anual** | Simulacro de conmutación por error al nodo cloud | OTI (Infraestructura) |

Los resultados de cada prueba deben documentarse en un informe que incluya:
- Datos restaurados y su estado.
- Tiempo total de restauración (comparado con el RTO definido en P-SGSI-05).
- Incidencias encontradas y acciones correctivas tomadas.

## Responsabilidades

| Rol | Responsabilidad |
|---|---|
| **Dueño del Proceso** | Clasificar la información de su área según esta política; autorizar el acceso a información Confidencial. |
| **OTI (Sistemas)** | Implementar y monitorear los respaldos; ejecutar pruebas de restauración; mantener la infraestructura de backup. |
| **Usuario (Personal)** | Identificar y etiquetar la información que genera según su clasificación; reportar cualquier anomalía en el respaldo de sus archivos. |
| **Oficial de Seguridad** | Auditar el cumplimiento de esta política; revisar anualmente los criterios de clasificación y retención. |

## Incumplimiento
El manejo inadecuado de información clasificada (ej. envío de datos confidenciales por canales no seguros, almacenamiento de datos institucionales en servicios cloud personales) será gestionado según la sección 9 de la POL-SGSI-05 y el régimen disciplinario aplicable.

## Documentos Relacionados

| Código | Nombre |
|---|---|
| D-SGSI-02 | Alcance del SGSI |
| P-SGSI-05 | Resiliencia y Continuidad en Nube Híbrida |
| P-SGSI-07 | Procedimiento de Eliminación Segura de Información |
| F-SGSI-05 | Acta de Eliminación Segura de Activos |
| POL-SGSI-05 | Política de Seguridad para Dispositivos Móviles del Personal |

***
---
