expression = input("expression:")
searched_expression = input("searched_expression: ")
if expression.find(searched_expression) == -1:
    print("The search phrase was not found.")
else:
    print(expression[expression.find(searched_expression) -1: expression.find(searched_expression) + len(searched_expression) +1])