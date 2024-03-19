import math

# given values
w = 101  # top-right value
y = 97  # bottom-right value
z = 98  # given arc

# find a
a = 0

# Equation: w = 1/2(z + a)
# rewrie in terms of a
# New Equation: a = 2w - z

a = (2*w) - z


# find b
b = 0

# to find b we first need to find the unlabeled arc. Let x represet the unlabled arc

x = 0

# Equation: y = 1/2(z + x)
# rewrite in terms of x, similar to when we found a
# New Equation: x = 2y-z

x = (2*y) - z

# now we can find b
# since we have the value of 3/4 arcs we can simply add the 3 we have together then subtract that from 260
arcs = z + a + x

b = 360 - arcs


# find c
c = 0

# finding c will be very simple. Add a and b then half

c = (a + b)/2


# find d
d = 0

# d is similar to c, add x and b then half

d = (x + b)/2



# return all values
# x is only required to solve fo b and c but not neccesary to return

print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
print(f'd={d}')