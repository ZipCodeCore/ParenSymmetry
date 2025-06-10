# ParenSymmetry Lab

## Overview

This lab teaches you to implement a **balanced parentheses checker**, a fundamental algorithm used in programming language processing. You'll learn to determine whether parentheses `()` in a string are properly balanced - meaning every opening parenthesis has a corresponding closing parenthesis in the correct order.

## Why This Matters: Lexing and Parsing

Checking balanced delimiters is a core component of how programming languages are processed by computers. This involves two key steps:

### Lexing (Lexical Analysis)
**Lexing** is the process of breaking source code into meaningful pieces called "tokens." Think of it like breaking a sentence into individual words. A lexer scans through your code character by character and groups them into tokens like keywords (`if`, `while`), operators (`+`, `-`), identifiers (variable names), and delimiters (`()`, `{}`, `[]`).

For example, the code `if (x > 5)` would be tokenized as:
- `if` (keyword)
- `(` (opening delimiter)  
- `x` (identifier)
- `>` (operator)
- `5` (number)
- `)` (closing delimiter)

### Parsing (Syntax Analysis)
**Parsing** takes the tokens from lexing and builds a structure that represents the program's syntax - like creating a sentence diagram. The parser needs to verify that delimiters are properly balanced to ensure the code structure makes sense.

Consider this code:
```
if (condition) {
    print("hello")
}
```

The parser must verify that:
- The `(` after `if` has a matching `)`
- The opening `{` has a matching `}`
- They're nested correctly

## Real-World Applications

Balanced delimiter checking is used in:
- **Code editors** - highlighting matching brackets as you type
- **Compilers** - validating program structure before translation
- **IDEs** - providing syntax error detection
- **Mathematical expressions** - ensuring formulas are correctly formed

## Lab Structure

- `java/` - Java implementation with Maven build system
- `python/` - Python implementation with unittest framework

Both versions include the same core challenge: implement the `isBalanced()` method to correctly identify balanced parentheses in strings.

## Getting Started

Choose your preferred language directory and follow the README instructions to implement and test your solution. Remember: this simple algorithm is the foundation for understanding how programming languages are processed!