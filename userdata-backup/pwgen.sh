#!/bin/bash
echo "enter the length of the password"
read num
password=$( openssl rand -base64 $num |cut -c 1-$num )
#$(echo $password | cut -c 1-$num)
echo $password >p1
echo $password

