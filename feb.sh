echo="enter n"
read n
a=0
b=1
i=1
while [$i -le $n ]
do
	echo $a
	c=`expr $a + $b `
	a=$b
	b=$c
	i=`expr $i + 1`
done
