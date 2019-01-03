x=10
y=9

import os
print os.getcwd()
import glob

os.chdir('C:\Users\siaher\Desktop')
# print os.getcwd()
# print os.listdir('C:\Users\siaher\Desktop')
# os.mkdir('hey.text')

list_of_files = glob.glob('C:/Users/siaher/Desktop/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print latest_file

print os.listdir('C:/Users/siaher/Desktop')

if(x>y):
    os.rmdir('hey.text')
    print 'File succesfully removed'
print os.listdir('C:/Users/siaher/Desktop')