
import ply.yacc as yacc
from one import tokens
from ast_nodes import *

symbol_table = {}

def p_program(p):
    'program : statement_list'
    p[0] = Program(p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : declaration SEMICOLON
                 | assignment SEMICOLON
                 | print_stmt SEMICOLON
                 | if_stmt
                 | while_stmt
                 | for_stmt'''
    p[0] = p[1]

def p_declaration(p):
    'declaration : LET IDENTIFIER COLON type ASSIGN expression'
    if p[2] in symbol_table:
        print(f"Semantic Error: Variable '{p[2]}' already declared")
    else:
        symbol_table[p[2]] = p[4]
    p[0] = Declaration(p[2], p[4], p[6])

def p_type(p):
    '''type : INT
            | BOOL'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression'
    if p[1] not in symbol_table:
        print(f"Semantic Error: Undeclared variable '{p[1]}'")
    p[0] = Assignment(p[1], p[3])

def p_print_stmt(p):
    'print_stmt : PRINT LPAREN expression RPAREN'
    p[0] = Print(p[3])

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expression RPAREN block
               | IF LPAREN expression RPAREN block ELSE block'''
    if len(p) == 6:
        p[0] = If(p[3], p[5])
    else:
        p[0] = If(p[3], p[5], p[7])

def p_while_stmt(p):
    'while_stmt : WHILE LPAREN expression RPAREN block'
    p[0] = While(p[3], p[5])

def p_for_stmt(p):
    'for_stmt : FOR IDENTIFIER IN expression block'
    if p[2] in symbol_table:
        print(f"Semantic Error: Loop variable '{p[2]}' already declared")
    p[0] = ForLoop(p[2], p[4], p[5])

def p_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = Block(p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression'''
    p[0] = BinaryOp(p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Literal(p[1])

def p_expression_true(p):
    'expression : TRUE'
    p[0] = Literal(True)

def p_expression_false(p):
    'expression : FALSE'
    p[0] = Literal(False)

def p_expression_var(p):
    'expression : IDENTIFIER'
    if p[1] not in symbol_table:
        print(f"Semantic Error: Undeclared variable '{p[1]}'")
    p[0] = Var(p[1])

def p_error(p):
    print("Syntax error at", p)

parser = yacc.yacc()
