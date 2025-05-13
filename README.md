
# RUST COMPILER

## Project Overview

Welcome to the **Rust Compiler** project! This project is a simple compiler designed to interpret a Rust-like programming language. Built from scratch, it utilizes fundamental concepts from compiler design, including:

- **Lexical Analysis**: 
  - The `one.py` file contains a lexer that tokenizes the input source code into meaningful symbols, such as keywords, identifiers, operators, and literals.

- **Parsing**: 
  - The `two.py` file implements a parser that takes the tokens produced by the lexer and constructs an **Abstract Syntax Tree (AST)**. This tree represents the hierarchical structure of the source code, allowing for easier manipulation and analysis.

- **Intermediate Representation Generation**: 
  - The `ir_gen.py` file generates **Three-Address Code (TAC)** from the AST. This intermediate representation simplifies the code, making it easier to optimize and translate into machine code.

- **Interpretation**: 
  - The `three.py` file interprets the generated TAC, executing the instructions and producing output based on the input source code.

## Features

The project allows users to write simple programs in a Rust-like syntax, which can include:
- Variable declarations
- Assignments
- Control flow statements (if, while, for)
- Print statements

The compiler processes the input code, generates intermediate code, and executes it, providing output directly to the console.

## Author Information

- **Name**: VRAJ SHAH
- **Roll Number**: 22000776

## Instructions to Run the Code

To run this project, follow these steps:

1. **Open Terminal**: 
   - Navigate to the project folder where all the files are located.

2. **Run the Compiler**: 
   - Type the following command in the terminal:
     ```bash
     python three.py
     ```

3. **Input Your Code**: 
   - After running the command, you will be prompted to enter your Rust-like code. You can type or paste your code directly into the terminal.

4. **End Input**: 
   - To terminate the input, use:
     - **Ctrl + D** (on Unix/Linux/Mac)
     - **Ctrl + Z** (on Windows)

5. **View Output**: 
   - The compiler will process your input code, generate the intermediate representation, and execute it. The output will be displayed in the terminal.

## Termination of the Code

To terminate the execution of the program at any time, you can simply close the terminal window or use the keyboard shortcuts mentioned above to end the input. If the program is running and you wish to stop it, you can use:
- **Ctrl + C** to interrupt the execution.

## File to Run for Output

The main file to run for output is **`three.py`**. This file serves as the entry point for the compiler, handling user input, invoking the parser, generating intermediate code, and executing the instructions.



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bPoO8GTw)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19513683&assignment_repo_type=AssignmentRepo)

---

Thank you for exploring the Rust Compiler project! Happy coding!
