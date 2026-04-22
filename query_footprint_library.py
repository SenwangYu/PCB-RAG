def query_footprint_library(library_name: str,
                            limit: Optional[int] = 20,
                            offset: int = 0,
                            json_path: Optional[str] = None,
                            case_insensitive: bool = True) -> dict:
    """
    查询指定库中的封装名列表（支持分页）。
    - library_name: 库名，如 "Audio_Module"
    - limit: 每次返回个数（None 表示全部返回，不建议太大）
    - offset: 起始偏移
    - json_path: 自定义JSON文件路径，不传则使用默认路径
    - case_insensitive: 是否大小写不敏感匹配库名

    返回结构：
    {
      "library_name": "Audio_Module",
      "exists": true,
      "total": 123,
      "items": ["Reverb_BTDR-1", ...],
      "limit": 50,
      "offset": 0,
      "has_more": true
    }
    """
    index = _load_footprint_index(json_path)

    # 库名匹配（大小写不敏感）
    key = library_name
    if case_insensitive:
        mapping = {k.lower(): k for k in index.keys()}
        canonical = mapping.get(library_name.lower())
        if canonical:
            key = canonical

    items = index.get(key)
    if items is None:
        return {
            "library_name": library_name,
            "exists": False,
            "total": 0,
            "items": [],
            "limit": limit,
            "offset": offset,
            "has_more": False
        }

    total = len(items)
    start = max(0, int(offset))
    if limit is None:
        end = total
    else:
        end = min(total, start + max(1, int(limit)))

    sliced = items[start:end]
    return {
        "library_name": key,
        "exists": True,
        "total": total,
        "items": sliced,
        "limit": limit,
        "offset": start,
        "has_more": end < total
    }