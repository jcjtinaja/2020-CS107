| Trace | Function | Evaluation | Derivative | Eval @ $$x$$ | Eval @ $$y$$ |
|-|-|-|-|-|-|
x1 | x | 1.57 | 1 | 1 | 0
x2 | y | 1.05 | 1 | 0 | 1
v1 | cos(x2) | 0.5 | -sin(x2)x2' | 0 | -0.87 
v2 | -v1 | -0.5 | -v1' | 0 | 0.87
v3 | sin(x1) | 1 | cos(x1)x1' | 0 | 0
v4 | v3 + v2 | 0.5 | v3' + v2' | 0 | 0.87
v5 | (v4)^2 | 0.25 | 2v4v4' | 0 | 0.87
v6 | -v5 | -0.25 | -v5' | 0 | -0.87
f | exp(v6) | 0.78 | exp(v6)v6' | 0 | -0.67