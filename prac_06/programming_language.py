"""
Programming Language Class.
Estimate: 15 minutes
Actual: 12 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgramingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year