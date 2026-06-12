# Lungotevere Testaccio / Emporium 现状诊断报告

生成日期：2026-06-12  
研究对象：Piazza dell'Emporio 至 Largo Giovanni Battista Marzi / Ponte Testaccio 之间约 500 米 Lungotevere Testaccio 河岸段。  
报告性质：作品集研究阶段的现状诊断，不替代现场测绘、水文计算、考古许可、结构审查或正式行政审批。

## 1. Scope and Evidence Boundary

### 1.1 Thesis Statement

The site should not be redesigned as a conventional waterfront park. Lungotevere Testaccio / Emporium is a layered infrastructural edge where ancient river-port remains, modern flood-control walls, traffic corridors, and heritage protection constraints overlap. The design priority should therefore shift from heavy transformation to selective reconnection: improving readability, access, thermal comfort, and low-maintenance seasonal use without compromising flood safety or archaeological integrity.

### 1.2 研究范围

研究段为 Lungotevere Testaccio 约 500 米线性河岸：

- 北端：Piazza dell'Emporio / Ponte Sublicio。
- 南端：Largo Giovanni Battista Marzi / Ponte Testaccio。
- 所属片区：Roma, Rione XX Testaccio，台伯河左岸。
- 核心空间结构：上层 Lungotevere 道路、防洪墙 / muraglioni、下层河岸步道、台伯河。

该范围不是任意选择的滨河绿地，而是 Testaccio 与台伯河之间最直接叠合古代河港、现代防洪墙和当代车行道路的线性界面。

### 1.3 证据等级

本报告将证据分为五级。所有图表和判断必须标明证据等级，避免把推导评分误写成实测数据。

| 等级 | 证据类型 | 本项目中的例子 | 使用方式 |
|---|---|---|---|
| A | 法律、官方机构、政府开放数据 | D.Lgs. 42/2004、Roma / Lazio 官方数据入口、流域管理机构资料 | 用于建立法规、规划、水文和行政约束的参考框架 |
| B | 考古机构、博物馆、官方遗产说明 | Sovrintendenza、SITAR、Museo Diffuso del Rione Testaccio、Digital Augustan Rome | 用于确认遗产叙事、遗迹位置、历史尺度 |
| C | 公开地图、遥感、Street View、OSM | OpenStreetMap、Google Earth、Street View、Copernicus、OpenTopography | 用于底图、路径、遥感趋势、远程现状观察 |
| D | 项目定性评分、推导模型、公式框架 | 阻隔指数、热暴露评分、可介入性等级、遗产可读性评分、优先级评分 | 用于作品集阶段判断，不作为实测或审批依据 |
| E | 设计假设、待现场验证内容 | 概念性季节可使用性、行为轨迹推测、维护状态推测 | 只能作为待核验假设 |

### 1.4 已使用数据

| 数据 | 文件/来源 | 证据等级 | 用途 |
|---|---|---|---|
| 场地长度与节点 | `Lungotevere_Testaccio_Emporium_现状与历史资料整理.md` | C/D | 确定 500 米线性研究范围和 5 个关键节点 |
| 阻隔、热暴露、可介入性、优先级评分 | `analysis_outputs/data/*.csv` | D | 用于作品集级现状诊断和方案优先级判断 |
| 历史与遗产资料 | Roma / Lazio / 遗产机构资料入口 | A/B/C | 判断历史成因和遗产叙事 |
| 法规与管理约束 | Normattiva、流域管理机构入口 | A | 作为设计谨慎原则，不构成正式法律判断 |

评分数据说明：当前 CSV 数据来自已有文档、公开地图/街景线索和公式框架，是 1-5 分定性评分，适合前期判断，不是遥感分类、交通实测、水位实测或工程模型。

## 2. Historical Formation of the River Edge

### 2.1 Emporium：河港系统

Emporium 是古罗马河港，约在公元前 2 世纪初形成，位置在 Aventine 与 Testaccio 一带。其功能与城市供应系统直接相关：来自 Ostia 和 Porto 的货物沿台伯河进入罗马，再在 Testaccio 一带卸载、储存和分配。

