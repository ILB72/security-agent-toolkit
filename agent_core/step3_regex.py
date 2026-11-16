import re, json
from collections import Counter

line = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"

print("3-1 결과:", re.search(r"from [\d.]+", line).group())
print("3-2 결과:", re.search(r"for [\w.]+", line).group())

print("\n[파일 전체 IP 찾기]")
with open("raw_logs.txt", encoding="utf-8") as f:
    for l in f:  
        print(re.findall(r"from [\d.]+", l.strip()))


PATTERN = r"[\d-]+ (?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"
m = re.search(PATTERN, line)
print("\n3-4 결과:", m.group("ip"))
print("3-5 결과:", m.groupdict())

print("\n[파일 정규화]")
rows = []
with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:  
        m = re.search(PATTERN, line.strip())
        if m:
            rows.append(m.groupdict())
print(f"정규화 {len(rows)}건")

users = [row["user"] for row in rows]
print("\n[도전 3-7]", dict(Counter(users)))

users = ["admin", "kim01", "admin"]
count = {}
for name in users:
    count[name] = count.get(name, 0) + 1
print("4-3 결과:", count)

fail_count = {}
for row in rows:
    if row["level"] == "WARN":
        fail_count[row["user"]] = fail_count.get(row["user"], 0) + 1
print("4-4 결과:", fail_count)

THRESHOLD = 3
print("\n[룰 1]")
for user, cnt in fail_count.items():
    if cnt >= THRESHOLD:
        print(f"확인 필요: {user} — 실패 {cnt}회")

ip_users = {}
for row in rows:
    ip, user = row["ip"], row["user"]
    if ip not in ip_users:
        ip_users[ip] = []
    if user not in ip_users[ip]:
        ip_users[ip].append(user)
print("\n4-7 결과:", ip_users)

print("\n[룰 2]")
for ip, users in ip_users.items():
    if len(users) >= 2:
        print(f"의심 IP: {ip} — 계정 {len(users)}개 시도")