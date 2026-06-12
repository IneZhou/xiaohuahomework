#!/usr/bin/env python3
"""Generate ecology, vegetation, hydrobio and human-bio benchmark outputs."""

from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis_outputs"
CHARTS = OUT / "charts"
DATA = OUT / "data"
FONT = '\"Noto Sans CJK SC\", \"Microsoft YaHei\", \"PingFang SC\", Arial, sans-serif'

ECOLOGY_BENCHMARKS = [
    {"indicator": "native_riparian_species_ratio", "baseline": "existing species unknown; reference palette only", "score_1": "few or no native riparian plants", "score_3": "some native species but fragmented", "score_5": "native trees, shrubs, herbs form stable structure", "data_source": "site plant survey + Roma / Lazio open data", "drawing_output": "planting strategy map", "current_confidence": "E"},
    {"indicator": "flood_recovery_capacity", "baseline": "seasonal flood response is conceptual", "score_1": "plants and facilities fail after flood", "score_3": "partial recovery with cleanup", "score_5": "washable, replaceable, regrowth-friendly edge", "data_source": "Regione Lazio hydrometric data + flood marks", "drawing_output": "flood recovery section", "current_confidence": "D/E"},
    {"indicator": "habitat_structural_complexity", "baseline": "hard river edge dominates", "score_1": "single hard edge", "score_3": "local rough edge and vegetation patches", "score_5": "tree, shrub, herb, wet edge and rough microhabitats", "data_source": "site sections + remote imagery", "drawing_output": "habitat section", "current_confidence": "D"},
    {"indicator": "disturbance_control", "baseline": "human use not measured by time period", "score_1": "people, dogs and light unmanaged", "score_3": "some path separation", "score_5": "clear low-disturbance edge and observation nodes", "data_source": "manual observation + night survey", "drawing_output": "human-bio interaction map", "current_confidence": "E"},
    {"indicator": "aquatic_edge_quality", "baseline": "vertical flood wall limits natural edge", "score_1": "no usable ecological edge", "score_3": "local resting or roughness elements", "score_5": "flood-compatible microhabitat stepping stones", "data_source": "section survey + authority constraints", "drawing_output": "aquatic edge detail", "current_confidence": "D/E"},
    {"indicator": "maintenance_ecology_balance", "baseline": "maintenance rules unknown", "score_1": "maintenance removes all succession", "score_3": "zoning exists but unclear", "score_5": "high/medium/low maintenance zones and cleanup routes", "data_source": "management interview + site records", "drawing_output": "maintenance zoning map", "current_confidence": "E"},
    {"indicator": "invasive_species_risk", "baseline": "invasive species not surveyed", "score_1": "high-risk species expanding", "score_3": "monitoring without action", "score_5": "avoidance, removal and monitoring strategy", "data_source": "plant survey + risk species checklist", "drawing_output": "ecological risk map", "current_confidence": "E"},
    {"indicator": "canopy_and_shade_gain", "baseline": "heat exposure scored qualitatively", "score_1": "no shade gain", "score_3": "local shade improvement", "score_5": "S3/S5 heat nodes measurably improved", "data_source": "tree survey + remote shade analysis", "drawing_output": "heat and canopy map", "current_confidence": "D/E"},
]

FLOOD_REGENERATION = [
    {"impact": "short inundation", "vegetation_response": "wet herbs and willow/poplar groups recover", "design_strategy": "use flood-tolerant, replaceable planting modules", "segment": "lower bank, S5 edge", "resilience": 4},
    {"impact": "sediment deposition", "vegetation_response": "plant bases may be buried", "design_strategy": "keep cleanup route and avoid dense blockage", "segment": "all lower bank", "resilience": 3},
    {"impact": "floating debris impact", "vegetation_response": "fine planting and fixtures are damaged", "design_strategy": "avoid high-maintenance flowerbeds below flood line", "segment": "S2/S5 low edge", "resilience": 3},
    {"impact": "root-heritage conflict", "vegetation_response": "deep roots can threaten remains", "design_strategy": "use shallow, containerized or offset planting", "segment": "S2", "resilience": 2},
    {"impact": "summer drought", "vegetation_response": "upper road plants need heat tolerance", "design_strategy": "combine Mediterranean drought-tolerant trees and shrubs", "segment": "S1/S3/S5 upper", "resilience": 4},
]

