# -*- coding:utf-8 -*-
import time,get_server_time,main_test,py_sql
import sys
import os
import time_point_read

# club_qita=[['00:45','02:45','04:45','06:45'],['08:45','10:45','12:45','14:45'],['16:45','18:45','20:45','22:45']]
# club_banzhang=[['01:45','03:45','05:45','07:10'],['09:45','11:45','13:45','15:10'],['17:45','19:45','21:45','23:10'],]
club_qita,club_banzhang=time_point_read.read_time_point()

day_list=['','夜班','白班','中班',]
ban_list=[[0,0,1,2,3],[2,3,0,0,1],[1,2,3,0,0],[0,1,2,3,0],[3,0,0,1,2]]
constant=86400
time_Rest=57600
#判断当前时间是否超过某个输入的时间
def change_2_stamp(date):
	time_stamp=time.mktime(time.strptime(date,"%Y-%m-%d %H:%M:%S"))
	return time_stamp
def get_date(date):
	current_date=time.strftime("%Y-%m-%d",time.localtime(date))
	time_stamp=time.mktime(time.strptime(current_date,"%Y-%m-%d"))
	#print(time_stamp)
	out_num=int(int(time_stamp-time_Rest)/constant)%5

	return int(out_num)
def get_time(date):
	current_time=time.strftime("%H:%M:%S",time.localtime(date))
	return current_time
def read_file(path_name):
	with open(path_name,'r') as fn:
		read_tp=fn.read()
	return read_tp
def data_judge(num,date,path_file):
	print(num,date.split(' ')[0],path_file)
	
	mat=main_test.operator_sys()
	if os.path.isdir(path_file):
		file_list=os.listdir(path_file)
		for i in file_list:
			# add_id=[]
			print(('read file'),i.split('.')[0],': ')
			temp=read_file(path_file+mat+i).split('#')[0].split(',')
			flag=read_file(path_file+mat+i).split('#')[2]
			if flag=='0':
				club_flag=club_qita
			elif flag=='1':
				club_flag=club_banzhang
			for j in temp:
				for i in club_flag[num-1]:
					add_id_ad=[]	
					dtime=date.split(' ')[0]+' '+i+':00'
					add_id_ad.append(j)
					add_id_ad.append(dtime)
					if py_sql.sql_query(add_id_ad) == False:
						return False

				
	elif os.path.isfile(path_file):
		print('read file:',path_file)
		temp2=read_file(path_file).split('#')[0].split(',')
		flag=read_file(path_file+mat+i).split('#')[2]
		if flag=='0':
			club_flag=club_qita
		elif flag=='1':
			club_flag=club_banzhang
		for j in temp2:
			for i in club_flag[num-1]:
				add_id_ad=[]	
				dtime=date.split(' ')[0]+' '+i+':00'
				add_id_ad.append(j)
				add_id_ad.append(dtime)
				if py_sql.sql_query(add_id_ad) == False:
					return False


	# pass

#将日期转化为时间戳
def select_day(bc,date,path_file):
	time_stamp=change_2_stamp(date)
	num=get_date(time_stamp)
	# print(num)
	# print(ban_list[bc][num])
	# print(type(bc))
	# data_judge(ban_list[bc][num],date,path_file)
	if ban_list[bc][num] == 3 and "23:20:00" < get_time(time_stamp) < "23:59:59" :
		print('this is:',day_list[ban_list[bc][num]],date,'time is ok!')
		if data_judge(ban_list[bc][num],date,path_file) == False:
			main_test.auto_run(path_file,ban_list[bc][num]-1)
		else:
			print('complete!')
	elif ban_list[bc][num] == 1 and "07:55:00" < get_time(time_stamp) < "08:30:00":
		print('this is:',day_list[ban_list[bc][num]],date,'time is ok!')
		if data_judge(ban_list[bc][num],date,path_file) == False:
			main_test.auto_run(path_file,ban_list[bc][num]-1)
		else:
			print('complete!')

	elif ban_list[bc][num] == 2 and "15:20:00" < get_time(time_stamp) < "16:00:00":
		print('this is:',day_list[ban_list[bc][num]],date,'time is ok!')
		if data_judge(ban_list[bc][num],date,path_file) == False:
			main_test.auto_run(path_file,ban_list[bc][num]-1)
		else:
			print('complete!')
	else:
		print('还没到工作时间！请稍后！')
if __name__ == '__main__':
	# for i in buf_list:
	# 	select_day(i)
	cur_time=get_server_time.get_time_url()
	# print(cur_time)
	select_day(0,cur_time,'聚丙烯')
	# select_day(0,'2019-03-20 08:05:14','聚丙烯')


# P8iT@Ore0#