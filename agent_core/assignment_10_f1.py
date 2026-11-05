def filter_over_three(values):
    result = []
    for v in values:
        if v >= 3:
            result.append(v)
    return result

print(filter_over_three([0, 4, 2, 5]))
print(filter_over_three([]))