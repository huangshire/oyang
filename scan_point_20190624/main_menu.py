import main_test,read_file,save_file,auto_time_select,get_server_time
import encryption_test
import os,sys,time
import get_usb_id
def MainMenu():
	print("""
                    ******************* The system menu *****************
                    *                                                        
                    *                                                       
                    *   1.input infomation                                
                    *   2.set running infomation	                        
                    *   3.run                                                
                    *   4.infomation read                                 
                    *   5.run data input                                   
                    *   6.quit                                               
                    *                                                        
                    ******************************************************
                    *                                                       
                    *   Please input you select num.                   
                    ******************************************************
		""")
	num=input('>>>:')
	return num
def create_path(path_name):
	if os.path.exists(path_name) is False:
		os.mkdir(path_name)
def auto_run_file_read():
	# with open('auto_run.txt','r',encoding='ISO-8859-1') as fn: #window读取目录是乱码 
	# with open('auto_run.txt','r') as fn: # 此处windows下读取目录正常
	# 	read_date=fn.read()
	read_date=encryption_test.read_file('auto_run.txt')
	auto_run=[]
	if '\n' in read_date:
		auto_temp=read_date.split('\n')
		for i in auto_temp:
			auto_run.append(i.split('#'))

	else:
		auto_run.append(read_date.split('#'))
	return auto_run
def save_infomation():
	server=input('Please input server IP:')
	user=input('Please input user name:')
	password=input('Please input password:')
	datebase=input('Please input datebase name:')
	buf_date=server+'\n'+user+'\n'+password+'\n'+datebase
	encryption_test.save_file('infomation.zlj',buf_date)
def auto_run_save():
	#多项数据传输项目的添加保存
	data=''
	while True:
		path_name=input("Please input auto_run path:")
		auto_run_flag=input("Please input run flag:")
		Name_of_team=input("Please input Name_of_team:")
		data=data+path_name+'#'+auto_run_flag+'#'+Name_of_team
		select_yes_no=input('Whether to save exit?(y/n)')
		if select_yes_no == 'Y' or select_yes_no=='y':
			data=data+'\n'
		elif select_yes_no == 'N' or select_yes_no=='n':
			break
	encryption_test.save_file('auto_run.txt',data)
def auto_run():
	#实现多项输入内容的读取，及间断查询读取上传
	run_temp=auto_run_file_read()
	while True:
		for auto_run_temp in run_temp:
			if auto_run_temp[1]=='auto':
				current_time=get_server_time.get_time_url()
				print(current_time)
				auto_time_select.select_day(int(auto_run_temp[2])-1,current_time,auto_run_temp[0])
			else:
				print('display %s'%(auto_run_temp[1]))
		time.sleep(1200)
def select_menu():
	while True:
		num_str=MainMenu()
		if num_str == '1':
			path_name=input('Please input project path name:')
			create_path(path_name)
			filename=input('Please input project file name:')
			mat=main_test.operator_sys()
			path_file_name=path_name+mat+filename
			save_file.Prompt(path_file_name)

		elif num_str == '2':
			print('2.this is run file set：')
			save_infomation()
		elif num_str == '3':
			print('3.run program.')
			main_test.main()

		elif num_str == '4':
			print('4.read file:')
			read_name=input('Please input file name:')
			print(encryption_test.read_file(read_name))
		elif num_str == '5':
			print('5.input data run program.')
			auto_run_save()
		elif num_str == '6':
			return num_str
			break
		else:
			print('input error')


def main():
	flag=0
	while True:
		if len(sys.argv)==3 and flag == 0:
			main_test.main()
			#print('sys.arge==3')
			flag=1
		
		elif len(sys.argv)==2 and sys.argv[1]=='auto':
			auto_run()

		elif  os.path.isfile('auto_run.txt'):
			auto_run_temp=encryption_test.read_file('auto_run.txt')
			print(auto_run_temp)
			if "auto" in auto_run_temp:
				select=input('want to auto_run input "y",input ESC to quit.')
				if select=='y' or select == 'Y':
					auto_run()
				elif select=='ESC' or select == "esc":
					break
		#select_menu()	
		askm=select_menu()
		if askm == '6':
			select_info=input('Are you sure you want to quit?(y/n)')
			if select_info == 'y' or select_info == 'Y':
				break
			else:
				continue
if __name__ == '__main__':
	if get_usb_id.get_disk_info()=='FEB21860A180':
		main()
	else:
		print('你进行了错误的操作！')

"""
author:.ByCow
modification date:2019.04.15
Edition:1.0.5
Modify content：
增加功能：可执行多时段，多岗位，数据查询及上传。
		多项自动输入内容的录入
"""