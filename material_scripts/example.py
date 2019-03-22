"""
This is the "example" module.

The example module supplies one function, is_japanese().  For example,

>>> is_japanese("テスト")
True
"""

def is_japanese(string):
    """Return true if even single character of the given string is japanese
    
    >>> is_japanese("テスト")
    True
    >>> [is_japanese(s) for s in ["test" , "あ" , "test あ"]]
    [False, True, True]
    >>> is_japanese(None)
    Traceback (most recent call last):
    ...
    ValueError: input text must not be None
    >>> is_japanese("")
    False
    """
    import unicodedata
    if string is None : raise ValueError("input text must not be None")
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