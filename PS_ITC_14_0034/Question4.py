 ## Template
#!/usr/bin/env python3

# Name: <Hakim Alhassan>
# Index number: <PS/ITC/14/0034>

# TODO: Put your codes here ...


def fib():
	total = 0

	i, j = 1, 1

	while j <= 4000000:
	         if j % 2 == 0:
	                 total += j
	                 
	         i, j = j, i + j

	return total

print(fib())
