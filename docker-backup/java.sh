#!/bin/bash
which java
if [ $? -eq 0 ];then
echo "java is already installed"
else
	sudo apt update -y
sudo apt install -y fontconfig openjdk-17-jre -y
java has been installed
fi
