#!/bin/bash
function print_fibonacci() {
max=$1
a=0
b=1
 echo " $max is "

while [ $a -le $max ]
do
   echo -n "$a" 
   fn=$((a+b))
   a=$b
   b=$fn
done
}
 read -p "enter" max_number
 print_fibonacci $max_number