HUMAN_BIO = [
    {"interaction": "walking and bird watching", "positive_value": "river ecology becomes visible", "risk": "disturbance near resting birds", "design_control": "distant observation point and low-disturbance edge", "priority": 4},
    {"interaction": "children nature learning", "positive_value": "connect heritage and ecology", "risk": "entry into unsafe low bank or ruins", "design_control": "rail, ground marks and clear path hierarchy", "priority": 3},
    {"interaction": "dog walking", "positive_value": "real daily use", "risk": "trampling, fecal pollution, bird disturbance", "design_control": "separate accessible path from core habitat strip", "priority": 5},
    {"interaction": "night use", "positive_value": "safety and extended use", "risk": "light spill affects insects and birds", "design_control": "low-level downward lighting away from habitat edge", "priority": 4},
    {"interaction": "tourism and photography", "positive_value": "supports heritage legibility", "risk": "crowding and trampling", "design_control": "durable viewing platform and reinforced path", "priority": 3},
    {"interaction": "maintenance", "positive_value": "keeps flood edge safe", "risk": "over-cleaning removes habitat", "design_control": "maintenance zoning and minimum disturbance rule", "priority": 5},
]

SEGMENT_ECOLOGY = [
    {"segment": "S1", "goal": "entry shade and low-disturbance orientation", "planting": "drought-tolerant canopy + low shrubs", "hydrobio_role": "gateway interpretation", "priority": 3},
    {"segment": "S2", "goal": "heritage-first ecological interpretation", "planting": "shallow herbs / reversible containers", "hydrobio_role": "no deep-root or heavy wetland insertion", "priority": 5},
    {"segment": "S3", "goal": "rain garden and heat mitigation", "planting": "canopy + Carex/Juncus wet-dry edge", "hydrobio_role": "stormwater filtration before river edge", "priority": 5},
    {"segment": "S4", "goal": "warehouse heritage with insect-friendly planting", "planting": "low shrubs + flowering drought herbs", "hydrobio_role": "micro stepping-stone habitat", "priority": 3},
    {"segment": "S5", "goal": "bridge cooling and flood recovery", "planting": "upper shade trees + lower robust herbs", "hydrobio_role": "floodable edge and bird resting potential", "priority": 5},
]

