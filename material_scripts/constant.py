
base_html_head = '''<!doctype html> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="format-detection" content="telephone=no">
<title></title> <meta name="description" content=""> <meta name="viewport" content="width=device-width, initial-scale=1"><meta name="format-detection" content="telephone=no">
<link rel="stylesheet" href="style.css"></head>
<body><div onclick="onClickBody(this);">
'''

base_html_tail = '''
</div></body>'''

exp_base_html_head = '''<!doctype html> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title></title> <meta name="description" content=""> <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style_exp.css"></head>
<body id="base-container">
'''

exp_base_html_tail = '''
</body>'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()