# 概要
教材作成を行うにあたってよく使う処理や、便利なメソッドを1つのリポジトリにまとめて共有しましょう。
material_scriptsには次のモジュールが含まれています

* str_utils : 文字列処理に関してよく使用するメソッド
* constant : どの教材でも共通に使われる定数
* html_utils : HTML操作に関してよく使用するメソッド

暫定的なモジュール分けなので、追加や編集をよろしくお願いします。


# インストール
pipもしくはpip3でインストールしてください。

```
pip3 install git+https://github.com/KitaharaMugiro/material_scripts.git 
```

最新版にアップデートしたい場合は最後に-Uをつけてください。

```
pip3 install git+https://github.com/KitaharaMugiro/material_scripts.git -U
```

aliasで登録しておくと便利かもしれません。以下のコマンドを１度実行すれば、次回以降はターミナルで「update_scripts」と打つだけで最新版へアップデートされます。

```
alias update_scripts='pip3 install git+https://github.com/KitaharaMugiro/material_scripts.git -U'
```

# How to use
各モジュールをインポートしてメソッドを使用します。

```
from material_scripts import str_utils
str_utils.is_japanese("これは日本語ですか？")
```

# 機能追加
自分が作ったメソッドはどんどん登録していきましょう。
以下のコマンドでクローンして編集をします。

```
git clone https://github.com/KitaharaMugiro/material_scripts.git 
```

## recommended style
ただ単にメソッドを追加していくことも十分な貢献ですが、doctestを書いておくことで次のようなメリットがあります。

* 使い方や挙動がドキュメントとして残る
* テストをすることでバグの発見につながる
* 境界値での挙動を確かめることができる


```python
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
```

## doctestの書き方について
https://docs.python.org/ja/3/library/doctest.html

## 外部ライブラリを使用する場合
setup.pyにその旨を記述する必要があります。
install_requiresに使用する外部ライブラリの名前を追加してください。


