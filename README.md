- This lexer was build in a python virtual environment running python version 3. It also uses python library ply
  You can use `source bin/activate` to activate virtual environment
- All files are located in the files directory. This project aims to create a simple lexer to perform arithmetic operations and generate a parse tree.
  You can use `python main.py` to run the program
- There are three main files we have main.py, passer.py and mylexer.py

## 1. main.py

This is the main Python script where the user interacts with the program. It is responsible for taking a user-defined arithmetic expression, parsing it, and generating a parse tree.
Here's an explanation of the key components of main.py:

  ### import passer
  This line imports the passer module, which is responsible for parsing the input expression.
   
  ### input_expr = input("Enter an arithmetic expression: ")
  This line prompts the user to input an arithmetic expression and stores it in the input_expr variable.
   
  ### parse_tree = passer.parse(input_expr)
  This line calls the parse function from the passer module to parse the input expression. The result is stored in the parse_tree variable.
  
  ### print("Parse Tree:", parse_tree)
  This line prints the parse tree generated from the input expression.

## 2. passer.py

This module defines the grammar and parsing rules for arithmetic expressions. It uses PLY (Python Lex-Yacc) to generate a parser for the input expressions. Here's an explanation of the key components of passer.py:
### Parsing Rules
The majority of the code in passer.py is dedicated to defining parsing rules for arithmetic expressions. The parsing rules use the PLY library to specify how different components of arithmetic expressions are recognized and how they form a parse tree.
### Importing Necessary Modules
The code begins with importing the ply.yacc module to work with the PLY parser generator.
### Token Definitions
The code defines token names for various components of arithmetic expressions (e.g., NUMBER, PLUS, MINUS, TIMES, DIVIDE, LPAREN, and RPAREN) along with regular expressions to recognize these tokens.
### Parsing Rules
The parsing rules are defined as functions, each associated with a specific component of the arithmetic expression, such as addition (p_expression_plus) and multiplication (p_term_times).

## 3. mylexer.py

This module defines the lexical analysis for the arithmetic expressions. It uses PLY (Python Lex-Yacc) to generate a lexer for the input expressions. Here's an explanation of the key components of mylexer.py:
### Token Definitions
The code defines token names for various components of arithmetic expressions (e.g., NUMBER, PLUS, MINUS, TIMES, DIVIDE, LPAREN, and RPAREN) along with regular expressions to recognize these tokens.
### Tokenization Rules
The code specifies how to tokenize the input string based on the defined regular expressions for tokens.
