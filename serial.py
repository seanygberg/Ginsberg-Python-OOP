"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initialize a new generator"""

        self.start = start
        self.next = start

    def __repr__(self):
        """How is this represented"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next number"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to start"""
        
        self.next = self.start