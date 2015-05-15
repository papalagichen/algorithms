def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == '__main__':
    import Test
    import random

    nums = list(range(100))
    random.shuffle(nums)
    sorted_nums = sorted(nums)
    bubble_sort(nums)
    Test.equal(sorted_nums, nums)
