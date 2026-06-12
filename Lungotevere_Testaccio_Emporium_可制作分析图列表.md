# Lungotevere Testaccio / Emporium 可制作分析图列表

## 0. 文档定位

本文件根据《数据公式》《Lungotevere Testaccio / Emporium 河岸现状与历史资料整理》和《Testaccio 初步选址报告》整理。目标是把已有公式、可公开搜集的数据资料和作品集表达需求转化为一份可直接执行的分析图清单。

本阶段不做工程级水利模拟、交通模型或土壤检测。所有图纸按作品集分析深度组织，重点服务后续设计判断：在防洪约束内重建 Testaccio 与台伯河、古河港遗迹、日常公共空间和微气候系统之间的关系。

## 1. 数据来源总表

| 数据类型 | 推荐来源 | 可支撑图纸 | 备注 |
|---|---|---|---|
| 城市底图、道路、建筑、公共空间 | Roma Capitale Geoportale、OpenStreetMap、Google Earth | 研究范围图、线性总图、城市连接网络图、可达性图 | Roma Capitale Geoportale 是罗马市级 GIS 入口；OSM 适合快速建立底图和步行网络。 |
| 区域 GIS、地形、土地利用 | Geoportale Regione Lazio、OpenTopography、NASA Earthdata | 剖面、高程关系、背景区土地利用、坡度判断 | 场地尺度高差仍需结合街景和手工剖面校正。 |
| 水文、降雨、水位、洪水风险 | Regione Lazio Ufficio Idrografico e Mareografico、Autorità di Bacino Distrettuale dell'Appennino Centrale | 季节水位图、防洪约束图、日常/洪水模式图 | 作品集阶段以水位约束和可淹没分区为主，不做精确洪水模型。 |
| 土地覆盖、不透水面、树冠、遥感影像 | Copernicus Land Monitoring Service、Copernicus Browser、Copernicus Data Space、ISPRA/SNPA | 树冠覆盖、热暴露、不透水面、NDVI、雨水滞留潜力 | Sentinel-2 可做 NDVI；Copernicus Land 可查土地覆盖和不透水面。 |
| 遗产、考古、历史叙事 | SITAR Roma、Sovrintendenza Capitolina、Soprintendenza Speciale Roma、Museo Diffuso del Rione Testaccio、Digital Augustan Rome | 历史层叠图、遗迹可读性图、叙事节点图 | Emporium 与 Porticus Aemilia 需要分开表达，避免把河港和仓储遗构混写。 |
| 行为、活动、日常使用 | OpenStreetMap POI、Google Maps、Street View、公开照片、后续现场观察 | 行为轨迹、停留潜力、使用时段图 | 公开数据较弱，应标注为 preliminary observation，后续用现场观察修正。 |

参考入口：

- Roma Capitale Geoportale: https://www.comune.roma.it/web/it/geoportale.page
- Geoportale Regione Lazio: https://geoportale.regione.lazio.it/
- Regione Lazio Ufficio Idrografico e Mareografico: https://www.idrografico.regione.lazio.it/
- Autorità di Bacino Distrettuale dell'Appennino Centrale: https://www.autoritadistrettoac.it/
- Copernicus Land Monitoring Service: https://land.copernicus.eu/en
- Copernicus Browser: https://browser.dataspace.copernicus.eu/
- Copernicus Data Space Ecosystem: https://dataspace.copernicus.eu/
- ISPRA Consumo di suolo: https://www.isprambiente.gov.it/it/attivita/suolo-e-territorio/il-consumo-di-suolo
- SITAR Roma: https://sitar.cultura.gov.it/
- Sovrintendenza Capitolina ai Beni Culturali: https://www.sovraintendenzaroma.it/
- OpenStreetMap: https://www.openstreetmap.org/
- OpenTopography: https://opentopography.org/

## 2. 必做核心分析图

### 2.1 历史-水文-工程化河岸多时段剖面图

**图纸目标**  
证明场地不是普通滨河绿地，而是古罗马河港、19-20 世纪防洪工程和当代道路系统共同形成的垂直断面。

