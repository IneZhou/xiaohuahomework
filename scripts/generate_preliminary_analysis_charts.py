#!/usr/bin/env python3
"""
Generate preliminary landscape analysis charts for the Lungotevere Testaccio /
Emporium project.

The script intentionally uses only the Python standard library. The underlying
scores are qualitative 1-5 planning judgments derived from the local project
documents, not field measurements or engineering/GIS outputs.
"""

from __future__ import annotations

import csv
import html
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis_outputs"
CHARTS = OUT / "charts"
DATA = OUT / "data"

FONT = '"Noto Sans CJK SC", "Microsoft YaHei", "PingFang SC", Arial, sans-serif'


SEGMENTS = [
    {
        "id": "S1",
        "distance_start_m": 0,
        "distance_end_m": 100,
        "name": "Piazza dell'Emporio / Ponte Sublicio",
        "physical_barrier": 4,
        "traffic_barrier": 4,
        "visual_barrier": 3,
        "perceived_safety": 3,
        "heritage_sensitivity": 3,
        "flood_safety_constraint": 4,
        "accessibility_need": 5,
        "maintenance_complexity": 3,
        "impervious_surface": 4,
        "lack_of_shade": 3,
        "low_vegetation": 3,
    },
    {
        "id": "S2",
        "distance_start_m": 100,
        "distance_end_m": 200,
        "name": "Emporium 可见遗迹 / Lungotevere 11",
        "physical_barrier": 5,
        "traffic_barrier": 4,
        "visual_barrier": 4,
        "perceived_safety": 4,
        "heritage_sensitivity": 5,
        "flood_safety_constraint": 5,
        "accessibility_need": 4,
        "maintenance_complexity": 4,
        "impervious_surface": 4,
        "lack_of_shade": 4,
        "low_vegetation": 3,
    },
    {
        "id": "S3",
        "distance_start_m": 200,
        "distance_end_m": 300,
        "name": "Via Franklin 横向联系",
        "physical_barrier": 4,
        "traffic_barrier": 3,
        "visual_barrier": 4,
        "perceived_safety": 3,
        "heritage_sensitivity": 3,
        "flood_safety_constraint": 4,
        "accessibility_need": 5,
        "maintenance_complexity": 3,
        "impervious_surface": 5,
        "lack_of_shade": 4,
        "low_vegetation": 4,
    },
    {
        "id": "S4",
        "distance_start_m": 300,
        "distance_end_m": 400,
        "name": "Via Rubattino / Via Branca 遗迹联系",
        "physical_barrier": 3,
        "traffic_barrier": 3,
        "visual_barrier": 3,
        "perceived_safety": 3,
        "heritage_sensitivity": 4,
        "flood_safety_constraint": 3,
        "accessibility_need": 4,
        "maintenance_complexity": 3,
        "impervious_surface": 4,
        "lack_of_shade": 3,
        "low_vegetation": 3,
    },
    {
        "id": "S5",
        "distance_start_m": 400,
        "distance_end_m": 500,
        "name": "Ponte Testaccio / Largo G. B. Marzi",
        "physical_barrier": 4,
        "traffic_barrier": 5,
        "visual_barrier": 3,
        "perceived_safety": 4,
        "heritage_sensitivity": 3,
        "flood_safety_constraint": 4,
        "accessibility_need": 5,
        "maintenance_complexity": 4,
        "impervious_surface": 5,
        "lack_of_shade": 4,
        "low_vegetation": 4,
    },
]

