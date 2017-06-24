#！usr/bin/env python
#-*-coding:utf-8-*-
# Author calmyan

import configparser
import os ,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取相对路径转为绝对路径赋于变量
sys.path.append(BASE_DIR)#增加环境变量

AUTH_FILE='%s/db/'%BASE_DIR#主机组 信息用户名密码文件路径
FILE_DIR='%s/put_file'%BASE_DIR#要上传文件所在的目录
GET_FILE_DIR='%s/get_file'%BASE_DIR#要上传文件所在的目录
#print(AUTH_FILE)
PWD='pwd'#密码
USER='user'
PORTS='ports'
INST_LIST=['put','get']#指令列表

PUT='put'
GET='get'