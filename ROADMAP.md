# 🗺️ Runik Dashboard API - Roadmap

Este roadmap define las fases de desarrollo para construir la API del dashboard empresarial **Runik**.

---

## 🚀 FASE 1: Configuración inicial
- [x] Inicializar proyecto FastAPI
- [x] Configurar PostgreSQL y conexión (SQLAlchemy)
- [x] Crear estructura de carpetas base
- [x] Configurar variables de entorno (.env)
- [x] Crear modelo de Usuario
- [x] Autenticación JWT
- [x] Hasheo de contraseñas
- [x] Documentación inicial con Swagger (`/docs`)

---

## 📦 FASE 2: Módulos de Inventario
- [ ] CRUD de Productos
- [ ] CRUD de Categorías
- [ ] CRUD de Marcas
- [ ] CRUD de Proveedores
- [ ] Entradas de productos
- [ ] Validaciones de stock mínimo y notificaciones internas

---

## 👥 FASE 3: Clientes y Órdenes
- [ ] CRUD de Clientes
- [ ] CRUD de Órdenes
- [ ] Cálculo de totales e impuestos
- [ ] Asociación de órdenes con clientes y productos
- [ ] Control de estados de orden

---

## 📊 FASE 4: Reportes y Dashboard
- [ ] Endpoint `/reports/sales`
- [ ] Endpoint `/reports/inventory`
- [ ] Endpoint `/reports/finances`
- [ ] Endpoint `/dashboard/overview`
- [ ] Integración con librería de gráficos

---

## 🔐 FASE 5: Seguridad avanzada y roles
- [ ] Sistema de roles
- [ ] Middleware de permisos
- [ ] Rate limiting
- [ ] Refresh tokens
- [ ] Logs de actividad

---

## 🚢 FASE 6: Despliegue y CI/CD
- [ ] Dockerizar la aplicación
- [ ] Configurar HTTPS
- [ ] CI/CD (GitHub Actions o GitLab CI)
- [ ] Deploy en Render, Railway o AWS
- [ ] Monitoreo

---

## 🧪 FASE 7: Testing y documentación final
- [ ] Tests unitarios (pytest)
- [ ] Tests de integración
- [ ] Cobertura mínima del 80%
- [ ] Documentar todos los endpoints

---

## 🎯 FASE FINAL: Optimización
- [ ] Refactorización
- [ ] Caching con Redis
- [ ] Revisión de seguridad (OWASP)
- [ ] Feedback de usuarios
