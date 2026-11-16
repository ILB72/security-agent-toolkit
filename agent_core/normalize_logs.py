import re
import json

PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"

def parse_raw_logs(line):
    m = re.search(PATTERN, line)
    if m:
        return m.groupdict()
    return None

rows = []
unmatched = []

with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line: continue
        row = parse_raw_logs(line)
        if row:
            rows.append(row)
        else:
            unmatched.append(line)

with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    for line in unmatched:
        f.write(line + "\n")

print(f"정규화 {len(rows)}건")
print(f"안 맞음 {len(unmatched)}건")