**图面内容**

- 横向结构：Testaccio 街区、Lungotevere 道路、防洪墙、下层河岸、台伯河。
- 纵向时间层：古代 Emporium 河港、19 世纪以前河岸、现代 muraglioni 建成后、当代现状。
- 标注日常可使用区、洪水影响区、遗迹敏感区、不可触碰防洪结构。

**可用公式**

```text
relative_height = point_elevation - normal_water_level
flood_clearance = design_surface_elevation - reference_flood_level
```

**数据来源**

- 历史地图、Digital Augustan Rome、SITAR Roma。
- Emporium / Porticus Aemilia 考古资料。
- Google Earth / OpenTopography 高程辅助。
- Street View 和公开照片校正墙体、道路、步道关系。

**制作优先级**  
最高。建议作为第一张分析板的核心图。

### 2.2 500 米现状线性总图 + 关键节点编号

**图纸目标**  
建立从 Piazza dell'Emporio 到 Largo Giovanni Battista Marzi / Ponte Testaccio 的清晰研究边界，并把后续所有分析落到同一条 500 米线性坐标上。

**图面内容**

- 研究范围线：Piazza dell'Emporio 至 Ponte Testaccio。
- 节点编号：北端桥头、Emporium 遗址点、Via Franklin 横向联系、Via Rubattino / Via Branca 遗迹联系、南端桥头、下层河岸入口。
- 上层道路、下层河岸、桥梁、横向街道、主要 POI。

**可用指标**

```text
segment_length
node_spacing
access_point_count
```

**数据来源**

- OpenStreetMap、Roma Capitale Geoportale、Google Earth 测距。
- 现状整理报告中的关键节点清单。

**制作优先级**  
最高。后续所有图纸应共用这张图的边界和节点编号。

### 2.3 典型横剖面组

**图纸目标**  
用剖面解释“上层城市 + 防洪墙 + 下层河岸 + 河面”的空间压缩关系。

**建议剖面**

1. 典型防洪墙剖面：上层道路、防洪墙、下层步道、台伯河。
2. 遗迹段剖面：Emporium 残段、栏杆、步道、树木、墙体。
3. 桥头剖面：桥梁、道路、楼梯或下河路径、河岸空间。

**可用指标**

```text
vertical_drop
accessible_width
lower_bank_width
wall_height_estimate
```

**数据来源**

- OpenTopography、Google Earth 高程、Street View、公开照片。
- 典型 muraglioni 剖面参考。

**制作优先级**  
最高。建议与 2.1 合并或连续排版。

### 2.4 季节水位与防洪约束图

**图纸目标**  
说明河岸不是全年同等可用，设计需要区分常年使用、季节性可用、可淹没和不可介入区域。

**图面内容**

- 横轴：月份或季节。
- 纵轴：台伯河水位 / 相对水位 / 风险等级。
- 叠加：正常水位、高水位、洪水警戒水位、防洪墙不可介入线。
- 对应空间：下层步道、可淹没平台、可恢复植被、不可移动设施。

**可用公式**

```text
usable_riverbank_width = total_lower_bank_width - inundated_width
seasonal_availability_ratio = usable_days_per_year / 365
```

**数据来源**

- Regione Lazio 水文气象数据入口。
- Autorità di Bacino 的台伯河流域和洪水风险资料。
- 若无法获得精确日水位，可做低水位季、常水位季、高水位季、洪水风险期的定性图。

**制作优先级**  
最高。它决定方案中哪些设施必须可拆卸、可淹没或可恢复。

### 2.5 阻隔强度与可达性图

**图纸目标**  
把“墙、道路、高差、围挡、入口不清楚”转化为可比较的线性阻隔热力图。

**图面内容**

- 按 20-50 米一段给 500 米场地分段。
- 分别评价物理阻隔、交通阻隔、视觉阻隔、心理/安全阻隔。
- 标出可达入口、疑似不可达段、危险过街点、视觉不可达点。

**可用公式**

```text
barrier_index =
physical_barrier_score +
traffic_barrier_score +
visual_barrier_score +
perceived_safety_score
```

