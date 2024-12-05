echo "enter the number:"
read num

result=1
i=1

while [ $i -le $num ]
do
	result=$((result * i))
	i=$((i +1))
done
echo "the fectorial number $num of $result"

