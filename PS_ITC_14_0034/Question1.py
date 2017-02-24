## Template
#!/usr/bin/env python3

# Name: <Hakim Alhassan>
# Index number: <PS/ITC/14/0034>

# TODO: Put your codes here ...

nl=[]
for x in range(1000, 7000):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
	