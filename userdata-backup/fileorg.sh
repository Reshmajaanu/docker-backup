#!/bin/bash
echo "enter a directory"
source_dir=$1
for i in $source_dir/* 
do
	if [ -f $file ];then
          ext=`ls -lrt $1 | awk -F " " '{print $NF}' | awk -F "." '{print $2}'`
        dest_dir= "/home/ubuntu/$ext"
	if [ ! -d $dest_dir ];then
		mkdir $dest_dir
	fi
	mv $file $dest_dir
	fi
done



	


