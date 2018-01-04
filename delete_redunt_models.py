import glob
import re
import os

all_model = dict()
files = glob.glob('models/ResNet/*/*')
for ifile in files:
#    print ifile
    a=re.match(r'(.*)iter_(\d*).[caffemodel|solverstate]',ifile,re.M|re.I)
    if a:
        key=a.group(1)
        num=int(a.group(2))
        if not all_model.has_key(key):
            all_model[key] = num 
        else:
            all_model[key] = num if all_model[key]< num else all_model[key]
print all_model

for ifile in files:
    a=re.match(r'(.*)iter_(\d*).[caffemodel|solverstate]',ifile,re.M|re.I)
    if a:
        key=a.group(1)
        num=int(a.group(2))
        if all_model.has_key(key):
#            all_model[key] = num if all_model[key]< num else all_model[key]
            if all_model[key] != num:
                os.system('rm -v '+ ifile)
    
