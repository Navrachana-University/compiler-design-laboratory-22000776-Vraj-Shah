# ir_gen.py (Intermediate Representation Generator)
from ast_nodes import *

class TACInstruction:
    def __init__(self, op, arg1=None, arg2=None, result=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        if self.op in ['assign', 'const']:
            return f"{self.result} = {self.arg1}"
        elif self.op == 'print':
            return f"print {self.arg1}"
        elif self.op == 'label':
            return f"{self.result}:"
        elif self.op == 'jmp':
            return f"jmp {self.result}"
        elif self.op == 'jz':
            return f"jz {self.arg1} {self.result}"
        else:
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"

class IRGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.symbol_table = {}

    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def new_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    def emit(self, op, arg1=None, arg2=None, result=None):
        self.instructions.append(TACInstruction(op, arg1, arg2, result))

    def generate(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.generate(stmt)
        elif isinstance(node, Declaration):
            value = self.generate(node.expr)
            self.symbol_table[node.name] = node.var_type
            self.emit('assign', value, None, node.name)
        elif isinstance(node, Assignment):
            value = self.generate(node.expr)
            self.emit('assign', value, None, node.name)
        elif isinstance(node, Print):
            value = self.generate(node.expr)
            self.emit('print', value)
        elif isinstance(node, If):
            cond = self.generate(node.condition)
            else_label = self.new_label()
            end_label = self.new_label() if node.else_block else None
            self.emit('jz', cond, None, else_label)
            self.generate(node.then_block)
            if node.else_block:
                self.emit('jmp', None, None, end_label)
            self.emit('label', None, None, else_label)
            if node.else_block:
                self.generate(node.else_block)
                self.emit('label', None, None, end_label)
        elif isinstance(node, While):
            start_label = self.new_label()
            end_label = self.new_label()
            self.emit('label', None, None, start_label)
            cond = self.generate(node.condition)
            self.emit('jz', cond, None, end_label)
            self.generate(node.body)
            self.emit('jmp', None, None, start_label)
            self.emit('label', None, None, end_label)
        elif isinstance(node, ForLoop):
            loop_var = node.var
            limit = self.generate(node.limit)
            counter = self.new_temp()
            self.emit('const', 0, None, counter)
            start_label = self.new_label()
            end_label = self.new_label()
            self.emit('label', None, None, start_label)
            cond_temp = self.new_temp()
            self.emit('lt', counter, limit, cond_temp)
            self.emit('jz', cond_temp, None, end_label)
            self.emit('assign', counter, None, loop_var)
            self.generate(node.body)
            inc_temp = self.new_temp()
            self.emit('add', counter, 1, inc_temp)
            self.emit('assign', inc_temp, None, counter)
            self.emit('jmp', None, None, start_label)
            self.emit('label', None, None, end_label)
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.generate(stmt)
        elif isinstance(node, BinaryOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            result = self.new_temp()
            op_map = {
                '+': 'add', '-': 'sub', '*': 'mul', '/': 'div', '%': 'mod',
                '==': 'eq', '!=': 'neq', '<': 'lt', '<=': 'le', '>': 'gt', '>=': 'ge'
            }
            self.emit(op_map[node.op], left, right, result)
            return result
        elif isinstance(node, Literal):
            temp = self.new_temp()
            self.emit('const', node.value, None, temp)
            return temp
        elif isinstance(node, Var):
            return node.name
        return None

    def get_ir(self):
        return self.instructions