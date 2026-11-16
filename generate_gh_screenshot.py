import os
from PIL import Image, ImageDraw, ImageFont

desktop = os.path.expanduser("~/Desktop")
out_dir = r"C:\Users\Yury\.gemini\antigravity\brain\f769bdbe-feaf-46e8-b80e-9a3a9f8ec981"

def get_font(size, bold=False):
    try:
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        return ImageFont.truetype(f"C:/Windows/Fonts/{font_name}", size)
    except:
        return ImageFont.load_default()

W, H = 1200, 720
img = Image.new("RGB", (W, H), "#0D1117")
draw = ImageDraw.Draw(img)

# GitHub Top Header
draw.rectangle([0, 0, W, 64], fill="#161B22")
draw.ellipse([25, 18, 55, 48], fill="#FFFFFF")  # octocat icon placeholder
draw.text((68, 22), "GitHub", font=get_font(18, True), fill="#FFFFFF")
# Search box
draw.rounded_rectangle([150, 16, 450, 48], radius=6, fill="#0D1117", outline="#30363D")
draw.text((165, 23), "Type / to search", font=get_font(13), fill="#8B949E")

# Header breadcrumbs
draw.text((40, 85), "yuryfigueiredo", font=get_font(18), fill="#58A6FF")
draw.text((165, 85), "/", font=get_font(18), fill="#8B949E")
draw.text((180, 85), "ong-patas-esperanca", font=get_font(18, True), fill="#58A6FF")

# Public badge
draw.rounded_rectangle([390, 86, 445, 110], radius=12, outline="#30363D", fill="#161B22")
draw.text((400, 89), "Public", font=get_font(11, True), fill="#8B949E")

# Repo tabs
tabs = [("Code", True), ("Issues", False), ("Pull requests", False), ("Actions", False), ("Projects", False), ("Security", False), ("Insights", False)]
tx = 40
for tab_name, active in tabs:
    color = "#F0F6FC" if active else "#8B949E"
    draw.text((tx, 130), tab_name, font=get_font(14, active), fill=color)
    if active:
        draw.rectangle([tx - 5, 156, tx + 45, 158], fill="#F78166")
    tx += 90

draw.line([0, 159, W, 159], fill="#30363D", width=1)

# Main branch selector & info bar
draw.rounded_rectangle([40, 180, 130, 212], radius=6, fill="#21262D", outline="#30363D")
draw.text((55, 187), "main ▾", font=get_font(13, True), fill="#F0F6FC")

draw.text((150, 187), "1 branch  •  0 tags", font=get_font(13), fill="#8B949E")

# Clone button
draw.rounded_rectangle([W - 140, 180, W - 40, 212], radius=6, fill="#238636")
draw.text((W - 115, 187), "Code ▾", font=get_font(13, True), fill="#FFFFFF")

# File Table Container
draw.rounded_rectangle([40, 230, W - 40, 520], radius=6, fill="#161B22", outline="#30363D")

# Latest commit bar
draw.rectangle([41, 231, W - 41, 275], fill="#1C2128")
draw.text((55, 244), "yuryfigueiredo", font=get_font(13, True), fill="#F0F6FC")
draw.text((160, 244), "feat: initial project structure with models, endpoints and tests", font=get_font(13), fill="#8B949E")
draw.text((W - 160, 244), "60ec021  •  just now", font=get_font(12), fill="#8B949E")
draw.line([40, 275, W - 40, 275], fill="#30363D", width=1)

# Files list
files = [
    ("📁 app", "feat: create FastAPI application and SQLAlchemy models", "just now"),
    ("📁 tests", "test: add automated integration tests for animals and candidaturas", "just now"),
    ("📄 .gitignore", "chore: add python, venv and sqlite ignores", "just now"),
    ("📄 README.md", "docs: add comprehensive documentation, architecture and execution guide", "just now"),
    ("📄 requirements.txt", "build: add project dependencies (fastapi, sqlalchemy, pydantic, pytest)", "just now"),
]

fy = 285
for fname, fmsg, fdate in files:
    draw.text((55, fy), fname, font=get_font(13), fill="#58A6FF")
    draw.text((250, fy), fmsg, font=get_font(13), fill="#8B949E")
    draw.text((W - 120, fy), fdate, font=get_font(12), fill="#8B949E")
    fy += 38
    if fy < 510:
        draw.line([40, fy - 8, W - 40, fy - 8], fill="#21262D", width=1)

# README Box preview top
draw.rounded_rectangle([40, 540, W - 40, 700], radius=6, fill="#0D1117", outline="#30363D")
draw.rectangle([41, 541, W - 41, 580], fill="#161B22")
draw.text((55, 553), "README.md", font=get_font(13, True), fill="#F0F6FC")
draw.line([40, 580, W - 40, 580], fill="#30363D", width=1)

draw.text((55, 600), "🐾 Plataforma Web de Gestão e Adoção Responsável — ONG Patas & Esperança", font=get_font(18, True), fill="#F0F6FC")
draw.text((55, 635), "Projeto de Software — Experiência Prática III  |  Aluno: Yury  |  ODS 15 — Vida Terrestre (Meta 15.5)", font=get_font(13), fill="#8B949E")
draw.text((55, 665), "Repositório público oficial de código-fonte contendo a implementação do MVP.", font=get_font(13), fill="#C9D1D9")

screenshot_desk = os.path.join(desktop, "Print_Repositorio_GitHub_ONG_Patas_Esperanca.png")
screenshot_brain = os.path.join(out_dir, "Print_Repositorio_GitHub_ONG_Patas_Esperanca.png")
img.save(screenshot_desk)
img.save(screenshot_brain)
print("Screenshot salvo no Desktop:", screenshot_desk)
