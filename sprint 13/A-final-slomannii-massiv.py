def broken_search(nums, target) -> int:
    start = 0
    stop = len(nums) - 1

    while start <= stop:
        center = (start + stop) // 2
        if nums[center] == target:
            return center
        elif nums[start] <= nums[center]:
            if nums[start] <= target <= nums[center]:
                stop = center - 1
            else:
                start = center + 1
        else:
            if nums[center] <= target <= nums[stop]:
                start = center + 1
            else:
                stop = center - 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
