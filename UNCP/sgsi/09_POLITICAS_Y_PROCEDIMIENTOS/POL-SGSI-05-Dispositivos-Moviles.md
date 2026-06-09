---
title: Política de Seguridad para Dispositivos Móviles del Personal
code: POL-SGSI-05
---

# Política de Seguridad para Dispositivos Móviles del Personal

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Norma:** ISO/IEC 27001:2022 (Controles A.8.1, A.6.7, A.5.10)
**Alineamiento:** D-SGSI-02 (Alcance del SGSI), P-SGSI-03 (Gestión de Accesos), P-SGSI-02 (Gestión de Incidentes)

***

## Objetivo
Establecer medidas de seguridad proporcionales para proteger la información institucional procesada, almacenada o accedida desde dispositivos móviles (laptops, smartphones, tablets), diferenciando entre equipos institucionales bajo control de la UNCP, dispositivos personales usados voluntariamente para fines laborales (BYOD) y dispositivos personales de estudiantes o docentes usados solo para servicios académicos generales.

## Alcance

### 2.1 Sujetos Obligados
Esta política aplica de forma obligatoria a todo **Personal Administrativo, Autoridades, Contratistas y Docentes** cuando utilicen dispositivos institucionales asignados por la UNCP o cuando accedan a sistemas administrativos, datos personales de terceros, registros académicos, expedientes, sistemas internos o activos de información cubiertos por el SGSI-UNCP.

Los dispositivos personales de docentes no quedan bajo control técnico general de la universidad. Solo se aplicarán condiciones de acceso cuando el docente solicite voluntariamente usar BYOD para funciones laborales que involucren información institucional no pública o sistemas internos.

### 2.2 Alcance Obligatorio (Personal)
Aplica a dispositivos institucionales y a dispositivos personales inscritos voluntariamente en BYOD para acceso laboral. El cumplimiento es **exigible** sobre el acceso a recursos institucionales y sobre los activos de información de la UNCP; no implica control general sobre el dispositivo personal completo.

### 2.3 Alcance Informativo (Estudiantes y uso académico general)
La Universidad no ejerce control técnico ni jurídico sobre los dispositivos personales de alumnos y docentes usados para actividades académicas generales, por lo que no puede imponer requisitos de seguridad obligatorios sobre dichos equipos. Sin embargo, en su compromiso con la protección de la información académica y datos personales, la UNCP establece el siguiente **alcance informativo y de concientización** dirigido a la comunidad universitaria:

#### 2.3.1 Campañas de Concientización
Se implementará un programa anual de concientización en seguridad móvil para estudiantes, con los siguientes componentes:

| Actividad | Descripción | Frecuencia | Canal |
|---|---|---|---|
| **Cápsulas formativas** | Contenido breve sobre riesgos móviles: phishing, redes Wi-Fi públicas, protección de credenciales | Bimestral | Campus Virtual (Moodle) / Redes sociales UNCP |
| **Guía de seguridad móvil** | Documento descargable con recomendaciones prácticas para proteger dispositivos y cuentas | Publicación única + actualización anual | Portal institucional |
| **Infografías periódicas** | Tips visuales sobre cifrado, bloqueo de pantalla, actualizaciones y apps seguras | Mensual | Correo institucional estudiantil / Redes sociales |
| **Semana de la Ciberseguridad** | Evento anual con charlas, talleres y simulacros de phishing dirigidos a la comunidad estudiantil | Anual | Presencial / Streaming |
| **Alertas de amenazas** | Comunicados sobre amenazas activas detectadas (campañas de phishing, apps maliciosas, fraudes) | Según evento | Correo institucional / SMS / Redes sociales |

#### 2.3.2 Recomendaciones de Seguridad para Estudiantes
La UNCP recomienda a sus estudiantes adoptar las siguientes prácticas para proteger su información académica y personal:

