
from two import parser
from ir_gen import IRGenerator, TACInstruction
from ast_nodes import *

def interpret_tac(instructions):
    symbol_table = {}
    labels = {instr.result: i for i, instr in enumerate(instructions) if instr.op == 'label'}
    pc = 0

    while 0 <= pc < len(instructions):
        instr = instructions[pc]
        op = instr.op

        if op in ['add', 'sub', 'mul', 'div', 'mod', 'eq', 'neq', 'lt', 'le', 'gt', 'ge']:
            a = symbol_table.get(instr.arg1, instr.arg1) if isinstance(instr.arg1, str) else instr.arg1
            b = symbol_table.get(instr.arg2, instr.arg2) if isinstance(instr.arg2, str) else instr.arg2
            operations = {
                'add': lambda x, y: x + y,
                'sub': lambda x, y: x - y,
                'mul': lambda x, y: x * y,
                'div': lambda x, y: x // y,
                'mod': lambda x, y: x % y,
                'eq': lambda x, y: x == y,
                'neq': lambda x, y: x != y,
                'lt': lambda x, y: x < y,
                'le': lambda x, y: x <= y,
                'gt': lambda x, y: x > y,
                'ge': lambda x, y: x >= y
            }
            symbol_table[instr.result] = operations[op](a, b)
            pc += 1
        elif op == 'const':
            symbol_table[instr.result] = instr.arg1
            pc += 1
        elif op == 'assign':
            value = symbol_table.get(instr.arg1, instr.arg1) if isinstance(instr.arg1, str) else instr.arg1
            symbol_table[instr.result] = value
            pc += 1
        elif op == 'print':
            value = symbol_table.get(instr.arg1, instr.arg1) if isinstance(instr.arg1, str) else instr.arg1
            print(value)
            pc += 1
        elif op == 'jz':
            condition = symbol_table.get(instr.arg1, instr.arg1) if isinstance(instr.arg1, str) else instr.arg1
            if not condition:
                pc = labels[instr.result]
            else:
                pc += 1
        elif op == 'jmp':
            pc = labels[instr.result]
        elif op == 'label':
            pc += 1
        else:
            raise ValueError(f"Unknown TAC operation: {op}")

print("Mini Rust Compiler with IR Generation and Interpretation")
print("Enter your Rust-like code. End with Ctrl+D (Unix) or Ctrl+Z (Windows)\n")

try:
    code = ""
    while True:
        line = input()
        code += line + '\n'
except EOFError:
    pass

ast = parser.parse(code)
ir_gen = IRGenerator()
ir_gen.generate(ast)
ir = ir_gen.get_ir()

print("\nGenerated Three-Address Code (TAC):")
for instr in ir:
    print(instr)

print("\nOutput:")
interpret_tac(ir)