# Requerimiento de Información para la Finalización del PGTD-UNCP 2026-2030

## Universidad Nacional del Centro del Perú (UNCP)
### Mayo 2026


## 1. Introducción

Para la culminación exitosa del **Plan de Gobierno y Transformación Digital (PGTD) 2026-2030**, es imperativo contar con datos técnicos, financieros y organizacionales reales de la Universidad Nacional del Centro del Perú. Actualmente, el borrador maestro contiene secciones marcadas como "PENDIENTE" debido a la indisponibilidad de repositorios institucionales críticos (files.uncp.edu.pe) y la necesidad de validación interna.

Este documento detalla los requerimientos específicos de información y los activos visuales necesarios que, por su naturaleza técnica o gráfica, deben ser proporcionados por las unidades correspondientes (OTI, Planeamiento, Administración).

## 2. Información sobre Estrategia y Organización

### 2.1 Planeamiento Estratégico Real
*   **PEI 2024-2030 (PDF):** Documento completo aprobado para extraer los indicadores de los Objetivos Estratégicos Institucionales (OEI).
*   **POI Multianual 2026-2028:** Detalle de las actividades operativas relacionadas con tecnologías de la información.

### 2.2 Estructura del CGTD
*   **Resolución Rectoral Actualizada:** Copia de la resolución que conforma el Comité de Gobierno y Transformación Digital.
*   **Directorio Real:** Nombres, cargos y correos institucionales de los miembros actuales para la conformación de la Matriz RACI.

### 2.3 Activos Visuales (Imágenes)
*   **Organigrama Institucional:** Imagen en alta resolución (.png o .jpg) para el anexo de estructura.
*   **Mapa de Procesos (Nivel 0 y 01):** Diagramas en formato imagen para la sección de situación actual.

## 3. Información Técnica de Infraestructura (AS-IS)

### 3.1 Redes y Comunicaciones
*   **Diagrama de Topología de Red:** Imagen o PDF del esquema de conexión entre el campus central y las sedes descentralizadas (Tarma, Jauja, Satipo).
*   **Contratos de Conectividad:** Ancho de banda real contratado por sede y nombres de los proveedores de servicios (ISP).
*   **Línea Base de Consumo de Red:** Desplegar un analizador de NetFlow temporal o SNMP básico durante una semana de máxima demanda (exámenes finales o matrícula) para obtener la gráfica real de saturación de los 300 Mbps actuales. Este dato es crítico para justificar técnicamente ante el MEF la ampliación a 1 Gbps.

### 3.2 Inventario de Hardware y Software
*   **Listado Maestro de Servidores:** Detalle de modelos, antigüedad, sistemas operativos y roles (ej. Servidor de Base de Datos ADESA).
*   **Estado de Licenciamiento:** Cantidad de licencias de Microsoft 365, licencias de VMware y bases de datos Oracle/SQL Server.
*   **Escaneo Automatizado de Activos (Discovery Pasivo):** Desplegar herramientas de código abierto (GLPI con agentes de descubrimiento, FMC para gestión de flujos) para mapear en 48 horas el inventario real de switches, routers, servidores físicos y sistemas operativos en todas las facultades, sin depender de archivos Excel desactualizados.

### 3.3 Datos de Seguridad
*   **Log de Incidentes 2025:** Resumen cuantitativo de incidentes de seguridad reportados (sin nombres, solo tipo y frecuencia).
*   **Estado de Backups:** Periodicidad real y medios de almacenamiento (on-premise o cloud).

### 3.4 Matriz de Deuda Técnica de Software
Para cada sistema misional (ADESA/SGA, SIGA, Moodle, DSpace, GESDOC, Tesorería), documentar:
*   Lenguaje de programación y versión (PHP, Java, Python, etc.)
*   Base de datos subyacente (MySQL, PostgreSQL, Oracle, SQL Server)
*   Estado de soporte del fabricante (con soporte vigente, obsoleto, sin soporte)
*   Compatibilidad con contenedores (Docker/Kubernetes) para planificar la migración
*   Dependencias críticas y versiones de librerías

Esta matriz justificará legal y técnicamente la necesidad de migración hacia la arquitectura de contenedores y nube híbrida planteada en los proyectos estratégicos.

### 3.5 Arquitectura de Identidad (IdM)
*   **Censo de Directorios de Usuarios:** Identificar todos los repositorios de credenciales existentes (Active Directory, base de datos del SGA, Moodle, LDAP, Microsoft 365 Azure AD) y su estado de sincronización.
*   **Mapeo de Flujos de Autenticación:** Documentar cómo inician sesión actualmente estudiantes, docentes y administrativos en cada sistema.
*   **Protocolos Soportados:** Determinar qué sistemas soportan SAML, OAuth2, LDAP o solo autenticación por formulario/cookies.

### 3.6 APIs e Integraciones
*   **Catálogo de APIs Existentes:** Identificar si los sistemas actuales exponen APIs REST/SOAP, su estado de documentación y nivel de seguridad (autenticación, rate limiting).
*   **Integraciones Manuales:** Detallar los procesos de intercambio de datos que actualmente se realizan de forma manual (archivos CSV, transferencias FTP, correos electrónicos) para priorizar su automatización vía API Gateway.

### 3.7 Costos Cloud y FinOps
*   **Gasto Actual en Nube:** Detalle del gasto mensual en servicios cloud (Microsoft 365, AWS, Azure u otros) y su proyección a 12 meses.
*   **Políticas de Autoescalado:** Estado actual de configuración de escalado automático en servicios contratados.
*   **Recursos sin Etiquetar:** Identificación de recursos cloud sin etiquetas de proyecto/unidad que impiden la trazabilidad del gasto.

## 4. Información Financiera y Presupuestal

### 4.1 Histórico de Gastos TI
*   **Ejecución Presupuestal 2024-2025:** Montos reales ejecutados en los clasificadores de gasto relacionados con equipos informáticos y servicios de TI.

### 4.2 Fuentes de Financiamiento
*   **Disponibilidad de Canon:** Monto proyectado del Canon y Sobrecanon que puede ser destinado a proyectos de transformación digital.
*   **Recursos Directamente Recaudados (RDR):** Capacidad de inversión proyectada para servicios digitales universitarios.

## 5. Próximos Pasos para la Consolidación

Una vez recibida la información solicitada, se procederá a:

1.  **Eliminar los subrayados y estados "PENDIENTE"** de los documentos maestros.
2.  **Ajustar el presupuesto** total (S/ 6.4M) a la realidad financiera de la universidad.
3.  **Insertar los activos gráficos** en los anexos correspondientes del PDF final.
4.  **Validar los indicadores** de cumplimiento frente a la SGTD y la CGR.
5.  **Alimentar el registro maestro de activos** con los datos del escaneo automatizado (GLPI) para la línea base del SGSI (PGTD-01).
6.  **Ajustar las políticas de FinOps** con base en el gasto real cloud y las proyecciones de crecimiento.

**Elaborado por:** Equipo Consultor SGSI-UNCP
**Estado:** Requerimiento Actualizado
**Fecha:** 31 de mayo de 2026
