import json
from pathlib import Path
import base64

def video_a_base64(path: Path) -> str:

    ext = path.suffix.lower().replace(".", "")

    mime_map = {
        "mp4": "video/mp4",
        "webm": "video/webm",
        "mov": "video/mp4",
        "mkv": "video/mp4",
        "avi": "video/mp4"
    }

    mime = mime_map.get(
        ext,
        "video/mp4"
    )

    with open(path, "rb") as f:

        data = base64.b64encode(
            f.read()
        ).decode()

    return f"data:{mime};base64,{data}"

TEMPLATE_PATH = (
    Path(__file__).parent
    / "templates"
    / "video_carousel_template.html"
)

def videos_de_carpeta(carpeta: Path) -> list[str]:
    videos = []
    for ext in [
        "*.mp4",
        "*.mov",
        "*.avi",
        "*.mkv",
        "*.webm"
    ]:
        videos.extend(carpeta.glob(ext))
    return sorted(videos)

def cargar_template() -> str:
    with open(
        TEMPLATE_PATH,
        encoding="utf-8"
    ) as f:
        return f.read()

def build_video_carousel(
    videos: list[Path],
    titulo: str
    ) -> str:
    videos_js = json.dumps(
        [
            video_a_base64(v)
            for v in videos
        ],
        ensure_ascii=False
    )
    template = cargar_template()
    html = (
        template
        .replace(
            "{{VIDEOS}}",
            videos_js
        )
        .replace(
            "{{TITULO}}",
            titulo
        )
    )
    return html

def render_video_carousel_desde_carpeta(
    carpeta: str | Path,
    titulo: str = "🎥 Videos de Campaña"
    ) -> str | None:
    carpeta = Path(carpeta)
    if not carpeta.exists():
        return None
    videos = videos_de_carpeta(carpeta)
    if not videos:
        return None
    return build_video_carousel(
        videos,
        titulo
    )