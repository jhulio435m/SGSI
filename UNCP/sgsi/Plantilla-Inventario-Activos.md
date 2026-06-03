# Plantilla de Inventario de Activos de Informacion - UNCP

## Instrucciones

1. El responsable de cada unidad organizacional debe completar una fila por activo.
2. Los niveles de clasificacion (C-I-D) se asignan segun la tabla de criterios en la Seccion 3.
3. Entregar a la OTI para consolidacion en el registro maestro.
4. Actualizar semestralmente o ante cambios significativos.

---

## 1. Registro de Activos

| # | ID Activo | Nombre del Activo | Descripcion | Tipo | Propietario | Custodio | Ubicacion Fisica | Ubicacion Logica | Formato / Soporte | Usuarios |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HW-001 | Servidor ADESA | Servidor principal de gestion documental | Hardware | OTI | OTI | Data Center - Sede Central | 192.168.x.x | Fisico-Servidor | Administrativos OTI |
| 2 | SW-001 | Sistema GESDOC | Sistema de gestion documental | Software | OTI | OTI | Servidor ADESA | gesdoc.uncp.edu.pe | Digital-Aplicacion Web | Toda la comunidad UNCP |
| 3 | DT-001 | Base Datos Matricula | Registro de estudiantes matriculados | Dato | Secretaria Academica | OTI | Servidor BD Principal | db.uncp.edu.pe | Digital-Base de Datos | Secretaria Academica, OTI |
| 4 | PR-001 | Red LAN Sede Central | Infraestructura de red cableada | Red | OTI | OTI | Sede Central - Campus | 10.0.0.0/16 | Fisico-Red | Toda la sede |
| 5 | PE-001 | Personal OTI (2) | Personal administrativo de OTI | Persona | OTI | RRHH | OTI - Sede Central | N/A | N/A | N/A |

### Tipos de Activo
- **Hardware (HW)**: Servidores, computadoras, equipos de red, dispositivos moviles
- **Software (SW)**: Sistemas, aplicaciones, licencias
- **Dato (DT)**: Bases de datos, archivos, documentos
- **Red (PR)**: Infraestructura de red, conectividad
- **Persona (PE)**: Personal con roles criticos
- **Servicio (SV)**: Servicios TI prestados
- **Instalacion (IN)**: Data centers, racks, cableado estructurado
- **Soporte Fisico (SF)**: Documentos impresos, medios removibles

---

## 2. Clasificacion de Seguridad (C-I-D)

| ID Activo | Confidencialidad | Integridad | Disponibilidad | Nivel Criticidad | Fecha Evaluacion |
|---|---|---|---|---|---|
| HW-001 | 2 - Uso Interno | 3 - Alta | 3 - Alta | Alta | 2025-05-30 |
| SW-001 | 1 - Publico | 2 - Media | 2 - Media | Media | 2025-05-30 |
| DT-001 | 3 - Confidencial | 3 - Alta | 3 - Alta | Critico | 2025-05-30 |
| PR-001 | 1 - Publico | 2 - Media | 3 - Alta | Alta | 2025-05-30 |
| PE-001 | 2 - Uso Interno | 2 - Media | 2 - Media | Media | 2025-05-30 |

### Escala de Valoracion
| Nivel | Confidencialidad | Integridad | Disponibilidad |
|---|---|---|---|
| 3 - Alto | Datos personales, academicos, financieros | Requiere exactitud total, no se tolera alteracion | Tolerancia < 4 hrs, impacto critico |
| 2 - Medio | Uso interno, no publico | Alteracion afecta operaciones pero es recuperable | Tolerancia 4-24 hrs, impacto significativo |
| 1 - Bajo | Informacion publica | Sin consecuencias graves por alteracion | Tolerancia > 24 hrs, impacto menor |

### Nivel de Criticidad
| Combinacion C-I-D | Criticidad |
|---|---|
| C>=2 e I>=2 y D>=2, o cualquier C=3 | **Critico** |
| C>=2 o I>=2 o D>=2 | **Alta** |
| C=1 e I=1 y D=1 | **Media** |
| C=1 y (I=1 o D=1) | **Baja** |

---

## 3. Controles Asociados (ISO 27001:2022 - Anexo A)

