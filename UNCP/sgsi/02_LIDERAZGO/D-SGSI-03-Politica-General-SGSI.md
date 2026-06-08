---
title: Política General de Seguridad de la Información
code: D-SGSI-03
---

# Política General de Seguridad de la Información

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Aprobado por:** Rector / Presidente del Comité de Gobierno Digital
**Norma:** ISO/IEC 27001:2022 (Cláusula 5.2)

***

## Declaración de Compromiso

La Universidad Nacional del Centro del Perú (UNCP), consciente de que la información es un activo crítico para el cumplimiento de sus fines misionales —formación académica, investigación científica y responsabilidad social— y en estricta alineación con el Plan de Gobierno y Transformación Digital (PGTD 2026-2030), la Política Nacional de Transformación Digital al 2030 (PNTD) y la Política General de Gobierno 2025-2026 (D.S. N.° 141-2025-PCM), establece la presente Política General de Seguridad de la Información.

La Alta Dirección, representada por el Rectorado y el Comité de Gobierno Digital (CGD), se compromete a liderar, respaldar y dotar de los recursos necesarios para la implementación, mantenimiento y mejora continua del Sistema de Gestión de Seguridad de la Información (SGSI), garantizando la confidencialidad, integridad y disponibilidad de la información institucional, protegiendo así los intereses de estudiantes (≈11,700), docentes, personal administrativo y la sociedad en general.

## Objetivos de Seguridad de la Información

El SGSI de la UNCP se alinea al Objetivo de Gobierno y Transformación Digital 3 (OGTD3 — Seguridad y Confianza Digital) y persigue los siguientes objetivos específicos:

1. **Confidencialidad:** Garantizar que la información académica, personal y médica (datos sensibles según Ley N.° 29733) sea accesible únicamente al personal autorizado, mediante controles de acceso basados en roles y cifrado de datos en tránsito y reposo.

2. **Integridad:** Proteger la exactitud y completitud de los registros académicos (notas, grados, títulos), información financiera y expedientes institucionales contra modificaciones no autorizadas, asegurando la confiabilidad de los procesos digitales mediante firmas electrónicas y controles de cambio.

3. **Disponibilidad:** Asegurar que los servicios tecnológicos críticos —Campus Virtual (Moodle 4.1), ERP ADESA, correo institucional (Microsoft 365) y portal web— operen con los niveles de disponibilidad establecidos en el PGTD (mínimo 99.5% en horario académico), respaldando la continuidad operativa de la universidad.

4. **Cumplimiento Normativo:** Cumplir estrictamente con la Ley N.° 29733 (Protección de Datos Personales), el D.L. N.° 1412 (Gobierno Digital), el D.S. N.° 029-2021-PCM (Marco de Confianza Digital), la Ley de Ciberdefensa, y los requisitos de SUNEDU aplicables a los sistemas de información universitarios.

5. **Cultura de Seguridad:** Desarrollar un nivel óptimo de cultura digital (OGTD5 y OGTD6), concienciando a toda la comunidad universitaria sobre sus responsabilidades en ciberseguridad mediante programas anuales de sensibilización y capacitación obligatoria.

## Alcance

Esta política es de cumplimiento obligatorio para:

- Todo el personal docente, administrativo, autoridades y estudiantes de la UNCP, incluyendo a aquellos que accedan a los recursos informáticos institucionales de forma remota.
- Proveedores de servicios tecnológicos (ej. Huawei Cloud, Microsoft 365), contratistas y terceros con acceso a los activos de información de la UNCP.
- Todos los procesos, servicios e infraestructuras contemplados en el documento D-SGSI-02 (Alcance del SGSI), abarcando las cuatro sedes universitarias y los puntos de acceso remoto autorizados.

## Principios Rectores

1. **Gestión de Riesgos:** Las medidas de seguridad se adoptarán con base en la evaluación periódica de riesgos (ISO 31000), buscando mitigarlos hasta un nivel aceptable para la UNCP. La metodología de evaluación de riesgos se describe en el documento D-SGSI-04.

