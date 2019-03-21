"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> is_japanese("テスト")
True
"""

def is_japanese(string):
    import unicodedata
    """Return true if even single character of the given string is japanese

    >>> [is_japanese(s) for s in ["test" , "あ" , "test あ"]]
    [False , True , True]
    >>> factorial(None)
    [False]
    """

    for ch in string:
        try:
            name = unicodedata.name(ch) 
            if "CJK UNIFIED" in name \
            or "HIRAGANA" in name \
            or "KATAKANA" in name:
                return True
        except ValueError:
            return False
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()