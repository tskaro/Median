my_list = [1, 2, 3, 4, 5, 6]


def median(data):
    n = len(data)
    data.sort()

    if n % 2 == 0:
        median1 = data[n // 2]
        median2 = data[n // 2 - 1]
        med = (median1 + median2) / 2
    else:
        med = data[n // 2]
    return f"Median for your list is: {str(med)}"


print(median(my_list))
