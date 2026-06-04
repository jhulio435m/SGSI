# POL-SGSI-02: Política de Uso Aceptable, Escritorio Limpio, Teletrabajo y Comunicaciones

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 2.0
**Norma:** ISO/IEC 27001:2022 (Controles A.5.10 — Uso aceptable, A.6.7 — Teletrabajo, A.7.7 — Escritorio y pantalla limpios, A.8.10 — Eliminación de información, A.8.23 — Filtrado web)
**Alineamiento:** POL-SGSI-05 (Dispositivos Móviles), POL-SGSI-06 (Contraseñas), P-SGSI-02 (Gestión de Incidentes)

***

## 1. Objetivo
Establecer las normas de conducta que todo usuario de los recursos informáticos de la UNCP debe observar, garantizando un uso adecuado, ético y seguro de los activos de información institucionales.

## 2. Alcance
Esta política aplica a todo el personal administrativo, docente, autoridades, contratistas y cualquier tercero que utilice los recursos informáticos o acceda a la información de la UNCP. Los estudiantes están sujetos a las disposiciones de uso aceptable del reglamento académico y a las campañas de concientización definidas en el P-SGSI-08.

---

## 3. Política de Uso Aceptable (Control A.5.10)

### 3.1 Uso de Recursos Institucionales
- Los recursos informáticos de la UNCP (correo, internet, sistemas, equipos) son proporcionados para fines institucionales. Se permite un uso personal incidental siempre que no interfiera con las funciones laborales, no consuma recursos excesivos y no infrinja esta política.
- Queda prohibido el uso de los sistemas de la UNCP para:
  - Actividades ilegales o no éticas (acoso, discriminación, difamación, pornografía, apuestas).
  - Descarga, instalación o distribución de software sin licencia (software pirata).
  - Acceso no autorizado a sistemas, cuentas o información de otros usuarios.
  - Actividades que puedan dañar la reputación de la UNCP.
  - Minería de criptomonedas o cualquier uso intensivo de recursos no autorizado.
  - Participación en ataques de denegación de servicio, hacking, o cualquier actividad maliciosa.

### 3.2 Correo Electrónico
- El correo institucional es propiedad de la UNCP y debe usarse preferentemente para comunicaciones académicas y administrativas.
- Queda prohibido:
  - Enviar correos masivos no autorizados (spam), cadenas de correos o material publicitario no institucional.
  - Suplantar la identidad de otro usuario (spoofing).
  - Enviar información clasificada como Confidencial sin cifrado (según POL-SGSI-03).
  - Usar el correo institucional para registrarse en servicios personales (redes sociales no laborales, servicios de streaming, etc.).
- Los correos electrónicos institucionales no deben considerarse privados. La UNCP se reserva el derecho de acceder a los buzones en caso de investigación legal o necesidad operativa, con la debida autorización.

### 3.3 Internet y Navegación Web
- El acceso a Internet se proporciona para fines laborales. La navegación es monitoreada y registrada.
- Categorías de sitios bloqueados por el proxy/filtro web:
  - Contenido ilegal, pornográfico, violencia explícita.
  - Piratería de software, torrents, sitios de descarga no autorizados.
  - Juegos de azar, apuestas online.
  - Sitios de hacking o que promuevan actividades maliciosas.
  - Redes sociales y streaming de video (permitido en horario de refrigerio, excepto para áreas que requieran su uso laboral).
- Cualquier intento de eludir el proxy/filtro web (VPN no autorizada, túneles, proxies web) está prohibido.

### 3.4 Software y Licencias
- Solo el personal de la OTI puede instalar software en equipos institucionales.
- El uso de software sin licencia está terminantemente prohibido.
- El personal no debe instalar software en sus estaciones de trabajo sin autorización de la OTI.
- Las licencias de software deben ser gestionadas por la OTI y registradas en el inventario de activos de software.

### 3.5 Redes Sociales y Comunicación Pública
- El personal que publique en redes sociales en representación de la UNCP debe hacerlo siguiendo los lineamientos de comunicación institucional y abstenerse de divulgar información interna no autorizada.
- Queda prohibido publicar información clasificada como Confidencial o Uso Interno en redes sociales personales.
- Los comentarios sobre la UNCP en redes personales deben ser éticos y respetuosos.

---

## 4. Política de Escritorio y Pantalla Limpia (Control A.7.7)

