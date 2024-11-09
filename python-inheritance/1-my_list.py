#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that includes a method to return the list in sorted order."""

    def print_sorted(self):
        """Returns the list in ascending sorted order without modifying the original list."""
        return sorted(self)

