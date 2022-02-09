class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, (len(numbers)-1)
        
        while l < (len(numbers)-1):
            total = numbers[l] + numbers[r]

            if total > target:
                r-=1

            elif total < target: 
                l+=1

            else:
                return[l+1, r+1]
            
        return[]
    
print(Solution().twoSum([1,2,3,4,5,9], 10))