- Al ausentarse del puesto de trabajo, todo documento clasificado como **Confidencial** o **Uso Interno** debe guardarse bajo llave en un archivador o cajón cerrado.
- No se debe dejar información sensible visible sobre el escritorio (notas, actas, planillas, contraseñas escritas en papel).
- Las pantallas de las computadoras deben bloquearse automáticamente tras **5 minutos** de inactividad, mediante política de grupo o MDM. El bloqueo manual (Win+L) es obligatorio al ausentarse, incluso por períodos cortos.
- Al finalizar la jornada laboral, todo documento sensible debe estar guardado, la computadora apagada o bloqueada, y el escritorio despejado.
- Las impresiones de documentos confidenciales deben retirarse inmediatamente de las bandejas de las impresoras. No deben dejarse documentos impresos desatendidos.

---

## 5. Política de Teletrabajo y Trabajo Remoto (Control A.6.7)

### 5.1 Condiciones Generales
- El teletrabajo solo está permitido para el personal que cuente con autorización expresa de su jefe inmediato y de la OTI.
- El personal en teletrabajo debe utilizar **obligatoriamente la VPN institucional** con MFA para acceder a cualquier sistema de la UNCP.
- Queda prohibido el acceso a sistemas críticos (ERP ADESA, SIGA, SIAF, bases de datos) desde redes Wi-Fi públicas abiertas (hoteles, aeropuertos, cafeterías) o equipos compartidos.

### 5.2 Entorno de Trabajo
- El personal debe garantizar que su entorno de trabajo remoto sea seguro:
  - La pantalla del equipo no debe ser visible para terceros no autorizados.
  - Las conversaciones y llamadas de trabajo deben realizarse en un entorno privado.
  - Los documentos impresos en el domicilio deben ser protegidos y destruidos de forma segura cuando ya no sean necesarios.

### 5.3 Dispositivos en Teletrabajo
- Aplican todos los requisitos de la **POL-SGSI-05 (Dispositivos Móviles)**, incluyendo cifrado, bloqueo de pantalla y actualizaciones.
- El robo o pérdida del dispositivo debe reportarse según el procedimiento establecido en la POL-SGSI-05 (máximo 2 horas).

---

## 6. Almacenamiento y Transferencia de Información

- Los datos institucionales deben almacenarse exclusivamente en:
  - Servidores institucionales (locales o cloud autorizado como Huawei Cloud).
  - Carpetas de red compartidas.
  - Microsoft 365 (OneDrive for Business, SharePoint) proporcionado por la UNCP.
- Queda **prohibido** almacenar datos institucionales clasificados como Confidenciales o de Uso Interno en:
  - Servicios cloud personales (Google Drive personal, Dropbox personal, iCloud personal).
  - Memorias USB no cifradas.
  - Equipos personales no gestionados por la OTI (salvo excepciones del programa BYOD según POL-SGSI-05).

---

## 7. Monitoreo y Privacidad

- El usuario no debe tener expectativa de privacidad absoluta al utilizar los recursos informáticos de la UNCP. Los sistemas pueden ser monitoreados para garantizar la seguridad, el cumplimiento de políticas y la continuidad operativa.
- El monitoreo incluye, sin limitarse a: logs de navegación web, registro de acceso a sistemas, correo electrónico (metadatos y contenido en investigaciones autorizadas), uso de aplicaciones.
- Cualquier investigación que implique la revisión del contenido de comunicaciones de un usuario debe ser autorizada por el Comité de Gobierno Digital o la autoridad competente.

---

## 8. Reporte de Incidentes

Todo usuario tiene la obligación de reportar cualquier incidente de seguridad, actividad sospechosa o incumplimiento de esta política a través de:
- Correo: `incidentes-seguridad@uncp.edu.pe`
- Mesa de ayuda: [teléfono/extensión de la OTI]
- Reporte directo al jefe inmediato (quien debe escalar a la OTI).

---

## 9. Incumplimiento

El incumplimiento de esta política puede resultar en:
- Amonestación verbal o escrita.
- Suspensión temporal o permanente del acceso a los recursos informáticos.
- Medidas disciplinarias según el régimen laboral aplicable.
- Acciones legales en caso de actividades ilegales.

---

## 10. Documentos Relacionados

| Código | Nombre |
|---|---|
| POL-SGSI-05 | Política de Seguridad para Dispositivos Móviles del Personal |
| POL-SGSI-06 | Política de Contraseñas y Autenticación Segura |
| POL-SGSI-03 | Política de Clasificación de la Información y Respaldos |
| P-SGSI-02 | Marco de Respuesta a Incidentes (CSIRT) |
| P-SGSI-08 | Plan Anual de Capacitación y Concientización |

***

**Versión 2.0 — Incluye secciones de correo electrónico, navegación web, licencias de software, redes sociales, almacenamiento de datos, monitoreo y privacidad.**
