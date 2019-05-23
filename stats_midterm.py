import numpy as np
## To know P(A|B) What is A and B? 
a = 'Knows the material'
b = 'Answered correctly'

p_a = 0.60
p_b_a = 0.85
p_b = 1 - 0.15 - 0.20

p_a_b = (p_b_a * p_a) / p_b
print(p_a_b)