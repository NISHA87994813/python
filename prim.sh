
echo "enter the range"
read n
is_prime=true
		if [ $n -lt 2 ]; then
			is_prime=false
		fi

		for ((i=2; i<$n; i++)); do
			
			if [ $((n % i)) -eq 0 ]; then
        			is_prime=false
			break
		fi
	done

	if $is_prime; then
		echo "$n is prime "

	else
		echo "$n is not prime"
	fi



	
