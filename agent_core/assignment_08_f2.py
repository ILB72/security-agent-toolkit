import json

logs = [
    {"user": "kim01", "count": 4},
    {"user": "lee02", "count": 1}
]

# 파일로 저장 (dump)
with open("logs.json", "w", encoding="utf-8") as f:
    json.dump(logs, f)

# 파일에서 읽기 (load)
with open("logs.json", encoding="utf-8") as f:
    loaded_logs = json.load(f)

print(loaded_logs[0]["user"])