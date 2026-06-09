---
title: "Resumen Ejecutivo Directivo: Propuesta del Plan de Gobierno y Transformación Digital (PGTD 2026-2030) y Diseño del SGSI-UNCP"
subtitle: "Dirigido a la Alta Dirección, Rectorado y Comité de Gobierno y Transformación Digital"
author: "Oficina de Tecnologías de la Información (OTI)"
date: "Huancayo, Junio de 2026"
...

# Relación con el Plan de Gobierno Digital Vigente

La Universidad Nacional del Centro del Perú (UNCP) cuenta actualmente con el **Plan de Gobierno Digital (PGD) 2025-2027**, formalmente aprobado mediante la **Resolución Rectoral N.° 3887-R-2025**. Este es el instrumento de gestión legalmente vigente de la institución. 

El presente documento de **Plan de Gobierno y Transformación Digital (PGTD) 2026-2030** constituye una **propuesta estratégica de actualización y evolución** del plan vigente. Esta propuesta ha sido diseñada para:
1.  Alinear el horizonte de planificación tecnológica con el Plan Estratégico Institucional (PEI) 2024-2030 (aprobado por R. N.° 3934-CU-2024).
2.  Adecuar las directrices tecnológicas de la UNCP a la Política Nacional de Transformación Digital al 2030 (D.S. N.° 103-2023-PCM) y a las recientes normas del gobierno peruano (tales como el D.S. N.° 016-2024-JUS de Protección de Datos y el D.S. N.° 098-2025-PCM modificatorio del reglamento de la LGD).

---

# Diagnóstico de la Situación Actual (AS-IS 2026)

El diagnóstico de la infraestructura, redes y sistemas de la UNCP en base a la documentación vigente y la Encuesta Nacional de Activos Digitales (ENAD 2025) evidencia las siguientes brechas y realidades operativas:

## Capacidad Operativa y Cambios organizacionales en OTI
*   **Jefatura de OTI / Oficialía de Seguridad:** Tras la designación inicial del Oficial de Seguridad de la Información integrada al CGD mediante la **Resolución N.° 2143-R-2023**, la Jefatura de la OTI ha experimentado una actualización reciente. El directorio vigente del Comité de Gobierno y Transformación Digital se encuentra en proceso de actualización y validación formal.
*   **Estructura de Personal:** El número exacto de personal de planta permanente de la OTI se encuentra **[PENDIENTE DE CONFIRMACIÓN DE CANTIDAD EXACTA POR PARTE DE OTI]**. 
*   **Colaboración de Practicantes:** De forma complementaria y con fines de formación preprofesional, la OTI recibe el apoyo de practicantes para tareas operativas menores y soporte técnico básico de primer nivel. Sus accesos lógicos están limitados de forma estricta, excluyéndose de la administración de sistemas críticos o datos de producción.

## Burocracia en Adquisiciones del Estado
*   **Procesos de Compra:** Las adquisiciones de bienes y servicios tecnológicos (servidores, licencias, firewalls) bajo la Ley de Contrataciones del Estado son complejas y burocráticas. Representan históricamente cuellos de botella con retrasos de entre **6 y 12 meses** para la renovación de soportes y hardware perimetral.

## Brechas de Seguridad Identificadas en Redes y Sistemas
*   **Seguridad Física y de Datos:** El Data Center central de Huancayo presenta deficiencias en control de acceso biométrico en los racks de servidores y falta de monitoreo ambiental automatizado. Adicionalmente, las bases de datos del ERP ADESA y Recursos Humanos carecen de cifrado de datos en reposo.
*   **Frontera de APIs y Redes de Filiales:** Las filiales perimetrales de Tarma, Satipo y Mantaro se interconectan mediante enlaces WAN (fibra, radioenlace, conexión móvil) que operan sobre una red plana de enrutamiento simple. Esto representa una vulnerabilidad de red, permitiendo la posibilidad técnica de pivotar lateralmente desde una red académica perimetral hacia los servidores centrales de administración en Huancayo. Las APIs de consulta pública y verificación de certificados (FUDEC, Pregrado, UNCP) operan sin WAF perimetral ni control de tasa de consultas (Rate Limiting).
*   **Control de Versiones y Código Fuente:** No se cuenta con una plataforma institucional centralizada y unificada de control de versiones en el AS-IS. El código fuente de las aplicaciones locales se gestiona de forma fragmentada en servidores locales de la OTI o repositorios de desarrollo individuales, sin auditoría de accesos.

