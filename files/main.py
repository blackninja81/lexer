import mylexer  # Import the lexer module from mylexer.py
import passer   # Import the parser module from passer.py

# Input expression
input_expr = input("Enter an arithmetic expression: ")

# Use the parser object directly to parse the input
parse_tree = passer.parser.parse(input_expr)
print("Parse Tree:", parse_tree)
