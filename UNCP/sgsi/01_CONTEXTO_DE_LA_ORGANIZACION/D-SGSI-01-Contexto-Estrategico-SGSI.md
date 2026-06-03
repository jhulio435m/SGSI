# D-SGSI-01: Análisis del Contexto Estratégico del SGSI-UNCP

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 1.0 (Análisis 360°: PESTEL, Porter, MEFE, MEFI, CAME)
**Referencia:** ISO/IEC 27001:2022 (Cláusula 4)

***

## Fase 1: Análisis del Entorno (Cláusula 4.1)

### 1.1. Análisis PESTEL (Macroentorno)

| Factor | Descripción y Diagnóstico | Impacto en SGSI |
| :--- | :--- | :--- |
| **Político** | Mandato nacional de Transformación Digital (PCM/SGTD). | **Alto.** Obliga a la implementación del SGSI por ley. |
| **Económico** | Presupuesto institucional (Canon/RDR) sujeto a priorización. | **Medio.** Riesgo de retraso en compras de hardware crítico. |
| **Social** | Generación de estudiantes digitalmente nativos con alta expectativa. | **Alto.** Exige disponibilidad 24/7 y servicios móviles seguros. |
| **Tecnológico** | Auge de la Inteligencia Artificial y servicios Cloud (Huawei Cloud). | **Crítico.** Requiere controles de seguridad avanzados y auditoría de IA. |
| **Ecológico** | Política de "Cero Papel" y eco-eficiencia (Green IT). | **Medio.** Impulsa la digitalización segura y reducción de energía en DC. |
| **Legal** | Nueva Ley de Protección de Datos (D.S. 016-2024-JUS) y Ciberdefensa. | **Alto.** Incrementa las sanciones por brechas de datos. |

### 1.2. Las 5 Fuerzas de Porter (Microentorno)

1.  **Rivalidad entre competidores:** Otras universidades públicas y privadas compiten por prestigio y licenciamiento SUNEDU. La seguridad es un diferenciador de calidad.
2.  **Poder de negociación de proveedores:** Alta dependencia de proveedores de Nube (Huawei) e Internet. Se requiere gestión de SLAs (A.15).
3.  **Amenaza de nuevos competidores:** Programas de educación virtual global. Exige una plataforma UNCP resiliente y segura.
4.  **Amenaza de productos sustitutos:** Cursos online y certificaciones técnicas. La UNCP debe proteger su valor oficial (Grados y Títulos).
5.  **Poder de negociación de los alumnos:** Los estudiantes demandan transparencia y protección de su privacidad.

***

## Fase 2: Diagnóstico Estratégico Cuantificado

### 2.1. Matriz de Evaluación de Factores Internos (MEFI)

| Fortaleza / Debilidad | Peso | Calificación | Ponderado |
| :--- | :--- | :--- | :--- |
| **F1:** Comité de Gobierno Digital formalizado (Res. 1862). | 0.15 | 4 | 0.60 |
| **F2:** Infraestructura Cloud Huawei Cloud operativa. | 0.15 | 4 | 0.60 |
| **D1:** Nivel de madurez digital inicial (1.569). | 0.20 | 1 | 0.20 |
| **D2:** Resistencia al cambio cultural en personal antiguo. | 0.20 | 2 | 0.40 |
| **D3:** Limitada segmentación de red en facultades. | 0.30 | 1 | 0.30 |
| **TOTAL** | **1.00** | - | **2.10** |
*(Nota: Un puntaje de 2.10 indica una posición interna débil; se requiere fortalecer la segmentación y la cultura).*

### 2.2. Matriz de Evaluación de Factores Externos (MEFE)

| Oportunidad / Amenaza | Peso | Calificación | Ponderado |
| :--- | :--- | :--- | :--- |
| **O1:** Presupuesto asignado al PGTD (S/ 6.4M). | 0.25 | 4 | 1.00 |
| **O2:** Apoyo técnico de la PCM/SGTD para interoperabilidad. | 0.15 | 3 | 0.45 |
| **A1:** Incremento de ataques de Ransomware a universidades. | 0.35 | 1 | 0.35 |
| **A2:** Nuevas exigencias legales de protección de datos (JUS). | 0.25 | 2 | 0.50 |
| **TOTAL** | **1.00** | - | **2.30** |
*(Nota: Un puntaje de 2.30 indica que la UNCP está respondiendo de forma promedio a las amenazas externas; debe acelerar el SGSI).*

***

## Fase 3: Estrategia Proactiva (Análisis CAME)

Basado en el FODA cruzado, se establecen las siguientes acciones:

| Estrategia | Acción Concreta (Plan de Acción) |
| :--- | :--- |
| **Corregir (D3+O1)** | Ejecutar el proyecto PGTD-04 para implementar **Microsegmentación ZTNA** y remediar la debilidad de red. |
| **Afrontar (A1+F2)** | Utilizar la **Resiliencia Cloud** y backups inmutables en Huawei Cloud para defenderse del Ransomware. |
| **Mantener (F1+O2)** | Fortalecer la gobernanza del Comité de Gobierno Digital mediante la auditoría continua (P-SGSI-09). |
| **Explotar (O2+D1)** | Aprovechar los lineamientos de la PCM para elevar rápidamente el nivel de madurez en servicios digitales. |

***

## Fase 4: Definición del Alcance Basado en Riesgos (Cláusula 4.3)

El alcance del SGSI (definido en `Alcance-SGSI-UNCP.md`) se ratifica considerando que los mayores riesgos provienen de la **interacción de la red de facultades con servicios externos**. Se confirma la necesidad de un enfoque **Zero Trust** para mitigar las debilidades internas detectadas en la MEFI.

***
**Resultado del Diagnóstico:** La UNCP posee una base tecnológica sólida (Cloud) pero una infraestructura de red y una cultura orgánica vulnerables. El SGSI debe priorizar la **Capacitación (OGTD6)** y la **Seguridad de Red (ZTNA)** para equilibrar la balanza estratégica.
