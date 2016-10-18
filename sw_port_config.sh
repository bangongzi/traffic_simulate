#!/bin/bash
#This file is writen to configure a special port like s1-eth1
#The input format is like ./port_config.sh (s)i (-eth)j rate=1(Gbit/s) latency=3(ms)

config_single(){
	echo "dev s${1}-eth${2} are going to be configured"
	tc qdisc delete dev s${1}-eth${2} root
	tc qdisc add dev s${1}-eth${2} handle 1: root dsmark indices 1 default_index 0
	tc qdisc add dev s${1}-eth${2} handle 2: parent 1: tbf burst 2048KB latency ${3} mtu 1514 rate ${4}Gbit
	tc qdisc show dev s${1}-eth${2}
}

latency=`expr 1000 \* ${3}`
if test $# -eq 4
then
	config_single ${1} ${2} ${latency} ${4}
else
	echo "The input number format is not right,the right 
format is like ./port_config.sh (s)i (-eth)j rate=1(Gbit/s) latency=3(ms)"
fi