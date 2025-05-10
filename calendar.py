# 用python写日历
# y:年，m:月，d:日
# 计算星期几的公式

def get_week_with_data(y,m,d):
    # if m == 1:
    #     y-=1
    #     m = 13
    # elif m == 2:
    #         y -= 1
    #         m = 14
    if m ==1 or m == 2:
        y-=1
        m+=12
    # print(f'Today is {w}')
    return (d + 2*m + 3*(m+1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1

def is_leap_year(y):
    """ 判断一个年份是否是闰年 """
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0): # 判断是否闰年（2月29天）
        return True
    return False
def get_days_in_month(y,m):
    """ 获取指定年月的天数 """
    if m in [1, 3, 5, 7, 9, 11]:
        return 31
    elif m in [4, 6, 8, 10, 12]:
        return 30
    else:
        return 29 if is_leap_year(y) else 28

'''1. 提示用户输入年份和月份'''
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
# year = 2019; month = 2

'''2. 计算这个月有多少天'''
days =  get_days_in_month(year, month)

'''3. 按照指定格式显示日期'''
print("W1 W2 W3 W4 W5 W6 W7")
print('-' * 20)
for i in range(1,days+1,1):
    ''' 输出这个月的天数列表 '''
    w = get_week_with_data(year,month,i)
    if i==1:
        # 一 0
        # 二 3
        print(f"{' '*(w-1)*3}", end ='')
    else:
        if w == 1:
            print('')
    print(f"{i:2d}",end=' ')
print()
# 输出函数名、文档注释的小功能
# print(is_leap_year.__name__)
# print(is_leap_year.__doc__)

