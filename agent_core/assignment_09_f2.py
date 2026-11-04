def check_status(count):
    if count >= 3:
        return "추가 확인"
    else:
        return "기록 유지"

print(check_status(2))
print(check_status(3))