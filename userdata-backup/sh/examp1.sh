#!/bin/bash
echo My name is $1 I am from $2
echo "$*"
echo "$#"
echo "$@"
sleep 5&
echo "$$"
echo "$!"
echo "$0"
