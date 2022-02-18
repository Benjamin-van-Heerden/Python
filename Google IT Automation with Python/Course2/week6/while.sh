#!/bin/bash

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n += 1))
done;

line="-----------------------"

echo $line
echo $line

n=1
command=$1

while ! $command && [ $n -le 5 ]; do
    echo "Sleep $n seconds then retry"
    echo $line
    sleep $n
    echo "Retry #$n"

    ((n += 1))
done;

echo $line
echo "n = $n"
echo $line

if [ $n -eq 6 ]; then
    echo "Unsuccessful"
else
    echo "Successful"
fi