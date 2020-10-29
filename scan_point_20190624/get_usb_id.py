import os, sys
import time
import wmi



def get_disk_info():
	tmplist = []
	encrypt_str = ""
	c = wmi.WMI ()
	disk_id=None
	for physical_disk in c.Win32_DiskDrive():
		#print(physical_disk.SerialNumber.strip())
#硬盘序列号
		check_info=physical_disk.InterfaceType.strip() # 获取磁盘类型
		#print(encrypt_str)
		if check_info == 'USB':
			disk_id = physical_disk.SerialNumber.strip()
			# print ('disk id:', disk_id)
			# print('InterfaceType:',check_info)
		# else:
		# 	disk_id=None
	return disk_id
if __name__ == '__main__':
	print(get_disk_info())