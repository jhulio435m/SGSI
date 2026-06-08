---
title: Marco de Resiliencia y Continuidad en Nube Híbrida
code: P-SGSI-05
---

# Marco de Resiliencia y Continuidad en Nube Híbrida

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Aprobado por:** Jefe de la Oficina de Tecnologías de la Información
**Norma:** ISO/IEC 27001:2022 (Controles A.5.29, A.5.30)
**Alineamiento:** OGTD4 y Anexo H.3 (Estrategia de Alta Disponibilidad del PGTD)

***

## Estrategia de Continuidad: Activo-Activo

La UNCP garantiza la continuidad de sus servicios críticos (ERP ADESA, Campus Virtual Moodle) mediante una arquitectura de **nube híbrida**. Los servicios no dependen de un solo centro de datos; operan simultáneamente entre el Datacenter Local (Huancayo) y Huawei Cloud, con balanceo de carga global (GSLB) para conmutación automática por error.

Esta arquitectura permite:

- **Alta disponibilidad:** Los servicios críticos permanecen operativos incluso si uno de los centros de datos falla completamente.
- **Escalabilidad:** Capacidad de escalar recursos en cloud durante picos de demanda (matrícula, exámenes finales).
- **Recuperación automatizada:** El failover es automático, sin intervención humana para los servicios core.

## Clasificación de Servicios por Criticidad

| Nivel | Definición | Servicios UNCP | RTO | RPO |
|:------|:-----------|:---------------|:---:|:---:|
| **Crítico** | Indisponibilidad afecta directamente la misión académica. Impacto legal o reputacional severo | ERP ADESA (matrícula, notas), BD de estudiantes, Portal de matrícula | < 1 hora | < 15 min |
| **Alto** | Indisponibilidad afecta procesos misionales con impacto significativo | Campus Virtual Moodle, SIGA/SIAF, correo institucional | < 2 horas | < 1 hora |
| **Medio** | Indisponibilidad afecta procesos administrativos internos | GESDOC, DSpace, portal web, VPN corporativa | < 8 horas | < 4 horas |
| **Bajo** | Indisponibilidad sin impacto crítico en la operación | Sistemas de prueba, laboratorios de investigación no críticos, servicios auxiliares | < 48 horas | < 24 horas |

## Niveles de Recuperación (RTO / RPO)

| Servicio Crítico | RTO | RPO | Estrategia Técnica |
|:-----------------|:---:|:---:|:-------------------|
| ERP ADESA (Notas, Matrícula) | < 1 hora | < 15 minutos | Replicación sincrónica de BD + Balanceo GSLB entre Data Center y Huawei Cloud |
| Campus Virtual (Moodle 4.1) | < 2 horas | < 1 hora | Clúster de contenedores autoescalables (Kubernetes) en cloud |
| Correo Institucional (Microsoft 365) | Inmediato | Inmediato | Servicio SaaS con SLA Microsoft 99.9% |
| SIGA/SIAF (RRHH, Planillas) | < 4 horas | < 2 horas | Backup transaccional + failover manual si es necesario |
| Sistema GESDOC (Trámite Documentario) | < 4 horas | < 4 horas | Backup diario + restauración en cloud |
| Portal Web Institucional | < 2 horas | < 1 hora | Cloudflare CDN + hosting cloud con failover automático |
| VPN Corporativa | < 1 hora | N/A | Gateway redundante con failover automático |
| Repositorio DSpace | < 8 horas | < 24 horas | Backup semanal + replicación a cloud |
| Red LAN / WiFi | < 2 horas | N/A | Enlaces redundantes, switches core en HA |

## Plan de Recuperación ante Desastres (DRP)

### Detección de Falla

- **Monitoreo GSLB:** El Global Server Load Balancing monitorea la disponibilidad de los nodos local y cloud. Si el nodo local no responde (health check falla 3 veces consecutivas en 30 segundos), el tráfico se redirige automáticamente al nodo cloud.
- **Monitoreo SIEM:** Alertas de anomalías en los patrones de tráfico, latencia o disponibilidad de servicios.
- **Monitoreo de Infraestructura:** Temperature, humedad, estado de UPS, conectividad de red en el Data Center local.

### Activación de Contingencia

| Escenario | Activación | Acción | Tiempo de Activación |
|:----------|:-----------|:-------|:--------------------:|
| Falla del Data Center local (incendio, inundación, corte eléctrico prolongado) | Automática (GSLB) | Redirección completa del tráfico a Huawei Cloud | < 1 minuto |
| Falla de enlace de internet principal | Automática (SD-WAN) | Conmutación a enlace de respaldo (segundo proveedor) | < 30 segundos |
| Ciberataque (ransomware, DDoS masivo) | Manual (CSIRT) | Aislamiento de sistemas afectados, activación de DRP cloud | < 15 minutos |
| Falla de hardware crítico (servidor, storage) | Automática (HA) | Failover a nodo secundario o cloud | < 5 minutos |

