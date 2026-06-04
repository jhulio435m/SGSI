# R-SGSI-01: Inventario de Activos de Informacion - UNCP

## Instrucciones

1. El responsable de cada unidad organizacional debe completar una fila por activo.
2. Los niveles de clasificacion (Confidencialidad, Integridad, Disponibilidad) se asignan segun la Sección 2.
3. Entregar a la Oficina de Tecnologías de la Información (OTI) para consolidacion.
4. Actualizar semestralmente o ante cambios significativos.

***

## 1. Registro Maestro de Activos

\begin{compacttable}[Inventario de Activos Críticos (Parte A)]
\begin{tabularx}{\textwidth}{|c|L{1.5cm}|L{2cm}|Y|L{2cm}|L{1.5cm}|L{1.5cm}|}
\hline
\tableheader \# & ID & Nombre & Descripcion & Tipo & Prop. & Cust. \\ \hline
1 & HW-001 & Servidor ADESA & Gestion documental principal & Hardware & OTI & OTI \\ \hline
2 & SW-001 & Sistema GESDOC & Tramite documentario & Software & OTI & OTI \\ \hline
3 & DT-001 & BD Matricula & Registro de estudiantes & Dato & Acad. & OTI \\ \hline
4 & PR-001 & Red LAN & Red cableada central & Red & OTI & OTI \\ \hline
5 & PE-001 & Personal OTI & Administradores & Persona & OTI & RRHH \\ \hline
\end{tabularx}
\end{compacttable}

\begin{compacttable}[Inventario de Activos Críticos (Parte B: Ubicación y Soporte)]
\begin{tabularx}{\textwidth}{|L{1.5cm}|L{2.5cm}|L{2.5cm}|L{2cm}|Y|}
\hline
\tableheader ID & Ubicacion Fisica & Ubicacion Logica & Soporte & Usuarios \\ \hline
HW-001 & Data Center & 192.168.x.x & Servidor & Administrativos \\ \hline
SW-001 & Servidor ADESA & gesdoc.uncp.edu.pe & Web App & Comunidad UNCP \\ \hline
DT-001 & Servidor BD & db.uncp.edu.pe & BD Digital & Academica, OTI \\ \hline
PR-001 & Campus & 10.0.0.0/16 & Fisico-Red & Sede Central \\ \hline
PE-001 & Oficina OTI & N/A & Humano & N/A \\ \hline
\end{tabularx}
\end{compacttable}

***

## 2. Clasificacion de Seguridad (C-I-D)

| ID Activo | Confidencialidad | Integridad | Disponibilidad | Criticidad | Fecha |
|---|---|---|---|---|---|
| HW-001 | 2 - Interno | 3 - Alta | 3 - Alta | Alta | 2026-06-03 |
| SW-001 | 1 - Publico | 2 - Media | 2 - Media | Media | 2026-06-03 |
| DT-001 | 3 - Confidencial | 3 - Alta | 3 - Alta | Critico | 2026-06-03 |
| PR-001 | 1 - Publico | 2 - Media | 3 - Alta | Alta | 2026-06-03 |
| PE-001 | 2 - Interno | 2 - Media | 2 - Media | Media | 2026-06-03 |

***

## 3. Controles Asociados (ISO 27001:2022)

| ID Activo | Controles Aplicables | Estado | Observaciones |
|---|---|---|---|
| HW-001 | A.5.9, A.7.9, A.8.1 | Pendiente | Sin biometría |
| SW-001 | A.5.23, A.8.8, A.8.20 | Pendiente | Versión antigua |
| DT-001 | A.5.13, A.5.33, A.8.11 | Pendiente | Requiere cifrado |

***

## 4. Formulario de Auditoria por Unidad

### 4.1 Identificación de la Unidad
| Campo | Información |
| :--- | :--- |
| **Unidad Organizacional:** | _________________________________ |
| **Responsable Inventario:** | _________________________________ |
| **Fecha de Registro:** | _________________________________ |

### 4.2 Detalle del Activo (Completar por cada activo)
| Atributo | Espacio para Registro |
| :--- | :--- |
| **ID Activo / \#:** | _________________________________ |
| **Nombre del Activo:** | _________________________________ |
| **Descripción:** | _________________________________ |
| **Tipo:** | [ ] Hardware [ ] Software [ ] Dato [ ] Red [ ] Persona |
| **Ubicación Lógica:** | _________________________________ |
| **Usuarios Autorizados:** | _________________________________ |
| **Valor C-I-D:** | C:[ ] I:[ ] D:[ ] |

***
*Este documento es propiedad de la Universidad Nacional del Centro del Perú.*
