from __future__ import division
import os
#coding : utf8

def get_size(path,f=False):
    if f:
        size=os.path.getsize(os.path.join(path,f))                                                      #the file size
    else:
        size=sum(os.path.getsize(os.path.join(dirpath, f)) for dirpath,_,filenames in os.walk(path) for f in filenames) #the whole path folder size

    byte_list={0:" Bytes",1:" KiB", 2:" MiB", 3: " GiB", 4: " TiB"}
    i=0
    while size>=2**10:
        size/=2**10
        i+=1
    return str(round(size,3))+byte_list[i]

def list_files(path):
    for root,dirs,files in os.walk(path):
        level=root.replace(path, '').count(os.sep)
        indent=' '*4*(level)
        base=os.path.basename(root)
        print "{}/{:<{}}{}".format(indent,base,85-4*level,get_size(root))
        x=4*(level+1)
        subindent=' '*x
        for f in files:
            print "{}{:<{}}{}".format(subindent,f,100-x,get_size(root,f))
list_files("G:\\")