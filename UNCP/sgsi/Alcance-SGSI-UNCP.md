# Alcance del SGSI - Universidad Nacional del Centro del Perú

## 1. Organización

**Universidad Nacional del Centro del Perú (UNCP)**  
RUC: 20172030258  
Domicilio legal: Av. Mariscal Ramón Castilla km. 5, N° 3809-4089, El Tambo, Huancayo  
Naturaleza: Universidad pública peruana, con autonomía académica, normativa y económica (Ley N° 30220)

---

## 2. Alcance del SGSI

El Sistema de Gestión de Seguridad de la Información (SGSI) de la UNCP abarca:

### 2.1 Ámbito Organizacional
Todas las unidades académicas y administrativas de la UNCP, incluyendo:
- Rectorado, Vicerrectorados y órganos de gobierno central
- Dirección General de Administración (DGA) y sus unidades
- OTI (Oficina de Tecnología de la Información)
- **22 facultades** en la sede central Huancayo
- **3 facultades** en sedes descentralizadas (Mantaro, Satipo, Tarma)
- Instituto de Investigación y centros de investigación
- Escuela de Posgrado
- Bibliotecas Central, facultades y virtual

### 2.2 Ámbito Geográfico
Las **4 sedes** oficiales de la UNCP:

| Sede | Ubicación |
|---|---|
| Sede Central | Km. 5 Carretera Central, El Tambo, Huancayo |
| Sede Mantaro | Carretera Central, El Mantaro, Jauja |
| Sede Satipo | Río Negro, Satipo |
| Sede Tarma | Av. Tupac Amaru, Tarma |

### 2.3 Ámbito Tecnológico (Sistemas de Información e Infraestructura)
Los sistemas misionales y de soporte, incluyendo:

| Sistema | Función |
|---|---|
| ADESA | Gestión académica (estudiantes, notas, matrícula) |
| SIGA | Gestión administrativa, presupuestal y RRHH |
| Campus Virtual (Moodle 4.1) | Educación virtual |
| Repositorio Institucional (DSpace) | Tesis e investigación |
| Correo institucional (Microsoft 365) | Comunicación |
| Sistema de Trámite Documentario | Gestión de expedientes |
| Sistema de Tesorería | Recaudación y pagos |
| Portal Web (WordPress) | Comunicación institucional y transparencia |
| Biblioteca Virtual (MyLOFT, ProQuest, Springer) | Recursos académicos |
| CTI Vitae | Investigación (CONCYTEC) |

Asimismo, el ámbito tecnológico abarca la infraestructura TO-BE definida en el informe técnico de arquitectura del PGTD, incluyendo:

| Componente de Infraestructura TO-BE | Descripción |
|---|---|
| **Red de Telemetría** | TAP físico en Datacenter, SPAN en facultades, NetFlow/IPFIX en routers, SNMPv3 cifrado (AES) |
| **Alta Disponibilidad** | Nube Híbrida Activo-Activo (Proxmox/Ceph o vSAN), GSLB, contenedores Docker/Kubernetes |
| **Seguridad Perimetral** | NGFW con IPS/IDS, microsegmentación ZTNA, 802.1X, SD-WAN con IPsec entre sedes |
| **Conectividad Cloud** | AWS Direct Connect / Azure ExpressRoute para replicación sincrónica |
| **SIEM** | Wazuh o Microsoft Sentinel para correlación de eventos y detección por IA |

### 2.4 Ámbito de Información
Toda la información gestionada por la UNCP, independientemente de su formato:
- **Digital**: bases de datos, archivos, correos, respaldos
- **Física**: actas de notas, expedientes, resoluciones, contratos, tesis impresas
- **Transmitida**: videoconferencias, llamadas, comunicaciones internas

### 2.5 Procesos Misionales
- Gestión académica (admisión, matrícula, enseñanza, evaluación, grados y títulos)
- Gestión de investigación y publicaciones
- Gestión de proyección social y extensión cultural
- Gestión administrativa y financiera (presupuesto, tesorería, abastecimiento, RRHH)
- Gestión documentaria y archivo

### 2.6 Marco Normativo Aplicable
- NTP ISO/IEC 27001:2022 (cláusulas 4-10 y controles Anexo A)
- Ley N° 29733 - Protección de Datos Personales
- D.S. N° 016-2024-JUS - Nuevo Reglamento de la Ley N° 29733 (DPIA, transferencias internacionales, regulación IA)
- D.L. N° 1412 - Ley de Gobierno Digital
- D.S. N° 029-2021-PCM - Reglamento de Gobierno Digital
- D.S. N° 098-2025-PCM - Modificatoria del Reglamento de Gobierno Digital
- D.S. N° 103-2023-PCM - Política Nacional de Transformación Digital
- Ley N° 31814 y D.S. N° 115-2025-PCM - Ley de IA y su Reglamento
- R.M. N° 119-2018-PCM - Comité de Gobierno Digital
- R.S. N° 001-2025-PCM/SGTD - Lineamiento de accesibilidad digital
- Directiva N° 001-2025-PCM/SGTD - Consumo seguro de servicios PIDE y medidas de seguridad digital
- Ley N° 30220 - Ley Universitaria
- Directiva N° 006-2019-CG/INTEG - Control Interno
- Plan de Gobierno y Transformación Digital UNCP 2026-2030

---

## 3. Exclusiones

| Aspecto excluido | Justificación |
|---|---|
| Sistemas de seguridad física perimetral (cámaras, alarmas) fuera de lo necesario para protección de información | Se gestionan bajo la unidad de seguridad patrimonial, no bajo el SGSI |
| Infraestructura vial, redes de agua, electricidad no relacionadas con TI | No son activos de información; aplican solo controles de seguridad física del Anexo A |
| Proveedores externos (su infraestructura interna) | Se gestionan mediante acuerdos de nivel de servicio (SLA) y cláusulas contractuales, sin auditar sus sistemas internos |

---

## 4. Interfaces y Dependencias

- **SUNEDU**: licenciamiento institucional
- **MINEDU**: políticas educativas
- **PCM/Secretaría de Gobierno Digital**: lineamientos de gobierno digital
- **CONCYTEC**: sistemas CTI Vitae, financiamiento de investigación
- **Contraloría General**: control gubernamental
- **Google**: Workspace for Education
- **Proveedores de internet y hosting**: conectividad y alojamiento
- **Bibliotecas**: MyLOFT, ProQuest, Springer (proveedores de contenido)

---

## 5. Declaración

El presente alcance aplica a todas las actividades, procesos, sistemas, personas e instalaciones descritas en la sección 2. Cualquier cambio en la estructura organizacional, tecnológica o geográfica de la UNCP deberá ser evaluado para determinar su impacto en este alcance.

*Versión 1.0 - Aprobado para el proyecto SGSI-UNCP, en el marco del PGTD 2026-2030.*
