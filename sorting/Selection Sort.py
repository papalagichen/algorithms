def selection_sort(nums):
    for i in range(len(nums)):
        m = i
        for j in range(i + 1, len(nums)):
            if nums[m] > nums[j]:
                m = j
        nums[m], nums[i] = nums[i], nums[m]


if __name__ == '__main__':
    import Test
    import random

    nums = list(range(100))
    random.shuffle(nums)
    sorted_nums = sorted(nums)
    selection_sort(nums)
    Test.equal(sorted_nums, nums)
