import base64
import json
from pathlib import Path

# ── Rutas ─────────────────────────────────────────────────────────────────────

TEMPLATE_PATH = Path(__file__).parent / "templates" / "flipbook_template.html"
LOGO_PATH     = Path("assets/logo.png")

# ── Helpers de imagen ─────────────────────────────────────────────────────────

def imagen_a_base64(path: Path) -> str:
    path = Path(path)
    ext  = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "png")
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{data}"

def imagenes_de_carpeta(carpeta: Path) -> list[Path]:
    imagenes = []
    for ext in ["*.png", "*.jpg", "*.jpeg", "*.webp"]:
        imagenes.extend(carpeta.glob(ext))
    return sorted(imagenes)

# ── Carga de template ─────────────────────────────────────────────────────────

def cargar_template() -> str:
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        return f.read()

# ── Constructor principal ─────────────────────────────────────────────────────

def build_flipbook(grupos: list[list[Path]], encabezados: list[str], titulo: str = "📖 Imágenes de campaña") -> str:
    # Serializar páginas como JSON
    pages = [
        {
            "label": encabezados[i],
            "imgs":  [imagen_a_base64(img) for img in grupo],
        }
        for i, grupo in enumerate(grupos)
    ]
    pages_js = json.dumps(pages, ensure_ascii=False)

    logo_src = imagen_a_base64(LOGO_PATH)

    template = cargar_template()

    html = (
        template
        .replace("{{PAGES}}",    pages_js)
        .replace("{{TITULO}}",   titulo)
        .replace("{{LOGO_SRC}}", logo_src)
    )

    return html

# ── Función de conveniencia para Streamlit ────────────────────────────────────

def render_flipbook_desde_carpeta(
    carpeta: str | Path,
    titulo: str,
    imgs_por_pagina: int = 6,
) -> str | None:
    carpeta = Path(carpeta)
    if not carpeta.exists():
        return None
    imagenes = imagenes_de_carpeta(carpeta)

    if not imagenes:
        return None

    grupos = [
        imagenes[i : i + imgs_por_pagina]
        for i in range(
            0,
            len(imagenes),
            imgs_por_pagina
        )
    ]

    encabezados = [
        f"{titulo} - Pág. {i + 1}"
        for i in range(len(grupos))
    ]
    return build_flipbook(grupos, encabezados, titulo)