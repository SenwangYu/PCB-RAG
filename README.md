
## `footprints_index.json`

封装索引文件，结构大致如下：

```json
{
  "Battery": [
    "BatteryHolder_Keystone_1057_1x2032",
    "BatteryHolder_Keystone_1058_1x2032"
  ],
  "Package_SO": [
    "SOIC-8_3.9x4.9mm_P1.27mm",
    "SOP-8_3.9x4.9mm_P1.27mm"
  ]
}
```

含义：

- key：封装库名称
- value：该库下的封装名列表

## `structured_qa_testset.json`

结构化测试集样例，特点如下：

- 共 20 条测试样例
- 每题都包含 `query`
- 每题都包含多个可接受答案 `acceptable_footprints`
- 所有可接受答案都严格来自 `footprints_index.json`

结构如下：

```json
{
  "dataset_description": "...",
  "total_components": 20,
  "answer_policy": "...",
  "test_cases": [
    {
      "id": 1,
      "component_info": {
        "model": "...",
        "category": "...",
        "description": "..."
      },
      "retrieval_task": {
        "query": "...",
        "acceptable_footprints": ["...", "..."],
        "evaluation_criteria": "..."
      }
    }
  ]
}
```
## 辅助脚本：

- [footprints.py](/c:/Users/huang/Desktop/结构化测试集/footprints.py:1)
  - 用于从 KiCad `footprints` 目录扫描并生成封装索引

## 结构化检索函数
参考的检索工具示例：query_footprint_library.py
