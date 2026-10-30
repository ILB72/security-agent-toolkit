values = ["2", "bad", "3"]
total = 0

for value in values:
    try:
        total += int(value)
    except ValueError:
        print(f"건너뜀 {value}")

print(f"합계 {total}")