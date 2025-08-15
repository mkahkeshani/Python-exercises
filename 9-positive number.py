# برنامه ای بنویسید که عددی از کاربر بگیرد و و مشخص کند که
# آن عدد مثبت است یا منفی است یا صفر

input = int(input('enter a number: '))

if input > 0:
    print('positive')
elif input < 0:
    print('negative')
else:
    print('zero')