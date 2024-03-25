# 判断闰年
year = 2024   #变量year在使用前要赋值
isLeapYear = (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0)
if isLeapYear == True:
    print("闰年")
else:
    print("平年")