import pandas as pd

import re

import os

from os import path
from os import listdir
from os.path import isfile, join

file_path = os.path.dirname(__file__)
if file_path != "": # Checks that the file path is not empty
    os.chdir(file_path) # Changes the working directory to the current folder

path="../archive" # Now the path to the archive can be defined as relative to this file. No more data leaks when this goes live!

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] # Gets list of files

df=pd.DataFrame(onlyfiles) # Convert file list to a dataframe

df=df[0].str.split("-", expand=True) # Split the filename into columns via the delimitter

df.drop(columns=[2], inplace=True) # Gets rid of column 2. Currently this only stores the timestamp of when the archive was taken. Might cause issues later.

urls={}

count=1

for i in onlyfiles:
    with open('../archive/'+i) as f:
        for line in f:
            
            if count < 3:
                count+=1
            else:
                g=line.strip('url: ')
                g=g[:-2]
                count=1
                break
    urls[i]=g

df.rename(columns={0: "Title", 1: "Author"}, inplace=True) # Names the columns

# print(df)

# List of archives to be made public


def HTMLize(title,path): # This function creates clickable HTML links for a given file.
    pub=[
         "NA"
         ]    

    title=str(title)
    path=str(path)
    
    special_characters="[#]" # Putting the pound symbol in the link was messing things up. This method of replacing it might not be future proof.
    subs="%23"
    
    for i in pub: # If the title is found in the pub list, then it uses the link to the archive. Otherwise, it will use the actual URL.
        if i in title:
            path=re.sub(special_characters,subs,path)
            
            name="<a href="+'"'+"archive/"+path+'"'+">"+title+"</a>"
            
        else:
            
            name="<a href="+'"'+urls[path]+'"'+">"+title+"</a>"
                
    #print(name)
    return name


g=[]
for i in range(0,df.shape[0]):# Create a directory
    a=HTMLize(df.iat[i,0],onlyfiles[i])
    
    g.append(a)
    
df.drop(["Title"],axis=1,inplace=True)
    
df.insert(0,"Title",g)

text=df.to_html(index=False,justify='center',escape=False)
f=open("../directory.html", "w")

# def fuckmylife():
#     return text.replace('\n','')

# df_styled=df.style.format({'Text': fuckmylife}) # df to html kept putting new line markers in my links, thus breaking them. This line might break the program someday, but I don't care!!!

# html_table=df_styled.render()



f.write(text)
f.close()


# for i in range(0,df.shape[0]):# Create a directory
#     a=HTMLize(df.iat[i,0],onlyfiles[i])
#     if i==0:
#         f=open("../archive.html", "w")
        
#     else:
#         f=open("../archive.html", "a")
        
#     f.write(a)
#     print(a)
# f.close()