1. **Cifrado:** Activar el cifrado nativo del dispositivo (Android/iOS se encuentra activado por defecto al establecer un código de acceso).
2. **Bloqueo de pantalla:** Configurar PIN, patrón o biometría con bloqueo automático a los 2 minutos como máximo.
3. **Actualizaciones:** Mantener el sistema operativo y las aplicaciones actualizadas.
4. **Redes Wi-Fi:** Evitar acceder al campus virtual, correo institucional o sistemas de matrícula desde redes Wi-Fi públicas o abiertas.
5. **Apps oficiales:** Utilizar exclusivamente las aplicaciones oficiales de la UNCP (Moodle Mobile, Microsoft 365) descargadas desde tiendas oficiales (Google Play, App Store).
6. **Phishing:** No hacer clic en enlaces sospechosos ni proporcionar credenciales institucionales en sitios no verificados.
7. **Reporte:** Reportar cualquier actividad sospechosa o pérdida de acceso a la mesa de ayuda de la OTI a través del correo incidentes-seguridad@uncp.edu.pe.

#### 2.3.3 Límites del Alcance Informativo
- Ninguna de las recomendaciones anteriores constituye una obligación exigible para los estudiantes.
- El incumplimiento de estas recomendaciones no generará medidas disciplinarias académicas ni restricciones sobre los servicios estudiantiles.
- La UNCP no se hace responsable por compromisos de información académica derivados del uso inseguro de dispositivos personales por parte de los estudiantes, siempre que haya cumplido con su deber de informar y concientizar.

### 2.4 Tipos de Dispositivo Cubiertos

| Tipo | Ejemplos | Nivel de Control Aplicable |
|---|---|---|
| **Laptop institucional** | Equipo asignado por la OTI | Control total: cifrado, MDM, inventario obligatorio |
| **Smartphone institucional** | Equipo con línea corporativa | Control total: MDM, perfil de trabajo, borrado remoto |
| **Tablet institucional** | Equipo para uso en campo | Control total: mismas reglas que laptop |
| **BYOD — Laptop personal autorizada** | Equipo personal usado voluntariamente para funciones laborales | Control de acceso: VPN + MFA + contenedor o perfil separado cuando aplique |
| **BYOD — Smartphone personal autorizado** | Teléfono personal con correo o apps UNCP para funciones laborales | Control de acceso: perfil de trabajo recomendado; sin control sobre datos personales |
| **Dispositivo personal de estudiante/docente para uso académico general** | Equipo usado para Moodle, correo, consulta de notas o servicios públicos | Sin control técnico obligatorio; recomendaciones, MFA cuando esté disponible y bloqueo de acceso ante compromiso de cuenta |

## Requisitos de Seguridad

### 3.1 Cifrado del Dispositivo
Todo dispositivo institucional o BYOD autorizado que almacene o acceda a información institucional no pública debe tener el almacenamiento interno cifrado mediante mecanismos nativos del sistema operativo:

| SO | Mecanismo Exigido |
|---|---|
| Windows | BitLocker con TPM + PIN de arranque |
| macOS | FileVault 2 |
| iOS | Cifrado nativo por hardware (activado por defecto con código de acceso) |
| Android | Cifrado basado en archivos (Android 10+) con PIN de arranque |

El Oficial de Seguridad podrá realizar verificaciones periódicas del estado de cifrado mediante MDM o auditoría directa solo sobre dispositivos institucionales o BYOD inscritos. Para dispositivos personales no inscritos, el cifrado se mantiene como recomendación de seguridad.

### 3.2 Bloqueo de Pantalla y Autenticación
- **Mecanismo aceptado:** PIN (mínimo 6 dígitos), patrón complejo (mínimo 6 nodos), huella dactilar o reconocimiento facial.
- **Tiempo de bloqueo automático:** Máximo **2 minutos** de inactividad.
- **Política de tolerancia a fallos:** Tras 5 intentos fallidos de desbloqueo, el dispositivo debe ejecutar un borrado local de los datos institucionales (wipe parcial o total según configuración MDM).
- Se prohíbe el uso de patrones de desbloqueo simples (línea recta, formas evidentes) o PINs predecibles (1234, fechas de nacimiento).

### 3.3 Integridad del Sistema y Restricciones de Software
Se prohíbe el acceso a sistemas internos, datos personales de terceros o recursos administrativos de la UNCP desde dispositivos institucionales o BYOD autorizados que presenten las siguientes condiciones:

