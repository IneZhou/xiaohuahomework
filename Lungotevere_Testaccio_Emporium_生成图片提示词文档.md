# Lungotevere Testaccio / Emporium 生成图片提示词文档

生成日期：2026-06-12  
用途：根据项目现有研究资料、图片资料评价和分析图清单，整理后续需要生成或重绘的图片资产及提示词。本文面向作品集图板制作，不替代现场照片、官方地图、GIS 数据、水文数据或授权图片。

## 1. 总体原则

### 1.1 可以生成的图片类型

- 概念性剖面、轴测、爆炸图、图解场景。
- 根据公开资料重绘的分析图风格底图、节点图、叙事图。
- 设计策略效果图、材料节点图、植物与洪水恢复逻辑图。
- 案例机制图和风格统一的参考卡片插图。

### 1.2 不应生成的图片类型

- 伪装成真实现场照片的 Lungotevere Testaccio / Emporium 现状照片。
- 伪装成 Google Earth、Street View、Roma Capitale、SITAR 或水文机构原始截图的图片。
- 带有精确坐标、实测水位、审批边界、法定保护范围但没有真实数据支撑的图。
- 大规模拆除防洪墙、深挖遗迹、固定低位商业或重型滨水建筑的方案图。

### 1.3 统一视觉要求

建议整套图片采用同一作品集视觉语言：

```text
architectural portfolio diagram, clean academic landscape architecture style, restrained color palette, off-white background, thin black linework, muted terracotta brick, Tiber blue-green water, soft olive planting, light grey infrastructure, clear sectional depth, precise labels left blank, no fake map labels, no photorealistic claim, high resolution
```

通用负面提示词：

```text
no fake Google Maps screenshot, no fake official GIS interface, no inaccurate text labels, no watermark, no crowds blocking the site, no fantasy architecture, no demolished flood wall, no deep excavation into archaeological remains, no luxury waterfront commercial development, no glossy resort style, no exaggerated tropical planting, no unreadable tiny text
```

## 2. 图片资产总表

| 编号 | 图片名称 | 优先级 | 图板用途 | 生成类型 | 证据边界 |
|---|---|---:|---|---|---|
| IMG-01 | 历史-水文-工程化河岸多时段剖面 | 最高 | 项目主论点 / 第一张核心图 | 剖面图解 | 概念剖面，不是实测断面 |
| IMG-02 | 500m 线性研究范围轴测总图 | 最高 | 统一 S1-S5、节点和场地边界 | 轴测重绘图 | 需后续用 OSM / Google Earth 校准 |
| IMG-03 | 三类典型横剖面组 | 最高 | 解释上层道路、防洪墙、下层河岸和河面关系 | 剖面组 | 高差为示意，需现场核验 |
| IMG-04 | Emporium 遗迹可读性场景图 | 高 | 遗产策略 / S2 节点 | 概念场景 | 不能当真实现状照片 |
| IMG-05 | 日常 / 洪水双模式河岸场景 | 高 | 防洪与季节性使用策略 | 对比场景 | 水位为概念模型 |
| IMG-06 | S1/S3/S5 入口与导视节点策略 | 高 | 可达性、横向连接、桥头门户 | 节点轴测 | 入口位置需街景复核 |
| IMG-07 | 遮阴、低维护种植与热暴露缓解场景 | 高 | 微气候和植被策略 | 场景 / 剖透视 | 植物为参考适生类群 |
| IMG-08 | 透水铺装、雨水花园和维护分区节点 | 中高 | 材料 / 水文友好策略 | 构造节点图 | 不作工程详图 |
| IMG-09 | S2 遗产敏感段可逆轻介入细部 | 中高 | 遗产保护与材料策略 | 细部轴测 | 不触碰遗迹和防洪主结构 |
| IMG-10 | 人-生物低干扰互动河岸图 | 中 | 生态 / 水文生物 / 夜间照明 | 场景图 | 动物为潜在类群，不代表现场确认 |
| IMG-11 | 六个案例机制卡片统一插图 | 中 | 案例研究板 | 小图标 / 机制图 | 表达机制，不复刻案例照片 |
| IMG-12 | 材料与洪水后恢复拼贴图 | 中 | 材料策略板 | 材料板 / moodboard | 应标注为 design material reference |

## 3. 单张图片提示词

### IMG-01 历史-水文-工程化河岸多时段剖面

目标：说明场地不是普通滨水公园，而是古代河港、现代防洪墙、上层道路和当代下层河岸叠合形成的基础设施边缘。

应包含：

- Testaccio 街区、Lungotevere 上层道路、muraglioni 防洪墙、下层步道、台伯河。
- 古代 Emporium 河港遗迹、19-20 世纪防洪墙、当代道路系统三层时间关系。
- 可使用区、遗产敏感区、防洪不可介入区以不同透明色块表达。

