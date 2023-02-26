### Chapter 2: Object-Oriented Programming

- ### 2.1 Goals, Principles and Patterns

    - [ ] 2.1.1 Object-Oriented Design Goals
        - The main actors in the object-oriented paradigm are called objects.
        - Each object is an instance of a class.
        - Each class presents to the outside world a concise and consistent view of the objects that are instances of this class.
        - Software implementations should achieve robustness, adaptability, and reusability:
            - Robustness
                - Every good programmer wants to develop software that is correct, which means taht a program produces the right output for all the anticipated inputs in the program's application. In addition, we want software to be robust, that is, capable of handling unexpected inputs that are not explictly defined for its application. For example, if a program is expecting a positive integer (perhaps representing the price of an item) and instead is given a negative integer, then the program should be able to recover gracefully from this error.
            - Adaptability
                - Modern software applications, such as Web browsers and Internet search engines, typically involve large programs that are used for many years. Software, there- fore, needs to be able to evolve over time in response to changing conditions in its environment. Thus, another important goal of quality software is that it achieves adaptability (also called evolvability). Related to this concept is portability, which is the ability of software to run with minimal change on different hardware and operating system platforms. An advantage of writing software in Python is the portability provided by the language itself.
            - Reusability
                - For example the front-end and back-end frameworks for web development

    - [ ] 2.1.2 Object-Oriented Design Principles
        - some details here

    - [ ] 2.1.3 Object-Oriented Design Principles
        - some details here

- ### 2.2 Software Development

    - [ ] 2.2.1 Design
        - Some information about design here.

    - [ ] 2.2.2 Pseudo-Code
        - Some information about pseudo-code here.

    - [ ] 2.2.3 Coding Style and Documentation
        - Some information about coding style and docs here.

    - [ ] 2.2.4 Testing and Debugging
        - Some information about testing and debugging here.

- ### 2.3 Class Definitions
    - Some introduction about de 2.3 point chapter Class Definitions here

    - [ ] 2.3.1 Example: CreditCard Class
        - Some information about design here.
![Screenshot from 2023-02-26 00-25-18](https://user-images.githubusercontent.com/118082275/221390707-7a3ac3f9-6249-4505-a4dd-edf8c7203d7c.png)

        - Some other subtopic in here

    - [ ] 2.3.2 Operator Overloading and Python's Special methods
        - Python's built-in classes provide natural semantics natural for many operators. For example, the syntax a + b invokes addition for numeric types, yet concatenation for sequence types. When defining a new class, we must consider whether a syntax like a + b should be defined when a or b is an instance of that class.
        
        - This is important: By default, the + operator is undefined for a new class. However, the author of a class may provide a definiton using a technique known as "operator overloading". This is done by implementing a specially name method. In particular the + operator is overloaded by implementing a method name __add__, which takes the right-hand operand as a parameter and which return the result of the expresion. That is, the syntax, a + b, is converted to a method call on object a of the form, a.__add__(b). Similar specially named methods exist for other operators.

        - When a binary operator is applied to two instances of different types, as in 3 * 'love me', Python gives diference to the class of the left operand. In this example, it would effectively check if the int class provides a sufficient definition for how to multiply an instance by a string, via the __mul__ method. However, if that class does not implement such a behavior, Python checks the class definition for the right-han operand, it the form of a special method name __rmul__ (i.e., "right multiply"). This provides a way for a new user-defined class to support mixed operations that involve an instance of an existing class (given that the existing class would presuambly not have defined a behavior involving this new class).

        - The distinction between __mul__ and __rmul__ also allows a class to define a different semantics in cases, such as matrix multiplication, in which an operation is noncommutative (that is, A * x may differ from x * A).
