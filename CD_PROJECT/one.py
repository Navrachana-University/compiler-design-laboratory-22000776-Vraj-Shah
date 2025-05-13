
import ply.lex as lex

tokens = (
    'NUMBER', 'IDENTIFIER',
    'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD',
    'EQ', 'NEQ', 'LT', 'GT', 'LE', 'GE',
    'ASSIGN', 'COLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON',
)

reserved = {
    'let': 'LET',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'print': 'PRINT',
    'true': 'TRUE',
    'false': 'FALSE',
    'int': 'INT',
    'bool': 'BOOL'
}

tokens += tuple(reserved.values())

t_PLUS     = r'\+'
t_MINUS    = r'-'
t_MUL      = r'\*'
t_DIV      = r'/'
t_MOD      = r'%'
t_EQ       = r'=='
t_NEQ      = r'!='
t_LT       = r'<'
t_GT       = r'>'
t_LE       = r'<='
t_GE       = r'>='
t_ASSIGN   = r'='
t_COLON    = r':'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
