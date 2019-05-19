# Problem: https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input())
print(is_leap(year))

#def is_leap(year):    
#    if year%4==0:
#        return True
#    elif year%100==0:
#        return False
#    elif year%400==0:
#        return True
