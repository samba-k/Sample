#!/bin/bash

BACKUP_DATE=$(date +%b-%d-%y)
read input
for i in $input
do
tar -Pczf ./$i-$BACKUP_DATE.tar.gz $i
if [ $? -eq 0 ]
then
echo "$i backup is successful"
else
echo "$i backup is not successful"
fi
done