- **Jailbreak** (iOS) o **root** (Android): cualquier modificación que eleve privilegios por encima de lo previsto por el fabricante.
- **Sistema operativo no oficial** (ROMs custom, builds no firmadas).
- **Gestor de arranque desbloqueado** sin autorización expresa de la OTI (solo aplica para equipos de desarrollo debidamente justificados).
- **Instalación de aplicaciones de fuentes no oficiales** (sideloading, tiendas de terceros) en dispositivos que acceden a datos institucionales.

La OTI implementará mecanismos de detección remota en dispositivos institucionales o BYOD inscritos y bloqueará el acceso al detectar incumplimiento. En dispositivos personales no inscritos solo podrá bloquear o reforzar la autenticación de la cuenta institucional cuando exista evidencia de compromiso.

### 3.4 Actualizaciones y Parches
- El usuario debe instalar las actualizaciones de seguridad del sistema operativo dentro de los **15 días calendario** posteriores a su publicación por el fabricante.
- Las actualizaciones críticas (parches de día cero o vulnerabilidades con CVE de severidad crítica) deberán instalarse en un plazo máximo de **72 horas**.
- No se permitirá la conexión a servicios UNCP desde dispositivos que ejecuten versiones de sistema operativo que hayan alcanzado su **fin de soporte (End of Life)** por parte del fabricante.
- La OTI podrá auditar el nivel de parches mediante el MDM en dispositivos institucionales o BYOD inscritos y restringir el acceso condicional en caso de incumplimiento.

### 3.5 Conexiones de Red y Acceso Remoto
- Queda prohibido el acceso a sistemas críticos (ERP ADESA, SIGA, SIAF, bases de datos, consolas de administración cloud) desde redes Wi-Fi públicas (aeropuertos, hoteles, cafeterías, centros comerciales) o redes no seguras.
- Todo acceso remoto a la red interna de la UNCP debe realizarse exclusivamente a través de la **VPN institucional** con autenticación multifactor (MFA) y solo desde dispositivos institucionales o BYOD autorizados.
- El tráfico de la VPN debe permanecer activo durante toda la sesión de acceso a recursos institucionales. No se permite el "split tunneling" para conexiones que manejen datos clasificados como Confidenciales o de Uso Interno.
- Para conexiones de bajo riesgo (correo web, portal institucional público) no es obligatorio el uso de VPN, pero sí de HTTPS/TLS 1.2 o superior.

### 3.6 Aplicaciones y Control de Software
- Solo se permite la instalación de aplicaciones aprobadas por la OTI en dispositivos institucionales. La lista de aplicaciones permitidas se publicará en el portal interno.
- Queda prohibida la instalación de aplicaciones de intercambio de archivos P2P, clientes de criptomonedas o software no licenciado.
- El personal debe utilizar exclusivamente las aplicaciones institucionales proporcionadas por la UNCP (Microsoft 365, Teams, Moodle Mobile) para el tratamiento de datos académicos y administrativos.

### 3.7 Separación de Datos Personales e Institucionales
En dispositivos BYOD, el personal debe garantizar que los datos institucionales se mantengan separados de los datos personales mediante:

- **Android:** Perfil de trabajo (Work Profile) gestionado por el MDM.
- **iOS:** Cuenta administrada con Managed Apple ID + contenedor de datos institucionales.
- **Laptops:** Partición o volumen cifrado independiente para datos laborales, o sesión de usuario separada.
- **Prohibición expresa:** No almacenar datos institucionales (actas, listas de notas, comunicaciones internas) en servicios personales de almacenamiento en la nube (Google Drive personal, iCloud personal, Dropbox personal).

## Gestión de Dispositivos Móviles (MDM)

### 4.1 Perfil Obligatorio
Todo dispositivo institucional que acceda a recursos internos de la UNCP deberá inscribirse en la plataforma de **Gestión de Dispositivos Móviles (MDM)** designada por la OTI. Los dispositivos personales solo se inscribirán si el usuario participa voluntariamente en el esquema BYOD autorizado para funciones laborales.

- Exigencia de cifrado y código de acceso.
- Borrado remoto selectivo (solo datos institucionales en BYOD) o total (en dispositivos institucionales).
- Bloqueo condicional por versión de SO, nivel de parche o detección de jailbreak/root.
- Instalación forzada de perfiles de VPN y Wi-Fi institucional.
- Restricción de instalación de aplicaciones no autorizadas.

