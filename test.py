import numpy as np
a = np.array([[1,2,3],[4,5,6]], dtype=np.int64)
print(a)
print("dim:", a.ndim)
print("shape:", a.shape)
print("dtype:", a.dtype)

a = np.zeros((3,4))
print(a)

a = np.ones((3,4), dtype=np.int16)
print(a)

a = np.arange(12).reshape(3, 4)
print(a)

a = np.linspace(1, 10, 5)
print(a)

a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print(c)
c = a + b
print(c)
c = a * b
print(c)
print(a**2)

a = np.array([[1,2],[2,3]])
b = np.arange(4).reshape(2, 2)
print(a)
print(b)

# 普通乘法与矩阵乘法
c = a*b
c_dot = np.dot(a, b)

print(c)
print(c_dot)

a = np.random.random((2, 3))
print(a)
print(np.sum(a, axis=1))
print(np.min(a, axis=0))
print(np.max(a, axis=1))

# 数组索引的最小值、最大值
print(np.argmin(a))
print(np.argmax(a))

# 平均值
print(np.average(a))

# 逐行输出
for row in a:
    print(row)

# 逐列输出
for column in a.T:
    print(column)

a = np.arange(12).reshape(3, 4)
print(np.split(a, 3, axis=0))