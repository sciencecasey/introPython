class Charge:
    """
    docstring
    """
    coulumb = 6.24E18

    def __init__(self, q):
        self.q = q

    def coulumb_to_electrons(self, C):
        return C * self.coulumb

    def __str__(self):
        return f"{self.q}"

