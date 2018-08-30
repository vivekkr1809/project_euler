"""
This is the main file to solve the problems on Project Euler.

Author(s) : Vivek Kumar

"""

import numpy as np
import math
import sympy as sp
import scipy as scp
import time

def problem_140():
	"""
	Consider the infinite polynomial series /[A_G(x) = xG_1+x^2G_2+x^3G_3+../] where /[G_k/] is the
	/[k^{th}/] term of the second order recurrence relation G_k = G_{k-1}+G_{k-2}, G_1 = 1 and G_2 =4

	Find the sum of the first thirt golden nuggets
	"""
	"Solution to problem 140"
	start_time = time.time()

	print 'Problem 140 Runtime:', str(time.time() - start_time), 'seconds'

def problem_45():
	"""
	Find the next triangle number that is also pentagonal and hexagonal.
	"""
	pass


# def course_refine():


# def find_divisors():
def problem_12():
	"""
	The sequence of triangle numbers is generated by adding the natural numbers.
	What is the value of the first triangle number to have over five hundred divisors?
	"""
	"Solution to problem 12"
	start_time = time.time()

	n_divisors = 500 # Number of divisors required

	course_step = 1000
	# if(course_refine()):


	print 'Problem 12 Runtime:', str(time.time() - start_time), 'seconds'

def problem_10():
	"""
	Find the sum of all primes below two millon
	"""
	"Solution to problem 10"
	start_time = time.time()

	n = 2000000 # sum to nth prime to find

	# Find all the primes upto n
	prime_n = erato(n)

	# Sum them up
	val_sum = np.sum(prime_n)

	print('The sum of primes smaller than %d is %d' %(n, val_sum))
	# Print the time taken to run 
	print 'Problem 10 Runtime:', str(time.time() - start_time), 'seconds'

def problem_9():
	"""
	Find the product of the terms of the pythogorean triplet whose sum is 1000
	i.e. a+b+c = 1000; a^2+b^2=c^2; abc =?
	NOTE : The answer is unique
	"""
	# Solved by old school pen-paper method
	pass

def problem_8():
	# The number we are interested in
	num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	n_digit = 1000 # number of digits
	cons_digit = 13 # Number of consecutive digits we are interested in
	split = np.zeros([n_digit]).astype(int) # Create an array
	len_split = len(split)
	for i in range(len_split):
		split[i] = ((num/10**n_digit) % 10**(n_digit-i))/(10**(n_digit-i-1))
	
	# There will be 1000-(13-1) 13 digits numbers
	thirteen_digit_numbers = np.zeros((1000-13+1, 13))
	# Loop over
	pass

def problem_7():
	"""
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10 001st prime number?
	"""
	"Solution to problem 7"
	start_time = time.time()

	n = 10001 # 10001 # nth prime to find

	i=0 # counter
	# Loop while we haven't reached the required prime number
	k = 2 # first prime assume given
	while (i<n):
		if(check_prime(k)):
			i+=1
		k+=1

	print('The %dth prime is %d' %(n, k-1))
	# Print the time taken to run 
	print 'Problem 7 Runtime:', str(time.time() - start_time), 'seconds'


def problem_6():
	"""
	The sum of the squares of the first ten natural numbers is,
	1^2+2^2+....+10^2= 385
	The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)^2 = 552 = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	"""
	"Solution to problem 6"
	start_time = time.time()

	# Number upto which we are interested
	num = 100
	diff = 0
	# Using the property
	# (\sum_i a_i)^2 - (\sum_i a_i^2) = \sum_{i,j i!=j}2*a_i*a_j
	for i in range(num):
		j=i+2
		while j <=num:
			diff += 2*(i+1)*j
			j+=1
		i+=1

	print('The difference between the sum of squares and squre of sum is %d' %diff)
	# Print the time taken to run 
	print 'Problem 6 Runtime:', str(time.time() - start_time), 'seconds'

# @[param] n : an array containing the numbers whose LCM we have to find
# This is not the most efficient way to solve fo 1 to n numbers though
def find_lcm(n):
	len_n = len(n)

	return lcm

# Using sieve of Eratosthenes to find all the primes upto n
# Taken from Alon Amit's answer to the question
# https://www.quora.com/What-is-the-exact-number-of-prime-numbers-between-1-to-157-176
def erato(n):
    # Evolving list of primes
    nums = [k for k in range(2,n+1)]
    # Current prime we are sieving
    # Initialize with 2
    prime=2
    # Stop once prime^2 exceeds n
    while prime*prime <= n:
    	# Sieve!
        nums = [k for k in nums if not (k>prime and k%prime==0)]
        # Move on to next prime
        prime = nums[nums.index(prime)+1]
    return nums

def problem_5():
	"""
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	"""
	"Solution to problem 5"
	start_time = time.time()
	num = 20 # The number upto which we want the LCM of

	# Obtain all the primes upto a certain number
	prime_n = erato(num)

	# Use the property that LCM(1,2..,n) = \product_{p\in primes} p^{\floor{log_p n}}
	len_pr = len(prime_n)

	# Initialize the lcm
	lcm = 1

	# Use the property to compute the lcm
	for i in range(len_pr):
		lcm *= (prime_n[i])**(math.floor(math.log(num, prime_n[i])))

	print('The LCM of numbers from 1 to %d is %d' %(num,lcm))

	# Print the time taken to run 
	print 'Problem 5 Runtime:', str(time.time() - start_time), 'seconds'