VEGETATION_PALETTE = [
    {"group": "riparian trees", "reference_species": "Salix alba; Populus alba; Populus nigra; Alnus glutinosa", "function": "bank shade, bird perch, leaf-litter food chain", "testaccio_use": "only where roots and heritage risk are controlled", "confidence": "B/E"},
    {"group": "wetland emergents", "reference_species": "Phragmites australis; Typha latifolia; Iris pseudacorus", "function": "filtering, cover, flood-regrowth capacity", "testaccio_use": "low edge or containerized wet belt; do not block maintenance", "confidence": "B/E"},
    {"group": "wet meadow edge", "reference_species": "Carex spp.; Juncus spp.; Equisetum spp.", "function": "low maintenance texture and small habitat", "testaccio_use": "S3/S5 rain garden and upper edge", "confidence": "B/E"},
    {"group": "aquatics", "reference_species": "Potamogeton spp.; Lemna spp.", "function": "aquatic refuge and nutrient uptake", "testaccio_use": "reference only; do not introduce into main Tiber", "confidence": "B/E"},
    {"group": "Mediterranean dry edge", "reference_species": "Quercus ilex; Phillyrea spp.; Viburnum tinus; Pistacia lentiscus", "function": "heat tolerance, shade, bird food", "testaccio_use": "S1/S3/S5 upper exposed zones", "confidence": "B/E"},
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def wrap(text: object, max_chars: int) -> list[str]:
    words = str(text).replace("/", " / ").replace(";", "; ").split()
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
    return lines[:5]


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
<rect width=\"100%\" height=\"100%\" fill=\"#fbfaf7\"/>
<style>
text {{ font-family: {FONT}; fill: #263238; }}
.title {{ font-size: 24px; font-weight: 700; }}
.subtitle {{ font-size: 12px; fill: #607d72; }}
.header {{ font-size: 12px; font-weight: 700; fill: #ffffff; }}
.cell {{ font-size: 11px; }}
.small {{ font-size: 10px; fill: #607d72; }}
.score {{ font-size: 13px; font-weight: 700; fill: #ffffff; }}
</style>
{body}
</svg>
"""


def score_color(value: int) -> str:
    return {1: "#d7e9d2", 2: "#b7d3bc", 3: "#e4c979", 4: "#ca8751", 5: "#9f4d4a"}[int(value)]


def confidence_color(value: str) -> str:
    if "E" in value:
        return "#9f4d4a"
    if "D" in value:
        return "#ca8751"
    if "C" in value:
        return "#e4c979"
    if "B" in value:
        return "#7aa386"
    return "#4f6f64"


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = DATA / name
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def ecology_benchmark_chart() -> None:
    write_csv("ecology_benchmark_matrix.csv", ECOLOGY_BENCHMARKS)
    width, height = 1560, 830
    x0, y0 = 50, 125
    col_w = [260, 275, 250, 250, 260, 135]
    headers = ["indicator", "baseline", "score 3 threshold", "score 5 threshold", "drawing output", "confidence"]
    body = '<text x="50" y="48" class="title">Ecological Protection Benchmark Matrix</text>'
    body += '<text x="50" y="72" class="subtitle">D/E-level project benchmark; replace with field and official monitoring data when available.</text>'
    x = x0
    for i, header in enumerate(headers):
        body += f'<rect x="{x}" y="{y0}" width="{col_w[i]}" height="42" fill="#4f6f64"/>'
        body += f'<text x="{x + 12}" y="{y0 + 27}" class="header">{esc(header)}</text>'
        x += col_w[i]
    row_h = 76
    for r, row in enumerate(ECOLOGY_BENCHMARKS):
        y = y0 + 42 + r * row_h
        fill = "#edf3ec" if r % 2 == 0 else "#f7f4ed"
        values = [row["indicator"], row["baseline"], row["score_3"], row["score_5"], row["drawing_output"], row["current_confidence"]]
        x = x0
        for c, value in enumerate(values):
            body += f'<rect x="{x}" y="{y}" width="{col_w[c]}" height="{row_h}" fill="{fill}" stroke="#d7ded7"/>'
            if c == 5:
                body += f'<circle cx="{x + 42}" cy="{y + 34}" r="18" fill="{confidence_color(str(value))}"/>'
                body += f'<text x="{x + 42}" y="{y + 39}" text-anchor="middle" class="score">{esc(value)}</text>'
            else:
                for line_no, line in enumerate(wrap(value, max(12, int(col_w[c] / 11)))):
                    body += f'<text x="{x + 10}" y="{y + 22 + line_no * 14}" class="cell">{esc(line)}</text>'
            x += col_w[c]
    (CHARTS / "10_ecology_benchmark_matrix.svg").write_text(svg(width, height, body), encoding="utf-8")


def flood_regeneration_chart() -> None:
    write_csv("flood_regeneration_strategy.csv", FLOOD_REGENERATION)
    width, height = 1320, 560
    x0, y0 = 70, 125
    body = '<text x="70" y="48" class="title">Flood and Vegetation Regeneration Strategy</text>'
    body += '<text x="70" y="72" class="subtitle">Design logic for floodable lower-bank planting and post-flood recovery.</text>'
    col_w = [210, 275, 385, 190, 105]
    headers = ["flood impact", "vegetation response", "design strategy", "segment", "resilience"]
    x = x0
    for i, header in enumerate(headers):
        body += f'<rect x="{x}" y="{y0}" width="{col_w[i]}" height="40" fill="#4f6f64"/>'
        body += f'<text x="{x + 10}" y="{y0 + 26}" class="header">{esc(header)}</text>'
        x += col_w[i]
    row_h = 72
    for r, row in enumerate(FLOOD_REGENERATION):
        y = y0 + 40 + r * row_h
        fill = "#eef2ed" if r % 2 == 0 else "#f7f4ed"
        values = [row["impact"], row["vegetation_response"], row["design_strategy"], row["segment"]]
        x = x0
        for c, value in enumerate(values):
            body += f'<rect x="{x}" y="{y}" width="{col_w[c]}" height="{row_h}" fill="{fill}" stroke="#d7ded7"/>'
            for line_no, line in enumerate(wrap(value, max(12, int(col_w[c] / 11)))):
                body += f'<text x="{x + 10}" y="{y + 23 + line_no * 14}" class="cell">{esc(line)}</text>'
            x += col_w[c]
        val = int(row["resilience"])
        body += f'<rect x="{x}" y="{y + 13}" width="54" height="42" rx="5" fill="{score_color(val)}"/>'
        body += f'<text x="{x + 27}" y="{y + 40}" text-anchor="middle" class="score">{val}</text>'
    (CHARTS / "11_flood_regeneration_strategy.svg").write_text(svg(width, height, body), encoding="utf-8")


def human_bio_chart() -> None:
    write_csv("human_bio_interaction_matrix.csv", HUMAN_BIO)
    width, height = 1340, 620
    x0, y0 = 70, 125
    body = '<text x="70" y="48" class="title">Human-Bio Interaction Matrix</text>'
    body += '<text x="70" y="72" class="subtitle">Use patterns, ecological risk, and spatial controls for a public urban river edge.</text>'
    col_w = [215, 235, 285, 380, 100]
    headers = ["interaction", "positive value", "ecological risk", "design control", "priority"]
    x = x0
    for i, header in enumerate(headers):
        body += f'<rect x="{x}" y="{y0}" width="{col_w[i]}" height="40" fill="#4f6f64"/>'
        body += f'<text x="{x + 10}" y="{y0 + 26}" class="header">{esc(header)}</text>'
        x += col_w[i]
    row_h = 70
    for r, row in enumerate(HUMAN_BIO):
        y = y0 + 40 + r * row_h
        fill = "#eef2ed" if r % 2 == 0 else "#f7f4ed"
        values = [row["interaction"], row["positive_value"], row["risk"], row["design_control"]]
        x = x0
        for c, value in enumerate(values):
            body += f'<rect x="{x}" y="{y}" width="{col_w[c]}" height="{row_h}" fill="{fill}" stroke="#d7ded7"/>'
            for line_no, line in enumerate(wrap(value, max(12, int(col_w[c] / 11)))):
                body += f'<text x="{x + 10}" y="{y + 23 + line_no * 14}" class="cell">{esc(line)}</text>'
            x += col_w[c]
        val = int(row["priority"])
        body += f'<circle cx="{x + 35}" cy="{y + 34}" r="20" fill="{score_color(val)}"/>'
        body += f'<text x="{x + 35}" y="{y + 39}" text-anchor="middle" class="score">{val}</text>'
    (CHARTS / "12_human_bio_interaction_matrix.svg").write_text(svg(width, height, body), encoding="utf-8")


def segment_ecology_chart() -> None:
    write_csv("segment_ecology_goals.csv", SEGMENT_ECOLOGY)
    write_csv("local_reference_vegetation_palette.csv", VEGETATION_PALETTE)
    width, height = 1230, 600
    x0, y0 = 70, 125
    body = '<text x="70" y="48" class="title">S1-S5 Ecology Goals</text>'
    body += '<text x="70" y="72" class="subtitle">Segment-specific ecology tasks linked to planting and hydro-biological interpretation.</text>'
    col_w = [80, 270, 285, 360, 90]
    headers = ["seg", "ecological goal", "planting structure", "hydrobio role", "priority"]
    x = x0
    for i, header in enumerate(headers):
        body += f'<rect x="{x}" y="{y0}" width="{col_w[i]}" height="40" fill="#4f6f64"/>'
        body += f'<text x="{x + 10}" y="{y0 + 26}" class="header">{esc(header)}</text>'
        x += col_w[i]
    row_h = 75
    for r, row in enumerate(SEGMENT_ECOLOGY):
        y = y0 + 40 + r * row_h
        fill = "#eef2ed" if r % 2 == 0 else "#f7f4ed"
        values = [row["segment"], row["goal"], row["planting"], row["hydrobio_role"]]
        x = x0
        for c, value in enumerate(values):
            body += f'<rect x="{x}" y="{y}" width="{col_w[c]}" height="{row_h}" fill="{fill}" stroke="#d7ded7"/>'
            for line_no, line in enumerate(wrap(value, max(8, int(col_w[c] / 11)))):
                body += f'<text x="{x + 10}" y="{y + 25 + line_no * 14}" class="cell">{esc(line)}</text>'
            x += col_w[c]
        val = int(row["priority"])
        body += f'<rect x="{x + 10}" y="{y + 16}" width="48" height="40" rx="5" fill="{score_color(val)}"/>'
        body += f'<text x="{x + 34}" y="{y + 42}" text-anchor="middle" class="score">{val}</text>'
    (CHARTS / "13_segment_ecology_goals.svg").write_text(svg(width, height, body), encoding="utf-8")


def update_readme() -> None:
    path = OUT / "README.md"
    text = path.read_text(encoding="utf-8") if path.exists() else "# Python 初步分析图表输出说明\n"
    section = """
## 生态、水文生物与人-生物互动图表

10. `charts/10_ecology_benchmark_matrix.svg`  
    生态保护评价基准矩阵，包含本地河岸植物比例、洪水恢复力、生境复杂度、干扰控制、水体边缘质量、维护平衡、入侵风险和树冠遮阴等指标。

11. `charts/11_flood_regeneration_strategy.svg`  
    洪水影响与植被再生策略图，用于表达低位河岸“可淹没、可冲刷、可恢复”的植物和材料逻辑。

12. `charts/12_human_bio_interaction_matrix.svg`  
    人类活动与生物干扰控制矩阵，覆盖观鸟、儿童自然教育、遛狗、夜间使用、摄影停留和维护。

13. `charts/13_segment_ecology_goals.svg`  
    S1-S5 分段生态目标图，将种植结构、水文生物解释和优先级对应到空间段落。
"""
    if "## 生态、水文生物与人-生物互动图表" not in text:
        text = text.rstrip() + "\n" + section
    path.write_text(text, encoding="utf-8")


def main() -> None:
    CHARTS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    ecology_benchmark_chart()
    flood_regeneration_chart()
    human_bio_chart()
    segment_ecology_chart()
    update_readme()
    print(f"Generated ecology benchmark outputs in {CHARTS}")


if __name__ == "__main__":
    main()
