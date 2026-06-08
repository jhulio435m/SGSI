---
title: Formato de Solicitud de Alta / Baja / Cambio de Acceso
code: F-SGSI-01
---

# Formato de Solicitud de Alta / Baja / Cambio de Acceso

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**ID Solicitud:** SOL-ACC-2026-001
**Fecha de Solicitud:** 02/06/2026
**Fecha Requerida de Implementación:** 05/06/2026

---

## Datos del Solicitante

- **Nombre Completo:** Ing. Luis Castillo Gutierrez
- **DNI:** 20456789
- **Unidad Orgánica:** Oficina de Seguridad y Confianza Digital
- **Cargo:** Oficial de Seguridad
- **Correo Institucional:** lcastillo@uncp.edu.pe
- **Teléfono / Anexo:** 987654321 / Anexo 4521
- **Jefe Inmediato (Nombre y Cargo):** Ing. Marco Antonio Quispe Laura -- Jefe de OTI

## Datos del Usuario Destinatario (si es distinto al solicitante)

- **Nombre Completo:** Bach. Carlos Alberto Huamán Rojas
- **DNI:** 48123456
- **Unidad Orgánica:** OTI -- Infraestructura
- **Cargo / Rol:** Analista de Seguridad TI
- **Tipo de Contrato:** [x] CAS [ ] Nombrado [ ] Tercero [ ] Proveedor [ ] Practicante

## Tipo de Solicitud

[ ] Alta de Usuario (Nuevo Ingreso)
[ ] Baja de Usuario (Cese / Renuncia / Término de Contrato)
[ ] Cambio de Perfil (Promoción / Traslado / Cambio de funciones)
[ ] Acceso Temporal (Proveedor / Practicante / Evento específico)
    Período: Desde -- Hasta
[ ] Desbloqueo de Cuenta (Bloqueo por intentos fallidos)
[x] Reseteo de Contraseña (Olvido / Expirada)

## Sistemas / Recursos Requeridos

### Sistemas Transaccionales

[ ] ERP ADESA (Módulo: __________)
[ ] SIGA / SIAF
[ ] Campus Virtual (Rol: __________ / Curso: __________)
[ ] Sistema de Investigación (SINIA / REDIAM)
[ ] Sistema de Grados y Títulos
[ ] Sistema de Biblioteca

### Acceso a Infraestructura

[x] VPN / Acceso Remoto (Perfil: Administrador de Infraestructura)
[x] Carpeta de Red Compartida (Ruta: \\servidor-sgsiactas)
[ ] Correo Institucional (Microsoft 365)
[ ] Acceso a Servidor (SSH/RDP -- Especificar: __________)
[ ] Base de Datos (Sistema: __________)

### Servicios en la Nube (Huawei Cloud)

[x] Consola de Administración (Rol: IAM Operator)
[ ] Almacenamiento OBS (Bucket: __________)
[ ] Base de Datos Cloud (Instancia: __________)

### Perfiles y Privilegios

**Nivel de Acceso Requerido:**

[ ] Solo Lectura
[x] Lectura/Escritura
[ ] Administrador (requiere autorización especial)
[ ] Acceso con Privilegios (PAM -- Justificación requerida)

**¿Requiere MFA?**

[x] Sí [ ] No

**¿Requiere acceso desde dispositivo móvil?**

[ ] Sí [x] No

## Justificación

El Bach. Carlos Huamán ha sido designado como Analista de Seguridad TI para apoyar la implementación del SIEM Wazuh y el monitoreo continuo de los servicios cloud. Requiere acceso a la consola Huawei Cloud (IAM Operator) para revisar logs de CBR y configurar alertas de monitoreo, así como acceso a la carpeta de actas del SGSI para documentar hallazgos de auditoría. Se le reasigna la contraseña de su cuenta institucional por expiración de la contraseña temporal.

## Autorizaciones

### Jefe Inmediato del Solicitante

**Nombre:** Ing. Marco Antonio Quispe Laura
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Fecha:** 02/06/2026

### Oficial de Seguridad (si aplica -- accesos críticos, privilegiados, proveedores)

**Nombre:** Ing. Luis Castillo Gutierrez
**Visto Bueno:** [x] Aprobado [ ] Denegado
**Observaciones:** Acceso temporal por 90 días para proyecto SIEM. Evaluar renovación según desempeño.
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Fecha:** 02/06/2026

### Ejecutado por (OTI)

**Nombre del Ejecutor:** Ing. Miguel Ángel Paredes Torres
**Fecha de Implementación:** 05/06/2026
**Comprobante / Ticket:** TICKET-OTI-2026-0891
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Confirmación de Cierre (para bajas)

[ ] Correo institucional desactivado
[ ] Acceso a sistemas revocado
[ ] VPN/Carpetas de red eliminadas
[ ] Cuenta de cloud desactivada
[ ] Activos físicos devueltos (ver F-SGSI-03)

---

**Nota:** Este formulario debe ser archivado por la OTI y por el Oficial de Seguridad durante el período de retención establecido en POL-SGSI-03 (mínimo 3 años).