需要明确：Emporium 是河港和码头系统，不应与 Porticus Aemilia 合并为同一个遗址。资料中 Emporium 可见遗存包括约 500 米长、90 米深的码头结构、台阶、坡道和系船构造。对本项目而言，它说明当前河岸不是自然岸线，而是长期被卸货、停靠、仓储和运输使用改造过的工作岸线。

设计含义：

- Emporium 适合作为河港叙事核心。
- 遗迹段不适合重型进入和深基础设施。
- 设计应通过可逆解说、尺度标记、远观节点和剖面表达其历史结构。

### 2.2 Porticus Aemilia：街区内部仓储系统

Porticus Aemilia 与 Emporium 同属古代河港-仓储系统，但功能和空间位置不同。Porticus Aemilia 更靠街区内部，是大型仓储建筑，典型尺度约 487 米长、60 米深，几乎与本项目 500 米研究段相当。

与 Porticus Aemilia 相关的可见残段主要不在下层河岸，而在 Testaccio 街区内部，例如 Via Rubattino、Via Beniamino Franklin、Via Giovanni Branca、Via Florio 一带。因此本项目应将其表达为“街区内部仓储带 + 河岸 Emporium 港口”的复合系统。

设计含义：

- S4 / Via Rubattino / Via Branca 更适合承接仓储系统解释。
- Via Franklin 可作为街区到河港的横向叙事联系。
- 图纸应区分“河港遗迹”“仓储遗构”“推测历史范围”“现代道路与防洪墙”。

### 2.3 Monte Testaccio：城市代谢结果

Monte Testaccio 是由大量破碎陶罐和运输容器堆积形成的人工丘。它与 Emporium 的货物流动直接相关：货物入城、容器废弃、碎片堆积，最终形成独特地貌。

设计含义：

- Testaccio 的身份不是普通滨水街区，而是贸易、劳动、基础设施和城市代谢叠合的片区。
- 历史叙事可形成“河港卸货 -> 仓储分配 -> 陶片堆积 -> 现代市场和工业遗产”的链条。

### 2.4 1875-1926：现代防洪墙与 Lungotevere

19 世纪以前，罗马长期受台伯河洪水影响。1870 年大洪水后，现代国家治理下的罗马需要稳定河道、防止城区反复被淹、建设沿河道路和排水系统。1875 年相关工程获批，1876 年开工，至 1926 年前后完成。

工程内容包括：

- Lungotevere 沿河道路。
- muraglioni 防洪墙。
- 河道整治。
- 排水和洪水控制。

该工程提升了防洪安全，但在空间上造成四个结果：

1. 城市路面与河面被垂直高差分离。
2. 河岸由开放、可接触、可经营的工作岸线，转为受墙体控制的低位通道。
3. 上层道路占据河岸界面，使亲水路径变成交通边界。
4. 古代遗迹被压入墙体、下层岸线和树荫之间，成为“可见但不易理解”的残片。

因此，今天的核心矛盾不是“缺少景观设计”，而是两个历史系统叠压后的结果：古代港口系统需要接触河流，现代防洪系统需要隔离河流。

## 3. Regulatory and Infrastructure Constraints

### 3.1 文化遗产与景观法规参考

The project is framed with reference to D.Lgs. 42/2004, the Italian Code of Cultural Heritage and Landscape. At this stage, the code is used to define design precautions rather than to make a formal legal determination of authorization procedures.

本报告不判断某项设计是否必然需要某类许可。法规条文在此仅用于转译成作品集阶段的 design constraints / regulatory implications。

