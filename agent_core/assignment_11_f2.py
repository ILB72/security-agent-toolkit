import json

with open("gichan_input.json", encoding="utf-8") as f:
    data = json.load(f)

total = len(data)
fail_count = 0

for item in data:
    if item["result"] == "FAIL":
        fail_count += 1

summary_text = f"전체 {total}건, 실패 {fail_count}건"

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)