import base64
import json
from pathlib import Path

TEMPLATE_PATH = (
    Path(__file__).parent
    / "templates"
    / "photo_grid_template.html"
)


def imagen_a_base64(path: Path) -> str:

    ext = (
        path.suffix
        .lower()
        .replace(".", "")
    )

    mime = {
        "jpg": "jpeg",
        "jpeg": "jpeg",
        "png": "png",
        "webp": "webp"
    }.get(ext, "png")

    with open(path, "rb") as f:

        data = (
            base64
            .b64encode(f.read())
            .decode()
        )

    return (
        f"data:image/{mime};base64,{data}"
    )


def imagenes_de_carpeta(
    carpeta: Path
) -> list[Path]:

    imagenes = []

    for ext in [
        "*.png",
        "*.jpg",
        "*.jpeg",
        "*.webp"
    ]:

        imagenes.extend(
            carpeta.glob(ext)
        )

    return sorted(imagenes)


def cargar_template() -> str:

    with open(
        TEMPLATE_PATH,
        encoding="utf-8"
    ) as f:

        return f.read()


def build_photo_grid(
    imagenes: list[Path],
    titulo: str
) -> str:

    images_js = json.dumps(
        [
            imagen_a_base64(img)
            for img in imagenes
        ],
        ensure_ascii=False
    )

    template = cargar_template()

    html = (
        template
        .replace(
            "{{IMAGES}}",
            images_js
        )
        .replace(
            "{{TITULO}}",
            titulo
        )
    )

    return html


def render_photo_grid_desde_carpeta(
    carpeta: str | Path,
    titulo: str
) -> str | None:

    carpeta = Path(carpeta)

    if not carpeta.exists():
        return None

    imagenes = imagenes_de_carpeta(
        carpeta
    )

    if not imagenes:
        return None

    return build_photo_grid(
        imagenes,
        titulo
    )