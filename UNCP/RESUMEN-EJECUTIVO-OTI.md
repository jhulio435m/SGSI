---
title: "Resumen Ejecutivo Técnico: Arquitectura y Estrategia del SGSI-UNCP"
subtitle: "Diseñado para la Jefatura de la Oficina de Tecnologías de la Información (OTI)"
author: "Equipo Consultor SGSI - UNCP"
date: "Junio de 2026"
numbersections: true
...

# Relación con el Plan de Gobierno Digital Vigente

El instrumento de gestión de tecnologías de la información legalmente vigente en la universidad es el **Plan de Gobierno Digital (PGD) 2025-2027**, aprobado formalmente por la **Resolución Rectoral N.° 3887-R-2025**.

El presente **Plan de Gobierno y Transformación Digital (PGTD) 2026-2030** constituye una **propuesta estratégica de actualización y evolución** del plan vigente. Busca modernizar el ecosistema tecnológico de la UNCP, adaptándolo al Plan Estratégico Institucional (PEI) 2024-2030 (Resolución N.° 3934-CU-2024) y a los recientes cambios normativos de PCM y del gobierno nacional en ciberseguridad, nube híbrida y protección de datos.

---

# Diagnóstico de la Situación Actual (AS-IS 2026)

El diagnóstico técnico de infraestructura, redes y sistemas en base a la documentación vigente y la Encuesta Nacional de Activos Digitales (ENAD 2025) presenta los siguientes factores y brechas operativas:

## Capacidad Operativa y Cambios en OTI
*   **Jefatura y Oficialía de Seguridad:** Tras la designación inicial del Oficial de Seguridad de la Información integrado al CGD mediante la **Resolución N.° 2143-R-2023**, la Jefatura de la OTI ha experimentado una actualización reciente. El directorio oficial del Comité se encuentra en proceso de validación formal.
*   **Personal Técnico Permanente:** La cantidad exacta de personal de planta de OTI está **[PENDIENTE DE CONFIRMACIÓN DE CANTIDAD EXACTA POR PARTE DE OTI]**. Este equipo de planta es el único responsable de la administración de la infraestructura y sistemas.
*   **Colaboración Preprofesional:** La OTI cuenta de manera complementaria con el apoyo de practicantes estudiantes de Ingeniería de Sistemas (FIIS) bajo un esquema de formación académica. Sus actividades se limitan estrictamente a tareas operativas menores y soporte técnico básico de primer nivel, manteniéndose excluidos del acceso o privilegios administrativos sobre bases de datos de producción y sistemas críticos.

## Burocracia en Adquisiciones del Estado
*   **Procesos de Compra:** La ejecución de compras públicas bajo la Ley de Contrataciones del Estado es compleja y burocrática. Esto genera retrasos históricos de entre **6 y 12 meses** para la adquisición de hardware perimetral, renovación de licencias de firewalls y contratación de servicios de nube.

## Brechas Críticas de Redes y Desarrollo de Software
*   **Exposición de APIs de Consulta Pública:** Los portales de consulta perimetrales y de verificación de certificados (FUDEC, Pregrado, UNCP), el sistema de comedor y el del Centro Médico operan de forma fragmentada en servidores locales de las facultades sin WAF, ni cifrado de base de datos en reposo y sin límites de tasa (Rate Limiting).
*   **Red de Filiales:** Las filiales perimetrales de Tarma, Satipo y Mantaro se interconectan con la sede central a través de enlaces WAN (fibra, radioenlace, conexión móvil) sobre una red plana de enrutamiento simple. Esto representa una vulnerabilidad de red, permitiendo la posibilidad técnica de pivotar lateralmente desde una red académica externa hacia la red interna de administración en Huancayo.

---

# Arquitectura y Diseño Tecnológico del SGSI (Modelo TO-BE)

La propuesta TO-BE del SGSI plantea los siguientes proyectos clave del portafolio:

*   **PGTD-01: SGSI ISO 27001 (S/ 850,000 / 30 meses):** Diseño y despliegue del Sistema de Gestión de Seguridad de la Información (ISO/IEC 27001:2022).
*   **PGTD-02: Portal de Servicios Digitales e Identidad Única:** SSO con MFA e interoperabilidad nativa vía la PIDE de PCM (SUNEDU, RENIEC).
*   **PGTD-03: Modernización del Data Center (Green IT):** Migración a nube híbrida activo-activo y métricas de eco-eficiencia digital.
*   **PGTD-04: Transición a IPv6 perimetral:** Plan de adopción progresiva de direccionamiento Dual-Stack.
*   **PGTD-05: Redes unificadas (SD-WAN) y Microsegmentación (Zero Trust):** Autenticación IEEE 802.1X en Core y conectividad SD-WAN cifrada para proteger las transacciones de las filiales.
*   **PGTD-06: Visibilidad de Eventos y CSIRT Universitario:** SIEM Wazuh perimetral.
```{=latex}
\begin{center}
\includegraphics[width=0.6\textwidth]{pgtd/imagenes/arquitectura_hibrida.png}
\end{center}
```


## Topología y Microsegmentación de Red (Control A.8.20 y A.8.22)
*   **Segmentación por VLANs (IEEE 802.1X):** Control de accesos a nivel de Core para aislar:
    *   VLAN 10: Servidores locales y base de datos del ERP ADESA.
    *   VLAN 20: Personal administrativo (con políticas LDAP restrictivas).
    *   VLAN 30: Personal docente.
    *   VLAN 40: Wi-Fi estudiantil (red perimetral con portal cautivo).
    *   VLAN 50: Videovigilancia y control de accesos.
