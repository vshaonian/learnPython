# -*- coding: utf-8 -*-




import math
def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

a = int(input('请输入a：'))
if not isinstance(a, (int, float)):
    raise TypeError('只能输入整数或小数')
b = int(input('请输入b：'))
if not isinstance(b, (int, float)):
    raise TypeError('只能输入整数或小数')
c = int(input('请输入c：'))
if not isinstance(c, (int, float)):
    raise TypeError('只能输入整数或小数')

if b*b-4*a*c < 0:
    print('该方程无解')
elif b*b-4*a*c == 0:
    print('该方程仅有一个解：',quadratic(a,b,c))
else:
    print('该方程的两个解为：',quadratic(a,b,c))