import abc


class Importance(abc.ABC):
    """
    Generic interface for importance metrics.

    Subclassess of Importance implement a method that takes the filename, and return
    an importance score for it.
    """

    def get_importance(self, filename: str) -> int:
        """
        Return an importance score for a file.
        """
        ...
