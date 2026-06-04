# POL-SGSI-07: Política de Seguridad Física y Áreas Seguras

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 2.0
**Norma:** ISO/IEC 27001:2022 (Controles A.7.1 — Perímetros de seguridad física, A.7.2 — Control de acceso físico, A.7.3 — Seguridad de oficinas, recintos e instalaciones, A.7.4 — Protección contra amenazas externas y ambientales, A.7.5 — Trabajo en áreas seguras, A.7.6 — Áreas de carga y despacho, A.7.7 — Escritorio y pantalla limpios, A.7.8 — Ubicación y protección de equipos, A.7.9 — Seguridad de los activos fuera de las instalaciones, A.7.10 — Almacenamiento seguro, A.7.11 — Cableado de seguridad, A.7.12 — Mantenimiento de equipos, A.7.13 — Retirada de activos fuera de las instalaciones, A.7.14 — Eliminación segura de activos)
**Alineamiento:** P-SGSI-03 (Gestión de Accesos), P-SGSI-07 (Eliminación Segura), F-SGSI-06 (Bitácora de Acceso a Áreas Críticas)

***

## 1. Objetivo
Establecer las medidas de seguridad física para proteger las instalaciones, equipos y activos de información de la UNCP contra accesos no autorizados, daños, interferencias y amenazas ambientales, garantizando la continuidad de los servicios críticos.

## 2. Alcance
Esta política aplica a todas las instalaciones de la UNCP, incluyendo sus **4 sedes** (Huancayo, Mantaro, Satipo, Tarma), con énfasis en las **áreas críticas** definidas en la sección 3. Aplica a todo el personal, visitantes, contratistas y proveedores que ingresen a dichas instalaciones.

## 3. Clasificación de Áreas

| Nivel | Área | Criterio |
|---|---|---|
| **Crítica** | Datacenter principal, sala de servidores, cuarto de comunicaciones, Archivo Central | Almacenan o procesan activos de información críticos. Acceso restringido al mínimo personal autorizado |
| **Restringida** | Oficina de OTI, Tesorería, Registros Académicos, RRHH, Centro Médico, sala de equipos de red por facultad | Manejan información confidencial o equipos sensibles. Acceso limitado al personal del área |
| **Controlada** | Oficinas administrativas, salas de reuniones, bibliotecas, laboratorios de cómputo | Acceso con identificación institucional o registro de ingreso |
| **Pública** | Hall principal, auditorios, cafetería, áreas comunes | Acceso libre al público con identificación en recepción |

## 4. Perímetros de Seguridad Física

### 4.1 Datacenter y Salas de Servidores (Área Crítica)
- El Datacenter debe contar con **barreras físicas sólidas** (muros de concreto desde losa a losa, puerta blindada con cerradura multipunto).
- Sistema de **control de acceso electrónico** con autenticación biométrica (huella dactilar) + tarjeta de proximidad, integrado a un sistema centralizado de registro.
- **Videovigilancia (CCTV)** continua con cámaras en todos los accesos, interior de la sala y perímetro exterior. Las grabaciones deben conservarse por un mínimo de **90 días**.
- **Sistema de detección de intrusiones** (sensores de puerta, detectores de movimiento) activo 24/7, monitoreado por seguridad patrimonial.
- **Bitácora de acceso** digital o física (**F-SGSI-06**) que registre toda entrada y salida, incluyendo personal, visitantes y contratistas.

### 4.2 Perímetro del Campus
- El ingreso al campus principal debe contar con **control de acceso** (caseta de vigilancia, barrera vehicular, identificación de visitantes).
- El perímetro debe estar delimitado por **cercos o muros perimetrales** en buen estado.
- Las puertas de acceso peatonal y vehicular deben permanecer cerradas o controladas durante el horario no laboral.

## 5. Control de Acceso a Áreas Críticas

### 5.1 Personal Autorizado
- Solo el personal de la OTI con autorización expresa del Jefe de la OTI puede ingresar al Datacenter. La lista de autorizados debe revisarse trimestralmente.
- El acceso a áreas Restringidas se limita al personal asignado a esa unidad. Personal de otras áreas solo puede ingresar acompañado por un miembro del área.

### 5.2 Visitantes y Contratistas
- Todo visitante debe:
  1. Registrarse en recepción (nombre, DNI, empresa, motivo, hora de ingreso y salida, persona a quien visita).
  2. Portar un **solapín o carnet de visitante** visible en todo momento.
  3. Ser acompañado por un empleado autorizado de la UNCP durante su permanencia en áreas Críticas o Restringidas.
- Los contratistas de mantenimiento deben presentar orden de servicio y registrar sus herramientas/herramientas al ingreso.

### 5.3 Acceso Fuera del Horario Laboral
- El acceso a las instalaciones fuera del horario laboral (19:00 - 07:00) y fines de semana debe ser autorizado por el jefe inmediato y registrado en el sistema de control de acceso o bitácora.
- El personal de seguridad patrimonial debe verificar la identidad y autorización antes de permitir el ingreso.

## 6. Protección contra Amenazas Ambientales

### 6.1 Incendios
- El Datacenter debe contar con sistema de **detección temprana de incendios** (sensores de humo, temperatura, aspiración VESDA).
- Sistema de **extinción por gas limpio** (FM-200, Novec 1230 o equivalente) que no dañe los equipos electrónicos. No se aceptan sistemas de agua en el Datacenter.
- Extintores portátiles de CO2 en puntos estratégicos del Datacenter y pasillos.
- Pruebas periódicas del sistema contra incendios según la frecuencia indicada por el fabricante o la normativa municipal, coordinadas con la OTI para minimizar falsas alarmas.

