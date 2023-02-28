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
        - Programs often tend to fail on special cases of the input. Such cases need to be carefully identified and tested.

        - The dependencies among the classes and functions of a program introduce a hierarchy. Namely, a component A is above a component B in the hierarchy if A depends upon B, such as when function A calls function B, or function A relies on a parameters that is an instance of class B.

        - There are two main testing strategies, top-down and bottom-up, which differ in the order in which components are tested.

        - Top-down testing proceeds from the top of the bottom of the program hierarchy. It is typically used in conjunction with stubbing, a boot-strapping technique that replaces a lower-level component with a stub, a replacement for the component that simulates the functionality of the original. For example, if function A calls function B to get the first line of a file, when testing A we can replace B with a stub that returns a fixed string.

        - Bottom-up testing proceeds from lower-level components to higher-level components. For example, bottom-levels functions, which do not invoke other functions, are tested first, followed by functions that call only bottom-level functions, and so on.

        - Similarly a class that does not depend upon any other classes can be tested before antoher class that depends on the former. This form of testing is usually described as unit testing, as the functionality of a specific component is tested in isolation of the larger software project.

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

        - Non-Operator Overloads
            - In addition to traditional operator overloading, Python relies on specially named methods to control the behavior of various other functionality, when applied to user-defined classes. For example, the syntax, str(foo), is formally a call to the constructor for the string class. Of course, if the parameter is an instance of a user-defined class, the original authors of the string class constructor calls a specially named method, foo.__str__(), that must return an appropiate string representation.

            - Similar special methods are used to determine how to constructo an int, float, or bool based on a parameter from a user-defined class. The conversion to a Boolean value is particularly important, because the syntax, if foo:, can be used even when foo is not formally a Boolean value (see Section 1.4.1). For a user-defined class, that condition is evaluated by the special method foo.__bool__().


            - Several other top-level functions rely on calling specially named methods. For example, the standard way to determine the size of a container type is by caling the top-level len function. Note well that the calling syntax, len(foo), is not the traditional method-calling syntax with the dot operator. However, in the case of a user-defined class, the top-level len function relies on a call to a specially named __len__ method of that class. That is, the call len(foo) is evaluated through a method call, foo.__len__(). When developing data structures, we will routinely define the __len__ method to return a measure of the size of the structure.

        - Implied Methods
            - As a general rule, if a particular method is not implemented in a user-defined class, the standard syntax that relies upon that method will raise an exception. For example, evaluating the expression, a + b, for instances of a user-defined class without __add__ or __radd__ will raise an error.

            - However, there are some operators that have default definitions provided by Python, in the absence of special methods, and there are some operators whose definitions are derived from others. For example, the __bool__ method, which supports the syntax if foo:, has default semantics so that every object other than None is evaluated as True, However, for container types, the __len__ method is typically defined to return the size of the container, If such a method exists, then the evaluation of bool(foo) is interpreted by default to be Ture for instances with nonzero length, and False for instances with zero length, allowing a syntax such as if waitlist: to be be used whether there are one or more entries in the waitlist.

            - In Section 2.3.4 we will discuss Python`s mechanism for providing iterators for collections via the special method, __iter__. With that said, if a container class provides implementations for both __len__ and __getitem__, a default iteration is provided automatically (using means we describe in Section 2.3.4). Furthermore once an interator is defined, default functionality of __contains__ is provided.

            - In section 1.3 we drew attention to the distinction between expression (a is b) and expression (a == b), with the former evaluating whether identifiers a and b are aliases for the same object, and the latter testing a notion of whether the two identifiers reference equivalent values. The notion of "equivalence" depends upon the context of the class, and semantics is defined with the __eq__ method. However, if no implementation is given for __eq__, the syntax (a == b) is legal with semantics of a is b, that is, an instance is equivalent ot itself and no others.

    - [ ] 2.3.3 Example: Multidimensional Vector Class
        - To demostrate the use of operator overloading via special methods, we provide an implementation of a Vecotr class, representing the coordinates of a vector in a multidimensional space. For example, in a three-dimensional space, we might wish to represent a vector with coordinates (5, -2, 3). Although it might be tempting to directly use a Python list to represent those coordinates, a list does not provide an appropiate abstraction for a geometric vector. In particular if using list, the expression [5, -2, 3] + [1, 4, 2) it results in the list [5, -2, 3, 1, 4, 2]. When working with vectors, if u = 5, -2, 3 and v = 1, 4, 2, one would expect the expression u + v, to return a three-dimensional vector with coordinates (6, 2, 5).

        - We therefore define a Vector class, in Code Fragment 2.4, that provides a better abstraction for the notion of a geometric vector. Internally, our vector relies upon an instance of a list, named _coords, as its storage mechanism. BY keeping the internal list encapsulated, we can enforce the desired public interface for instances of our class. A demostration of supported behaviors includes the follwing:

        # implicit iteration via __len__ and __getitem__
            
            v = Vector(5)       # construct five-dimensional <0, 0, 0, 0, 0>
            v[1] = 23           # <0, 23, 0, 0, 0> (based on use of __setitem__)
            v[-1] = 45          # <0, 23, 0, 0, 45> (also based via __setitem__)
            print(v[4])         # print 45 (via __getitem__)
            u = v + v           # <0, 46, 0 , 0, 90> <via __add__)
            print(u)            # print <0, 46, 0, 0, 0, 90)

            total = 0
            for entry in v:     # implicit iteration via __len__ and __getitem__ 
                total += entry

    - [ ] 2.3.4 Iterators
        - Iteration is an important concept in the design of data structures. We introduce Python's mechanism for iteration in Section 1.8. In short, an iterator for a collection provides one key behavior: It supports a special method name __next__ that returns the next element of the collection, if any, or raises a StopIteration exception to indicate that there are no further elements.
