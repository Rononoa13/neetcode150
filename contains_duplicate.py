nums = [1,2,3,1]
duplicate_test = []
for num in nums:
    if num in duplicate_test:
        print(True)
    duplicate_test.append(num)