# 🧭 Runik Dashboard API

API RESTful desarrollada con **FastAPI** y **PostgreSQL**, diseñada para servir como backend de un **dashboard empresarial**.  
Permite gestionar usuarios, inventarios, productos, órdenes, clientes, reportes y estadísticas en tiempo real.  
Su enfoque principal es ofrecer una experiencia moderna, rápida y segura para la administración integral de negocios.

---

## 🚀 Características principales

- ⚡ **FastAPI** — rendimiento y tipado moderno en Python.
- 🗃️ **PostgreSQL** + **SQLAlchemy** + **Alembic** para ORM y migraciones.
- 🔐 **Autenticación JWT** (JSON Web Tokens) con control de roles (admin/user).
- 📦 Módulos de gestión: usuarios, productos, inventario, proveedores, clientes y órdenes.
- 📊 Endpoints para **reportes** y **dashboard** con métricas.
- 🧰 Arquitectura escalable y limpia (routers, servicios, schemas, models).
- 🧪 Preparado para testing y despliegue (CI/CD ready).

---

## 🏗️ Estructura del proyecto

```
project/
│
├─ app/
│   ├─ api/
│   │   └─ v1/
│   │       ├─ routes/
│   │       │   ├─ auth.py
│   │       │   ├─ users.py
│   │       │   ├─ products.py
│   │       │   ├─ categories.py
│   │       │   ├─ suppliers.py
│   │       │   ├─ customers.py
│   │       │   ├─ orders.py
│   │       │   ├─ reports.py
│   │       │   └─ dashboard.py
│   │       └─ __init__.py
│   │
│   ├─ core/
│   │   ├─ config.py
│   │   ├─ database.py
│   │   └─ security.py
│   │
│   ├─ models/
│   ├─ schemas/
│   ├─ services/
│   └─ main.py
│
├─ .env
├─ requirements.txt
├─ README.md
└─ ROADMAP.md
```

---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/runik-dashboard-api.git
cd runik-dashboard-api
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno (.env)

```bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost:port/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5️⃣ Migraciones con Alembic

```bash
alembic upgrade head
```

### 6️⃣ Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor correrá en:
👉 http://127.0.0.1:8000

---

## 📍 Rutas base (v1)

| Módulo        | Endpoint base        |
| ------------- | -------------------- |
| Autenticación | `/api/v1/auth`       |
| Usuarios      | `/api/v1/users`      |
| Productos     | `/api/v1/products`   |
| Categorías    | `/api/v1/categories` |
| Marcas        | `/api/v1/brands`     |
| Proveedores   | `/api/v1/suppliers`  |
| Clientes      | `/api/v1/customers`  |
| Órdenes       | `/api/v1/orders`     |
| Reportes      | `/api/v1/reports`    |
| Dashboard     | `/api/v1/dashboard`  |

---

## 🔐 Seguridad

- Autenticación basada en **JWT Tokens**.
- Encriptación de contraseñas con **bcrypt**.
- Control de acceso mediante roles (`admin`, `user`).
- Validación estricta de datos con **Pydantic**.
- CORS habilitado y configuración para HTTPS.

---

## 🧪 Testing

```bash
pytest
```

---

## 🧰 Tecnologías

- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn
- PostgreSQL
- PyJWT
- bcrypt

---

## 🧭 Roadmap

Consulta el archivo [`ROADMAP.md`](./ROADMAP.md).

---

## 📜 Licencia

Proyecto bajo licencia MIT.  
© 2025 - Runik Dashboard API