| 条文 | 设计谨慎含义 | 对本项目的约束 |
|---|---|---|
| Art. 10 | 具有艺术、历史、考古或民族人类学价值的不动产和动产可构成文化遗产 | Emporium、Porticus Aemilia 相关遗构不能按普通边角地处理 |
| Art. 20 | 不应毁坏、损害文化遗产，或使其用途与历史/艺术性质不相容 | 遗迹段避免压覆、遮挡、深挖、重型活动设施 |
| Art. 21 | 涉及文化遗产拆除、移动、结构改变等行为通常需主管部门授权 | 钻孔、基础、墙体附着、固定平台不能直接假设可行 |
| Art. 45 | 间接保护可涉及距离、尺度、视线、光照和环境条件 | 即使不触碰遗迹，也需控制高度、灯光、视线和环境尺度 |
| Art. 142 | 河流及岸线可能涉及法定景观保护 | 台伯河岸不能按普通铺装广场处理 |
| Art. 146 | 受保护景观内改变外观的工程涉及景观许可判断 | 栏杆、照明、平台、墙面标识、树木更新应保持轻量和可逆 |

设计结论：

- S2 / Emporium 遗迹段按 A 类“不可触碰 / 严格保护”处理。
- 可做的是可逆导视、地面尺度标记、低干预照明、可移除解说设施。
- 不应做深基础观景台、固定大棚、下挖展示坑或会改变墙体/遗迹结构的装置。

### 3.2 防洪与流域管理约束

台伯河属于流域尺度管理对象，不能只按街区公共空间处理。PAI / PGRA 等工具用于水文地质风险、洪水风险和流域管理。当前阶段未核验具体法定洪水风险边界，因此本报告只提出设计谨慎原则：

- 防洪墙是基础设施，不是普通景观挡墙。
- 下层河岸应默认存在季节性淹没、清淤、检修和应急通行需求。
- 任何减少河道过水断面、增加固定障碍、改变堤防结构或影响检修路径的方案，都应视为高风险。

### 3.3 Conceptual Seasonal Usability Model

Conceptual seasonal usability model based on typical flood-risk logic, pending verification with hydrometric data.

| 月份 | 相对水位/洪水风险 1-5 | 下层河岸可使用性 |
|---|---:|---:|
| Jan | 4 | 45% |
| Feb | 4 | 50% |
| Mar | 3 | 65% |
| Apr | 2 | 80% |
| May | 2 | 85% |
| Jun | 1 | 90% |
| Jul | 1 | 92% |
| Aug | 1 | 90% |
| Sep | 2 | 82% |
| Oct | 3 | 70% |
| Nov | 4 | 55% |
| Dec | 4 | 45% |

This table is a design-stage conceptual model. It does not represent measured daily water-level data. It should be verified through hydrometric records from Regione Lazio / Ufficio Idrografico e Mareografico and relevant Tiber basin flood-risk documents.

证据等级：E 级设计假设 / D 级概念模型。  
设计用途：用于区分常年可用、季节性可用、可淹没和不可介入区域。

设计结论：

- 下层空间应采用“日常使用 + 洪水后恢复”模式。
- 可淹没区只适合耐水、可冲洗、可拆卸、低维护设施。
- 不应把全年高强度商业、固定室内功能或难清理设施布置在低位河岸。

### 3.4 无障碍与公共开放约束

如果后续方案把河岸作为公共步行系统或公共停留空间，新增路径、坡道、台阶、栏杆、照明和导视应按公共空间安全和无障碍原则处理。由于场地存在显著高差，不能只画“从城市到河边的箭头”，必须说明：

- 哪些入口可作为无障碍入口。
- 哪些入口只能作为楼梯或观景点。
- 哪些段落因防洪墙、道路和遗产保护限制，不能强行做连续坡道。

若用大坡道解决 10 米级高差，坡道长度、转折平台、占地和遗迹冲突都会迅速变成主要矛盾。因此本阶段更合理的表达是“桥头和既有入口优先优化，遗迹段以可读性而非强进入为主”。

## 4. Segment-by-Segment Existing Conditions

本阶段按 100 米一段，将 500 米场地拆成 S1-S5。所有分段评分均为 D 级定性评分，不是实测数据。

