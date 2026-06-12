#!/usr/bin/env python3
"""Generate matrix-style SVG/CSV outputs for report-to-board translation."""

from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis_outputs"
CHARTS = OUT / "charts"
DATA = OUT / "data"
FONT = '\"Noto Sans CJK SC\", \"Microsoft YaHei\", \"PingFang SC\", Arial, sans-serif'

DIAGNOSIS_ROWS = [
    {"issue": "heritage sensitivity", "evidence": "Emporium / Porticus Aemilia remains", "segment": "S2, S4", "response": "reversible interpretation; no deep foundation", "drawing": "heritage readability map + section"},
    {"issue": "flood-control constraint", "evidence": "muraglioni + lower-bank seasonality", "segment": "all; especially S2/S5", "response": "floodable, washable, removable elements", "drawing": "flood constraint section"},
    {"issue": "accessibility barrier", "evidence": "high barrier score in S2/S5", "segment": "S1, S3, S5", "response": "gateway, signage, safer crossing, stair upgrade", "drawing": "accessibility map"},
    {"issue": "heat exposure", "evidence": "S3/S5 score 4.4/5", "segment": "S3, S5", "response": "shade, permeable paving, low-maintenance planting", "drawing": "heat exposure map"},
    {"issue": "maintenance complexity", "evidence": "lower bank + heritage interface", "segment": "S2, S5", "response": "simple materials, controlled vegetation, maintenance routes", "drawing": "material-maintenance matrix"},
]

MATERIAL_ROWS = [
    {"material": "permeable paving", "reversibility": 3, "flood_resistance": 3, "maintenance": 3, "heritage": 2, "thermal": 4, "segment": "S3/S5"},
    {"material": "open-graded gravel base", "reversibility": 4, "flood_resistance": 3, "maintenance": 3, "heritage": 3, "thermal": 3, "segment": "S3/S4 edge"},
    {"material": "metal grating / raised deck", "reversibility": 5, "flood_resistance": 4, "maintenance": 3, "heritage": 4, "thermal": 2, "segment": "S2 edge / S4"},
    {"material": "floodable stone / concrete repair", "reversibility": 2, "flood_resistance": 5, "maintenance": 4, "heritage": 4, "thermal": 2, "segment": "lower bank"},
    {"material": "bioretention soil + rain garden", "reversibility": 3, "flood_resistance": 2, "maintenance": 3, "heritage": 2, "thermal": 5, "segment": "S3/S5 upper"},
]

