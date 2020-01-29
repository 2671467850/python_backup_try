import os
import time

source = ['F:\\hello', 'F:\\world']
target_dir = 'F:\\Backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)
now = time.strftime('%H%M%S')
comment = input('Enter a comment ==> ')
if len(comment) == 0:
    backup = today + os.sep + now + '.zip'
else:
    backup = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'
zip_command = 'zip -r {0} {1}'.format(backup,
                                      ' '.join(source))
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', backup)
else:
    print('Backup FAILED')