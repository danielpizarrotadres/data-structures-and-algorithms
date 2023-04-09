from progression import Progression

class FibonacciProgression(Progression):       # inherit from Progression
    """Iterator producing a Fibonacci progression."""

    def __init__(self, first = 0, second = 1):
        """Create a new fibonacci progression.

        first        the first term of the progression  (default 0)
        second       the second term of the progression (default 1)
        """
        super().__init__(first)                # initialize base class
        self._prev = second - first            # fictitious value preceding the first

    def _advance(self):                        # override inherited version
        """Update current value by adding the fixed increment."""
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == '__main__':
    # print('Default progression:')
    # default_progression = Progression().print_progression(10)
    # print(default_progression)

    print('FibonacciProgression')
    fibo = FibonacciProgression(4, 6).print_progression(3)
    print('------- end')
    print(fibo)