每项建议 1-5 分，总分越高，阻隔越强。

**数据来源**

- Street View、Google Maps、OSM 道路。
- 现场照片或远程观察。
- 交通强度先用道路等级和车道宽度推断，不写成实测车流。

**制作优先级**  
高。它直接导出入口强化、导视、横向连接和桥头节点策略。

### 2.6 遗产可读性与叙事节点图

**图纸目标**  
解释 Emporium、Porticus Aemilia、Monte Testaccio 和现代 Lungotevere 的关系，识别哪些历史信息“可见但不可读”。

**图面内容**

- 确定可见遗迹：实线边界、照片编号。
- 历史推测范围：半透明色块、虚线边界。
- 叙事连接线：河港、仓储、Monte Testaccio、市场、屠宰场。
- 分级：看得见 / 看不见 / 看不懂 / 可解说。

**可用公式**

```text
heritage_readability_score =
visibility_score +
accessibility_score +
interpretation_potential_score -
damage_risk_score
```

**数据来源**

- SITAR Roma、Sovrintendenza Capitolina、Soprintendenza Speciale Roma。
- Museo Diffuso del Rione Testaccio。
- Digital Augustan Rome。
- Street View 和公开照片。

**制作优先级**  
高。它是项目区别于普通滨水更新的关键。

### 2.7 遮阴、热暴露与树冠覆盖图

**图纸目标**  
说明罗马夏季热环境如何影响河岸使用，并找出最需要遮阴、降温和树冠补强的位置。

**图面内容**

- 树冠覆盖分布。
- 硬质铺装和暴晒区域。
- 夏季下午重点阴影图。
- 需要遮阴的入口、停留点、桥头、遗迹观看点。

**可用公式**

```text
tree_canopy_cover_ratio = tree_canopy_area / site_area
shade_coverage_ratio = shaded_area_at_target_time / public_space_area

heat_exposure_score =
impervious_surface_ratio * 0.4 +
lack_of_shade_ratio * 0.4 +
low_vegetation_index_score * 0.2

ndvi = (nir - red) / (nir + red)
ndvi = (B8 - B4) / (B8 + B4)
```

**数据来源**

- Copernicus Browser / Sentinel-2。
- Copernicus Land Monitoring Service。
- Google Earth 卫星图、Street View 树冠核验。

**制作优先级**  
高。它能直接转化为树荫、轻量遮阳、透水铺装和停留点选址。

### 2.8 不透水面、径流与雨水滞留潜力图

**图纸目标**  
支撑“轻量雨水策略”：不改变台伯河水文，而是处理场地内硬化面、道路侧径流、低洼点和可透水改造区。

**图面内容**

- 硬质铺装比例。
- 现有径流方向。
- 可透水改造区。
- 雨水花园、下凹绿地、植被缓冲带潜力点。

**可用公式**

```text
impervious_surface_ratio = impervious_area / total_site_area
q = c * i * a
runoff_reduction_ratio = (runoff_existing - runoff_proposed) / runoff_existing
```

**数据来源**

- Copernicus Land Monitoring Service 的 imperviousness / land cover。
- ISPRA/SNPA 土壤消耗和人工覆盖资料。
- 卫星图和街景铺装判读。

**制作优先级**  
高。它为透水铺装、雨水花园和低维护植被提供依据。

## 3. 可做增强分析图

### 3.1 城市连接网络图

**图纸目标**  
证明 Lungotevere Testaccio 不是孤立河岸，而是连接 Piazza dell'Emporio、Ponte Sublicio、Ponte Testaccio、Monte Testaccio、Ex Mattatoio、Testaccio 市场、Porticus Aemilia 等节点的线性界面。

**可用公式**

```text
walking_time_minutes = distance_meters / walking_speed_m_per_minute
```

建议取 `walking_speed_m_per_minute = 80`，5 分钟约 400 米，10 分钟约 800 米。

**数据来源**

- OSM 路网、Google Maps POI、Roma Geoportale。

**建议位置**  
适合放在区位分析板或现状总图旁边。