HERITAGE_NODES = [
    {
        "name": "Piazza dell'Emporio",
        "visibility": 3,
        "accessibility": 4,
        "interpretation_potential": 4,
        "damage_risk": 2,
    },
    {
        "name": "Emporium 遗址点",
        "visibility": 4,
        "accessibility": 2,
        "interpretation_potential": 5,
        "damage_risk": 4,
    },
    {
        "name": "Via Franklin 联系线",
        "visibility": 2,
        "accessibility": 3,
        "interpretation_potential": 4,
        "damage_risk": 2,
    },
    {
        "name": "Via Rubattino / Branca",
        "visibility": 4,
        "accessibility": 3,
        "interpretation_potential": 5,
        "damage_risk": 3,
    },
    {
        "name": "Ponte Testaccio 桥头",
        "visibility": 2,
        "accessibility": 4,
        "interpretation_potential": 3,
        "damage_risk": 2,
    },
]

SEASONAL = [
    ("Jan", 4, 45),
    ("Feb", 4, 50),
    ("Mar", 3, 65),
    ("Apr", 2, 80),
    ("May", 2, 85),
    ("Jun", 1, 90),
    ("Jul", 1, 92),
    ("Aug", 1, 90),
    ("Sep", 2, 82),
    ("Oct", 3, 70),
    ("Nov", 4, 55),
    ("Dec", 4, 45),
]

