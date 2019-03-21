# インストール

```
pip3 install git+https://github.com/KitaharaMugiro/material_scripts.git 
```

# How to use
```
from material_scripts import example
example.is_japanese("これは日本語ですか？")
```

# 機能追加
```
git clone https://github.com/KitaharaMugiro/material_scripts.git 
```

## recommended style
doctestを使ってテストを書いておくことで、後から使う人にとって使いやすくなる。
doctestについて(https://docs.python.org/ja/3/library/doctest.html)

```python
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
```