import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def evaluate_expression(expression):
    tokens = expression.split()

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            try:
                float(token)
            except ValueError:
                return f"Invalid number: {token}"
        else:
            if token not in OPERATORS:
                return f"Invalid operator: {token}"
    numbers = []
    operations =[]

    def apply_operator():
        operator_func = OPERATORS[operations.pop()]
        right = numbers.pop()
        left = numbers.pop()
        numbers.append(operator_func(left, right))
    
    for token in tokens:
        if token in OPERATORS:
            while(operations and OPERATORS[token] in (operator.add, operator.sub) and
              OPERATORS[operators[-1]] in (operator.mul, operator.truediv)):
                apply_operator()
        else:
            numbers.append(float(token))
            
    while operations:
        apply_operator()
        
    return numbers[0]

expression = input("Enter an equation: ")
result = evaluate_expression(expression)
print(result)
    
    


