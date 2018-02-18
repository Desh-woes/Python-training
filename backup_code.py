import os
import time

# 1. The files and directories to be backed up are specified in a list.
#The problem is on line 6. I cannot use this directory. But I can save from my main dir
source = [r'C:\Users\ALU STUDENT\Desktop\Python-training']
target_dir = 'D:\Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
