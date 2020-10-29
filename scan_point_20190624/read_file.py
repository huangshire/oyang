import os

def read_info(name):
	nh_list=[]
	try:
		with open(name,'r') as fn:
			read_temp=fn.read()
		nh_list=read_temp.split('#')[0].split(',')
		bh=read_temp.split('#')[1]
		shux=read_temp.split('#')[2]
		return nh_list,bh,shux
	except Exception as e:
		print('ERROR:',e)
	
	return 'the file Non-existent!'
if __name__ == '__main__':
	name='挤压.txt'
	print(read_info(name))