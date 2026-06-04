# F-SGSI-01: Formato de Solicitud de Alta / Baja / Cambio de Acceso

**Organización:** Universidad Nacional del Centro del Perú (UNCP)
**Versión:** 2.0 (Alineado a P-SGSI-03 — Gestión de Identidades Zero Trust)
**ID Solicitud:** SOL-ACC-[Año]-[Nro]
**Fecha de Solicitud:** [Fecha]
**Fecha Requerida de Implementación:** [Fecha]

***

## 1. Datos del Solicitante
*   **Nombre Completo:** [Nombre]
*   **DNI:** [DNI]
*   **Unidad Orgánica:** [Facultad/Oficina]
*   **Cargo:** [Cargo]
*   **Correo Institucional:** [Correo]
*   **Teléfono / Anexo:** [Teléfono]
*   **Jefe Inmediato (Nombre y Cargo):** [Nombre]

## 2. Datos del Usuario Destinatario (si es distinto al solicitante)
*   **Nombre Completo:** [Nombre]
*   **DNI:** [DNI]
*   **Unidad Orgánica:** [Facultad/Oficina]
*   **Cargo / Rol:** [Cargo]
*   **Tipo de Contrato:** [ ] CAS [ ] Nombrado [ ] Tercero [ ] Proveedor [ ] Practicante

## 3. Tipo de Solicitud
[ ] **Alta de Usuario** (Nuevo Ingreso)
[ ] **Baja de Usuario** (Cese / Renuncia / Término de Contrato)
[ ] **Cambio de Perfil** (Promoción / Traslado / Cambio de funciones)
[ ] **Acceso Temporal** (Proveedor / Practicante / Evento específico)
    Período: Desde [Fecha] — Hasta [Fecha]
[ ] **Desbloqueo de Cuenta** (Bloqueo por intentos fallidos)
[ ] **Reseteo de Contraseña** (Olvido / Expirada)

## 4. Sistemas / Recursos Requeridos
### 4.1 Sistemas Transaccionales
[ ] ERP ADESA (Módulo: __________)
[ ] SIGA / SIAF
[ ] Campus Virtual (Rol: __________ / Curso: __________)
[ ] Sistema de Investigación (SINIA / REDIAM)
[ ] Sistema de Grados y Títulos
[ ] Sistema de Biblioteca

### 4.2 Acceso a Infraestructura
[ ] VPN / Acceso Remoto (Perfil: __________)
[ ] Carpeta de Red Compartida (Ruta: __________)
[ ] Correo Institucional (Microsoft 365)
[ ] Acceso a Servidor (SSH/RDP — Especificar: __________)
[ ] Base de Datos (Sistema: __________)

### 4.3 Servicios en la Nube (Huawei Cloud)
[ ] Consola de Administración (Rol: __________)
[ ] Almacenamiento OBS (Bucket: __________)
[ ] Base de Datos Cloud (Instancia: __________)

### 4.4 Perfiles y Privilegios
**Nivel de Acceso Requerido:**
[ ] Solo Lectura
[ ] Lectura/Escritura
[ ] Administrador (requiere autorización especial)
[ ] Acceso con Privilegios (PAM — Justificación requerida)

**¿Requiere MFA?**
[ ] Sí [ ] No

**¿Requiere acceso desde dispositivo móvil?**
[ ] Sí [ ] No

## 5. Justificación
[Describir el motivo de la solicitud y las funciones que el usuario desempeñará que requieren estos accesos. Para accesos privilegiados, detalle la necesidad específica.]

## 6. Autorizaciones

### 6.1 Jefe Inmediato del Solicitante
**Nombre:** [Nombre]
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Fecha:** [Fecha]

### 6.2 Oficial de Seguridad (si aplica — accesos críticos, privilegiados, proveedores)
**Nombre:** [Nombre]
**Visto Bueno:** [ ] Aprobado [ ] Denegado
**Observaciones:** [Observaciones]
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Fecha:** [Fecha]

### 6.3 Ejecutado por (OTI)
**Nombre del Ejecutor:** [Nombre]
**Fecha de Implementación:** [Fecha]
**Comprobante / Ticket:** [ID de ticket]
**Firma:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## 7. Confirmación de Cierre (para bajas)
[ ] Correo institucional desactivado
[ ] Acceso a sistemas revocado
[ ] VPN/Carpetas de red eliminadas
[ ] Cuenta de cloud desactivada
[ ] Activos físicos devueltos (ver F-SGSI-03)

***

**Nota:** Este formulario debe ser archivado por la OTI y por el Oficial de Seguridad durante el período de retención establecido en POL-SGSI-03 (mínimo 3 años).