| 分段 | 距离 | 节点 | 阻隔指数 /20 | 热暴露评分 /5 | 可介入性 | 证据等级 | 初步判断 |
|---|---:|---|---:|---:|---|---|---|
| S1 | 0-100m | Piazza dell'Emporio / Ponte Sublicio | 14 | 3.4 | B 轻量附着 / 可逆介入 | D | 北端入口价值高，但受道路和防洪墙限制 |
| S2 | 100-200m | Emporium 可见遗迹 / Lungotevere 11 | 17 | 3.8 | A 不可触碰 / 严格保护 | D | 全线阻隔最高，遗产敏感和防洪约束最高 |
| S3 | 200-300m | Via Franklin 横向联系 | 14 | 4.4 | B 轻量附着 / 可逆介入 | D | 热暴露最高之一，横向导视和遮阴需求强 |
| S4 | 300-400m | Via Rubattino / Via Branca 遗迹联系 | 12 | 3.4 | C 可使用界面优化 | D | 阻隔相对最低，适合做街区-遗迹联系节点 |
| S5 | 400-500m | Ponte Testaccio / Largo G. B. Marzi | 16 | 4.4 | B 轻量附着 / 可逆介入 | D | 南端桥头交通压力大，热暴露高，入口组织重要 |

### 4.1 S1：Piazza dell'Emporio / Ponte Sublicio，0-100m

数据：阻隔 14/20，热暴露 3.4/5，可介入性 B。  
成因：桥头、广场、上层道路和河岸入口叠合，空间识别重要但交通干扰明显。  
约束：可做导视和轻量公共空间优化，但不能改变防洪结构。  
现状判断：适合做北端门户、历史起点、过街和入口识别，不适合做重型构筑物。

### 4.2 S2：Emporium 可见遗迹 / Lungotevere 11，100-200m

数据：阻隔 17/20，全线最高；热暴露 3.8/5；可介入性 A；heritage_sensitivity 5/5，flood_safety_constraint 5/5。  
成因：古河港遗迹、防洪墙、低位河岸和上层道路在此叠合。  
约束：文化遗产和防洪安全均要求轻量、可逆、低接触。  
现状判断：这是项目的历史核心，但不是施工核心。应以可逆解说、视线整理、地面标记、远观平台为主。

### 4.3 S3：Via Franklin 横向联系，200-300m

数据：阻隔 14/20，热暴露 4.4/5，并列最高；accessibility_need 5/5。  
成因：街区到河岸的横向联系存在，但道路、墙体和硬化地表削弱体验。  
约束：若不触碰遗迹和防洪结构，可做较多轻量导视、铺装和遮阴优化。  
现状判断：适合作为“从街区走向河岸”的主要导视段，优先做遮阴和铺装改善。

### 4.4 S4：Via Rubattino / Via Branca 遗迹联系，300-400m

数据：阻隔 12/20，全线最低；热暴露 3.4/5；可介入性 C；遗产可读性节点分 9。  
成因：Porticus Aemilia / 仓储系统相关遗构与街区内部空间联系更强。  
约束：仍需避开遗产敏感范围，但相对适合界面优化和叙事组织。  
现状判断：这是最适合做“街区遗产解释 + 慢行联系 + 小尺度停留”的段落。

### 4.5 S5：Ponte Testaccio / Largo G. B. Marzi，400-500m

数据：阻隔 16/20，热暴露 4.4/5，traffic_barrier 5/5，accessibility_need 5/5。  
成因：桥头交通、跨河联系、下层入口和河岸空间转换叠合。  
约束：桥头和河岸均需服从交通安全、防洪和景观管理约束。  
现状判断：适合做南端门户和过渡节点，但必须处理交通边界、遮阴和安全识别。

## 5. Key Problems

### 5.1 Accessibility and Barrier

数据：

- S1、S3、S5 的 accessibility_need 均为 5/5。
- S2 accessibility_need 为 4/5，但 heritage_sensitivity 和 flood_safety_constraint 均为 5/5。
- 全线阻隔指数最高的是 S2 17/20，其次 S5 16/20。

诊断：

