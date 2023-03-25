from progression import Progression

class ArithmeticProgression(Progression):       # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment = 1, start = 0):
        """Create a new arithmetic progression.

        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """
        super().__init__(start)                 # initialize base class
        self.increment = increment

    def _advance(self):                         # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment

if __name__ == '__main__':
    progression = Progression(2)
    data = progression.print_progression(3)
    print(data)