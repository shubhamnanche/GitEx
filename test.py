from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curNums, sum):
            if len(curNums) == 4 and sum == target:
                res.append(curNums[:])
                print("matched >", res)
                return

            for i in range(len(nums)):
                if len(curNums) == 4:
                    # print("len(curNums) == 4 breaking...")
                    break
                if sum + nums[i] > target:
                    # print("sum + nums[i] > target breaking...")
                    break
                curNums.append(nums[i])
                sum += nums[i]
                backtrack(i + 1, curNums, sum)
                value = curNums.pop()
                sum -= value

        backtrack([], 0)
        return res
    
sol = Solution()
print(sol.fourSum([1,-2,-5,-4,-3,3,3,5],-11))