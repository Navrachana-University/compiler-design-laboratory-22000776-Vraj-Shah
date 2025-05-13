# ### ast_nodes.py
# class ASTNode:
#     pass

# class Program(ASTNode):
#     def __init__(self, statements):
#         self.statements = statements

# class Declaration(ASTNode):
#     def __init__(self, name, expr):
#         self.name = name
#         self.expr = expr

# class Assignment(ASTNode):
#     def __init__(self, name, expr):
#         self.name = name
#         self.expr = expr

# class Print(ASTNode):
#     def __init__(self, expr):
#         self.expr = expr

# class While(ASTNode):
#     def __init__(self, condition, body):
#         self.condition = condition
#         self.body = body

# class If(ASTNode):
#     def __init__(self, condition, then_block, else_block=None):
#         self.condition = condition
#         self.then_block = then_block
#         self.else_block = else_block

# class BinaryOp(ASTNode):
#     def __init__(self, op, left, right):
#         self.op = op
#         self.left = left
#         self.right = right

# class Literal(ASTNode):
#     def __init__(self, value):
#         self.value = value

# class Var(ASTNode):
#     def __init__(self, name):
#         self.name = name

# class Block(ASTNode):
#     def __init__(self, statements):
#         self.statements = statements












class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Declaration(ASTNode):
    def __init__(self, name, var_type, expr):
        self.name = name
        self.var_type = var_type
        self.expr = expr

class Assignment(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForLoop(ASTNode):
    def __init__(self, var, limit, body):
        self.var = var
        self.limit = limit
        self.body = body

class If(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class BinaryOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements
