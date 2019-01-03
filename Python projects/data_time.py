from datetime import datetime
import glob2

delta=datetime.now()- datetime(2018,11,18,01,12,34)

print delta.days

a=[1,2,3]
b=['a','c','d']
from datetime import datetime

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")

for a, b in zip(a,b):
    print("{} is {}").format(a,b)
"""with statement takes cae of closing the file"""
with open('example.txt','w')as my:
    my.write('hurraaay')
