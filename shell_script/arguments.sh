#!/bin/sh

ARGS="$@"
echo $ARGS
echo $# 
echo $1
echo $2
SNM=$2
SNM=`whoami`
echo "Changed second is: $SNM"