提示词：

```text
conceptual architectural section of Lungotevere Testaccio and the ancient Emporium river port in Rome, showing layered urban edge from Testaccio street block to upper Lungotevere road, tall muraglioni flood wall, lower riverbank path and the Tiber River, ancient brick port remains embedded near the lower edge, 19th century flood control infrastructure compressing the historical river-port interface, contemporary traffic corridor above, diagrammatic time layers, floodable lower zone, heritage sensitive zone, non-intervention flood wall zone, clean landscape architecture portfolio drawing, precise thin linework, muted terracotta brick, pale concrete grey, Tiber blue-green, soft olive vegetation, off-white background, labels left blank, high resolution
```

负面提示词：

```text
no fake measured dimensions, no fake official labels, no demolished flood wall, no deep archaeological excavation, no photorealistic tourist photo, no fantasy Roman ruins, no luxury waterfront park
```

### IMG-02 500m 线性研究范围轴测总图

目标：建立从 Piazza dell'Emporio / Ponte Sublicio 到 Ponte Testaccio / Largo Giovanni Battista Marzi 的 500m 线性坐标，统一 S1-S5 分段。

应包含：

- 线性河岸、两端桥头、Piazza dell'Emporio、Via Franklin、Via Rubattino / Via Branca、Ponte Testaccio。
- 上层道路、下层河岸、桥梁、街区内部遗产联系。
- S1-S5 五段以浅色分区表达，文字可留空后期排版。

提示词：

```text
clean axonometric site diagram of a 500 meter linear riverfront study area in Testaccio Rome, from Piazza dell'Emporio and Ponte Sublicio to Ponte Testaccio, showing the Tiber River on one side, Lungotevere road, flood wall, lower riverbank path, surrounding compact urban blocks, bridgeheads, transverse streets including Via Franklin and Via Rubattino, relationship to ancient Emporium river-port remains and Porticus Aemilia warehouse system, five equal study segments indicated with subtle transparent bands, academic landscape architecture portfolio style, simplified accurate urban massing, no readable map text, off-white background, muted terracotta and grey, blue-green river, thin black linework, high resolution
```

负面提示词：

```text
no fake satellite screenshot, no Google map interface, no random street names, no distorted Rome landmarks, no decorative fantasy city, no heavy new buildings
```

### IMG-03 三类典型横剖面组

目标：用一组并列剖面解释不同段落的空间限制。

建议三张小剖面：

1. 典型防洪墙剖面：上层道路、防洪墙、下层步道、河面。
2. 遗迹段剖面：砖拱遗迹、栏杆、树荫、低接触观察路径。
3. 桥头剖面：桥梁、道路、楼梯或既有下河路径、桥下或桥头空间。

提示词：

```text
triptych of three architectural cross sections for a constrained historic riverfront in Rome, section A typical muraglioni flood wall with upper road, vertical drop, lower riverside path and Tiber water; section B Emporium archaeological brick remains beside railings, trees and a low-contact observation path; section C bridgehead condition with bridge structure, traffic edge, stairs or existing river access and shaded lower bank, all drawn in consistent clean portfolio style, thin linework, muted terracotta ruins, light grey infrastructure, soft green tree canopy, blue-green water, off-white background, blank label areas, high resolution
```

负面提示词：

```text
no precise fake elevation numbers, no fantasy ruins, no monumental new ramps crossing ruins, no deep foundations, no resort promenade
```

### IMG-04 Emporium 遗迹可读性场景图

目标：表达 S2 遗迹段“可见但不可读”的问题，以及可逆解说、远观、地面尺度标记和低照度照明的策略。

应包含：

- 砖拱 / 码头遗存的片段感。
- 现代栏杆、树荫、下层步道、防洪墙。
- 小尺度可拆卸解说牌、地面线性标记、远观停留点。
- 避免人群踩踏遗迹。

提示词：

```text
conceptual design scene of the Emporium archaeological river-port remains along Lungotevere Testaccio, ancient terracotta brick arches and port fragments visible behind simple railings, shaded lower riverside path under mature plane trees, tall flood wall and upper city road implied in the background, reversible interpretation elements, low removable signage, subtle ground scale markers showing the former port dimension, small quiet observation point set away from the ruins, restrained lighting, heritage-sensitive landscape architecture visualization, not photorealistic, clean realistic materials, calm public use, high resolution
```

负面提示词：

```text
no people walking on ruins, no excavation pit, no glass museum box, no heavy platform attached to ruins, no fake tourist photograph, no theatrical ancient reconstruction
```

### IMG-05 日常 / 洪水双模式河岸场景

目标：展示低位河岸在平时可使用、涨水时可淹没、退水后可清理恢复的策略。

应包含：

- 左右或上下对比：normal day / high water after flood。
- 可冲洗铺装、可移动家具、耐水植物、维护通道。
- 洪水后泥沙和清理逻辑用图解表达。