*   **Perímetro Defensivo:** Despliegue de perfiles NGFW activos: prevención de intrusiones (IPS), inspección profunda de paquetes SSL/TLS (Deep Packet Inspection), y filtrado de aplicaciones para bloquear túneles VPN no autorizados.

## Telemetría y SIEM (Control A.8.16)
*   **Estrategia de Visibilidad:** Captura pasiva mediante **TAP físico** y puertos espejo (**SPAN**) en switches de distribución. Correlación activa de logs perimetrales, syslogs de servidores locales y virtuales, y telemetría de flujos (**NetFlow v9** / SNMPv3) con Wazuh SIEM perimetral.

---

# Ingeniería de Software y Seguridad Ágil (DevSecOps)

Para salvaguardar los desarrollos del ERP ADESA y las APIs públicas de las filiales:
```{=latex}
\begin{center}
\includegraphics[width=0.6\textwidth]{pgtd/imagenes/flujo_integracion.png}
\end{center}
```


## Control de Versiones e Integración de Código
*   **Repositorios Centralizados:** Se propone centralizar de forma obligatoria el código fuente en una plataforma o servidor Git institucional (ej. GitHub, GitLab o solución autohospedada), configurando repositorios privados con autenticación centralizada y MFA una vez que se implemente bajo el proyecto PGTD-01.
*   **Políticas de Integración:** Restricción de la subida directa de cambios a las ramas estables o de producción. Se propone establecer un flujo de control de cambios integrado donde la integración del código requiera una validación previa técnica o automatizada.
*   **Escaneo de Seguridad Integrado:** Implementación de herramientas para el escaneo de código en busca de fugas accidentales de secretos (credenciales o claves de API).

## CI/CD y Pruebas Automatizadas
*   **SAST & SCA:** Escaneo automatizado de código (SonarQube) para mitigar fallas (SQLi, XSS) y análisis de dependencias (Dependency-Check) para generar el inventario de librerías (**SBOM**).
*   **Integración de Firmas:** Uso de firmas en confirmaciones de cambios (commits) para asegurar la trazabilidad y autoría del código.

---

# Resiliencia Operativa y Plan de Recuperación ante Desastres (DRP)

Alineado con el Plan de Continuidad Operativa de la UNCP (aprobado por **Resolución N.° 3255-R-2024**):

*   **Réplica en Nube:** Replicación continua asincrónica de bases de datos mediante enlace VPN IPsec seguro hacia instancias RDS de Huawei Cloud.
*   **Balanceo Global DNS (GSLB):** El GSLB de Huawei Cloud monitorea activamente la salud del nodo local. Ante un fallo de conectividad física en Huancayo, actualiza automáticamente los registros DNS para desviar las solicitudes HTTPS al nodo contingente en la nube en menos de 1 minuto.

---

# Privacidad de Datos y Gobierno de la Información (Ley N.° 29733)

*   **Enmascaramiento Obligatorio:** Anonimización automática mediante scripts para la sustitución de datos sensibles en el entorno de pruebas de practicantes.
*   **Logs de Auditoría en ERP ADESA:** Middleware dedicado que audita cualquier consulta o modificación en campos de datos personales (nombres, notas, planillas), exportando los registros cifrados directamente al SIEM (Wazuh).

---

# Estrategias de Gobernanza y Despliegue Técnico (TO-BE)

Para asegurar la viabilidad del proyecto frente a las limitaciones de personal y resistencia al cambio en el AS-IS, se plantean las siguientes estrategias:

## Resolución del Conflicto de Interés
*   **Plaza CAS de Seguridad:** Se propone como prioridad presupuestal la creación de una **plaza CAS dedicada** para un Administrador de Seguridad de la Información / Auditor de TI.
*   **Delegación Transitoria:** Mientras se formaliza la plaza CAS, un integrante del equipo técnico permanente actual de la OTI (distinto al jefe de desarrollo) asumirá el rol de suplencia de seguridad para validar técnicamente y auditar los pases a producción en los sistemas institucionales, evitando que el área de desarrollo valide de forma unilateral sus propios despliegues.

## Despliegue Progresivo frente a Resistencia Cultural
*   **MFA y Restricciones Lógicas:** Para evitar el rechazo inicial de docentes y administrativos frente a controles restrictivos (MFA obligatorio, bloqueos de puertos USB perimetrales), el despliegue se realizará de forma progresiva:
    *   *Fase 1:* OTI y miembros del Comité de Gobierno y Transformación Digital.
    *   *Fase 2:* Oficinas administrativas centrales de la sede Huancayo (DGA, Planillas, Abastecimiento).
    *   *Fase 3:* Personal docente, facultades y filiales periféricas (Tarma, Satipo, Mantaro).
*   **Capacitación Previa:** Cada fase irá precedida de talleres de concientización y soporte técnico local para facilitar la transición del usuario.

## Registro de Software Público (Compromiso 13 CGR)
*   Remitir la ficha técnica del ERP ADESA a la PCM, formalizando su registro según la designación de Responsable del Software Público de la **R. N.° 2140-R-2023**.

## Transición a IPv6 (Compromiso 14 CGR)
*   Diseñar el plan de Dual-Stack IPv4/IPv6 en los routers perimetrales de la UNCP.

## Validación de Compromisos CGR Internos
*   Coordinar internamente la recopilación de evidencias para verificar el estado de Datos Abiertos (Compromiso 8), Encuesta de Activos Digitales (Compromiso 17) y Oficial de Gobierno de Datos (Compromiso 20).