PRIORITY_NODES = [
    {
        "name": "北端入口强化",
        "impact": 4.5,
        "difficulty": 3.0,
        "heritage_value": 4,
        "accessibility_gain": 5,
        "microclimate_benefit": 3,
        "ecological_benefit": 2,
        "maintenance_feasibility": 4,
    },
    {
        "name": "Emporium 解说平台",
        "impact": 5.0,
        "difficulty": 4.5,
        "heritage_value": 5,
        "accessibility_gain": 3,
        "microclimate_benefit": 2,
        "ecological_benefit": 1,
        "maintenance_feasibility": 2,
    },
    {
        "name": "Via Franklin 导视",
        "impact": 3.8,
        "difficulty": 2.0,
        "heritage_value": 3,
        "accessibility_gain": 5,
        "microclimate_benefit": 2,
        "ecological_benefit": 1,
        "maintenance_feasibility": 5,
    },
    {
        "name": "道路侧遮阴座椅",
        "impact": 4.0,
        "difficulty": 2.0,
        "heritage_value": 2,
        "accessibility_gain": 4,
        "microclimate_benefit": 5,
        "ecological_benefit": 3,
        "maintenance_feasibility": 4,
    },
    {
        "name": "下层可淹没平台",
        "impact": 4.6,
        "difficulty": 4.8,
        "heritage_value": 3,
        "accessibility_gain": 4,
        "microclimate_benefit": 3,
        "ecological_benefit": 4,
        "maintenance_feasibility": 2,
    },
    {
        "name": "墙体轻量标识",
        "impact": 3.2,
        "difficulty": 1.5,
        "heritage_value": 4,
        "accessibility_gain": 2,
        "microclimate_benefit": 1,
        "ecological_benefit": 1,
        "maintenance_feasibility": 5,
    },
    {
        "name": "南端桥头节点",
        "impact": 4.4,
        "difficulty": 3.5,
        "heritage_value": 2,
        "accessibility_gain": 5,
        "microclimate_benefit": 4,
        "ecological_benefit": 3,
        "maintenance_feasibility": 3,
    },
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def ensure_dirs() -> None:
    CHARTS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def svg_root(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="#fbfaf7"/>
<style>
text {{ font-family: {FONT}; fill: #263238; }}
.title {{ font-size: 24px; font-weight: 700; }}
.subtitle {{ font-size: 13px; fill: #607d72; }}
.axis {{ stroke: #607d72; stroke-width: 1; }}
.grid {{ stroke: #d8ded8; stroke-width: 1; stroke-dasharray: 3 4; }}
.label {{ font-size: 12px; }}
.small {{ font-size: 10px; fill: #607d72; }}
.note {{ font-size: 11px; fill: #789087; }}
</style>
{body}
</svg>
"""


def color_scale(value: float, min_value: float, max_value: float) -> str:
    if max_value == min_value:
        t = 0
    else:
        t = max(0, min(1, (value - min_value) / (max_value - min_value)))
    start = (220, 237, 220)
    mid = (242, 199, 122)
    end = (178, 84, 74)
    if t < 0.5:
        tt = t * 2
        rgb = tuple(round(start[i] + (mid[i] - start[i]) * tt) for i in range(3))
    else:
        tt = (t - 0.5) * 2
        rgb = tuple(round(mid[i] + (end[i] - mid[i]) * tt) for i in range(3))
    return f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"


def add_title(title: str, subtitle: str) -> str:
    return f"""
<text x="48" y="48" class="title">{esc(title)}</text>
<text x="48" y="72" class="subtitle">{esc(subtitle)}</text>
"""


def chart_barrier_heatmap() -> None:
    rows = []
    for s in SEGMENTS:
        barrier = (
            s["physical_barrier"]
            + s["traffic_barrier"]
            + s["visual_barrier"]
            + s["perceived_safety"]
        )
        row = dict(s)
        row["barrier_index"] = barrier
        rows.append(row)
    write_csv(DATA / "segment_barrier_scores.csv", rows)

    width, height = 1200, 520
    x0, y0 = 90, 155
    seg_w, seg_h = 190, 90
    gap = 8
    max_score = 20
    body = add_title(
        "阻隔强度热力图 Barrier Index",
        "1-5 定性评分；总分 = physical + traffic + visual + perceived safety。Preliminary observation.",
    )
    body += f'<line x1="{x0}" y1="{y0 + seg_h + 60}" x2="{x0 + 5 * (seg_w + gap) - gap}" y2="{y0 + seg_h + 60}" class="axis"/>'
    for s in rows:
        i = SEGMENTS.index(next(seg for seg in SEGMENTS if seg["id"] == s["id"]))
        x = x0 + i * (seg_w + gap)
        score = s["barrier_index"]
        fill = color_scale(score, 10, max_score)
        body += f'<rect x="{x}" y="{y0}" width="{seg_w}" height="{seg_h}" fill="{fill}" rx="5"/>'
        body += f'<text x="{x + 14}" y="{y0 + 34}" class="label" font-weight="700">{esc(s["id"])}  {score}/20</text>'
        body += f'<text x="{x + 14}" y="{y0 + 57}" class="small">{esc(s["distance_start_m"])}-{esc(s["distance_end_m"])} m</text>'
        for j, part in enumerate(("physical_barrier", "traffic_barrier", "visual_barrier", "perceived_safety")):
            bar_x = x + 12 + j * 42
            bar_h = int(s[part] * 10)
            body += f'<rect x="{bar_x}" y="{y0 + 118 - bar_h}" width="28" height="{bar_h}" fill="#4f6f64" opacity="0.75"/>'
        wrapped = wrap_label(str(s["name"]), 18)
        for line_no, line in enumerate(wrapped):
            body += f'<text x="{x + seg_w / 2}" y="{y0 + seg_h + 88 + line_no * 15}" text-anchor="middle" class="small">{esc(line)}</text>'
    legend_y = 420
    for k in range(11):
        val = 10 + k
        body += f'<rect x="{90 + k * 26}" y="{legend_y}" width="26" height="18" fill="{color_scale(val, 10, 20)}"/>'
    body += f'<text x="90" y="{legend_y + 38}" class="small">低阻隔</text><text x="330" y="{legend_y + 38}" class="small">高阻隔</text>'
    body += '<text x="760" y="442" class="note">柱状小条从左到右：物理 / 交通 / 视觉 / 心理安全</text>'
    write_text(CHARTS / "01_barrier_index_heatmap.svg", svg_root(width, height, body))


def chart_intervention_classes() -> None:
    rows = []
    for s in SEGMENTS:
        sensitivity = (
            s["heritage_sensitivity"] * 0.30
            + s["flood_safety_constraint"] * 0.30
            + s["accessibility_need"] * 0.25
            + s["maintenance_complexity"] * 0.15
        )
        if sensitivity >= 4.4:
            klass = "A 不可触碰 / 严格保护"
        elif sensitivity >= 3.8:
            klass = "B 轻量附着 / 可逆介入"
        elif sensitivity >= 3.2:
            klass = "C 可使用界面优化"
        else:
            klass = "D 铺装植被优化"
        rows.append({**s, "intervention_sensitivity": round(sensitivity, 2), "recommended_class": klass})
    write_csv(DATA / "intervention_class_scores.csv", rows)

    width, height = 1180, 500
    x0, y0 = 80, 160
    line_w = 980
    body = add_title(
        "防洪墙与河岸可介入性分级",
        "综合遗产敏感、防洪安全、可达需求和维护复杂度；分级用于限制设计动作强度。",
    )
    class_colors = {
        "A": "#b95850",
        "B": "#d99a55",
        "C": "#7a9d78",
        "D": "#5c8a99",
    }
    for row in rows:
        x = x0 + row["distance_start_m"] / 500 * line_w
        w = (row["distance_end_m"] - row["distance_start_m"]) / 500 * line_w - 4
        klass_key = row["recommended_class"][0]
        body += f'<rect x="{x}" y="{y0}" width="{w}" height="85" fill="{class_colors[klass_key]}" rx="4"/>'
        body += f'<text x="{x + w / 2}" y="{y0 + 35}" text-anchor="middle" fill="#fff" font-size="19" font-family="{FONT}" font-weight="700">{klass_key}</text>'
        body += f'<text x="{x + w / 2}" y="{y0 + 60}" text-anchor="middle" fill="#fff" font-size="11" font-family="{FONT}">{row["intervention_sensitivity"]}</text>'
        body += f'<text x="{x + w / 2}" y="{y0 + 112}" text-anchor="middle" class="small">{esc(row["id"])}</text>'
        body += f'<text x="{x + w / 2}" y="{y0 + 130}" text-anchor="middle" class="small">{esc(row["distance_start_m"])}-{esc(row["distance_end_m"])}m</text>'
    legend = [
        ("A", "不可触碰：防洪主结构 / 遗迹敏感段"),
        ("B", "轻量附着：标识、灯光、可逆装置"),
        ("C", "可使用界面：台阶、栏杆、临时家具"),
        ("D", "铺装植被：下层河岸或边角空间"),
    ]
    for i, (key, text) in enumerate(legend):
        y = 330 + i * 32
        body += f'<rect x="90" y="{y - 15}" width="20" height="20" fill="{class_colors[key]}" rx="3"/>'
        body += f'<text x="124" y="{y}" class="label">{key}  {esc(text)}</text>'
    write_text(CHARTS / "02_intervention_classes.svg", svg_root(width, height, body))


def chart_environment_risk() -> None:
    rows = []
    for s in SEGMENTS:
        heat = (
            s["impervious_surface"] * 0.4
            + s["lack_of_shade"] * 0.4
            + s["low_vegetation"] * 0.2
        )
        rows.append({**s, "heat_exposure_score": round(heat, 2)})
    write_csv(DATA / "environment_heat_exposure_scores.csv", rows)

    width, height = 1180, 620
    x0, y0 = 110, 470
    chart_h = 310
    bar_w = 120
    body = add_title(
        "热暴露与硬化压力评分",
        "heat = impervious*0.4 + lack_of_shade*0.4 + low_vegetation*0.2；定性 1-5 分。",
    )
    for tick in range(0, 6):
        y = y0 - tick / 5 * chart_h
        body += f'<line x1="{x0 - 10}" y1="{y}" x2="1050" y2="{y}" class="grid"/>'
        body += f'<text x="{x0 - 24}" y="{y + 4}" text-anchor="end" class="small">{tick}</text>'
    body += f'<line x1="{x0}" y1="{y0}" x2="1050" y2="{y0}" class="axis"/>'
    colors = ["#c7785a", "#d8a85f", "#7ca982"]
    keys = ["impervious_surface", "lack_of_shade", "low_vegetation"]
    names = ["不透水面", "缺少遮阴", "低植被活性"]
    for i, row in enumerate(rows):
        base_x = x0 + i * 185
        for j, key in enumerate(keys):
            val = row[key]
            h = val / 5 * chart_h
            x = base_x + j * 38
            body += f'<rect x="{x}" y="{y0 - h}" width="30" height="{h}" fill="{colors[j]}" rx="3"/>'
            body += f'<text x="{x + 15}" y="{y0 - h - 8}" text-anchor="middle" class="small">{val}</text>'
        body += f'<text x="{base_x + 38}" y="{y0 + 28}" text-anchor="middle" class="label">{esc(row["id"])}</text>'
        body += f'<text x="{base_x + 38}" y="{y0 + 46}" text-anchor="middle" class="small">heat {row["heat_exposure_score"]}</text>'
    for j, name in enumerate(names):
        body += f'<rect x="{740 + j * 120}" y="95" width="18" height="18" fill="{colors[j]}" rx="3"/>'
        body += f'<text x="{764 + j * 120}" y="109" class="small">{esc(name)}</text>'
    body += '<text x="110" y="565" class="note">S1-S5 对应 0-500m 五个线性分段；分数为远程资料初判，需由遥感/现场复核。</text>'
    write_text(CHARTS / "03_environment_heat_exposure.svg", svg_root(width, height, body))


def chart_heritage_readability() -> None:
    rows = []
    for n in HERITAGE_NODES:
        score = (
            n["visibility"]
            + n["accessibility"]
            + n["interpretation_potential"]
            - n["damage_risk"]
        )
        rows.append({**n, "heritage_readability_score": score})
    write_csv(DATA / "heritage_readability_scores.csv", rows)

    width, height = 1180, 600
    x0, y0 = 120, 470
    chart_h = 310
    max_score = 15
    body = add_title(
        "遗产可读性评分",
        "readability = visibility + accessibility + interpretation potential - damage risk。",
    )
    for tick in range(0, 16, 3):
        y = y0 - tick / max_score * chart_h
        body += f'<line x1="{x0 - 10}" y1="{y}" x2="1050" y2="{y}" class="grid"/>'
        body += f'<text x="{x0 - 24}" y="{y + 4}" text-anchor="end" class="small">{tick}</text>'
    body += f'<line x1="{x0}" y1="{y0}" x2="1050" y2="{y0}" class="axis"/>'
    for i, row in enumerate(rows):
        x = x0 + i * 180
        h = row["heritage_readability_score"] / max_score * chart_h
        body += f'<rect x="{x}" y="{y0 - h}" width="80" height="{h}" fill="#6f8f7a" rx="5"/>'
        body += f'<text x="{x + 40}" y="{y0 - h - 10}" text-anchor="middle" class="label" font-weight="700">{row["heritage_readability_score"]}</text>'
        wrapped = wrap_label(str(row["name"]), 10)
        for line_no, line in enumerate(wrapped):
            body += f'<text x="{x + 40}" y="{y0 + 28 + line_no * 15}" text-anchor="middle" class="small">{esc(line)}</text>'
    body += '<text x="120" y="555" class="note">高分代表“更适合作为解释节点”，不代表可施工性更高；遗迹敏感段仍需可逆介入。</text>'
    write_text(CHARTS / "04_heritage_readability.svg", svg_root(width, height, body))


def chart_seasonal_availability() -> None:
    rows = [
        {
            "month": month,
            "relative_water_risk_1_low_5_high": risk,
            "qualitative_availability_percent": availability,
        }
        for month, risk, availability in SEASONAL
    ]
    write_csv(DATA / "seasonal_availability_assumptions.csv", rows)

    width, height = 1180, 600
    x0, y0 = 90, 470
    chart_w, chart_h = 980, 320
    body = add_title(
        "季节水位风险与可使用性关系",
        "无日水位序列时使用低/常/高水位季的定性曲线；后续可替换为 Lazio 水文数据。",
    )
    for tick in range(0, 101, 20):
        y = y0 - tick / 100 * chart_h
        body += f'<line x1="{x0}" y1="{y}" x2="{x0 + chart_w}" y2="{y}" class="grid"/>'
        body += f'<text x="{x0 - 16}" y="{y + 4}" text-anchor="end" class="small">{tick}%</text>'
    points = []
    risk_points = []
    for i, (month, risk, availability) in enumerate(SEASONAL):
        x = x0 + i / 11 * chart_w
        y = y0 - availability / 100 * chart_h
        ry = y0 - (risk / 5 * 100) / 100 * chart_h
        points.append((x, y))
        risk_points.append((x, ry))
        body += f'<text x="{x}" y="{y0 + 28}" text-anchor="middle" class="small">{month}</text>'
    body += polyline(points, "#5c8a99", 4)
    body += polyline(risk_points, "#b95850", 3)
    for x, y in points:
        body += f'<circle cx="{x}" cy="{y}" r="5" fill="#5c8a99"/>'
    for x, y in risk_points:
        body += f'<circle cx="{x}" cy="{y}" r="4" fill="#b95850"/>'
    body += '<rect x="760" y="105" width="18" height="4" fill="#5c8a99"/><text x="790" y="112" class="small">下层河岸可使用性</text>'
    body += '<rect x="760" y="132" width="18" height="4" fill="#b95850"/><text x="790" y="139" class="small">相对水位/洪水风险</text>'
    body += '<text x="90" y="555" class="note">该图用于空间分区判断：常年可用、季节性可用、可淹没、不可介入。</text>'
    write_text(CHARTS / "05_seasonal_availability.svg", svg_root(width, height, body))


def chart_priority_matrix() -> None:
    rows = []
    for n in PRIORITY_NODES:
        weighted = (
            n["heritage_value"] * 0.25
            + n["accessibility_gain"] * 0.25
            + n["microclimate_benefit"] * 0.20
            + n["ecological_benefit"] * 0.15
            + n["maintenance_feasibility"] * 0.15
        )
        simple = n["impact"] / n["difficulty"]
        rows.append({**n, "weighted_priority_score": round(weighted, 2), "impact_over_difficulty": round(simple, 2)})
    write_csv(DATA / "design_priority_scores.csv", rows)

    width, height = 1180, 720
    x0, y0 = 140, 580
    chart_w, chart_h = 820, 430
    body = add_title(
        "设计机会优先级矩阵",
        "横轴为实施难度，纵轴为设计价值；点大小为加权优先级。",
    )
    for tick in range(1, 6):
        x = x0 + (tick - 1) / 4 * chart_w
        y = y0 - (tick - 1) / 4 * chart_h
        body += f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 - chart_h}" class="grid"/>'
        body += f'<line x1="{x0}" y1="{y}" x2="{x0 + chart_w}" y2="{y}" class="grid"/>'
        body += f'<text x="{x}" y="{y0 + 25}" text-anchor="middle" class="small">{tick}</text>'
        body += f'<text x="{x0 - 20}" y="{y + 4}" text-anchor="end" class="small">{tick}</text>'
    body += f'<line x1="{x0}" y1="{y0}" x2="{x0 + chart_w}" y2="{y0}" class="axis"/>'
    body += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 - chart_h}" class="axis"/>'
    body += f'<text x="{x0 + chart_w / 2}" y="{y0 + 60}" text-anchor="middle" class="label">实施难度 Implementation Difficulty</text>'
    body += f'<text x="50" y="{y0 - chart_h / 2}" transform="rotate(-90 50 {y0 - chart_h / 2})" text-anchor="middle" class="label">设计价值 Impact</text>'
    body += f'<line x1="{x0 + chart_w / 2}" y1="{y0}" x2="{x0 + chart_w / 2}" y2="{y0 - chart_h}" stroke="#b8c5bd" stroke-width="1"/>'
    body += f'<line x1="{x0}" y1="{y0 - chart_h / 2}" x2="{x0 + chart_w}" y2="{y0 - chart_h / 2}" stroke="#b8c5bd" stroke-width="1"/>'
    for row in rows:
        x = x0 + (row["difficulty"] - 1) / 4 * chart_w
        y = y0 - (row["impact"] - 1) / 4 * chart_h
        r = 8 + row["weighted_priority_score"] * 4
        fill = color_scale(row["weighted_priority_score"], 2.2, 4.2)
        body += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#263238" stroke-width="1.2" opacity="0.92"/>'
        body += f'<text x="{x + r + 8}" y="{y + 4}" class="small">{esc(row["name"])}</text>'
    body += '<text x="735" y="170" class="note">高价值 / 低难度：优先转入方案</text>'
    body += '<text x="735" y="610" class="note">低价值 / 高难度：谨慎处理</text>'
    write_text(CHARTS / "06_design_priority_matrix.svg", svg_root(width, height, body))


def polyline(points: list[tuple[float, float]], color: str, width: int) -> str:
    coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def wrap_label(text: str, max_len: int) -> list[str]:
    if len(text) <= max_len:
        return [text]
    chunks = []
    current = ""
    for part in text.replace("/", " / ").split():
        if len(current) + len(part) + 1 <= max_len:
            current = f"{current} {part}".strip()
        else:
            if current:
                chunks.append(current)
            current = part
    if current:
        chunks.append(current)
    if len(chunks) == 1 and len(chunks[0]) > max_len:
        return [chunks[0][i : i + max_len] for i in range(0, len(chunks[0]), max_len)]
    return chunks[:3]


def write_readme() -> None:
    readme = """# Python 初步分析图表输出说明

本目录由 `scripts/generate_preliminary_analysis_charts.py` 生成。

## 输出图表

1. `charts/01_barrier_index_heatmap.svg`  
   阻隔强度热力图。按 0-500m 五段，汇总物理、交通、视觉、心理安全阻隔。

2. `charts/02_intervention_classes.svg`  
   防洪墙与河岸可介入性分级。用于限制设计动作强度。

3. `charts/03_environment_heat_exposure.svg`  
   热暴露与硬化压力评分。比较不透水面、缺少遮阴、低植被活性。

4. `charts/04_heritage_readability.svg`  
   遗产可读性评分。识别更适合作为叙事和解说的节点。

5. `charts/05_seasonal_availability.svg`  
   季节水位风险与可使用性关系。用于日常/洪水双模式空间分区。

6. `charts/06_design_priority_matrix.svg`  
   设计机会优先级矩阵。横轴为实施难度，纵轴为设计价值。

## 数据边界

- 当前数据是基于已有文档、公开地图/街景线索和公式框架形成的定性评分，不是实测结果。
- 评分尺度为 1-5 或派生总分，适合用于作品集前期判断和图纸草稿。
- 后续如获得 GIS、遥感、水位或现场观察数据，应替换脚本顶部的数据表后重新生成。
- 图表建议标注 `Preliminary observation / qualitative scoring`。

## 可编辑数据

CSV 文件位于 `data/`：

- `segment_barrier_scores.csv`
- `intervention_class_scores.csv`
- `environment_heat_exposure_scores.csv`
- `heritage_readability_scores.csv`
- `seasonal_availability_assumptions.csv`
- `design_priority_scores.csv`
"""
    write_text(OUT / "README.md", readme)


def main() -> None:
    ensure_dirs()
    chart_barrier_heatmap()
    chart_intervention_classes()
    chart_environment_risk()
    chart_heritage_readability()
    chart_seasonal_availability()
    chart_priority_matrix()
    write_readme()
    print(f"Generated charts in {CHARTS}")
    print(f"Generated data in {DATA}")


if __name__ == "__main__":
    main()
