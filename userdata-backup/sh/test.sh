#!/bin/bash
#set -x

	if [[ $# -lt 1 ]];then
		echo pass the path to check
		exit 1
	fi

for i in $*;do
if [[ ! -e "$i" ]];then
echo "$i doesnot exists"
exit 1
fi
if [[ -f "$i" ]];then
	echo "$i is a file"
fi	
if [[ -d "$i" ]];then
	echo "$i is a dir"
fi
done