### 3.2 行为轨迹与停留潜力图

**图纸目标**  
避免项目只讲历史和工程，补充居民、游客、文化活动人群、老人儿童和行动不便者的日常使用逻辑。

**可用公式**

```text
stay_potential_score =
shade_score +
view_score +
noise_comfort_score +
seat_availability_score +
accessibility_score
```

**数据来源**

- OSM POI、Google Maps、Street View、公开照片、后续现场观察。

**表达方式**

- 路径箭头 + 停留气泡 + 时间段条形图。
- 标注 preliminary observation，避免写成精确人流统计。

### 3.3 防洪墙可介入性分级图

**图纸目标**  
判断哪里不能动，哪里只能轻量附着，哪里可以做平台、台阶、栏杆、铺装或植被优化。

**分级建议**

- A 类：不可触碰，防洪主结构、遗迹敏感段。
- B 类：轻量附着，可做标识、灯光、可逆装置。
- C 类：可使用界面，台阶、平台、栏杆、临时家具。
- D 类：可进行铺装和植被优化的下层河岸或边角空间。

**可用公式**

```text
intervention_potential_score =
heritage_sensitivity_weight * heritage_score +
flood_safety_weight * flood_safety_score +
accessibility_weight * accessibility_score +
maintenance_weight * maintenance_score
```

**建议位置**  
适合与机会图合并，形成“轻量介入优先区”。

### 3.4 植被维护压力图

**图纸目标**  
说明河岸设计不能做高维护花园，而应选择耐旱、耐热、耐污染、可淹没、低维护的分区植物策略。

**可用公式**

```text
maintenance_risk_score =
irrigation_need_score +
pruning_need_score +
flood_damage_risk_score +
trampling_risk_score +
heritage_constraint_score
```

**建议处理**

- 不建议单独占一整张 A1。
- 可并入热暴露图、雨水图或设计策略板。

### 3.5 土壤与地表扰动风险图

**图纸目标**  
在缺少土壤检测的情况下，用历史河港、城市填土、硬化地、遗迹敏感区推断不同区域的施工和种植风险。

**可用公式**

```text
soil_intervention_sensitivity =
heritage_risk_score +
compaction_score +
contamination_uncertainty_score +
root_conflict_score
```

**表达原则**

- 写成风险假设图，不写成污染检测图。
- 分为浅层种植、容器种植、架空平台、不深挖区域。

### 3.6 材料适宜性矩阵

**图纸目标**  
把材料选择从审美判断转化为防洪、遗产、维护和热舒适的综合判断。

**可比较材料**

- 石材 / 再生石材。
- 透水铺装。
- 金属格栅。
- 木平台。
- 可拆卸座椅。
- 耐候钢。
- 砾石。
- 植被基质。
- 低照度灯具。
- 标识系统。

**可用公式**

```text
material_suitability_score =
reversibility_score +
flood_resistance_score +
maintenance_score +
heritage_compatibility_score +
thermal_comfort_score
```

**建议位置**  
适合放在设计策略板，而不是前期分析板。

## 4. 暂缓精密化的图

| 图名 | 暂缓原因 | 当前替代表达 |
|---|---|---|
| 精确洪水模拟图 | 缺少工程级断面、水位、流速、边界条件 | 做季节水位、防洪约束和可淹没分区 |
| 精确人流统计图 | 缺少现场计数、手机信令或长期观察 | 做路径推测、停留潜力和时段使用假设 |
| 精确土壤污染图 | 需要现场采样或官方污染调查 | 做历史填土、硬化、遗迹敏感和扰动风险图 |
| 精确噪音等值线图 | 缺少实测噪音或交通流量 | 用道路等级、车道宽度、桥头车流压力做噪音风险推断 |

## 5. 最推荐的 10 张分析图组合

这组图可以直接支撑 10 张 A1 作品集中的前期分析部分，也能自然过渡到策略、总平面、剖面和节点设计。

