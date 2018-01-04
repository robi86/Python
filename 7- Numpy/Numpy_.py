# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Numpy Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import numpy as np
# ----------------------------------------------------------------------------------
#---------------------- creating numpy array----------------------------------------

x = np.array([1, 2, 3, 4])
y = np.linspace(-5, 1, 10)
z = np.arange(0, 10)
print(x)
print(y)
print(z)

type(x)
print(x.dtype)
# ----------------------------------------------------------------------------------
#---------------------- Step Size---------------------------------------------------
x1 = np.arange(0, 10, 2)
x2 = np.arange(0, 5, .5)
x3 = np.arange(0, 1, .1)

y1 = np.linspace(1, 5, 2)

List = list(x1)
print(List)

Min = np.amin(x1)
print(Min)

Max = np.amax(y1)
print(Max)
# ----------------------------------------------------------------------------------
#---------------------- Array Operands----------------------------------------------

a1 = np.array([1, 1, 1, 1]) + np.array([2, 2, 2, 2])
print(a1)

a2 = np.array([1, 1, 1, 1]) - np.array([2, 2, 2, 2])
print(a2)

a3 = np.array([1, 1, 1, 1]) * np.array([2, 2, 2, 2])
print(a3)

a4 = np.array([1, 1, 1, 1]) / np.array([2, 2, 2, 2])
print(a4)

a5 = np.array([True, True, False]) + np.array([True, False, False])
print(a5)

a6 = np.array([True, True, False]) * np.array([True, False, False])
print(a6)
# ----------------------------------------------------------------------------------
#---------------------- Mathematical Function---------------------------------------
print (abs(-2))

list1 = [-1, -2, -3]
s1 = []
for i in range(len(list1)):
    s1.append(abs(list1[i]))
print(s1)

np.abs(-3)
np.abs([-2, -7, 1])

# ----------------------------------------------------------------------------------
#---------------------- Indexing----------------------------------------------------
a7 = np.arange(1, 5, .5)
print(len(a7))

second_element = a7[1]
print(second_element)

first_three_elements = a7[0:3]
print(first_three_elements)
# ----------------------------------------------------------------------------------
# --------------------------Masking-------------------------------------------------
print(a7)

bigger_than_3 = a7 > 3
print(bigger_than_3)

type(bigger_than_3)
len(bigger_than_3)

d2 = [i for i, v in enumerate(a7) if v > 3]
print(d2)

[i for i, v in enumerate(a7) if v > 3]
d3 = [v for i, v in enumerate(a7) if v > 26]
print(d3)


sum(bigger_than_3)
len(d2)

large_nums = a7[bigger_than_3]
len(a7[bigger_than_3])
print(large_nums)

large_nums = a7[a7 > 3]
print(large_nums)

# ----------------------------------------------------------------------------------
# --------------------------More----------------------------------------------------
a8 = np.logical_and(a7 > 1, a7 < 3)
print(a8)

a9 = a7[np.logical_and(a7 > 1, a7 < 3)]
print(a9)


a10 = np.logical_or(a7 < 3, a7 > 4)
print(a10)

a11= a7[np.logical_or(a7 < 22, a7 > 27)]
print(a11)

# ----------------------------------------------------------------------------------
# --------------------------Vectorizing Function-------------------------------------
def f(x):
    return x ** 2 > 2

f_v = np.vectorize(f)
print(f_v([1,2,3]))
# ----------------------------------------------------------------------------------
# --------------------------Matrix -------------------------------------------------
Matrix  = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]])
print(Matrix)

type(Matrix)

shape_ = Matrix.shape
nrows, ncols = Matrix.shape

print(shape_)
print(nrows)
print(ncols)
# ----------------------------------------------------------------------------------
# --------------------------Matrix Elements------------------------------------------
element = Matrix[1, 3]


Matrix[0, :]
Matrix[0, 0:2]
Matrix[:, 2]
Matrix[1:3, 2]
Matrix[1:3, 2:3]  #

# ----------------------------------------------------------------------------------
# --------------------------Matrix Transpose----------------------------------------
Matrix_T = Matrix.transpose()
print(Matrix_T)


d = np.array([.1, .6, .8, .2, .9])
d1 = d.transpose()
print(d)
print(d1)

d3 = np.array([1, 2, 3, 4])
d4 = d3.transpose()
print(d3)
print(d4)

d5 = d3.T
print(d5)

d6 = d3[:, None]
print(d6)

d7 = d3.reshape((-1, 1))
print(d7)

# ----------------------------------------------------------------------------------
# --------------------------Numpy Zeros and Ones------------------------------------

np.zeros((3, 3), dtype=int)
np.ones((5, 2), dtype=float)
np.full((6, 2), -1)
# ----------------------------------------------------------------------------------
# --------------------------Numpy Random Number-------------------------------------

np.random.uniform(low=0, high=100)
np.random.uniform(low=0, high=100, size=10)

d9 = np.random.uniform(0, 1, 10)
print(d9)

d10 = np.random.rand(10, 2)
print(d10)

y = np.random.uniform(100, 200, 10000)


d11 = [i for i, v in enumerate(y) if v > 100 and v <= 110]
len(d11)
print(d11)

sum(np.logical_and(y > 100, y <= 110))
sum(np.logical_and(y > 160, y <= 170))



np.mean(y)
np.median(y)


np.percentile(y, 50)
np.percentile(y, 25)
np.percentile(y, 75)
# ----------------------------------------------------------------------------------
# --------------------------Normal Distribution-------------------------------------
y = np.random.normal(loc=0, scale=1, size=100000)  # lets make 100,000 this time

np.mean(y)
np.std(y)

np.percentile(y, [25, 50, 75])
np.percentile(y, 16)
np.percentile(y, [2.5, 1.5])



