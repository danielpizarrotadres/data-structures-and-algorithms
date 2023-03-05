
### Chapter 1: Python Primer

- ### 1.1 Python Overview

    - [ ] 1.1.1 The Python Interpreter
        - Python is formally an interpreted lenguage.
        - Commands are executed through a piece of software known as the Python interpreted.
        - The interpreter receives a command, evaluates that command, and reports the result of the command.
        - While the interpreter can be used interactively (especially when debugging), a programmer typically defines a series of commands in advance and saves those commands in a lain text file known a source code or a script.
        - For Python, source code is convencionally stored in a file name with the .py suffix (e.g., demo.py).

    - [ ] Preview of Python Program
        - No relevant information (my opinion)

- ### 1.2 Objects in Python
        
    - [ ] Identifiers, Objects and the Assignment Statement
        - The most important of all Python command is an assignment statement
        - e.g., temperature = 98.6
        - This command establishes temperature as an identifier and then associates it with the object expressed on the right-hand side of the equal sign, in this case a floating-point object with value 98.6.
        - A python identifier (also called variable or constant in other interpreted programming lenguages) is most similar to a reference variable in java or a pointer variable in C++.
        - Each identifier is implicity associated with the memory address of the object (in the e.g., 98.6 floating-point object) to which it refers.
        - Unlike Java and C++, Python is dynamically typed lenguage because there is no necessary that each idenifier has a particular data type
        
    - [ ] Creating and Using Objects
        - No relevant information (my opinion)


- ### 1.3 Expressions, Operators and Precedence
        
    - [ ] Compound Expressions and Operator Precedence


- ### 1.4 Control Flow
        
    - [ ] Condititonals
        - No added anything yet
    - [ ] Loops
        - Python offers two distinct looping constructs. A while loop: allows general repetition based upon the repeated testing of a Boolean condition. A foor loop: provides convenient iteration of values from a defined series (such as characters of a string, element of a list, or numbers within a given range). We discuss both form in this section.

        - While Loops
            - The syntax of a while loop in Python is as follows:
            
                        while condition:
                            body

            - As with if statement, condition can be an arbitrary Boolean expression, and body can be an arbitrary block of code (including nested control structures). The execution of a while loop begins with a test of the Boolean condition. If that condition evaluates to True, the body of the loop is performed. After each execution of the body, the loop condition is retested, and if it evaluates to True, another iteration of the body is performed. When conditional test evaluates to False (assuming it ever does), the loop is exited and the flow of controls continues just beyond the body of the loop.

                        j = 0
                            while j < len(data) and data[j] != 'X':
                                j += 1

- ### 1.5 Functions
- ### 1.6 Simple Input and Output
- ### 1.7 Exception Handling

- ### 1.8 Iterators and Generators
    - In Python, the mechanism for iteration is base upon the following conventions:

        - [ ] An iterator
            - Is an object that manages an iteration through a series of values
            - If variable, i, identifies an iterator object, then each call to the built-in function, next(i), produces a subsequent element fron the underlying series, with a StopIteration exception raised to indicate that there are no further elements.
        - [ ] An iterable
            - Is an object that produces an iterator via the syntax iter(obj)

    - By these definitons, an instance of a list is an iterable, but not itself an iterator.
    - With data = [1, 2, 4, 8], it is not legal to call next(data).
    - However, an iterator object can be produced with syntax, i = iter(data), and then each subsequent call to next(i) will return an element of that list.
    - The for-loop syntax in Python simply automates this process, creating an iterator for the give iterable, and then repeatedly calling for the next element until catching the StopIteration exception.