提示词：

```text
split-screen landscape architecture diagram showing daily mode and flood mode for the lower Tiber riverbank at Lungotevere Testaccio, left side normal dry season with washable stone path, removable benches, low-maintenance riparian planting, shaded walking edge, heritage-sensitive railings; right side high water or post-flood mode with lower bank partially inundated, furniture removed, robust plants bending and recovering, mud and debris cleaning route indicated diagrammatically, flood wall intact and untouched, clean portfolio section-perspective style, muted colors, clear spatial logic, labels left blank, high resolution
```

负面提示词：

```text
no catastrophic disaster scene, no broken monuments, no permanent shops under flood level, no engineering water-level numbers, no dramatic storm sky
```

### IMG-06 S1/S3/S5 入口与导视节点策略

目标：表达北端门户、Via Franklin 横向联系、南端桥头的可达性和导视策略。

应包含：

- 城市街区到河岸的铺装线、标识、过街提示、遮阴和小尺度停留。
- 不强行画穿越遗迹的大坡道。
- 体现“到达河岸、看到遗迹、理解历史”三件事的分离。

提示词：

```text
axonometric node strategy diagram for three access points along Lungotevere Testaccio, showing a northern gateway at Piazza dell'Emporio, a transverse connection from Via Franklin, and a southern bridgehead near Ponte Testaccio, with subtle paving guidance lines, small wayfinding signs, safer crossing cues, shade trees, compact seating, views toward the Tiber and the Emporium heritage edge, flood wall left structurally untouched, no large new ramp over archaeological remains, clear urban landscape portfolio style, muted Roman materials, thin linework, high resolution
```

负面提示词：

```text
no massive pedestrian bridge, no continuous universal ramp drawn through ruins, no car-free fantasy boulevard unless marked conceptual, no fake road markings with readable text
```

### IMG-07 遮阴、低维护种植与热暴露缓解场景

目标：回应 S3/S5 热暴露高的问题，展示地中海耐旱植被、树池、低维护灌草和透水地面如何改善停留舒适度。

应包含：

- 上层入口 / 桥头空间。
- 耐旱乔木、低灌木、多年生草本、可维护树池。
- 浅色透水铺装、坐凳、阴影。

提示词：

```text
summer microclimate improvement scene for a Roman riverfront access node, Lungotevere Testaccio, showing heat-exposed paved entrance transformed with Mediterranean drought-tolerant shade trees, permeable light paving, low-maintenance shrubs and perennial grasses, simple seating in shade, wayfinding line leading toward the Tiber, traffic edge softened but still present, heritage and flood wall respected, warm daylight, clean landscape architecture visualization, not lush tropical, restrained urban public space, high resolution
```

负面提示词：

```text
no tropical planting, no high-maintenance flower beds, no dense forest blocking heritage views, no decorative resort atmosphere, no irrigation-heavy lawn
```

### IMG-08 透水铺装、雨水花园和维护分区节点

目标：为材料策略板提供一张可读的构造 / 节点图，说明透水铺装、雨水花园、维护通道和洪水后清理之间的关系。

应包含：

- 透水铺装层、开级配碎石基层、雨水花园、边缘排水。
- 维护通道和可替换材料。
- 不深挖遗迹段，适合 S3/S5 上层入口和桥头。

提示词：

```text
exploded landscape construction diagram for a water-sensitive urban riverfront node in Rome, showing permeable paving surface, open-graded gravel base, shallow rain garden planting, edge drainage, maintenance access strip, replaceable modular seating, suitable for upper access plazas and bridgeheads near Lungotevere Testaccio, no deep excavation, heritage-compatible reversible materials, clean technical axonometric drawing, muted grey stone, olive plants, terracotta context accents, off-white background, blank callout boxes, high resolution
```

负面提示词：

```text
no detailed engineering certification, no deep piles, no underground tanks under archaeology, no fake measurements, no glossy commercial plaza
```

### IMG-09 S2 遗产敏感段可逆轻介入细部

目标：聚焦 S2，表达“少挖、架空、可拆、低接触”的遗产保护策略。

应包含：

- 金属格栅或轻量架空观察边缘，但不压在遗迹本体上。
- 可拆卸标识、低照度灯具、地面尺度标记。
- 根系受控的容器化或浅层草本。

提示词：

```text
heritage-sensitive reversible intervention detail beside ancient Roman Emporium remains, lightweight metal grate observation edge set outside the archaeological fabric, removable interpretive panel, low-level downward lighting, subtle ground scale marker, shallow container planting with controlled roots, existing brick remains protected behind railing, flood wall and riverbank context, minimal contact strategy, clean architectural detail axonometric, restrained materials, high resolution
```

负面提示词：