| ID Activo | Controles Aplicables | Estado | Observaciones |
|---|---|---|---|
| HW-001 | A.5.9 (Inventario), A.7.9 (Seguridad en locales), A.8.1 (Proteccion equipos) | Pendiente | Data center sin control de acceso biometrico |
| SW-001 | A.5.23 (Filtrado web), A.8.8 (Gestion de vulnerabilidades tecnicas), A.8.20 (Seguridad en redes) | Pendiente | Sin actualizacion de software definida |
| DT-001 | A.5.13 (Etiquetado de informacion), A.5.33 (Proteccion de registros), A.8.11 (Control de acceso) | Pendiente | Sin clasificacion formal implementada |
| PR-001 | A.8.1 (Proteccion equipos), A.8.20 (Seguridad en redes), A.8.21 (Seguridad de servicios en red) | Pendiente | Sin segmentacion de red implementada |
| PE-001 | A.5.4 (Responsabilidades), A.5.6 (Contacto con la autoridad), A.6.3 (Toma de conciencia) | Pendiente | Sin capacitacion formal en seguridad |

---

## 4. Procedimiento de Auditoria AS-IS

### 4.1 Objetivo
Identificar, documentar y clasificar todos los activos de informacion de la UNCP como linea base para la implementacion del SGSI (PGTD-01).

### 4.2 Alcance
Todas las unidades organizacionales de la UNCP en las 4 sedes:
- Sede Central (Huancayo)
- Sede Mantaro (Jauja)
- Sede Satipo
- Sede Tarma

### 4.3 Metodologia

#### Fase 1: Preparacion (Semana 1)
1. Designar responsable de inventario por cada unidad organizacional
2. Distribuir la presente plantilla
3. Capacitar a los responsables en la clasificacion C-I-D

#### Fase 2: Levantamiento (Semana 2-3)
1. Cada unidad completa su inventario usando la plantilla
2. La OTI consolida y revisa consistencia
3. Identificar activos compartidos o duplicados entre unidades

#### Fase 3: Valoracion (Semana 4)
1. Asignar niveles C-I-D a cada activo
2. Calcular nivel de criticidad
3. Identificar controles ISO 27001 aplicables

#### Fase 4: Reporte (Semana 5)
1. Generar registro maestro de activos consolidado
2. Identificar brechas (activos sin controles)
3. Priorizar activos criticos para proteccion inmediata
4. Presentar informe a la Alta Direccion

### 4.4 Formulario de Auditoria por Unidad

```
UNIDAD ORGANIZACIONAL: _________________________________
RESPONSABLE DEL INVENTARIO: ____________________________
FECHA: _________________________________________________

---

ACTIVO #: ___
Nombre del Activo: _____________________________________
Descripcion: ___________________________________________
Tipo: [ ] HW  [ ] SW  [ ] DT  [ ] PR  [ ] PE  [ ] SV  [ ] IN  [ ] SF
Propietario: ____________________________________________
Custodio: _______________________________________________
Ubicacion Fisica: _______________________________________
Ubicacion Logica (IP/URL/Ruta): _________________________
Formato/Soporte: ________________________________________
Usuarios/Clientes: ______________________________________

Clasificacion:
  Confidencialidad: [ ] 1 - Publico  [ ] 2 - Interno  [ ] 3 - Confidencial
  Integridad:       [ ] 1 - Baja     [ ] 2 - Media     [ ] 3 - Alta
  Disponibilidad:   [ ] 1 - Baja     [ ] 2 - Media     [ ] 3 - Alta

Controles Actuales: _____________________________________

Observaciones: __________________________________________
```

### 4.5 Criterios de Aceptacion

- 100% de unidades organizacionales completan inventario
- Cada activo tiene clasificacion C-I-D asignada
- Registro maestro consolidado y aprobado por OTI
- Activos criticos identificados y reportados a la Alta Direccion

---

## 5. Registro de Cambios

| Version | Fecha | Descripcion del Cambio | Responsable |
|---|---|---|---|
| 1.0 | 2025-05-30 | Creacion inicial de la plantilla | Comite de Gobierno Digital UNCP |

---

*Documento: PL-ACT-001 | Version: 1.0 | Estado: Borrador | Proyecto: PGTD-01 (SGSI)*
