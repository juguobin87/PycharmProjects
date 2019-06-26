import pickle
import pprint
f = open("C:/Users/juguobin/Desktop/pythonfile.txt","w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好！！\n")
f.close()

f = open("C:/Users/juguobin/Desktop/pythonfile.txt","r")
#str  = f.read()
#strreadline  = f.readline()
strreadlines = f.readlines()
#print(str)
#print(strreadline)
print(strreadlines)
f.close()

data1 = {'a':[1,2.0,3,4+6j],'b':('string',u'Unicode string'),'c':None}
selfref_list=[1,2,3]
selfref_list.append(selfref_list)
output = open('data.pk1','wb')
pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()