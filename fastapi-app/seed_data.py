"""
Datos de seed para productos.
Para cargar el dataset completo, convierte src/seed/data/seed.data.ts a JSON
(sin el campo 'type') y reemplaza o amplía seed_data.json.
"""
import json
from pathlib import Path

_json_path = Path(__file__).parent / "seed_data.json"

if _json_path.exists():
    with open(_json_path, encoding="utf-8") as f:
        initial_data = json.load(f)
else:
    # Fallback: datos mínimos para que el seed funcione
    initial_data = {
        "products": [
            {
                "description": "Men's Chill Crew Neck Sweatshirt.",
                "images": ["1740176-00-A_0_2000.jpg", "1740176-00-A_1.jpg"],
                "stock": 7,
                "price": 75,
                "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
                "slug": "mens_chill_crew_neck_sweatshirt",
                "tags": ["sweatshirt"],
                "title": "Men's Chill Crew Neck Sweatshirt",
                "gender": "men",
            },
            {
                "description": "The Men's Quilted Shirt Jacket.",
                "images": ["1740507-00-A_0_2000.jpg", "1740507-00-A_1.jpg"],
                "stock": 5,
                "price": 200,
                "sizes": ["XS", "S", "M", "XL", "XXL"],
                "slug": "men_quilted_shirt_jacket",
                "tags": ["jacket"],
                "title": "Men's Quilted Shirt Jacket",
                "gender": "men",
            },
        ]
    }
