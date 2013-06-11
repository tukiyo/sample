# -*- coding: utf-8 -*-
import cgi
import os
from file_upload_func import upload_mode, print_contents, convert_encoding, is_windows, file_save

if is_windows():
    upload_mode()

form = cgi.FieldStorage()
if not form.has_key('file'):
    print_contents("アップロードが正しくありません。")
    exit()

item = form['file']
if item.file:
    upload_path = os.path.abspath("uploaded")
    file_save(upload_path, item.filename, item.file)

print_contents("アップロードしました。「%s」" % item.filename)
