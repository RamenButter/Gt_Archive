import os

from os import listdir
from os.path import isfile, join


path="C:\\Users\\kingc\\Documents\\GitHub\\Gt_Archive\\archiveactive\\FOJ"

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for x in range(1,len(onlyfiles)):
	onlyfiles[x]="<a href="+path+"\\"+onlyfiles[x]+">Link "+str(x)+"</a>"

print(onlyfiles)