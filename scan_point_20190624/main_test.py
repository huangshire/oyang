import read_file,save_file,random_time,py_sql
import sys
import os

#命令行模式直接输入要传输的数据　时间节点

# file_name=sys.argv[1]
# banci=sys.argv[2]

def operator_sys():
	if os.name=='nt':
		print('windows')
		return '\\'
	elif os.name=='posix':
		print('Linux or Mac')
		return '/'
	else:
		print('Other system')

def integrated_data(file_name,banci):
	nh_list,bh,shux=read_file.read_info(file_name)
	# print(nh_list,bh,shux)
	coeff=len(nh_list)
	# print(coeff)
	time_list=random_time.out_info(int(banci),shux,coeff)
	temp_list=[]

	for i in range(0,len(time_list),2):
		yxsj=time_list[i]
		xjsj_list=time_list[i+1]
		
		for j in range(len(nh_list)):
			temp=[]
			temp.append(nh_list[j])
			temp.append(xjsj_list[j])
			temp.append(bh)
			temp.append(yxsj)
			temp_list.append(temp)
	# print(temp_list)

	##打印整合好的数据
	# if len(temp_list)<5:
	# 	temp_list[0][3]=0
	# 	print(temp_list[0])
	# else:
	# 	for i in temp_list:
	# 		print(i)


	#对整合的数据进行发送
	
	if len(temp_list)<5:
		print('>>>'*2)
		temp_list[0][3]=0
		#print('>>>'*2)
		print(temp_list[0])
		py_sql.main(temp_list[0])
	else:
		print('>>>'*2)
		for a in temp_list:
			#print('>>>'*2)
			print(a)
			py_sql.main(a)

def auto_run(file_name,banci):
	mat=operator_sys()
	print(mat)
	if os.path.isdir(file_name):
		file_list=os.listdir(file_name)
		for i in file_list:
			print(('read file'),i.split('.')[0],': ')
			integrated_data(file_name+mat+i,banci)
	elif os.path.isfile(file_name):
		print('read file:',file_name)
		integrated_data(file_name,banci)

def main():

	if len(sys.argv)==3:
		print(len(sys.argv))
		file_name=sys.argv[1]
		banci=sys.argv[2]
		auto_run(file_name,banci)
	else:
		banci=input("Please input banci:")
		path=input("Please input data path:")
		auto_run(path,banci)


if __name__ == '__main__':

	main()