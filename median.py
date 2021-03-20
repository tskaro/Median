list = [1, 2, 3, 4, 5, 6]

def median(list):
    n = len(list)
    list.sort()

    if n % 2 == 0:
        median1 = list[n // 2]
        median2 = list[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list[n // 2]
    return f"Median for your list is: {str(median)}"

print(median(list))
