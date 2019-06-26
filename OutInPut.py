import math
s = 'Hello World'
strstr = str(s)
reprstr = repr(s)
print(strstr)
print(reprstr)
x = 10 * 3.15
y = 200 * 200
s = 'x的值为：'+repr(x)+', y的值为：'+repr(y)+'....'
print(s)
hello = 'Hello World\n'
print(repr(hello))
for x in range(1, 11):
    print('{0:2d},{1:3d},{2:4d}'.format(x, x*x, x*x*x))
s = '12'.zfill(5)
print(s)
print('{1}和{0}'.format('Google','Tencent'))
print('常量PI近似值：{0:.3f}'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'TaoTao': 3}
for name, number in table.items():
    print('{0:10}==>{1:10d}'.format(name ,number))


print('Runoob:{0[Runoob]:d}; Google:{0[Google]:d}; TaoTao:{0[TaoTao]:d}'.format(table))
