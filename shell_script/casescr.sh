#!/bin/sh

while :
do
INPUT=`whoami`
echo "enter username"
read INPUT
case $INPUT in
manaswini)
echo "username is found"
break
;;
*)
echo "username not found"
break
;;
esac
done

