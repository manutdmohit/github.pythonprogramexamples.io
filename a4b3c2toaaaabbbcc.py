s=input('Enter some string in which alphabet symbol should be followed by digits:')
output=''
for ch in s:
	if ch.isalpha():
		x=ch
	else:
		d=int(ch)
		output=output+x*d 
print(output)