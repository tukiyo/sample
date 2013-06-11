#! c:/Python27/python.exe
# -*- coding: utf-8 -*- 

from distutils.core import setup
import glob
import py2exe

option = {
    "compressed" : 1,
    "optimize"   : 2,
    "bundle_files" : 2
}

setup(
    options = { "py2exe" : option },
    console = [{
        "script":"main.py"
    }],
    data_files = [
        "main.py",
        #"hoge.py",
        #"fuga.py",
    ]
)
