def insertion_sort(nums):
    for i in range(1, len(nums)):
        n = nums[i]
        j = 0
        for j in range(i - 1, -1, -1):
            if n <= nums[j]:
                nums[j + 1] = nums[j]
            else:
                j += 1
                break
        nums[j] = n


if __name__ == '__main__':
    import Test
    import random

    nums = list(range(100))
    random.shuffle(nums)
    sorted_nums = sorted(nums)
    insertion_sort(nums)
    Test.equal(sorted_nums, nums)
