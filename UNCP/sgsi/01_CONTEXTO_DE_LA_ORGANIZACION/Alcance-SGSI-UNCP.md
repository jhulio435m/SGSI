# Alcance del SGSI - Universidad Nacional del Centro del Perú

## 1. Organización

**Universidad Nacional del Centro del Perú (UNCP)**  
RUC: 20172030258  
Domicilio legal: Av. Mariscal Ramón Castilla km. 5, N° 3809-4089, El Tambo, Huancayo  
Naturaleza: Universidad pública peruana, con autonomía académica, normativa y económica (Ley N° 30220).

***

## 2. Definición del Alcance Estratégico (Enfoque de Excelencia)

El Sistema de Gestión de Seguridad de la Información (SGSI) de la UNCP adopta una **Definición de Alcance Superior**, integrando los requisitos de la norma ISO/IEC 27001:2022 con metodologías de vanguardia para garantizar la protección de la información sin importar su ubicación, formato o método de acceso.

### 2.1 Filosofía de Implementación
*   **Enfoque Zero Trust (Confianza Cero):** El alcance no se limita a las paredes del campus. Se aplica una segmentación lógica estricta y verificación continua para cada intento de acceso, tratando las redes locales y remotas (VPN/Internet) con el mismo nivel de escrutinio.
*   **Ubicación Agnóstica y Ciclo de Vida del Dato:** La seguridad "viaja" con el dato. El alcance protege la información crítica (notas, datos personales, investigación) en tránsito, en uso y en reposo, ya sea que resida en servidores locales, dispositivos de usuarios o en la nube (Huawei Cloud / Microsoft 365).
*   **Inventario Dinámico y Mitigación de Shadow IT:** El alcance incluye todos los activos identificados mediante procesos de descubrimiento automático, asegurando que dispositivos no registrados o de reciente incorporación (IoT, BYOD) queden bajo el control del SGSI.
*   **Resiliencia NIST CSF:** El alcance está diseñado para soportar no solo la protección (ISO 27001), sino también las capacidades operativas de detección y respuesta rápida ante incidentes.

### 2.2 Ámbito Organizacional y Procesos Críticos
El SGSI abarca el flujo completo de los datos en los siguientes macroprocesos:
- **Gestión Académica:** Desde la admisión y matrícula hasta la emisión de grados y títulos (ERP ADESA).
- **Investigación y Propiedad Intelectual:** Protección de tesis y proyectos (Repositorio DSpace).
- **Gestión Administrativa y Financiera:** Planillas, tesorería y abastecimiento (SIGA / SIAF).
- **Educación Digital:** Plataformas de aprendizaje y colaboración (Moodle / Teams).

### 2.3 Ámbito Tecnológico (Infraestructura Híbrida)
| Activo / Entorno | Descripción del Alcance |
| :--- | :--- |
| **Infraestructura On-Premise** | Datacenter Huancayo, redes de facultades (Sedes Mantaro, Satipo, Tarma). |
| **Infraestructura Cloud** | IaaS/PaaS en Huawei Cloud, SaaS en Microsoft 365. |
| **Acceso Remoto / VPN** | Todos los túneles IPsec y accesos SSL-VPN utilizados por administrativos y docentes. |
| **Dispositivos Finales** | Laptops, tablets y estaciones de trabajo (incluyendo BYOD autorizados). |

### 2.4 Ámbito Geográfico
El SGSI protege la información en las 4 sedes de la UNCP y en cualquier ubicación remota desde la cual se acceda a los sistemas institucionales bajo los controles de seguridad establecidos.

***

## 3. Justificación de Inclusiones Basada en Riesgos

La delimitación de este alcance responde a los siguientes riesgos críticos identificados:
1.  **Fuga de datos sensibles:** Debido al acceso remoto masivo de docentes y administrativos.
2.  **Alteración de registros académicos:** Por debilidades en la segmentación de la red de facultades.
3.  **Indisponibilidad de servicios:** Ante fallas en la infraestructura local o ataques dirigidos (DDoS).

Al incluir el ciclo de vida del dato y el enfoque Zero Trust, la UNCP garantiza que la seguridad sea consistente independientemente de las fronteras físicas.

***

## 4. Mapa de Dependencias Críticas

| Proceso | Activo Crítico | Dependencia Tecnológica |
| :--- | :--- | :--- |
| Matrícula / Notas | Base de Datos ADESA | Huawei Cloud / IdM Keycloak |
| Gestión de Pagos | Sistema de Tesorería | SIAF / Pasarela de Pagos |
| Educación Virtual | Campus Virtual (Moodle) | Almacenamiento S3 / Contenedores |
| Investigación | Repositorio Digital | Red de Telemetría / SIEM |

***

## 5. Exclusiones Obligatorias
No se excluye ninguno de los requisitos de las cláusulas 4 a 10 de la norma ISO/IEC 27001:2022, ya que son indispensables para la conformidad del sistema. Se excluyen únicamente activos físicos de infraestructura civil (edificaciones, mobiliario) que no procesan ni almacenan información.

***
**Declaración de Conformidad:** Este documento establece los límites y aplicabilidad del SGSI-UNCP, alineado a la excelencia operativa y la protección integral del patrimonio informativo de la universidad.

*Versión 2.0 (Enfoque Vanguardia) - Aprobado para el proyecto SGSI-UNCP 2026.*
