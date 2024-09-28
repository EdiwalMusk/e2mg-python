import torch

x = torch.randn(3, 4, requires_grad = True)
b = torch.randn(3, 4, requires_grad = True)
t = x + b
y = t.sum()
print(y)
y.backward()
print(b.grad)