### 6.2 Clima y Humedad
- El Datacenter debe mantener condiciones ambientales controladas:
  - **Temperatura:** 18°C a 24°C (recomendado 22°C).
  - **Humedad relativa:** 40% a 60%.
- Sistema de monitoreo ambiental con alarmas automáticas ante desviaciones.
- Aire acondicionado de precisión (CRAC/CRAH) con redundancia N+1.

### 6.3 Energía Eléctrica
- **UPS (Sistema de Alimentación Ininterrumpida)** con autonomía suficiente para un apagado controlado de todos los servidores (mínimo 30 minutos a carga completa).
- **Generador eléctrico de respaldo** con capacidad para mantener todo el Datacenter operativo por al menos 24 horas.
- Pruebas mensuales del generador bajo carga.
- Cableado eléctrico y de datos segregado (canaletas separadas) para evitar interferencias electromagnéticas.

## 7. Seguridad de las Áreas de Trabajo (Escritorio y Pantalla Limpia)

- Todo el personal debe mantener su escritorio **limpio** al finalizar la jornada laboral:
  - Documentos clasificados como Confidenciales o de Uso Interno guardados bajo llave o en archivadores cerrados.
  - Dispositivos extraíbles (USB, discos externos) retirados y guardados.
- Las pantallas de computadora deben bloquearse automáticamente tras **5 minutos** de inactividad (configuración forzada por política de grupo/MDM).
- No se debe dejar información sensible visible en la pantalla cuando el puesto de trabajo está desatendido.

## 8. Seguridad de Activos Fuera de las Instalaciones

- Los equipos portátiles (laptops, tablets) que sean retirados del campus deben:
  - Tener el cifrado obligatorio activo (según POL-SGSI-05).
  - Ser transportados en fundas o maletines que no identifiquen su contenido.
  - No dejarse desatendidos en vehículos o lugares públicos.
- La retirada temporal de equipos del campus debe ser registrada en la OTI mediante el formato **F-SGSI-03**, indicando destino, responsable y fecha estimada de retorno.

## 9. Mantenimiento de Equipos

- Todo mantenimiento de equipos del Datacenter o áreas críticas debe:
  - Realizarse dentro de una **ventana de mantenimiento** previamente aprobada por el Jefe de la OTI.
  - Ser ejecutado por personal autorizado (interno o del fabricante).
  - Quedar registrado en una bitácora de mantenimiento (fecha, equipo intervenido, técnico, trabajo realizado, duración).
- El personal de mantenimiento externo debe estar acompañado en todo momento por un miembro de la OTI.

## 10. Cableado de Seguridad

- El cableado de red y eléctrico debe estar protegido contra interceptaciones y daños:
  - Cableado estructurado en canaletas cerradas o tuberías.
  - Los paneles de parcheo (patch panels) deben estar en racks cerrados con llave o en cuartos de comunicaciones con acceso restringido.
  - El cableado de fibra óptica entre edificios debe estar canalizado subterráneamente o protegido mecánicamente.

## 11. Eliminación Segura de Activos Físicos

La eliminación o retiro definitivo de activos físicos (equipos, mobiliario que contenía información) debe realizarse siguiendo el **P-SGSI-07 (Procedimiento de Eliminación Segura)** y registrarse en el **F-SGSI-05 (Acta de Eliminación Segura)**.

## 12. Responsabilidades

| Rol | Responsabilidad |
|---|---|
| **Oficina de Seguridad Patrimonial** | Controlar el acceso físico al campus; gestionar la vigilancia perimetral y CCTV; mantener las bitácoras de visitantes. |
| **OTI** | Gestionar el control de acceso electrónico del Datacenter; monitorear las condiciones ambientales; ejecutar el mantenimiento de equipos. |
| **Oficial de Seguridad** | Supervisar el cumplimiento de esta política; revisar trimestralmente las listas de acceso autorizado. |
| **Todo el Personal** | Cumplir las normas de escritorio limpio, bloqueo de pantalla y registro de visitantes. |

## 13. Monitoreo y Métricas

| Indicador | Meta | Frecuencia | Fuente |
|---|---|---|---|
| Accesos no autorizados al Datacenter | 0 | Mensual | Bitácora de acceso |
| Disponibilidad del UPS/generador | 100% | Mensual | Registro de pruebas |
| Temperatura del Datacenter fuera de rango | < 1 hora acumulada/mes | Continuo | Monitoreo ambiental |
| Cumplimiento de escritorio limpio | > 90% | Trimestral | Auditoría visual aleatoria |
| Tiempo de retención de CCTV | >= 90 días | Mensual | Verificación del sistema |

## 14. Documentos Relacionados

| Código | Nombre |
|---|---|
| P-SGSI-03 | Gestión de Identidades y Control de Acceso |
| P-SGSI-05 | Resiliencia y Continuidad en Nube Híbrida |
| P-SGSI-07 | Procedimiento de Eliminación Segura de Información |
| POL-SGSI-05 | Política de Seguridad para Dispositivos Móviles del Personal |
| F-SGSI-05 | Acta de Eliminación Segura de Activos |
| F-SGSI-06 | Bitácora de Acceso a Áreas Críticas |

***

**Aprobado por:**
Comité de Gobierno y Transformación Digital — UNCP
