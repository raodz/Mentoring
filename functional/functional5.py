nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
lst = [nums1, nums2, nums3]

sums = list(map(lambda *x: sum(x), *lst))
sum_of_lists = sum(sums)
print(sum_of_lists)
