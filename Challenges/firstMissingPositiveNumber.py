class FirstMissingPositive:
    def firstMissingPositive(self,nums):
        self.nums=nums
        self.nums.sort()
        while self.nums[0] < 1:
            del self.nums[0]
            if not self.nums:
                return 1

        self.current = self.nums[0]
        self.lengthNums = len(nums)
        self.count = 1
        while self.count < self.lengthNums:
            if self.nums[self.count] == self.current:
                del nums[self.count]
                self.lengthNums = len(self.nums)
            else:
                self.current = self.nums[self.count]
                self.count += 1

        self.lengthNums = len(self.nums)
        for i in range(self.lengthNums):
            if self.nums[i] != i + 1:
                return i + 1
        return self.nums[-1] + 1
_FirstMissingPositive=FirstMissingPositive()
nums=[1,2,0]
print(_FirstMissingPositive.firstMissingPositive(nums))
nums=[3,4,-1,1]
print(_FirstMissingPositive.firstMissingPositive(nums))