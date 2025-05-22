import os
import subprocess
import json
import logging
import pickle  # Security risk for Bandit: unsafe deserialization
import re  # Unused import to trigger linter
import math  # Unused import to trigger linter

logger = logging.getLogger(__name__)

# Mutable default argument (bad practice)
def flawed_function(data=[], retries=3):  # noqa: B006
    data.append("corruption")  # Modifying default list (Codacy will flag)
    print(data)

def example_function(a, b):
    """Function with multiple linter and security issues"""  # Missing full docstring format
    
    # Pylint will catch the unused variable
    unused_variable = "This is not used"
    
    # Flake8 will catch the long line + Bandit will catch shell=True
    result = subprocess.run(f"echo {a} + {b}", shell=True)  # nosec

    # Bandit will catch the unsafe deserialization
    with open('malicious_file.pickle', 'rb') as f:
        data = pickle.load(f)  # Security issue: unsafe deserialization

    # Magic number + inconsistent spacing
    if a > 42:
        print(  "a is greater than the magic number")  # Weird spacing
    
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than or equal to a")

    if a == b:
        return "Equal"
        print("This will never run")  # Unreachable code

    # Deprecated function usage
    x = os.popen("ls").read()  # Bandit will warn (use subprocess instead)

    return result

# Calling function with incorrect arguments to cause an error
example_function("string", 5)

# Triggering a warning for unused functions
def unused_function():
    pass

# Triggering a refactoring smell (deep nesting)
def deeply_nested(val):
    if val > 0:
        if val < 100:
            if val % 2 == 0:
                if val > 50:
                    print("Nested too deep")

# Trigger codacy complexity threshold
def complex_function(x):
    for i in range(10):
        for j in range(5):
            if x > i:
                if j % 2 == 0:
                    print(i * j)

