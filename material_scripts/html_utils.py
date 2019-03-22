import constant 
import str_utils

def hamburger_content_with_base_html(body_content) : 
    '''
    body_contentをhtmlタグで挟んで完成物にします。

    >>> print(hamburger_content_with_base_html("<div>TEST</div>"))
    <!doctype html> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="format-detection" content="telephone=no">
    <title></title> <meta name="description" content=""> <meta name="viewport" content="width=device-width, initial-scale=1"><meta name="format-detection" content="telephone=no">
    <link rel="stylesheet" href="style.css"></head>
    <body><div onclick="onClickBody(this);">
    <div>TEST</div>
    </div></body>
    '''
    return constant.base_html_head + body_content + constant.base_html_tail

def hamburger_content_with_ex_base_html(body_content) : 
    '''
    body_contentをhtmlタグで挟んで完成物にします(解説バージョン)

    >>> print(hamburger_content_with_ex_base_html("<div>TEST</div>"))
    <!doctype html> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title></title> <meta name="description" content=""> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style_exp.css"></head>
    <body id="base-container">
    <div>TEST</div>
    </body>
    '''
    return constant.exp_base_html_head + body_content + constant.exp_base_html_tail


def convert_iso_text(text, iso):
    splitted = text.split(iso)
    if len(splitted) > 1:
        text = '<b class="lang_header_image_text">' + splitted[0] + '</b><img class="lang_header_image" src=\'flag_' + iso.lower() + '.png\' width="40" height="20">' + splitted[1]
    return text

def create_exp_html(exp):
    if exp is None:
        return None
    exp = exp.replace('_x000B_', '\n')
    exp = exp.replace('\u2028', '\n')
    exp = exp.replace("<box>", "<span class='vocab_area'>")    
    exp = exp.replace("</box>", "</span>")    
    exp = exp.replace('\n', '<br>\n')
    exp = exp.replace("_x000D_", "")
    html_text_list = []
    html_text_list.append(constant.exp_base_html_head)
    html_text_list.append('''
        <div class="bottom_container">
        <div class="main_explanation">
    ''')
    
    html_text_list.append(str_utils.remove_invalid_space(exp))    
    html_text_list.append("</div></div>")
    return "\n".join(html_text_list)
    
def remove_underline(text):
    text = text.replace("</u>", "")
    for i in range(147, 201):
        text = text.replace(str(i) + " <u>", "")        
    text = text.replace("<u>", "") 
    return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()