### Contención y Modo Degradado

En caso de falla masiva de internet o cloud, se activan las siguientes medidas:

- **SD-WAN:** Los enlaces de respaldo priorizan el tráfico administrativo y académico crítico sobre el tráfico recreativo o no esencial.
- **Modo Degradado:** Los servicios se operan con funcionalidad reducida (ej. consulta de notas disponible, pero sin actualización en tiempo real).
- **Comunicación Manual:** Activación del protocolo de comunicación institucional (ver Sección 7).

### Restauración de Datos

- **Cloud Backup and Recovery (CBR):** Restauración de volúmenes de datos en caso de corrupción o ataque de ransomware. Los backups inmutables garantizan que no puedan ser cifrados por malware.
- **Pruebas de Restauración:** Se realizarán pruebas trimestrales de restauración de bases de datos desde backups para validar la integridad de los datos y el tiempo de recuperación.

## Pruebas de Continuidad

| Tipo de Prueba | Frecuencia | Descripción | Participantes |
|:---------------|:-----------|:------------|:--------------|
| Failover automático (GSLB) | Semestral (sin aviso) | Desconectar intencionalmente el nodo local y verificar que el cloud asume la carga sin interrupción perceptible | OTI (Sistemas, Redes) |
| Restauración de BD desde backup | Trimestral | Restaurar una base de datos crítica desde backup en un entorno de prueba y verificar integridad | OTI (Sistemas) |
| Simulacro de ransomware | Anual | Simular un ataque de ransomware para probar la detección, contención, erradicación y recuperación | CSIRT, OTI, Comunicaciones |
| Prueba de comunicación de crisis | Semestral | Activar el protocolo de comunicación y medir el tiempo de notificación a toda la comunidad universitaria | Comunicaciones, OTI |

## Gestión de la Comunicación en Crisis

En caso de interrupción mayor de servicios, se activa el siguiente protocolo de comunicación:

| Público | Canal Primario | Canal Secundario | Contenido | Tiempo Máximo |
|:--------|:---------------|:-----------------|:----------|:--------------|
| Estudiantes | Redes sociales oficiales (Facebook, Instagram) | SMS masivo, portal web | Estado del servicio, tiempo estimado de restauración, alternativas | < 30 minutos |
| Docentes | Correo institucional | Redes sociales, WhatsApp institucional | Instrucciones para continuidad académica | < 30 minutos |
| Personal administrativo | Correo institucional + Teams | SMS, llamada telefónica | Instrucciones operativas, activación de trabajo remoto si aplica | < 15 minutos |
| Alta Dirección (CGD) | Teléfono + Correo | WhatsApp, Teams | Reporte de impacto, acciones tomadas, decisiones requeridas | < 10 minutos |
| Proveedores críticos (Huawei, ISP) | Teléfono + Correo | Portal de servicio | Notificación de activación de contingencia | < 1 hora |

## Responsabilidades

| Rol | Responsabilidad en Continuidad |
|:----|:-------------------------------|
| **Jefe de OTI** | Activar el DRP; coordinar la respuesta técnica; informar al CGD |
| **Oficial de Seguridad** | Evaluar el impacto de seguridad; coordinar con CSIRT; gestionar comunicaciones con autoridades |
| **OTI (Sistemas)** | Ejecutar la conmutación por error; restaurar servicios; verificar integridad de datos |
| **OTI (Redes)** | Gestionar SD-WAN, enlaces de respaldo, segmentación de emergencia |
| **Comunicaciones / Imagen Institucional** | Ejecutar el protocolo de comunicación a comunidad universitaria |
| **Dueños de Procesos Críticos** | Validar la correcta operación de los servicios restaurados; priorizar procesos |

## Documentos Relacionados

| Código | Nombre |
|:-------|:-------|
| P-SGSI-02 | Marco de Respuesta a Incidentes (CSIRT) |
| P-SGSI-04 | Procedimiento de Gestión de Cambios en TI |
| R-SGSI-01 | Inventario de Activos de Información |
| R-SGSI-02 | Matriz de Evaluación y Tratamiento de Riesgos |
| PGTD Anexo H.3 | Estrategia de Alta Disponibilidad y Cloud Híbrido |

***

*Este documento se revisa anualmente o después de cada prueba de continuidad significativa.*