# f_1 = x^2 + y^2
| Trace | Function | Evaluation | Derivative | Eval @ $$x$$ | Eval @ $$y$$ |
|-|-|-|-|-|-|
x1 | x | 1 | 1 | 1 | 0
x2 | y | 1 | 1 | 0 | 1
v1 | (x2)^2 | 1 | 2x2x2' | 0 | 2
v2 | (x1)^2 | 1 | 2x1x1' | 2 | 0
f | v1 + v2 | 2 | v1' + v2' | 2 | 2

## f_1(1,1) = 4

# f_2 = exp(x+y)
| Trace | Function | Evaluation | Derivative | Eval @ $$x$$ | Eval @ $$y$$ |
|-|-|-|-|-|-|
x1 | x | 1 | 1 | 1 | 0
x2 | y | 1 | 1 | 0 | 1
v1 | x1 + x2 | 2 | x1' + x2' | 1 | 1
f | exp(v1) | 7.39 | exp(v1)v1' | 7.39 | 7.39
## f_2(1,1) = 14.78

# f_1(1,1) = 4
# f_2(1,1) = 14.78
# f(1,1) = [4, 14.78]