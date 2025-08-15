# سه عدد از کاربر دریافت کنید و با استفاده از شرط بزرگتیرن آنها 
# را مشخص کنید

a = int(input('first number: '))
b = int(input('second number: '))
c = int(input('third number: '))

if a >=b and a >= c:
    largest  = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
    
print(f'largest is: {largest}')