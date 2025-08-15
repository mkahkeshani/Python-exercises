# یک لیست بسازید و بزرگترین عدد موجود در لیست را در خروجی نمایش دهید
# از کتابخانه و توابع آماده نمیتوانید استفاده کنید

nums = [3, 15, 7, 0, -2, 99, 42]

largest = nums[0]

for i in nums:
    if i > largest:
        largest = i
print(f'the largest number is: {largest}')