### 4.2 Privacidad en BYOD
En dispositivos personales, el MDM se configurará bajo el principio de **mínima intervención**:

- El perfil MDM no recopilará datos personales del usuario (contactos, fotos, ubicación fuera del horario laboral, historial de navegación personal).
- La OTI solo podrá ejecutar acciones de borrado sobre el contenedor de datos institucionales, no sobre la partición personal del dispositivo.
- El empleado será notificado de forma transparente sobre el alcance de las políticas MDM antes de la inscripción.

### 4.3 Exclusiones del MDM
El Oficial de Seguridad podrá autorizar excepciones al perfil MDM en casos debidamente justificados (ej. dispositivos de investigación con software especializado incompatible), siempre que se apliquen controles compensatorios aprobados.

## BYOD — Procedimiento de Incorporación y Baja

### 5.1 Incorporación
1. El trabajador o docente presenta una solicitud mediante el formato **F-SGSI-01**, indicando que utilizará voluntariamente su dispositivo personal para fines laborales específicos.
2. El jefe inmediato autoriza la solicitud.
3. La OTI verifica que el dispositivo cumple los requisitos mínimos (versión de SO, capacidad de cifrado, compatibilidad con MDM).
4. Se instala el perfil MDM y se configura el contenedor de trabajo.
5. El solicitante firma el compromiso de cumplimiento de la presente política, limitado al contenedor, cuenta o acceso institucional autorizado.
6. La OTI registra el dispositivo en el inventario auxiliar de BYOD (no en el inventario de activos institucionales).

### 5.2 Baja y Desvinculación
- Al cesar la relación laboral o contractual, la OTI procederá al **borrado remoto inmediato** del contenedor de datos institucionales y a la desinscripción del MDM.
- El empleado que se desvincule voluntariamente del programa BYOD podrá solicitar la remoción del perfil MDM, previa verificación de que no existen datos institucionales en el dispositivo.
- En caso de pérdida o robo de un dispositivo BYOD, aplica el mismo procedimiento de la sección 6.2.

### 5.3 Riesgos Aceptados por el Usuario BYOD
El usuario que opte voluntariamente por BYOD acepta:
- Que el dispositivo será verificado periódicamente por el MDM para garantizar el cumplimiento.
- Que la OTI podrá bloquear el acceso a recursos UNCP si el dispositivo deja de cumplir los requisitos.
- Que los datos institucionales en el dispositivo podrán ser borrados remotamente sin posibilidad de recuperación por parte del usuario.

## Inventario, Pérdida y Robo

### 6.1 Inventario de Dispositivos Institucionales
- Todo dispositivo móvil de propiedad de la UNCP debe estar registrado en el inventario de activos de la OTI (**R-SGSI-01**) con los siguientes datos mínimos:
  - Número de serie y modelo.
  - IMEI (smartphones) y dirección MAC WiFi/Bluetooth.
  - Fecha de asignación y nombre del custodio.
  - Estado (activo, en reparación, dado de baja).
- Se realizará un inventario físico anual para conciliar los registros con los dispositivos asignados.

### 6.2 Procedimiento ante Pérdida, Robo o Extravío
1. **Reporte inmediato:** El usuario debe notificar a la OTI en un plazo máximo de **4 horas** desde el momento en que toma conocimiento de la pérdida o robo.
2. **Canales de reporte:** Llamada telefónica a la mesa de ayuda, portal de autoservicio de Microsoft 365, o correo electrónico a la dirección incidentes-seguridad@uncp.edu.pe.
3. **Acciones inmediatas de la OTI:**
   - Bloqueo de cuentas de acceso (correo, VPN, sistemas).
   - Borrado remoto del dispositivo (completo para equipos institucionales, selectivo para BYOD).
   - Revocación de certificados digitales almacenados en el equipo.
   - Registro del incidente en el sistema de gestión de incidentes (**P-SGSI-02**).
4. **Denuncia policial:** El usuario debe presentar la denuncia ante la comisaría dentro de las 24 horas siguientes y entregar una copia a la OTI para el expediente.