| 顺序 | 图名 | 类型 | 主要结论 |
|---|---|---|---|
| 1 | 历史-水文-工程化河岸多时段剖面图 | 历史 + 剖面 | 场地是被现代防洪工程压住的古河港界面 |
| 2 | 500 米现状线性总图 + 关键节点编号 | 总图 | 明确研究边界、节点和后续分析坐标 |
| 3 | 典型横剖面组 | 剖面 | 高差和墙体是设计的核心限制 |
| 4 | 季节水位与防洪约束图 | 水文 | 河岸需要日常/洪水双模式设计 |
| 5 | 阻隔强度与可达性图 | 可达性 | 入口、道路、高差和心理安全共同制造断裂 |
| 6 | 城市连接网络图 | 城市关系 | 河岸应连接市场、桥梁、Ex Mattatoio、Monte Testaccio 和遗迹网络 |
| 7 | 遗产可读性与叙事节点图 | 遗产 | 现有遗迹可见但不可读，需要路径、标识和节点解释 |
| 8 | 遮阴、热暴露与树冠覆盖图 | 微气候 | 夏季舒适度决定停留点和植被策略 |
| 9 | 不透水面、径流与雨水滞留潜力图 | 雨水 | 可通过透水铺装、雨水花园和低维护植被改善场地径流 |
| 10 | 问题叠加与设计机会优先级矩阵 | 综合决策 | 将历史、可达、微气候、雨水、维护转化为设计优先区 |

## 6. 综合机会优先级矩阵

最终综合图建议用“设计价值 / 实施难度”矩阵收束所有分析。

**可用公式**

```text
priority_score = impact_score / implementation_difficulty_score
```

或使用加权综合：

```text
priority_score =
heritage_value * 0.25 +
accessibility_gain * 0.25 +
microclimate_benefit * 0.20 +
ecological_benefit * 0.15 +
maintenance_feasibility * 0.15
```

**建议节点**

| 节点 | 价值 | 难度 | 建议 |
|---|---|---|---|
| Piazza dell'Emporio 入口强化 | 高 | 中 | 作为北端门户和历史起点 |
| Emporium 可见遗迹解说平台 | 高 | 高 | 采用可逆、轻量、低接触设计 |
| Via Franklin 横向导视 | 中高 | 低 | 用铺装线、标识和视线组织连接街区与河岸 |
| 道路侧遮阴和座椅 | 中高 | 低 | 快速提升日常使用舒适度 |
| 下层河岸可淹没平台 | 高 | 高 | 只在低风险区谨慎设置 |
| 墙体轻量标识系统 | 中 | 低 | 不改变防洪结构，提升历史可读性 |
| 桥头生态和公共空间节点 | 高 | 中高 | 同时处理入口、停留、过街和蓝绿连接 |

## 7. 制作顺序

1. 先做 500 米现状线性总图，统一底图、比例、节点编号。
2. 同步做历史层叠和多时段剖面，确立项目主线。
3. 做典型横剖面，明确高差、防洪墙和下层河岸关系。
4. 做可达性和阻隔强度图，找出入口与断点。
5. 做遗产可读性图，建立河港-仓储-城市代谢叙事。
6. 做树冠、热暴露和不透水面图，导出环境性能策略。
7. 做行为轨迹和停留潜力图，补足日常使用逻辑。
8. 最后做问题叠加和机会优先级矩阵，进入设计策略。

## 8. 关键表达注意事项

- 不要把 Emporium 和 Porticus Aemilia 混为同一个遗址。Emporium 偏河港和码头系统，Porticus Aemilia 偏仓储系统。
- 不要提出大规模拆除防洪墙。更合理的策略是轻量、可逆、可维护、分段介入。
- 水位、水文和土壤图应明确为作品集层面的约束分析，不包装成工程计算。
- 行为和人群图如果没有现场数据，应标注为公开地图资料、街景观察和后续现场验证。
- 遥感图用于判断植被和硬化趋势，不能替代树种、维护状态和地面材料的现场核验。
- 所有图纸应围绕同一核心判断：现代防洪系统切开了古代河港、城市街区和台伯河日常生活；设计任务是在防洪和遗产约束内重建可读性、可达性、微气候和日常使用。
