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
        - A CreditCard Class

                    class CreditCard:
                        """A consumer credit card."""
                        
                        def __init__(self, customer, bank, acnt, limit):
                            """Create a new credit card instance.
                            
                            The initial balance is zero.
                            
                            customer    the name of the customer (e.g., 'John Bownman')
                            bank        the name of the bank (e.g., 'California Savings')
                            acnt        the account identifier (e.g., '5391 0375 9387 5309')
                            limit       credit limit (measure in dollars)
                            """
                            
                            self._customer = customer
                            self._bank = bank
                            self._account = acnt
                            self._limit = limit
                            self._balance = 0
                            
                        def get_customer(self):
                            """Return name of the customer."""
                            return self._customer
                            
                        def get_bank(self):
                            """Return bank's name."""
                            return self._bank
                        
                        def get_account(self):
                            """Return the card identying number (typycally stored as a string)."""
                            return self._account
                            
                        def get_limit(self):
                            """Return current credit limit."""
                            return self._balance
                            
                        def charge(self, price):
                            """Charge given price to the card, assuming sufficient credit limit.
                            
                            Return True if charge was processed; False if charge was denied.
                            """
                            
                            if price + self._balance > self._limit
                                return False
                            else
                                self._balance += price
                                return True
                                
                         def make_payment(self, amount):
                            """Process customer payment that reduces balance."""
                            return._balance -= amount
                            
        - A user can create an instance of the CreditCard class using syntax as:

                    cc = CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 1000)
                    
        - Internally, this results in a call to the specially named __init__ method that serves as the constructor of the class.
        - Its primary responsibility is to establish the syaye of a newly created credit card object with appropiate instance variables.

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

        - Fortunately, it is rare to have to directly implement an iterator class. Our preferred approach is the use of the generator syntax (also described in Section 1.8), which  automatically produces an iterator of tielded values.

        - Python also helps by providing an automatic iterator implementation for any class that defines both __len__ and __getitem__. To provide an instructive example of a low-level iterrator, the following code demostrates just such an iterator class that works on any collection that supports both __len__ and __getitem__

                    class SequenceIterator:
                        """ An iterator for any of Python's sequence types."""
                    
                        def __init__(self, sequence):
                            """ Create an iterator for the given sequence.""""
                            self._seq = sequence    # keep a reference to the underlying data
                            self._k = -1            # will increment to 0 on first call to next
                         
                        def __next__(self):
                            """ Return the next element, or else raise StopIteration error.""""
                            self._ k += 1                     # advance to next index  
                            if self._k < len(self._seq):
                                return(self._seq[self._k])    # return the data element
                            else:
                                raise StopIteration()         # there are no more elements
                                
                        def __iter__(self):
                            """" By convention, an iterator must return itself as an iterator.""""
                            return self

    - [ ] 2.3.5 Example: Range Class
        - Make a Range Class as an example for this seccion