---

# Portafolio de Proyectos Estratégicos Propuestos (TO-BE)

Para mitigar los riesgos del AS-IS, la propuesta del PGTD se organiza en base a los siguientes proyectos estratégicos:

*   **PGTD-01: Implementación del SGSI y Marco de Ciberdefensa (S/ 850,000 / 30 meses):** Diseño y despliegue del Sistema de Gestión de Seguridad de la Información (ISO/IEC 27001:2022).
*   **PGTD-02: Portal de Servicios Digitales e Identidad Única:** Autenticación centralizada (SSO con MFA) e interoperabilidad nativa vía la PIDE de PCM (SUNEDU, RENIEC).
*   **PGTD-03: Modernización y Eco-eficiencia del Data Center (Green IT):** Transición a nube híbrida activo-activo complementada con métricas de sostenibilidad y reducción de la huella de carbono digital en los nodos físicos.
*   **PGTD-04: Transición a IPv6 perimetral:** Plan de adopción progresiva de direccionamiento Dual-Stack.
*   **PGTD-05: Redes unificadas (SD-WAN) y Microsegmentación (Zero Trust):** Autenticación IEEE 802.1X en Core y conectividad SD-WAN cifrada para proteger las transacciones de las filiales.
*   **PGTD-06: Visibilidad de Eventos y CSIRT Universitario:** Correlación activa de logs de seguridad local y nube mediante Wazuh SIEM perimetral.

---

# Estrategias Clave de Implementación y Gobernanza

## Resolución del Conflicto de Interés
*   **Propuesta de Puesto CAS:** Se propone la creación e inclusión en presupuesto de una **plaza CAS dedicada** para un Administrador de Seguridad de la Información / Auditor de TI.
*   **Solución Transitoria:** Mientras se tramita la plaza CAS, un miembro del equipo técnico permanente actual de la OTI (distinto al jefe de desarrollo) asumirá temporalmente la función de suplencia de seguridad para la validación y auditoría de los cambios de código y pases a producción en los sistemas institucionales (proponiendo evaluar e implementar una solución centralizada de control de versiones bajo el proyecto PGTD-01). Esto asegura que el área de desarrollo no valide de forma unilateral sus propios despliegues.

## Implementación Progresiva frente al Rechazo Cultural
*   **Despliegue por Fases:** La adopción de controles lógicos estrictos (MFA obligatorio, bloqueo de puertos USB en terminales administrativos, control de software) se implementará de forma progresiva para mitigar la resistencia al cambio del personal docente y administrativo:
    *   *Fase 1:* OTI y miembros del Comité de Gobierno y Transformación Digital.
    *   *Fase 2:* Oficinas administrativas centrales de la sede Huancayo (DGA, Planillas, Abastecimiento).
    *   *Fase 3:* Personal docente, facultades y filiales periféricas (Tarma, Satipo, Mantaro).
*   **Acompañamiento y Capacitación:** El despliegue de cada fase irá precedido de talleres prácticos de concientización para facilitar la transición.

---

# Siguientes Pasos y Compromisos ante CGR

1.  **Registro de Software Público (Compromiso 13 CGR):** Registrar el código fuente del ERP ADESA ante la PCM, amparado en la designación de software público establecida por la **R. N.° 2140-R-2023**.
2.  **Transición a IPv6 (Compromiso 14 CGR):** Presentar al Comité de Gobierno y Transformación Digital el cronograma detallado de adopción de IPv6 perimetral.
3.  **Validación de Compromisos CGR Internos:** Solicitar las evidencias correspondientes para verificar el estado de los compromisos de Datos Abiertos (Compromiso 8), Encuesta de Activos Digitales (Compromiso 17) y Oficial de Gobierno de Datos (Compromiso 20).