def swap_digits(num):
	"Function to swap the digits of a number"
	swap_num = 0
	while num > 0:
		swap_num = swap_num*10+num%10
		num = num/10
	return swap_num

def problem_4():
	"""
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99
	Find the largest palindrome made from the product of two 3-digit numbers.
	"""
	"Solution to problem 4"
	start_time = time.time()

	# n-digit number
	n = 3
	# Largest number which is the product of n-digit number
	largest_num = (10**n-1)**2
	
	split = np.zeros([n]).astype(int)
	num = 0
	# Split the numbers
	for i in range(len(split)):
		split[i] = ((largest_num/10**n) % 10**(n-i))/(10**(n-i-1))
		num += split[i]*10**(n-i-1)


	for i in range(num):
		current_num = num-i
		current_num = current_num*(10**n)+swap_digits(current_num)
		if current_num > largest_num:
			pass
		else:
			mod = 1
			div=0
			current_div = 10**n-1
			div = 0
			while(mod!=0 and div < 10**n):
				mod = current_num%current_div
				div = current_num/current_div
				current_div =current_div-1
			if (mod == 0 and div < 10**n):
				print('The largest such palindromic number is %d' %current_num)
				print('The divisors are %d and %d' %(current_div+1, div))
				break

	# Print the time taken to run 
	print 'Problem 4 Runtime:', str(time.time() - start_time), 'seconds'	

def check_prime(i):
	"Checks if a number is prime"
	sqrt_i = np.floor(np.sqrt(i)).astype(int)
	if sqrt_i==1:
		prime = 1
	for j in range(2,sqrt_i+1):
		if i % j ==0:
			prime = 0
			break
		else:
			prime = 1
			
	return prime

def problem_3():
	"Solution to problem 3"
	start_time = time.time()
	"""
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	"""
	num = 600851475143 # Number whose largets prime we are seeking
	
	"""
	The crude way is to find the largest prime upto sqrt(num) which divides num.
	"""
	largest_prime = 1 # Initialize the largest prime

	sqrt_num = np.sqrt(num)
	sqrt_num = np.floor(sqrt_num).astype(int)
	
	# Check if number is divisible by 2
	if num % 2 ==0:
		# Check if number by 2 is prime if prime it is the largest
		if check_prime(num/2):
			largest_prime = num/2
		else:
			largest_prime = 2

	for i in range(3, sqrt_num+1):
		if num % i == 0:
			if check_prime(i) :
				largest_prime = i

	if largest_prime == 1:
		print('The number itself is a prime')
	
	print('The largest prime divisor of %d is %d' %(num, largest_prime))

	# Print the time taken to run 
	print 'Problem 3 Runtime:', str(time.time() - start_time), 'seconds'


def problem_2():
	"Solution to problem 2"
	"""
	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
	"""
	start_time = time.time()

	max_num = 4000000 # Maximum number not exceeded in Fibonacci sequence

	fibonacci_num = np.array([0,1,1]).astype(int) # Variable to keep the fibonacci number, initialize with 0,1,1

	val_sum = 0 # Variable to keep the sum, initialize to 0

	while fibonacci_num[2] < max_num :
		if (fibonacci_num[2] % 2) == 0:
			val_sum += fibonacci_num[2]
		fibonacci_num[0] = fibonacci_num[1]
		fibonacci_num[1] = fibonacci_num[2]
		fibonacci_num[2] =  fibonacci_num[0]+fibonacci_num[1]


	print('The largest fibbonaci number less than %d is %d' %(max_num, fibonacci_num[1]))
	print('The sum of even fibonacci numbers upto %d is %d' %(max_num, val_sum)) # Print the sum

	# Print the time taken to run 
	print 'Problem 2 Runtime:', str(time.time() - start_time), 'seconds'

def problem_1():
	"Solution to problem 1"
	"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
	"""
	# Start time
	start_time = time.time()
	
	max_num = 1000 # The largest number we want to find the sum to
	
	divisors = np.array([3, 5]).astype(int) # List of divisors

	val_sum = 0 # Initialize the sum as 0

	for i in range(max_num-1): # Loop over all the numbers below max_num
		for j in range(len(divisors)): # Loop over all the divisors we are interested in
			if (i+1) % divisors[j] == 0: # Check if the divisor divides the number
				val_sum += (i+1) # If it does add the number to the sum
				break # Break from the j-loop to avoid repetitions
	
	print('The sum of numbers upto %d is %d' %(max_num, val_sum)) # Print the sum

	# Print the time taken to run 
	print 'Problem 1 Runtime:', str(time.time() - start_time), 'seconds'



if __name__ == '__main__':

	#problem_1()
	#problem_2()
	#problem_3()
	#problem_4()
	#problem_5()
	#problem_6()
	#problem_7()
	problem_8()
	#problem_9()
	#problem_10()
	#problem_11()
	#problem_12()
	problem_45()
	#problem_140()