DATA_GAPS = [
    {"gap": "Tiber water-level / rainfall records", "level": "E/D", "source": "Regione Lazio hydrometric records", "priority": 5},
    {"gap": "PAI / PGRA flood-risk boundaries", "level": "A pending", "source": "Autorita di Bacino / official GIS", "priority": 5},
    {"gap": "Emporium official heritage boundary", "level": "B pending", "source": "SITAR / Sovrintendenza", "priority": 5},
    {"gap": "S1-S5 access, stairs, ramps, fences", "level": "C/D pending", "source": "site survey + photos", "priority": 5},
    {"gap": "surface, railing, wall condition", "level": "C/D pending", "source": "site material record", "priority": 4},
    {"gap": "tree species, canopy, shade time", "level": "C/D pending", "source": "site observation + remote sensing", "priority": 4},
    {"gap": "people flow and staying points", "level": "E", "source": "manual time-period observation", "priority": 3},
    {"gap": "ownership and management body", "level": "A pending", "source": "Roma Capitale / river / heritage bodies", "priority": 5},
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def wrap(text: str, max_chars: int) -> list[str]:
    words = str(text).replace("/", " / ").split()
    lines: list[str] = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = f"{current} {word}".strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:4]


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
<rect width=\"100%\" height=\"100%\" fill=\"#fbfaf7\"/>
<style>
text {{ font-family: {FONT}; fill: #263238; }}
.title {{ font-size: 24px; font-weight: 700; }}
.subtitle {{ font-size: 12px; fill: #607d72; }}
.header {{ font-size: 12px; font-weight: 700; fill: #fff; }}
.cell {{ font-size: 11px; }}
.small {{ font-size: 10px; fill: #607d72; }}
</style>
{body}
</svg>
"""


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = DATA / name
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def matrix_table() -> None:
    write_csv("diagnosis_strategy_matrix.csv", DIAGNOSIS_ROWS)
    width, height = 1500, 620
    x0, y0 = 50, 125
    col_w = [230, 315, 180, 390, 275]
    headers = ["issue", "evidence", "spatial segment", "design response", "drawing output"]
    body = '<text x="50" y="48" class="title">Diagnosis to Strategy Matrix</text>'
    body += '<text x="50" y="72" class="subtitle">Board-ready matrix: issue -> evidence -> segment -> response -> drawing output</text>'
    x = x0
    for i, h in enumerate(headers):
        body += f'<rect x="{x}" y="{y0}" width="{col_w[i]}" height="42" fill="#4f6f64"/>'
        body += f'<text x="{x + 12}" y="{y0 + 27}" class="header">{esc(h)}</text>'
        x += col_w[i]
    row_h = 82
    for r, row in enumerate(DIAGNOSIS_ROWS):
        y = y0 + 42 + r * row_h
        x = x0
        fill = "#eef2ed" if r % 2 == 0 else "#f7f4ed"
        values = [row["issue"], row["evidence"], row["segment"], row["response"], row["drawing"]]
        for c, value in enumerate(values):
            body += f'<rect x="{x}" y="{y}" width="{col_w[c]}" height="{row_h}" fill="{fill}" stroke="#d7ded7"/>'
            for line_no, line in enumerate(wrap(value, max(12, int(col_w[c] / 11)))):
                body += f'<text x="{x + 12}" y="{y + 24 + line_no * 15}" class="cell">{esc(line)}</text>'
            x += col_w[c]
    (CHARTS / "07_diagnosis_strategy_matrix.svg").write_text(svg(width, height, body), encoding="utf-8")


def score_color(value: int) -> str:
    colors = {1: "#e5efe3", 2: "#c9dfc4", 3: "#f0d28c", 4: "#d99a55", 5: "#b95850"}
    return colors[int(value)]


def material_matrix() -> None:
    write_csv("material_suitability_matrix.csv", MATERIAL_ROWS)
    width, height = 1250, 650
    x0, y0 = 70, 135
    body = '<text x="70" y="48" class="title">Material Suitability Matrix</text>'
    body += '<text x="70" y="72" class="subtitle">Qualitative 1-5 scoring; D-level evidence. Higher score means stronger suitability in that dimension.</text>'
    dims = ["reversibility", "flood_resistance", "maintenance", "heritage", "thermal"]
    cell = 74
    body += '<text x="70" y="118" class="small">material / system</text>'
    for i, d in enumerate(dims):
        x = 355 + i * cell
        for line_no, line in enumerate(wrap(d, 10)):
            body += f'<text x="{x + cell/2}" y="{112 + line_no*12}" text-anchor="middle" class="small">{esc(line)}</text>'
    body += '<text x="780" y="118" class="small">suitable segment</text>'
    for r, row in enumerate(MATERIAL_ROWS):
        y = y0 + r * 86
        body += f'<text x="70" y="{y + 39}" class="cell">{esc(row["material"])}</text>'
        for i, d in enumerate(dims):
            x = 355 + i * cell
            val = int(row[d])
            body += f'<rect x="{x}" y="{y}" width="54" height="54" rx="5" fill="{score_color(val)}"/>'
            body += f'<text x="{x + 27}" y="{y + 34}" text-anchor="middle" class="header">{val}</text>'
        body += f'<text x="780" y="{y + 34}" class="cell">{esc(row["segment"])}</text>'
    body += '<text x="70" y="600" class="small">Note: maintenance score here means low and predictable maintenance demand, not no-maintenance.</text>'
    (CHARTS / "08_material_suitability_matrix.svg").write_text(svg(width, height, body), encoding="utf-8")


def data_gap_chart() -> None:
    write_csv("data_gap_priority.csv", DATA_GAPS)
    width, height = 1250, 680
    x0, y0 = 80, 135
    body = '<text x="80" y="48" class="title">Data Gaps and Verification Priority</text>'
    body += '<text x="80" y="72" class="subtitle">Items that require official data, site survey, or human judgement before being treated as confirmed.</text>'
    max_w = 620
    bar_h = 34
    for i, row in enumerate(DATA_GAPS):
        y = y0 + i * 62
        priority = int(row["priority"])
        body += f'<text x="80" y="{y + 23}" class="cell">{esc(row["gap"])}</text>'
        body += f'<rect x="520" y="{y}" width="{priority / 5 * max_w}" height="{bar_h}" fill="{score_color(priority)}" rx="5"/>'
        body += f'<text x="{530 + priority / 5 * max_w}" y="{y + 23}" class="cell">P{priority}</text>'
        body += f'<text x="80" y="{y + 45}" class="small">{esc(row["level"])} | {esc(row["source"])}</text>'
    (CHARTS / "09_data_gap_priority.svg").write_text(svg(width, height, body), encoding="utf-8")


def update_readme() -> None:
    path = OUT / "README.md"
    text = path.read_text(encoding="utf-8") if path.exists() else "# Python 初步分析图表输出说明\n"
    section = """
## 追加矩阵图表

7. `charts/07_diagnosis_strategy_matrix.svg`  
   诊断-策略矩阵，将 issue、evidence、segment、response 和 drawing output 对齐。

8. `charts/08_material_suitability_matrix.svg`  
   材料适宜性矩阵，按可逆性、耐洪水、维护、遗产兼容和热舒适评分。

9. `charts/09_data_gap_priority.svg`  
   数据缺口优先级图，标出必须通过官方资料、现场或人工判断补齐的内容。
"""
    if "## 追加矩阵图表" not in text:
        text = text.rstrip() + "\n" + section
    path.write_text(text, encoding="utf-8")


def main() -> None:
    CHARTS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    matrix_table()
    material_matrix()
    data_gap_chart()
    update_readme()
    print(f"Generated additional matrices in {CHARTS}")


if __name__ == "__main__":
    main()