```text
no drilling into ancient brick, no heavy concrete foundation, no glass enclosure, no tree roots over ruins, no crowding, no museum reconstruction
```

### IMG-10 人-生物低干扰互动河岸图

目标：展示散步、观鸟、儿童自然教育、遛狗、夜间使用和维护如何分区，减少对潜在鸟类、昆虫和河岸微生境的干扰。

应包含：

- 远观节点、低干扰边界、向下照明、昆虫友好小尺度种植。
- 人类活动分区，不把动物画成已确认现场物种。
- 可用符号表达 potential bird movement corridor。

提示词：

```text
ecological public use diagram for a historic urban riverfront along the Tiber, showing low-disturbance observation edge, walking path, small nature education point, dog walking area kept away from habitat edge, downward low-intensity lighting, pollinator planting patches, potential bird movement corridor indicated with abstract silhouettes, maintenance route, floodable lower bank, heritage remains respected, clean landscape architecture portfolio style, diagrammatic not documentary, muted colors, high resolution
```

负面提示词：

```text
no claim of confirmed species, no zoo-like wildlife scene, no bright floodlights, no people entering habitat patches, no dense wetland blocking maintenance access
```

### IMG-11 六个案例机制卡片统一插图

目标：为 Madrid Rio、Keilehaven、Bishan-Ang Mo Kio Park、De Ceuvel、Vitoria-Gasteiz Green Belt、Ladywell Fields 制作统一风格机制图，而不是复刻照片。

建议每个案例生成一张 1:1 或 4:3 小图：

- Madrid Rio：交通阻隔转为线性连接。
- Keilehaven：硬质港口边缘的湿干 / 高低生态梯度。
- Bishan-Ang Mo Kio Park：日常公园和暴雨基础设施双模式。
- De Ceuvel：污染 / 不可深挖场地的架空可逆系统。
- Vitoria-Gasteiz Green Belt：长期维护和生态廊道。
- Ladywell Fields：城市河道自然化、洪水缓冲和教育节点。

通用提示词模板：

```text
small mechanism diagram for a landscape architecture case study card, [case mechanism], simplified axonometric or section diagram, no photographic copying, clean academic portfolio style, muted colors, thin black linework, off-white background, blank title area, high resolution
```

可替换机制短语：

```text
Madrid Rio: transforming a traffic barrier into linear riverfront connections with bridge nodes and pedestrian links
Keilehaven: inserting ecological wet-dry gradients into a hard port edge
Bishan-Ang Mo Kio Park: everyday park space functioning as floodable blue-green infrastructure during storm events
De Ceuvel: reversible elevated structures on contaminated land with no deep excavation
Vitoria-Gasteiz Green Belt: long-term ecological corridor management with low-intensity public use
Ladywell Fields: urban river naturalization with flood buffering and small education nodes
```

负面提示词：

```text
no copied project photograph, no exact trademarked rendering, no fake designer logo, no excessive text, no photorealistic site claim
```

### IMG-12 材料与洪水后恢复拼贴图

目标：为最终材料策略板提供统一情绪和材料参考，包括透水铺装、可淹没石材、金属格栅、可移动座椅、低维护草本、低照度灯具。

提示词：

```text
architectural material strategy moodboard for a flood-resilient heritage riverfront in Rome, arranged as clean portfolio collage with samples of permeable light stone paving, washable concrete or stone edge, lightweight metal grating, removable timber or metal seating, low-maintenance Mediterranean grasses, riparian plants, downward low-intensity lighting, terracotta brick heritage reference, subtle blue-green water reference, restrained and technical, no text labels, off-white background, high resolution
```

负面提示词：

```text
no luxury resort materials, no tropical plants, no ornate fake Roman decoration, no glossy commercial furniture, no excessive color palette
```

## 4. 推荐生成顺序

1. 先生成 IMG-01、IMG-02、IMG-03：确立项目主线、范围和空间断面。
2. 再生成 IMG-04、IMG-05、IMG-06：分别回应遗产、防洪和可达性三个核心问题。
3. 然后生成 IMG-07、IMG-08、IMG-09、IMG-10：补足微气候、材料、生态和维护策略。
4. 最后生成 IMG-11、IMG-12：服务案例与材料板，统一图板风格。

## 5. 后期排版提醒

- 所有文字标签建议在 Illustrator、Figma、InDesign 或 CAD 后期添加，不依赖 AI 直接生成文字。
- 每张图应在图注标明 `conceptual diagram / design-stage hypothesis / to be verified on site` 中的适用表述。
- 与水位、遗产边界、入口位置、材料适用段相关的图，应和项目现有 CSV、Street View 核验、官方资料或现场资料交叉校对。
- 若图中出现真实来源改绘内容，应在图板角落保留来源说明，如 OSM、Google Earth observation、Roma Capitale / Regione Lazio data portal 等。
