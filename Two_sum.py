nums = [1,3,44,6,7] 
target = 50
a_dict = {}
for i in range (0, len(nums)): 
    if (target-nums[i]) in a_dict:
        print (a_dict[target- nums[i]], i)
    else:
        a_dict[nums[i]] = i

