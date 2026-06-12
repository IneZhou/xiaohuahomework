# 根据《交流》意见拆分的小任务清单

生成日期：2026-06-12  
目标：把《交流》中的修改意见拆成可连续执行的小任务，防止上下文压缩或 token 不足后丢失方向。

## 总目标

把现有 Lungotevere Testaccio / Emporium 项目从“基础现状诊断稿”推进为更严谨的作品集研究包。重点不是继续写空泛总结，而是补强证据等级、法规谨慎表述、历史尺度、水文假设说明、案例研究、低维护材料和可执行图板矩阵。

核心 thesis statement：

> The site should not be redesigned as a conventional waterfront park. Lungotevere Testaccio / Emporium is a layered infrastructural edge where ancient river-port remains, modern flood-control walls, traffic corridors, and heritage protection constraints overlap. The design priority should therefore shift from heavy transformation to selective reconnection: improving readability, access, thermal comfort, and low-maintenance seasonal use without compromising flood safety or archaeological integrity.

## Task 01：修订证据等级

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

操作：

- 将原来的三类数据边界改成五级证据体系。
- 五级如下：
  - A 级：法律、官方机构、政府开放数据。
  - B 级：考古机构、博物馆、官方遗产说明。
  - C 级：公开地图、遥感、Street View、OSM。
  - D 级：项目定性评分、推导模型、公式框架。
  - E 级：设计假设、待现场验证内容。
- 明确以下数据属于 D 级，不是实测：
  - 阻隔指数。
  - 热暴露评分。
  - 可介入性等级。
  - 遗产可读性评分。
  - 设计优先级评分。

验收标准：

- 报告中不再只写“公开资料 / 定性评分 / 法规资料”三类。
- 任何 1-5 分评分旁边都有证据等级或定性说明。

## Task 02：修订法规章节语气

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

操作：

- 将“适用法规：D.Lgs. 42/2004”改为“以 D.Lgs. 42/2004 作为设计谨慎原则的参考框架”。
- 加入英文或中英双语说明：

```text
The project is framed with reference to D.Lgs. 42/2004, the Italian Code of Cultural Heritage and Landscape. At this stage, the code is used to define design precautions rather than to make a formal legal determination of authorization procedures.
```

- 保留 Art. 10、20、21、45、142、146，但全部写成 design constraints / regulatory implications。
- 避免写成“本项目必然适用某条审批”。

验收标准：

- 法规章节不再像正式法律意见。
- 每条法规后面都转译成具体设计限制。

## Task 03：修正 Emporium 与 Porticus Aemilia 的历史关系

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

操作：

- 明确 Emporium 和 Porticus Aemilia 是“河港-仓储系统”，但不是同一个遗址。
- 补入尺度：
  - Emporium：古罗马河港，约公元前 2 世纪初形成；可见遗存包含约 500m 长、90m 深的码头结构、台阶、坡道和系船构造。
  - Porticus Aemilia：更靠街区内部的大型仓储建筑，约 487m 长、60m 深。
- 保留 Monte Testaccio 作为货物流动和城市代谢链条的一部分。

验收标准：

- 报告中不把 Emporium 和 Porticus Aemilia 混写。
- 图纸逻辑能区分河港、仓储、陶片山和现代防洪墙。

## Task 04：强化 1875-1926 防洪墙历史成因

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

操作：

- 保留并加强以下时间线：
  - 1875 年批准相关工程。
  - 1876 年开工。
  - 至 1926 年前后完成。
- 明确工程内容：
  - Lungotevere 沿河道路。
  - muraglioni 防洪墙。
  - 河道整治。
  - 排水和洪水控制。
- 明确空间结果：
  - 防洪安全提升。
  - 日常亲水关系被切断。
  - 古河港界面被压入墙体、下层岸线和树荫之间。

验收标准：

- 现代防洪墙不是背景叙述，而是现状问题的直接成因。

## Task 05：修订季节水位表

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

操作：

- 将表名改为：

```text
Conceptual seasonal usability model based on typical flood-risk logic, pending verification with hydrometric data.
```

- 表下注明：

```text
This table is a design-stage conceptual model. It does not represent measured daily water-level data. It should be verified through hydrometric records from Regione Lazio / Ufficio Idrografico e Mareografico and relevant Tiber basin flood-risk documents.
```

- 保留 Jan-Dec 的相对水位风险和可使用性百分比，但标为 E 级设计假设 / D 级概念模型。

验收标准：

- 水位表不会被误解为真实水文数据。

## Task 06：新增“诊断-策略矩阵”

目标文件：

- 优先加入 `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`
- 可另存为图板用摘要文档。

矩阵字段：

```text
issue -> evidence -> spatial segment -> design response -> drawing output
```

必须包含：

| issue | evidence | segment | design response | drawing output |
|---|---|---|---|---|
| heritage sensitivity | Emporium / Porticus Aemilia remains | S2, S4 | reversible interpretation, no deep foundation | heritage readability map + section |
| flood-control constraint | muraglioni and lower bank seasonality | all segments, especially S2/S5 | floodable, washable, removable elements | flood constraint section |
| accessibility barrier | high barrier score in S2/S5 | S1/S3/S5 | gateway, signage, safer crossing, stair upgrade | accessibility map |
| heat exposure | S3/S5 score 4.4/5 | S3/S5 | shade, permeable paving, low-maintenance planting | heat exposure map |
| maintenance complexity | lower bank and heritage interface | S2/S5 | simple materials, controlled vegetation, maintenance routes | material-maintenance matrix |