### 6.3 Reasignación y Baja de Activos
- Antes de reasignar un dispositivo institucional a otro usuario, la OTI debe realizar un formateo completo con borrado seguro (wipe conforme a **P-SGSI-07**).
- La baja definitiva de dispositivos por obsolescencia o daño debe registrarse en el formato **F-SGSI-05 (Acta de Eliminación Segura)**.

## Roles y Responsabilidades

| Rol | Responsabilidad |
|---|---|
| **Usuario (personal)** | Conocer y cumplir esta política; mantener su dispositivo actualizado y seguro; reportar incidentes de forma oportuna. |
| **Estudiantes y docentes en uso académico general** | Aplicar buenas prácticas recomendadas, proteger sus credenciales, activar MFA cuando esté disponible y reportar incidentes o accesos sospechosos. |
| **Jefe Inmediato** | Autorizar el acceso móvil y BYOD de su equipo; asegurar que el personal a su cargo recibe inducción en esta política. |
| **Oficial de Seguridad** | Mantener esta política actualizada; supervisar el cumplimiento; evaluar riesgos de dispositivos móviles. |
| **OTI (Mesa de Ayuda)** | Gestionar el MDM; atender reportes de pérdida/robo; ejecutar borrados remotos; mantener el inventario de dispositivos. |
| **OTI (Infraestructura)** | Configurar y mantener la VPN, el Conditional Access y las políticas de red para dispositivos móviles; realizar auditorías técnicas periódicas. |
| **Comité de Gobierno Digital** | Aprobar esta política y sus actualizaciones; revisar las métricas de cumplimiento de forma trimestral. |

## Métricas de Cumplimiento

| Indicador | Meta | Frecuencia | Fuente |
|---|---|---|---|
| % de dispositivos institucionales con cifrado activo | 100% | Mensual | MDM |
| % de dispositivos institucionales con SO sin soporte | < 2% | Trimestral | MDM |
| Tiempo medio de respuesta ante robo/pérdida | < 2 horas | Por evento | Sistema de tickets |
| % de personal capacitado en esta política | 100% | Anual | Moodle / F-SGSI-02 |
| % de BYOD inscritos con perfil activo | 100% de los autorizados | Mensual | MDM |
| % de estudiantes alcanzados por campañas de concientización móvil | 80% anual | Anual | Moodle / comunicaciones institucionales |

## Incumplimiento y Medidas Disciplinarias

El incumplimiento de esta política será gestionado de la siguiente forma:

| Nivel | Acción |
|---|---|
| **Leve** (olvido puntual de bloqueo, retraso en actualización) | Notificación por escrito del jefe inmediato; plazo de 5 días hábiles para subsanar. |
| **Grave** (acceso desde dispositivo con jailbreak/root, incumplimiento recurrente) | Restricción temporal del acceso remoto; comunicación al Comité de Gobierno Digital. |
| **Muy Grave** (fuga de datos por negligencia, pérdida de dispositivo sin reportar, incumplimiento doloso) | Restricción permanente del acceso remoto; apertura de proceso administrativo disciplinario según el régimen laboral aplicable; reporte a la Autoridad Nacional de Protección de Datos si corresponde (Ley N° 29733). |

## Revisión y Actualización
Esta política será revisada al menos una vez al año por el Oficial de Seguridad, o antes si ocurre un cambio significativo en el panorama de amenazas móviles, en la normativa nacional aplicable o en la infraestructura tecnológica de la UNCP. Las actualizaciones serán aprobadas por el Comité de Gobierno Digital.

## Documentos Relacionados

| Código | Nombre |
|---|---|
| D-SGSI-02 | Alcance del SGSI |
| P-SGSI-02 | Marco de Respuesta a Incidentes (CSIRT) |
| P-SGSI-03 | Gestión de Identidades y Control de Acceso |
| P-SGSI-07 | Procedimiento de Eliminación Segura de Información |
| POL-SGSI-02 | Política de Uso Aceptable, Escritorio y Teletrabajo |
| POL-SGSI-06 | Política de Contraseñas y Autenticación Segura |
| F-SGSI-01 | Formato de Solicitud de Alta/Baja/Cambio de Acceso |
| F-SGSI-03 | Formato de Baja de Usuario y Devolución de Activos |
| F-SGSI-05 | Acta de Eliminación Segura de Activos |
| R-SGSI-01 | Inventario de Activos de Información |

***
