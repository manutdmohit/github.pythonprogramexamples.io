n=int(input('Enter no of students:'))
d={}
for i in range(n):
	name=input('Enter Student Name:')
	marks=input('Enter Student Marks:')
	d[name]=marks
print('Student data insertion method completed')
print('*'*30)
print('NAME','\t\t','MARKS')
print('*'*30)
for k,v in d.items():
	print(k,'\t\t',v)
print('Search operation started....')
while(True):
	name=input('Enter student name:')
	marks=d.get(name,-1)
	if marks==-1:
		print('Student not found')
	else:
		print('Marks of',name,'are',marks)
	option=input('Do you want to find another Student Marks[yes/no]:')
	if option.lower()=='no':
		break
print('Thanks for using our application')



