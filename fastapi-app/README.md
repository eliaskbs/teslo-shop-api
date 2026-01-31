# Teslo Shop API (FastAPI)

Migración del proyecto NestJS/TypeORM a **FastAPI** con **SQLAlchemy** (ORM declarativo similar a TypeORM).

## Estructura

```
fastapi-app/
├── config.py           # Configuración (Pydantic Settings)
├── database.py         # Engine y sesión SQLAlchemy
├── main.py             # Aplicación FastAPI
├── requirements.txt
├── seed_data.py        # Loader de datos de seed
├── seed_data.json      # Datos de seed (opcional; ver abajo)
├── helpers/            # Filtro y nombre de archivos subidos
├── models/             # Modelos SQLAlchemy (Product, ProductImage)
├── routers/            # Products, Seed, Files
├── schemas/            # DTOs Pydantic (CreateProduct, UpdateProduct, paginación)
└── services/           # Lógica de negocio (Products, Seed, Files)
```

## Requisitos

- Python 3.11+
- PostgreSQL (misma base que el proyecto NestJS si quieres reutilizarla)

## Instalación

```bash
cd fastapi-app
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env con tu DB y HOST_API
```

## Ejecución

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

O desde `main.py`:

```bash
python main.py
```

## Endpoints (prefijo `/api`)

- **Products**: `GET/POST /api/products`, `GET/PATCH/DELETE /api/products/{id|slug|title}`
- **Seed**: `GET /api/seed` — ejecuta el seed (borra productos y vuelve a insertar)
- **Files**: `GET /api/files/product/{imageName}`, `POST /api/files/product` (subir imagen)

Las imágenes se guardan en `../static/products` (raíz del repo).

## Datos de seed

- Por defecto, `seed_data.py` carga `seed_data.json` si existe.
- Si no existe, usa una lista mínima de 2 productos.
- Para cargar **todos** los productos del proyecto NestJS, convierte `src/seed/data/seed.data.ts` a JSON (eliminando el campo `type` de cada producto) y guarda el resultado como `seed_data.json` en esta carpeta.

## Notas

- Las tablas se llaman `product` y `product_image`. Si usas la misma base que NestJS/TypeORM (tablas `Product` y `ProductImage`), ajusta `__tablename__` en `models/product.py` o crea una base nueva para FastAPI.