- 北端、Via Franklin、南端桥头是最需要改善可达性的三个位置。
- Emporium 遗迹段虽有展示价值，但不适合通过增加强进入来解决问题。
- 可达性策略应区分“到达河岸”“看到遗迹”“理解历史”三件事。

### 5.2 Heritage Readability

| 节点 | 可见性 | 可达性 | 解说潜力 | 损害风险 | 可读性分 | 证据等级 |
|---|---:|---:|---:|---:|---:|---|
| Piazza dell'Emporio | 3 | 4 | 4 | 2 | 9 | D |
| Emporium 遗址点 | 4 | 2 | 5 | 4 | 7 | D |
| Via Franklin 联系线 | 2 | 3 | 4 | 2 | 7 | D |
| Via Rubattino / Branca | 4 | 3 | 5 | 3 | 9 | D |
| Ponte Testaccio 桥头 | 2 | 4 | 3 | 2 | 7 | D |

诊断：

- Piazza dell'Emporio 和 Via Rubattino / Branca 的综合可读性最高，均为 9。
- Emporium 遗址点解说潜力最高 5/5，但损害风险 4/5、可达性 2/5，因此不适合被设计成高进入、高停留、高承载节点。
- 遗产展示应从“直接靠近遗迹”转为“沿线叙事 + 远观解释 + 地面尺度标记”。

### 5.3 Flood Seasonality and Maintenance

数据：

- S2 flood_safety_constraint 为 5/5，maintenance_complexity 为 4/5。
- S5 maintenance_complexity 为 4/5，traffic_barrier 为 5/5。
- 下层河岸冬季可使用性假设 Jan 45%、Dec 45%，夏季 Jul 92%，但该表为 E 级概念模型。

诊断：

- 河岸下层具有明显季节性。夏季适合更多日常使用，冬季和高水位期应降低设施复杂度。
- 低位空间的设计必须考虑洪水后清理、设施损坏、泥沙、栏杆安全和市政维护。

### 5.4 Heat Exposure and Microclimate

数据：

- S3 热暴露评分 4.4/5。
- S5 热暴露评分 4.4/5。
- S2 热暴露评分 3.8/5。
- S1、S4 热暴露评分 3.4/5。

诊断：

- 热问题不是均匀分布，而是集中在横向联系和桥头转换位置。
- 这些位置也是人最可能等待、过街、辨认入口和停留的位置。
- 遮阴不是装饰，而是可达性的一部分。

## 6. Design Implications

### 6.1 诊断-策略矩阵

| issue | evidence | spatial segment | design response | drawing output |
|---|---|---|---|---|
| heritage sensitivity | Emporium / Porticus Aemilia remains | S2, S4 | reversible interpretation, no deep foundation | heritage readability map + section |
| flood-control constraint | muraglioni and lower bank seasonality | all segments, especially S2/S5 | floodable, washable, removable elements | flood constraint section |
| accessibility barrier | high barrier score in S2/S5 | S1/S3/S5 | gateway, signage, safer crossing, stair upgrade | accessibility map |
| heat exposure | S3/S5 score 4.4/5 | S3/S5 | shade, permeable paving, low-maintenance planting | heat exposure map |
| maintenance complexity | lower bank and heritage interface | S2/S5 | simple materials, controlled vegetation, maintenance routes | material-maintenance matrix |

### 6.2 不应作为方案主张的方向

1. 大规模拆除或打开防洪墙。
2. 在遗迹段设置深基础、下挖展示、固定大平台或高承载活动空间。
3. 在低位河岸布置全年固定商业、复杂电气设施或高维护花园。
4. 用连续大坡道强行解决全线高差，而不说明占地、坡度、遗产和防洪冲突。
5. 把 Emporium 和 Porticus Aemilia 合并成一个单一遗址叙事。

### 6.3 可成立的设计方向

