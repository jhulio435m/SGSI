# Requerimiento de Información para la Finalización del PGTD-UNCP 2026-2030

## Universidad Nacional del Centro del Perú (UNCP)
### Mayo 2026


## 1. Introducción

Para la culminación exitosa del **Plan de Gobierno y Transformación Digital (PGTD) 2026-2030**, es imperativo contar con datos técnicos, financieros y organizacionales reales de la Universidad Nacional del Centro del Perú. Actualmente, el borrador maestro contiene secciones marcadas como "PENDIENTE" debido a la indisponibilidad de repositorios institucionales críticos (files.uncp.edu.pe) y la necesidad de validación interna.

Este documento detalla los requerimientos específicos de información y los activos visuales necesarios que, por su naturaleza técnica o gráfica, deben ser proporcionados por las unidades correspondientes (OTI, Planeamiento, Administración).

## 2. Información sobre Estrategia y Organización

### 2.1 Planeamiento Estratégico Real
*   **PEI 2024-2030:** Documento recibido e incorporado como referencia para extraer OEI, AEI e indicadores institucionales.
*   **POI Multianual 2026-2028:** Detalle de las actividades operativas relacionadas con tecnologías de la información.

### 2.2 Estructura del CGTD
*   **Resolución Rectoral vigente:** La conformación del Comité de Gobierno Digital se sustenta en la R. N.° 1862-R-2023. Se requiere validar si existe modificación posterior o reconformación vigente.
*   **Directorio Real:** Nombres, cargos y correos institucionales de los miembros actuales para la conformación de la Matriz RACI.
*   **Evidencia operativa:** Actas, convocatorias o reportes recientes del CGTD para documentar su funcionamiento y periodicidad de sesiones.

### 2.3 Resoluciones y evidencia documental a convertir a Markdown

El portal oficial de resoluciones rectorales (`https://uncp.edu.pe/la-universidad/resoluciones-rectorales/`) publica el listado vigente mediante el repositorio `https://resoluciones.uncp.edu.pe/documentos/R-RE`; el portal de resoluciones directorales (`https://uncp.edu.pe/la-universidad/resoluciones-directorales/`) usa `https://resoluciones.uncp.edu.pe/documentos/R-DR`. Para que el PGTD y el SGSI queden sustentados con evidencia real, se requiere convertir a Markdown, como mínimo, los siguientes documentos:

La matriz consolidada de estado documental se mantiene en `UNCP/referencias/Matriz-Evidencia-Documental-UNCP.md`.

*   **R. N.° 1862-R-2023:** Comité de Gobierno Digital de la UNCP. Existe referencia local (`UNCP/referencias/comite.md`), pero conviene reemplazarla por una conversión limpia del PDF cuando sea posible.
*   **R. N.° 2143-R-2023:** recibida en Markdown. Integra al CGD a la Mg. Rocío Rosanna Damián Alvarado, Jefa de la OTI, como Oficial de Seguridad de la Información.
*   **R. N.° 2140-R-2023:** recibida en Markdown. Designa a la Mg. Rocío Rosanna Damián Alvarado como Funcionaria Responsable del Software Público.
*   **PEI 2024-2030:** recibido como `Plan+Estratégico+Institucional+UNCP+2024-2030.md`. Se usará para validar OEI, AEI, indicadores y alineamiento estratégico del PGTD/SGSI.
*   **R. N.° 2443-R-2024:** recibida en Markdown. Aprueba el POI 2024.
*   **R. N.° 3524-R-2025 y R. N.° 3526-R-2025:** recibidas como PDF y resumidas en `UNCP/referencias/AGENTS.md`. Sustentan el Mapa de Procesos Nivel 0 y Nivel 1; el diagrama Mermaid fue convertido a PNG.
*   **R. N.° 3255-R-2024:** recibida en Markdown. Aprueba el Plan de Continuidad Operativa.
*   **R. N.° 0835-R-2022:** recibida en Markdown. Designa el Comité de Gestión Ambiental y sustenta Green IT y ecoeficiencia digital.
*   **Actas o informes CGTD 2024-2026:** no accesibles públicamente en red; deben solicitarse formalmente a la universidad para evidenciar sesiones, acuerdos, seguimiento del PGTD, asignación de responsables y reporte a Rectorado.
*   **Evidencia de compromisos CGR pendientes:** no accesible públicamente en red; solicitar a la universidad documentación sobre PIDE, IPv6, Datos Abiertos, Encuesta Nacional de Activos Digitales, Oficial de Gobierno de Datos y Política de Privacidad.

### 2.4 Requerimientos formales a la universidad

Los siguientes documentos deben solicitarse a la UNCP porque no se encuentran disponibles públicamente o requieren validación interna:

| Requerimiento | Unidad sugerida | Finalidad |
|---|---|---|
| Actas, convocatorias e informes del CGD 2024-2026 | Secretaría General / OTI / CGD | Evidenciar operación real del comité y seguimiento del PGTD/SGSI. |
| Directorio vigente del CGD y suplentes | Secretaría General / OTI | Completar matriz RACI y comunicaciones oficiales. |
| Asignación de dedicación, funciones o plan operativo del Oficial de Seguridad | OTI / DGA / RRHH | Sustentar capacidad operativa del SGSI. |
| Evidencia de integración PIDE | OTI / Secretaría General | Sustentar interoperabilidad institucional. |
| Plan de transición a IPv6 | OTI | Cerrar compromiso CGR pendiente. |
| Evidencia de datos abiertos en PNDA o plan de datos abiertos | OTI / Unidad de Modernización | Sustentar gobierno abierto. |
| Encuesta Nacional de Activos Digitales o inventario equivalente | OTI | Línea base de activos digitales. |
| Designación del Oficial de Gobierno de Datos | Rectorado / Secretaría General / OTI | Sustentar gobierno de datos. |
| Política de Privacidad y registro de tratamientos de datos personales | Asesoría Jurídica / OTI | Cumplimiento de Ley N.° 29733. |

### 2.5 Activos Visuales (Imágenes)
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
