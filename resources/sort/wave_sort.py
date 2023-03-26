class WaveSort:
    """Sorter that receive a progression of numbers

    Default sort produces the whole numbers: 2, 1, 3, ...
    """

    def __init__(self, numbers):
        """Initialize numbers to the given numbers."""
        self._numbers = numbers
    
    def search(self, currentPos, nextPos):
        currentPosValue, result = self._numbers[currentPos]
        nextPosValue = self._numbers[nextPos]
        if currentPosValue >= nextPosValue:
            return result

    def sort(self):
        print(len(self._numbers))
        for j in range(len(self._numbers)):
            print(j)
            numbers[j] = search(j, j + 1)
        print(numbers)

if __name__ == '__main__':
    data = WaveSort([0, 1, 2, 3])
    data.sort()