- ### 2.4 Inheritance
    - A hierarchical design is useful in software development, as common functionality can be grouped at the most general level, thereby promoting reuse of code while differentiated behaviors can be viewed as extensions of the general case.
    - In object-oriented programming, the mechanism for a modular and hierarchical organization is a technique known as inheritance.
    - This allows a new class to be defined bsae upon an existing class as the starting point.
    - In object-oriented terminology, the existing class is typically described as the base class, parent class or super-class, while the newly defined class is known as the subclass or child class.
    
    There are two ways in which a subclass can differentiate itself from its superclass:
    - A subclass may specialize an existing behavior by providing a new implementation that overrides an existing method.
    - A subclass may also extend its superclass by providing brand new methods.

    - [ ] 2.4.1 Extending the CreditCard Class
        - To demostrate the mechanism for inheritance in Python, we revisit the CreditCard class of Section 2.3, implementing a subclass that, for lack of a better name, we name PredatoryCreditCard. The new class will differ from the original in two ways:
            (1) If an attempted charge is rejected because it would have exceeded the credit limit, a $5 fee will be charged.
            (2) There will be a mechanism for assessoring a monthly interest on the outstanding balance, based upon an Annual Porcentage Rate (APR) specified as a constructor parameter.


                    class:              CreditCard
                    Fields:             _customer
                                        _bank
                                        _account
                                        _balance
                                        _limit
                    Behaviors:          get_customer()
                                        get_bank()
                                        get_account()
                                        make_payment(amount)
                                        get_balance()
                                        get_limit()
                                        charge(price)
                                        
                    class:              PredatoryCreditCard
                    Fields:             _apr
                    Behaviors:          process_month()
                                        charge(price)

        - To indicate that the new class inherits from the existing CreditCard class, our definition begins with the syntax PredatoryCreditCard(CreditCard). The body of the new class provides three member functions: __init__, charge(), and process_month(). The __init__ constructor serves a very similar role to the original CreditCard constructor. The mechanism for calling the inherited constructor relies on the syntax, super().

                    super().__init__(customer, bank, acnt, limit)
                    
        - call the __init__ method that was inherited from the CreditCard superclass. Note well that this method only accepts four parameters. We record the APR value in a new field named _apr.

        - In similar fashion, our PredatoryCreditCard class provides a new implementation of the carge method that overrides the inherited method. Yet, our implementation of the new method relies on a call to the inherited method, with syntax super().charge(price)

                    class PredatoryCreditCard(CreditCard):
                        """An extension to CreditCard that compounds interest and fees."""
                    
                        def __init__(self, customer, bank, acnt, limit, apr):
                            """Create a new predatory credit card instance
                                
                                The initial balance is zero
                                
                                customer        the name of the customer (e.g., 'John Bowman')
                                bank            the name of the bank (e.g., 'California Savings')
                                acnt            the acount identifier (e.g., '5931 0375 9387 5309')
                                limit           credit limit (measured in dollars)
                                apr             annual percentage rate (e.g., 0.0825 for 8.25% APR)
                            """"
                            super().__init__(customer, bank, acnt, limit)   # call super constructor
                            self._apr = apr
                            
                        def charge(self, price):
                            """Charge given price to the card, assuming sufficient credit limit.
                            
                            Return True if charge was processed.
                            Return False and assess $5 fee if charge is denied.
                            "
                            success = super().charge(price)     # call inherited method
                            if not success:
                                self._balance += 5              # assess penalty
                            return success                      # caller expects return value
                            
                        def process_month(self):
                            """Assess monthly interest on outstanding balance."""
                            if self._balance > 0:
                                # if positive balnce, convert APR to monthly multiplicative factor
                                month_factor = pow(1 + self._apr, 1/12)
                                self._balance *= monthly_factor

    - [ ] 2.4.2 Hierarchy of Numeric Progressions

        - As a second example of the use of inheritance, we develop a hierarchy of classes for iterating numeric progressions. A numeric progression is a sequence of numbers, where each number depends on one or more of the previous numbers. For example, an arithmetic progression determines the next number by adding a fixed constant to the previous value. A geometric progression determines the next number by multiplying the previous value by a fixed constant. In general a progression requires a first value, and a way of identifying a new value based on one or more previous values. In general a progression requires a first value, and a way of identifying a new value based on one or more previous values.

        - To maximize reusability of code, we develop a hierarchy of classes stemming from a general base class that we name Progression. Technically, the Progression class produces the progression of whole numbers: 0, 1, 2, ...

        - However, the idea of this class is designed to serve as the base class for other progression types, providing as much common functionality as possible, and thereby minimizing the burden on the subclasses.


                                                              Progression


                               ArithmeticProgression       GeometricProgression       FibonacciProgression

        - Our implementation of the basic Progression class is provided in in the code below. The constructor for this class accepts a starting value for the progression (0 by default), and initializes a data member, self._current, to that value.

        - The Progression class implements the conventions of a Python iterator (see Section 2.3.4), namely the special __next__ and __iter__ methods. If a user of the class creates a progression as seq = Progression(), each call to next(seq) will return a subsequent element of the progression sequence. It would also be possible to use a for-loop syntax, for value in seq:, although we note that our default progression is defined as an infine sequence.

                    class Progression:
                        """Iterator producing a generic progression.
                        
                        Default iterator produces the whole numbers 0, 1, 2, ...
                        """
                        
                        def __init__(self, start=0):
                            """Initialize current to the first value of the progression."""
                            self._current = start
                            
                        def _advance(self):
                            """Update self._current to a new value
                            
                            This should be overridden by a subclass to customize progression.
                            
                            By convention, if current is set to None, this designates the
                            end of a finite progression.
                            """
                            
                            self._current += 1
                            
                         def __next__(self):
                            """
