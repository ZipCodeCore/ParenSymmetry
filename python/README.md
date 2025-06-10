# ParenSymmetry - Python Version

This is the Python implementation of the ParenSymmetry lab.

## Structure

- `paren_symmetry.py` - Main implementation file with ParenSymmetry class
- `test_paren_symmetry.py` - Unit tests using Python's unittest framework

## Running the Code

### Run the main program:
```bash
python paren_symmetry.py
```

### Run the tests:
```bash
python test_paren_symmetry.py
```

Or use unittest module:
```bash
python -m unittest test_paren_symmetry.py
```

## Assignment

Implement the `is_balanced()` method in the `ParenSymmetry` class to check if parentheses in a string are balanced.

The method should:
- Return `True` if parentheses are balanced
- Return `False` if parentheses are unbalanced
- Handle empty strings and strings with no parentheses
- Ignore non-parentheses characters