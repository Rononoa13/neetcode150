nums = [1,2,3,1]
# Create hashset to store elements from the array
seen = set()

# Iterate through array
for num in nums:
    # check if item is already in set
    if num in seen:
        print("True")
    seen.add(num)