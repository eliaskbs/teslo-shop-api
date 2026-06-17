# Teslo Shop API

API REST de e-commerce construida con [NestJS](https://nestjs.com/) para gestionar un catálogo de productos, autenticación de usuarios y carga de imágenes. Incluye documentación interactiva con Swagger y soporte para WebSockets.

## Características

- **Productos**: CRUD completo con paginación, búsqueda por término (slug, título o ID), tallas, género, etiquetas e imágenes.
- **Autenticación JWT**: Registro, inicio de sesión y verificación de estado del token. Rutas protegidas con roles.
- **Archivos**: Subida y servicio de imágenes de productos almacenadas localmente.
- **Seed**: Endpoint para poblar la base de datos con usuarios y productos de prueba.
- **WebSockets**: Gateway configurado para comunicación en tiempo real.
- **Swagger**: Documentación de la API disponible en `/api`.

## Stack tecnológico

| Tecnología | Uso |
|---|---|
| NestJS 11 | Framework backend |
| TypeORM | ORM y acceso a datos |
| PostgreSQL 15 | Base de datos |
| Passport + JWT | Autenticación |
| Swagger | Documentación de endpoints |
| Socket.io | WebSockets |
| Docker | Contenedor de PostgreSQL |

## Requisitos previos

- Node.js 18+
- Yarn
- Docker y Docker Compose (para la base de datos)

## Instalación

### 1. Clonar e instalar dependencias

```bash
git clone <url-del-repositorio>
cd teslo-shop-api
yarn install
```

### 2. Configurar variables de entorno

Copia el archivo de plantilla y completa los valores:

```bash
cp .env.template .env
```

Variables requeridas:

| Variable | Descripción |
|---|---|
| `DB_HOST` | Host de PostgreSQL (ej. `localhost`) |
| `DB_PORT` | Puerto de PostgreSQL (ej. `5432`) |
| `DB_NAME` | Nombre de la base de datos |
| `DB_USERNAME` | Usuario de PostgreSQL |
| `DB_PASSWORD` | Contraseña de PostgreSQL |
| `PORT` | Puerto del servidor (ej. `3000`) |
| `HOST_API` | URL base de la API (ej. `http://localhost:3000`) |
| `JWT_SECRET` | Clave secreta para firmar tokens JWT |

### 3. Levantar la base de datos

```bash
docker compose up -d
```

### 4. Ejecutar la aplicación

```bash
# Desarrollo (con hot-reload)
yarn run start:dev

# Producción
yarn run build
yarn run start:prod
```

La API estará disponible en `http://localhost:3000/api`.

## Endpoints principales

| Método | Ruta | Descripción | Auth |
|---|---|---|---|
| `POST` | `/api/auth/register` | Registrar usuario | No |
| `POST` | `/api/auth/login` | Iniciar sesión | No |
| `GET` | `/api/auth/check-status` | Verificar token | Sí |
| `GET` | `/api/products` | Listar productos (paginado) | No |
| `GET` | `/api/products/:term` | Buscar producto por término | No |
| `POST` | `/api/products` | Crear producto | Sí |
| `PATCH` | `/api/products/:id` | Actualizar producto | Sí |
| `DELETE` | `/api/products/:id` | Eliminar producto | No |
| `POST` | `/api/files/product` | Subir imagen de producto | No |
| `GET` | `/api/files/product/:imageName` | Obtener imagen de producto | No |
| `GET` | `/api/seed` | Poblar base de datos con datos iniciales | No |

## Seed de datos

Para cargar usuarios y productos de prueba, ejecuta:

```
GET http://localhost:3000/api/seed
```

> **Nota:** Este endpoint elimina todos los datos existentes antes de insertar los registros iniciales.

## Documentación Swagger

Con el servidor en ejecución, accede a la documentación interactiva en:

```
http://localhost:3000/api
```

## Scripts disponibles

```bash
yarn run start        # Iniciar en modo desarrollo
yarn run start:dev    # Iniciar con hot-reload
yarn run start:prod   # Iniciar en producción
yarn run build        # Compilar el proyecto
yarn run lint         # Ejecutar linter
yarn run test         # Ejecutar tests unitarios
yarn run test:e2e     # Ejecutar tests end-to-end
```

## Estructura del proyecto

```
src/
├── auth/           # Autenticación JWT, usuarios y roles
├── products/       # CRUD de productos e imágenes
├── files/          # Carga y servicio de archivos estáticos
├── seed/           # Datos iniciales de la base de datos
├── message-ws/     # Gateway de WebSockets
└── common/         # DTOs y utilidades compartidas
```
