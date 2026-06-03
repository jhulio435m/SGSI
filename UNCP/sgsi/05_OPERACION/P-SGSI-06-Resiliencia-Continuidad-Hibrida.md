# P-SGSI-06: Marco de Resiliencia y Continuidad en Nube Híbrida

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0 (Enfoque Resiliencia Activa)
**Norma:** ISO/IEC 27001:2022 (Control A.5.30)
**Alineamiento:** OGTD4 y Anexo H.3 (Estrategia de Alta Disponibilidad)

***

## 1. Estrategia de Continuidad: Activo-Activo
La UNCP garantiza la continuidad de sus servicios críticos (ERP ADESA, Campus Virtual) mediante una arquitectura de **Nube Híbrida**. Los servicios no dependen de un solo centro de datos; operan simultáneamente entre el Datacenter Local (Huancayo) y Huawei Cloud.

## 2. Niveles de Recuperación (RTO / RPO)
| Servicio Crítico | RTO (Tiempo de Recuperación) | RPO (Punto de Recuperación) | Estrategia Técnica |
| :--- | :--- | :--- | :--- |
| **ERP ADESA (Notas/Matrícula)** | < 1 hora | < 15 minutos | Replicación sincrónica de BD + Balanceo GSLB. |
| **Campus Virtual (Moodle)** | < 2 horas | < 1 hora | Clúster de contenedores autoescalables. |
| **Correo Institucional** | Inmediato | Inmediato | Servicio SaaS (Microsoft 365). |

## 3. Plan de Recuperación ante Desastres (DRP)
### 3.1. Detección de Falla
*   Monitoreo mediante **GSLB (Global Server Load Balancing)**. Si el nodo local no responde, el tráfico se redirige automáticamente al nodo Cloud en milisegundos.

### 3.2. Activación de Contingencia
*   **Modo Degradado:** En caso de falla masiva de internet, se activan los enlaces de respaldo (SD-WAN) priorizando el tráfico administrativo sobre el recreativo.

### 3.3. Restauración de Datos
*   Uso de **Cloud Backup and Recovery (CBR)** para restaurar volúmenes de datos en caso de corrupción o ataque de ransomware.

## 4. Pruebas de Continuidad (Ejercicios de Resiliencia)
*   Se realizarán pruebas de "conmutación por error" (failover) semestralmente, sin previo aviso a los administradores de sistemas, para validar la eficacia de los automatismos.

## 5. Gestión de la Comunicación
*   En caso de interrupción mayor, la OTI activará el protocolo de comunicación institucional para informar a los 10,000 estudiantes a través de redes sociales oficiales y SMS.
