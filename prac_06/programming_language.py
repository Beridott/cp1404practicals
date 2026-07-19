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

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"