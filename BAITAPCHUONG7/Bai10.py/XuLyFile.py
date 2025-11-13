def LuuFileJSON(tenFile, data):
    import json
    with open(tenFile, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def DocFileJSON(tenFile):
    import json
    with open(tenFile, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data