
line1 = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"
line2 = "2026-09-29 23:40:07 WARN failed login for invalid user guest from 185.220.101.34"

print("2-1 결과:", line1.split()[6]) 
print("2-2 결과:", line2.split()[6])  


print("2-3 결과:", len(line1.split()), len(line2.split())) 


print("2-4 결과:", line1.split()[len(line1.split())-1], line2.split()[len(line2.split())-1])


print("\n[2-5 파일의 6번 칸]")
with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) > 6:
            print(parts[6])


print("\n[도전 2-6: 9칸이 아닌 줄]")
with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        if len(line.strip().split()) != 9:
            print(line.strip())


warn_count = 0
with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        if "WARN" in line:
            warn_count += 1
print(f"\n[도전 2-7] WARN {warn_count}줄")