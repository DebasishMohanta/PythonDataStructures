import stack

string="gninraeL nIdekniL htiw tol a nrael"
reversed_string=""
s=stack.Stack()

# Your solution
for char in string:
    s.push(char)
while not s.is_empty():
    reversed_string+=s.pop()

print(reversed_string)
