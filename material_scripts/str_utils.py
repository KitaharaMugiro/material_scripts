import re
import unicodedata

def is_japanese(string):
    """
    Return true if even single character of the given string is japanese
    
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


#数字、uタグ系, スペース系の文字かどうか
num_Reg = re.compile(r'^[0-9]+$')
num_u_Reg = re.compile(r'^[0-9<uU>\s]+$')
al_Reg = re.compile(r'^[a-zA-Z]+$')

def is_alphabet(s):
    return al_Reg.match(s) is not None

def is_num(s):
    return num_Reg.match(s) is not None

def isvalidchar(s):
    return num_u_Reg.match(s) is not None

def remove_invalid_space(text):
    base_text = ""
    for i, s in enumerate(text):                
        if s == " ":
            if i > 0 and i < len(text) - 1:
                if is_japanese(text[i - 1]) and is_japanese(text[i + 1]):
                    continue
        base_text += s
    return base_text

def detect_invalid_space(text):
    if text is None : return False
    base_text = ""
    for i, s in enumerate(text):                
        if s == "(" or s == "（":
            if i > 0 and i < len(text) - 2:
                if is_alphabet(text[i + 1]) and is_japanese(text[i + 2]):
                    return True
    return False

def convert_phrase(text):
    text = text.replace("か゛", "が")
        
    text = text.replace("か゛", "が")
    text = text.replace("き゛", "ぎ")
    text = text.replace("く゛", "ぐ")
    text = text.replace("け゛", "げ")
    text = text.replace("こ゛", "ご")
    
    text = text.replace("さ゛", "ざ")
    text = text.replace("し゛", "じ")
    text = text.replace("す゛", "ず")
    text = text.replace("せ゛", "ぜ")
    text = text.replace("そ゛", "ぞ")
    
    text = text.replace("た゛", "だ")
    text = text.replace("ち゛", "ぢ")
    text = text.replace("つ゛", "づ")
    text = text.replace("て゛", "で")
    text = text.replace("と゛", "ど")

    text = text.replace("は゛", "ば")
    text = text.replace("ひ゛", "び")
    text = text.replace("ふ゛", "ぶ")
    text = text.replace("へ゛", "べ")
    text = text.replace("ほ゛", "ぼ")
    
    text = text.replace("カ゛", "ガ")
    text = text.replace("キ゛", "ギ")
    text = text.replace("ク゛", "グ")
    text = text.replace("ケ゛", "ゲ")
    text = text.replace("コ゛", "ゴ")
    
    text = text.replace("サ゛", "ザ")
    text = text.replace("シ゛", "ジ")
    text = text.replace("ス゛", "ズ")
    text = text.replace("セ゛", "ゼ")
    text = text.replace("ソ゛", "ゾ")
    
    text = text.replace("タ゛", "ダ")
    text = text.replace("チ゛", "ヂ")
    text = text.replace("ツ゛", "ヅ")
    text = text.replace("テ゛", "デ")
    text = text.replace("ト゛", "ド")

    text = text.replace("ハ゛", "バ")
    text = text.replace("ヒ゛", "ビ")
    text = text.replace("フ゛", "ブ")
    text = text.replace("ヘ゛", "ベ")
    text = text.replace("ホ゛", "ボ")
                        
    return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()