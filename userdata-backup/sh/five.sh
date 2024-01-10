#!/bin/bash
if [[ $# -ne 1 ]]
then 
	echo "Please pass one argument"
exit 1
elif [[ $1 -gt 5 ]]
then 
	echo "$1 is greater than 5"

elif [[ $1 -lt 5 ]]
then
	echo $1 is less than 5

else
	echo "$1 is equal to 5"

fi	
