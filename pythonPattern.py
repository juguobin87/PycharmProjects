#!/usr/bin/python
# re.match(pattern,str,flags=0)
# re.search(pattern,str,flag)
# re.sub(pattern, repl, string, count=0, flags=0)
# re.compile(pattern[, flags])
# findall(string[, pos[, endpos]])
# re.finditer(pattern, string, flags=0)
# re.split(pattern, string[, maxsplit=0, flags=0])
# m.group
# m.span
# m.start
# m.end
import re
print(re.match('www','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

line = "Cats are smaller than dogs "
searchObj = re.search(r'(.*) than (.*?).*',line,re.M|re.I)
if searchObj:
    print("searchObj.group：",searchObj.group())
    print("searchObj.group：",searchObj.group(1))
    print("searchObj.group：",searchObj.group(2))

else:
    print("Nothing Find")

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

phone="2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$',"", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)
m = pattern.match('one12twothree34four', 2, 10)
print(m)
m = pattern.match('one12twothree34four', 3, 10)
print(m)
print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

it = re.finditer(r"\d+", "12a324bc43jf3556")
for match in it:
    print(match.group())
