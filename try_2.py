import os
import time

# 需要备份的目录
source = ['F:\\hello', 'F:\\world']

# 备份保存的目录
target_dir = 'F:\\Backup'

# 如果保存目录不存在,创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 一个以日期命名的文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')

# 如果日期文件夹不存在,创建
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 当前时间的zip文件名
now = time.strftime('%H%M%S')

# 备份文件保存位置和命名
backup = today + os.sep + now + '.zip'

# zip命令将文件打包
# 注意在zip命令中加入空格,不可缺少
zip_command = 'zip -r {0} {1}'.format(backup, ' '.join(source))

# 脚本运行
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', backup)
else:
    print('Backuo FAILED')