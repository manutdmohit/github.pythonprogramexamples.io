f1=open('py.jpeg','rb')
data=f1.read()
f2=open('udemypy.jpeg','wb')
f2.write(data)
print('udemypy.jpeg is ready')
f1.close()
f2.close()