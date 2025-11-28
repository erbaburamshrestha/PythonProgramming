def minimumNumberOfOperation(number):
        lengthNumber = len(number)
        number= sorted(set(number))
        l = 0
        for i, num in enumerate(number):
            if number[l] + lengthNumber - 1 < num:
                l += 1
        return lengthNumber - (len(nums) - l)

nums = [1,2,3,5,6]
print(minimumNumberOfOperation(nums))