2. **Seguridad desde el Diseño:** Todo nuevo proyecto tecnológico definido en el PGTD debe incorporar requisitos de seguridad y privacidad desde su fase de concepción, conforme al principio de \emph{Privacy by Design} establecido en la Ley N.° 29733.

3. **Gestión de Incidentes:** Todo usuario tiene la obligación de reportar de inmediato cualquier evento, debilidad o incidente de seguridad sospechoso a través del canal oficial establecido (CSIRT UNCP / Mesa de Ayuda OTI), conforme al procedimiento P-SGSI-07.

4. **Sanciones:** El incumplimiento de esta política y de los controles del SGSI estará sujeto a medidas disciplinarias conforme al Reglamento Interno de la UNCP y la legislación vigente, sin perjuicio de las responsabilidades civiles o penales aplicables.

5. **Mejora Continua:** El SGSI opera bajo el ciclo PHVA (Planificar-Hacer-Verificar-Actuar), realizando auditorías internas anuales y revisiones por la dirección para asegurar su eficacia continua.

## Clasificación de la Información

La información institucional se clasifica en cuatro niveles, conforme al procedimiento P-SGSI-05:

| Nivel | Categoría | Ejemplos | Controles Mínimos |
|:------|:----------|:---------|:-------------------|
| 4 | Confidencial | Datos personales sensibles (salud, disciplina), secretos industriales, estrategias institucionales | Cifrado AES-256, acceso restringido por rol, auditoría de accesos |
| 3 | Interna Restringida | Expedientes académicos, contratos, planillas, resoluciones rectorales | Control de acceso, logs de auditoría, copias de seguridad cifradas |
| 2 | Interna | Comunicados, directivas, manuales, material didáctico | Acceso autenticado, prevención de fuga de datos |
| 1 | Pública | Información institucional publicable, portal web, datos abiertos (PNDA) | Integridad de publicación, disponibilidad del portal |

## Responsabilidades

- **Comité de Gobierno Digital (CGD):** Aprobar y revisar anualmente esta política, asegurando su alineación con los objetivos estratégicos de la UNCP y el PGTD.
- **Oficial de Seguridad y Confianza Digital:** Diseñar, implementar, operar y evaluar el SGSI, reportando su desempeño a la Alta Dirección y coordinando con la OTI la ejecución de controles técnicos.
- **Oficina de Tecnologías de la Información (OTI):** Ejecutar los controles técnicos y operativos definidos por el SGSI, administrar la infraestructura tecnológica y atender incidentes de seguridad.
- **Dueños de Procesos / Activos:** Identificar, clasificar y proteger la información bajo su responsabilidad, participando activamente en las evaluaciones de riesgo de sus procesos.
- **Usuarios (Comunidad Universitaria):** Leer, comprender y aplicar las normativas de seguridad en su trabajo diario, reportando cualquier anomalía o incidente de seguridad detectado.

## Revisión y Mejora Continua

La presente política será revisada al menos una vez al año por el Comité de Gobierno Digital o cuando ocurran cambios significativos en el entorno tecnológico, normativo o estratégico de la UNCP —tales como modificaciones a la Ley N.° 29733, entrada en vigor de nuevas disposiciones del Marco de Confianza Digital, o cambios mayores en la infraestructura tecnológica— con el fin de asegurar su conveniencia, adecuación y eficacia continua.

Los resultados de la revisión se documentarán en el acta del CGD y, de ser necesario, se generará una nueva versión de esta política siguiendo el procedimiento de control documental establecido en R-SGSI-00.

***

**Firmas de Aprobación:**

___________________________
**Rector de la UNCP**
Presidente del Comité de Gobierno Digital

___________________________
**Director(a) General de Administración**
Líder de Gobierno y Transformación Digital

___________________________
**Oficial de Seguridad y Confianza Digital**