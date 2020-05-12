'''def pisano(m): 
	previous, current = 0, 1
	for i in range(0, (m * m)): 
		previous, current= current, (previous + current) % m 
# 		print(previous,"   ",current)
 
		if (previous == 0 and current == 1): 
			return i + 1
 
def fibonacciModulo(n, m): 
	 
	pisano_p = pisano(m) 
# 	print(pisano_p)

	n = n % pisano_p 
	
	previous, current = 0, 1
	
	for i in range(n-1): 
		previous, current = current, previous + current 
		
	return (current % m) 

# Driver Code 
if __name__ == '__main__':
    n,m=map(int,input().split())
    print(fibonacciModulo(n, m))
'''
# Python 3 program to calculate 
# Fibonacci no. modulo m using 
# Pisano Period 

# Calculate and return Pisano Period 
# The length of a Pisano Period for 
# a given m ranges from 3 to m * m 
def pisanoPeriod(m): 
	previous, current = 0, 1
	for i in range(0, m * m): 
		previous, current = current, (previous + current) % m 
		
		# A Pisano Period starts with 01 
		if (previous == 0 and current == 1): 
			return i + 1

# Calculate Fn mod m 
def fibonacciModulo(n, m): 
	
	# Getting the period 
	pisano_period = pisanoPeriod(m) 
	
	# Taking mod of N with 
	# period length 
	n = n % pisano_period 
	
	previous, current = 0, 1
	
	for i in range(n-1): 
		previous, current= current, previous + current 
		
	return (current % m) 

# Driver Code 
if __name__ == '__main__': 
	n = 9999999999999
	m = 5
	print(fibonacciModulo(n, m)) 

