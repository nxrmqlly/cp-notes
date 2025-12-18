test_arr = [2, 1, 5, 4, 3, 0, 0]


def next_permutation(arr: list[int]) -> list[int]:

    breakpoint = -1
    # find the first pair where left < right from end
    for i in range(len(arr) - 2, 0, -1):
        left, right = arr[i], arr[i + 1]

        if right > left:
            breakpoint = i
            break

    if breakpoint == -1:
        return arr[::-1]

    # find the first element larger than arr[breakpoint] from end
    # its already sorted in descending order
    for i in range(len(arr) - 1, breakpoint, -1):
        if arr[i] > arr[breakpoint]:
            # this works as the rest of the arr is in descending order
            arr[breakpoint], arr[i] = arr[i], arr[breakpoint]
            break

    return arr[: breakpoint + 1] + arr[breakpoint + 1 :][::-1]


print(next_permutation(test_arr))
