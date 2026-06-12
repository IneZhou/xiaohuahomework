# Python 初步分析图表输出说明

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
