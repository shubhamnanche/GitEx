from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, curNums, sum):
            if len(curNums) == 4 and sum == target:
                res.append(curNums[:])
                print("matched >", res)
                return

            for i in range(start, len(nums)):
                print(
                    "loop > ",
                    i,
                    "start > ",
                    start,
                    "curNums > ",
                    curNums,
                    "sum > ",
                    sum,
                )
                if i > start and nums[i] == nums[i - 1]:
                    print("i > start and nums[i] == nums[i - 1] continue...")
                    continue
                if len(curNums) == 4:
                    print("len(curNums) == 4 breaking...")
                    break
                if sum + nums[i] > target:
                    print("sum + nums[i] > target breaking...")
                    break
                curNums.append(nums[i])
                sum += nums[i]
                backtrack(i + 1, curNums, sum)
                value = curNums.pop()
                sum -= value

        backtrack(0, [], 0)
        return res


sol = Solution()
arr = [1, 2, 3, -2, 0, 2, 4, 5, 1, -3, 7]
arr.sort()
print(arr)
print(sol.fourSum(arr, 11))