验收标准：

- 这张表可以直接复制到 A1 图板。

## Task 07：重构报告目录

目标文件：

- `Lungotevere_Testaccio_Emporium_现状诊断报告_数据法规历史.md`

目标目录：

1. Scope and Evidence Boundary
2. Historical Formation of the River Edge
3. Regulatory and Infrastructure Constraints
4. Segment-by-Segment Existing Conditions
5. Key Problems
6. Design Implications
7. Priority Intervention Zones
8. Data Gaps and Required Verification

操作：

- 不删除已有有效内容。
- 重新排序章节，使它更像研究报告而不是素材堆。
- 在开头加入 thesis statement。

验收标准：

- 报告既能完整阅读，也能快速提取为 A1 图板。

## Task 08：建立案例研究任务表

建议新增文件：

- `Lungotevere_Testaccio_Emporium_案例与材料研究任务.md`

核心案例只选 6 个：

1. Madrid Rio：城市连接与线性河岸。
2. Rotterdam Tidal Park / Keilehaven：硬质港口边缘生态化。
3. Bishan-Ang Mo Kio Park：可淹没公共空间。
4. De Ceuvel：不可深挖场地的可逆低成本介入。
5. Vitoria-Gasteiz Green Belt：长期生态维护与低强度公共使用。
6. Ladywell Fields：城市河道自然化与洪水缓冲。

每个案例回答：

1. What was the original problem?
2. What hydrological or ecological strategy was used?
3. What material or maintenance logic made it feasible?
4. What can be transferred to Lungotevere Testaccio, and what cannot?

验收标准：

- 不堆案例。
- 每个案例都有“可转译 / 不可照搬”。

## Task 09：建立低维护策略研究表

建议新增文件：

- `Lungotevere_Testaccio_Emporium_案例与材料研究任务.md`

四个方向：

1. 低维护种植设计。
2. 维护分区设计。
3. 可逆与可替换材料。
4. 洪水后恢复设计。

可用公式：

```text
maintenance_intensity =
irrigation_need +
pruning_frequency +
cleaning_frequency +
flood_damage_risk +
replacement_frequency
```

```text
flood_recovery_design =
washable_surfaces +
removable_furniture +
robust_planting +
maintenance_access +
low_electrical_dependency
```

验收标准：

- 低维护被写成“可预测、可分区、可承受的管理系统”，不是“不维护”。

## Task 10：建立水文友好材料评价表

建议新增文件：

- `Lungotevere_Testaccio_Emporium_案例与材料研究任务.md`

材料类型：

1. 透水铺装。
2. 开级配碎石基层 / 砾石稳定系统。
3. 金属格栅与架空平台。
4. 可淹没石材 / 混凝土修补。
5. 生物滞留基质和雨水花园材料。

评价维度：

- reversibility
- flood resistance
- maintenance demand
- heritage compatibility
- thermal comfort
- suitable segment

验收标准：

- 每种材料都说明适合位置和不适合位置。
- 特别标注 S2 遗迹段不能深挖，S3/S5 更适合透水与遮阴策略。

## Task 11：建立数据缺口与核验清单

目标文件：

- 加入现状诊断报告最后一章。

字段：

```text
data gap -> current evidence level -> required source -> purpose -> priority
```

必须包含：

- Regione Lazio 水位/降雨记录。
- 台伯河流域洪水风险文件。
- Emporium / Porticus Aemilia 官方遗产边界。
- S1-S5 实际入口、楼梯、坡道和围挡状态。
- Street View / 现场照片下的材料、树冠、阴影、维护状态。

验收标准：

- 每个缺口都有明确数据源和用途。

## Task 12：可选 Python 图表更新

目标文件：

- `scripts/generate_preliminary_analysis_charts.py`
- `analysis_outputs/`

操作：

- 只有在文档修订完成后再做。
- 可新增：
  - 诊断-策略矩阵 SVG。
  - 材料适宜性矩阵 SVG。
  - 数据缺口优先级表 CSV/SVG。

验收标准：

- 不先画新图，先保证报告和表格内容严谨。

## 推荐执行顺序

1. Task 01：证据等级。
2. Task 02：法规语气。
3. Task 03：历史关系。
4. Task 04：防洪墙成因。
5. Task 05：水位表说明。
6. Task 06：诊断-策略矩阵。
7. Task 07：报告目录重构。
8. Task 11：数据缺口表。
9. Task 08：案例研究表。
10. Task 09：低维护策略表。
11. Task 10：水文友好材料表。
12. Task 12：Python 图表更新。

## 当前不做的事

- 不新增未经核实的“实测数据”。
- 不把 1-5 分评分包装成 GIS / 水文 / 交通实测。
- 不继续扩大案例库到 20 个以上。
- 不提出大拆防洪墙、遗迹深挖、全年固定低位商业等高风险方案。

