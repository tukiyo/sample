# -*- coding: utf-8 -*-
import os

# pythonはhtmlヘッダーも出力しないとメッセージ表示されませんので。
def print_contents(message):
    print 'Content-Type: text/html\n'
    print message

# Windows用のアップロードモード
def upload_mode():
    try:
        import msvcrt
        msvcrt.setmode(0, os.O_BINARY)
        msvcrt.setmode(1, os.O_BINARY)
    except ImportError:
        pass

# Windows用のファイル名文字コード変換
def convert_encoding(original="utf-8", target="cp932", string=""):
    if original == target:
        return string
    return unicode(string, original).encode(target)

# Windowsか判定
def is_windows():
    if os.name == 'nt':
        return True
    return False

# 保存します
def file_save(savepath, fout_name, fileobj):
    if os.name == 'nt':
        fout_name = convert_encoding(string=fout_name)
    fout = file(os.path.join(savepath, fout_name), 'wb')
    while True:
        chunk = fileobj.read(1000000)
        if not chunk:
            break
        fout.write(chunk)
    fout.close()
