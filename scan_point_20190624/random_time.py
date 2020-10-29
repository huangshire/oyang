import random
import time_point_read
import get_server_time
import time
# club_qita=[['00:45','02:45','04:45','06:45'],['08:45','10:45','12:45','14:45'],['16:45','18:45','20:45','22:45']]
# club_banzhang=[['01:45','03:45','05:45','07:10'],['09:45','11:45','13:45','15:10'],['17:45','19:45','21:45','23:10'],]
club_qita,club_banzhang=time_point_read.read_time_point()
# Cycle_times=4

def select_info(num):
	if num == '0':
		return club_qita
	if num == '1':
		return club_banzhang

def Random_factor(Cycle_times):
	sum_temp=0
	if Cycle_times < 6:
		star_num=3
		stop_num=10
	elif Cycle_times >=6:
		star_num=1
		stop_num=5
	while sum_temp<16:
		
		num_list=[]
		for i in range(Cycle_times):
			num_list.append(random.randint(star_num,stop_num))
		#print(num_list)
		sum_temp=0
		for i in range(1,Cycle_times):
			sum_temp+=num_list[i]
		#print(sum_temp)
		if Cycle_times<2:
			sum_temp=0
			# print(num_list)
			break
	return num_list,sum_temp

def get_club(banci,serial_num,num,coeff):
	club_wx=select_info(num)
	# server_date_time=get_server_time.get_webservertime('http://192.168.28.143')
	# print('1',server_date_time)
	time_year=time.strftime("%Y-%m-%d", time.localtime()) #获取本机日期
	out_1=club_wx[banci][serial_num]
	out_club_1_1=[]
	random_temp,sum_temp=Random_factor(coeff)
	random_min=int(out_1.split(':')[1])
	random_hou=int(out_1.split(':')[0])
	for i in range(coeff):
		
		random_min=random_min+random_temp[i]
		if random_min > 59:
			out_club_1_1.append(time_year+" "+str("%02d"%(random_hou+1))+':'+str("%02d"%(random_min-60))+':00')
		else:
			out_club_1_1.append(time_year+" "+str("%02d"%(random_hou))+':'+str("%02d"%(random_min))+':00')
	# if coeff < 2:
	# 	print(out_club_1_1)
	return out_club_1_1,sum_temp
def out_info(Ban_Num,num,coeff):
	club_wx=select_info(num)
	time_list=[]
	for i in range(len(club_wx[Ban_Num])):
		out_list,sum_temp=get_club(Ban_Num,i,num,coeff)
		time_list.append(sum_temp)
		time_list.append(out_list)
	#print(time_list)
	return time_list
if __name__ == '__main__':
	print(out_info(0,'1',5))
