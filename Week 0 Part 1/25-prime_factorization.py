def prime_factorization(n):
	list = []
    for x in range(2, n):
    	if n % x == 0:
    		n //= x
    		list.append(x)
