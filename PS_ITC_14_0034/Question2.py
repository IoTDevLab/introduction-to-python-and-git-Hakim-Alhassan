## Template
#!/usr/bin/env python3

# Name: <Hakim Alhassan>
# Index number: <PS/ITC/14/0034>

# TODO: Put your codes here ...

x_sum = 0
for x in range(1, 2000):
 	if (x&3==0) or (x&5==0):
 		x_sum = x_sum + x
print ( x_sum)