1. 桥头和横向道路尽端做入口识别、导视和过街体验优化。
2. 遗迹段做可逆解说、尺度标记、远观节点和低干预照明。
3. S3、S5 做遮阴、透水铺装、可移动座椅和热暴露缓解。
4. S4 做街区内部遗产联系，将 Porticus Aemilia / 仓储系统与河港叙事连接。
5. 下层河岸采用可淹没、可冲洗、低维护的季节性公共空间。

## 7. Priority Intervention Zones

| 优先区 | 位置 | 依据 | 适合动作 | 不适合动作 |
|---|---|---|---|---|
| 北端入口门户 | S1 | accessibility_need 5/5，桥头门户位置 | 导视、过街提示、轻量停留、历史起点标识 | 深基础构筑物、改变防洪墙 |
| 遗迹解释核心 | S2 | 阻隔 17/20，heritage_sensitivity 5/5 | 可逆解说、远观节点、地面尺度标记、低干预照明 | 高承载活动、深挖、固定平台 |
| 横向导视与遮阴段 | S3 | 热暴露 4.4/5，accessibility_need 5/5 | 透水铺装、遮阴、导视、座椅 | 影响车行安全或遗产边界的重型设施 |
| 街区遗产联系段 | S4 | 阻隔 12/20，可读性 9 | Porticus Aemilia 叙事、慢行联系、小尺度停留 | 把仓储遗构误写成 Emporium 本体 |
| 南端桥头节点 | S5 | 阻隔 16/20，热暴露 4.4/5，traffic_barrier 5/5 | 入口识别、遮阴、桥头安全、可淹没设施边界 | 固定商业、高维护低位设施 |

## 8. Data Gaps and Required Verification

| data gap | current evidence level | required source | purpose | priority |
|---|---|---|---|---|
| 台伯河该段近年水位 / 降雨记录 | E / D | Regione Lazio / Ufficio Idrografico e Mareografico | 核验季节可使用性模型 | 高 |
| 洪水风险分区与 PAI / PGRA 约束 | A 待定位 | Autorità di Bacino Distrettuale dell'Appennino Centrale、官方 GIS | 判断低位设施和可淹没区边界 | 高 |
| Emporium 官方遗产边界 | B 待核验 | SITAR、Sovrintendenza、Museo Diffuso | 判断 S2 不可触碰边界 | 高 |
| Porticus Aemilia / 仓储遗构点位 | B/C 待核验 | 官方遗产资料、现场定位 | 判断 S4 历史叙事边界 | 高 |
| S1-S5 实际入口、楼梯、坡道、围挡状态 | C/D 待现场 | 现场照片、GPS 点位、Street View 复核 | 修正可达性图和入口策略 | 高 |
| 铺装、栏杆、墙体维护状态 | C/D 待现场 | 现场材料记录、照片 | 建立材料-维护矩阵 | 中高 |
| 树种、树冠质量、阴影时段 | C/D 待现场 | 现场观察、遥感复核、照片 | 修正热暴露与遮阴策略 | 高 |
| 人群活动和停留点 | E | 分时段人工观察 | 修正行为轨迹与停留潜力 | 中高 |
| 场地权属和管理主体 | A 待确认 | Roma Capitale、流域/遗产管理机构 | 判断长期维护和审批路径 | 高 |

## 9. 主要资料链接

- Roma Capitale Geoportale: https://www.comune.roma.it/web/it/geoportale.page
- Regione Lazio Geoportale: https://geoportale.regione.lazio.it/
- Regione Lazio Ufficio Idrografico e Mareografico: https://www.idrografico.regione.lazio.it/
- Autorità di Bacino Distrettuale dell'Appennino Centrale: https://www.autoritadistrettoac.it/
- Normattiva, D.Lgs. 42/2004: https://www.normattiva.it/
- Sovrintendenza Capitolina ai Beni Culturali: https://www.sovraintendenzaroma.it/
- Copernicus Land Monitoring Service: https://land.copernicus.eu/en
- Copernicus Browser: https://browser.dataspace.copernicus.eu/
- OpenStreetMap: https://www.openstreetmap.org/
- OpenTopography: https://opentopography.org/
