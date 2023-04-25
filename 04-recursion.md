### Chapter 4: Recursion

One way to describe repetition within a computer program is the use of loops, such as Python's while-loop and for-loop constructs described in Section 1.4.2. An entirely different way to achieve repetition is through a process known as recursion.

Recursion is a technique by which a function makes one or more calls to itself during execution, or by which a data structure relies upon smaller instances of the very same type of structure in its representation.


- ### 4.1 Ilustrative Examples

    - [ ] 4.1.1 The Factorial Function
        - Some information about the Factorial Function here

    - [ ] 4.1.2 Drawing an English Ruler
        - In the case of computing a factorial, there is no compelling reason for preferring recursion over a direct iteration with a loop.
        - As a more complex example of the use of recursion, consider how to draw the markings of a typical English ruler:
        - For each inch, we place a tick with a numeric label.
        - We denote the length of the tick designating a whole inch as the major tick length.
        - Between the marks for whole inches, the ruler contains a series of minor ticks
