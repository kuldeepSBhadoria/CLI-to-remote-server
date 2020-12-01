#Written by Kuldeep
#10/07/2020 
#Version : 1.2

import subprocess
import paramiko
import sys
import platform
import time
import glob
import math
from datetime import datetime
import os

l_host_ip=['W1-05','W1-06','W2-01','W2-02','W2-03','W2-04','W2-05','W2-06']


#l_bmc_ip =['10.0.128.159','10.0.128.159','10.0.128.159','10.0.128.159', '10.0.128.157','10.0.128.157','10.0.128.157','10.0.128.157', '10.0.128.158','10.0.128.158','10.0.128.158','10.0.128.158', '10.0.128.160','10.0.128.160','10.0.128.160','10.0.128.160', '10.0.128.161','10.0.128.161','10.0.128.161','10.0.128.161', '10.0.128.162','10.0.128.162','10.0.128.162','10.0.128.162',]

list_nvme="nvme list"

host_name= 'hostname'


def run_command(HOST, COMMAND):
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
    try:
       p.connect(HOST, port=22, username="root", password="xxxx")
       stdin, stdout, stderr = p.exec_command(COMMAND, timeout=10)
    except:
       print('oops  ...................')

    opt = stdout.readlines()
    opt = "".join(opt)
    p.close()
    return opt
    	
	
if __name__ == '__main__':
    length = len(l_host_ip)
    for i in range(length):
        print(" \n --#############################################-----")
        #print('HostIP is   :'+ l_host_ip[i] )
        try:
            result_c = run_command(l_host_ip[i], host_name)
            print ('Hostname is :' + result_c)
            result_c = run_command(l_host_ip[i], list_nvme)
            print ('nvme_list is :' + result_c)
        except:
            print(" -----xxxxxxx-------")   
            
        
