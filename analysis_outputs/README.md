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

## 追加矩阵图表

7. `charts/07_diagnosis_strategy_matrix.svg`  
   诊断-策略矩阵，将 issue、evidence、segment、response 和 drawing output 对齐。

8. `charts/08_material_suitability_matrix.svg`  
   材料适宜性矩阵，按可逆性、耐洪水、维护、遗产兼容和热舒适评分。

9. `charts/09_data_gap_priority.svg`  
   数据缺口优先级图，标出必须通过官方资料、现场或人工判断补齐的内容。

## 生态、水文生物与人-生物互动图表

10. `charts/10_ecology_benchmark_matrix.svg`  
    生态保护评价基准矩阵，包含本地河岸植物比例、洪水恢复力、生境复杂度、干扰控制、水体边缘质量、维护平衡、入侵风险和树冠遮阴等指标。

11. `charts/11_flood_regeneration_strategy.svg`  
    洪水影响与植被再生策略图，用于表达低位河岸“可淹没、可冲刷、可恢复”的植物和材料逻辑。

12. `charts/12_human_bio_interaction_matrix.svg`  
    人类活动与生物干扰控制矩阵，覆盖观鸟、儿童自然教育、遛狗、夜间使用、摄影停留和维护。

13. `charts/13_segment_ecology_goals.svg`  
    S1-S5 分段生态目标图，将种植结构、水文生物解释和优先级对应到空间段落。
