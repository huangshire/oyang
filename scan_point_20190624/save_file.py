#this is input infomation to file save.
def save_file(name,data):
	with open(name,'w') as fn:
		fn.write(data)
def read_file(name):
	with open(name,'r') as fn:
		temp=fn.read()
	#print(temp)
	for i in temp.split('#'):
		print(i)
def Prompt(file_name):
	NiuHao=input('Please input you want save nh data:(use "," separator)')
	Banghao=input('Please input you want save bh data:')
	TimePoint=input('Please input you want save TimePoint:')
	save_file(file_name+'.txt',NiuHao+'#'+Banghao+'#'+TimePoint)
	read_file(file_name+'.txt')
if __name__ == '__main__':
	file_name='info'
	Prompt(file_name)