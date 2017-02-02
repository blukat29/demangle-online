#!/usr/bin/env python3

import collections
import subprocess
import sys
import os

from flask import current_app


def exe_path(name):
    directory = current_app.config.get('BIN_DIR')
    return os.path.abspath(os.path.join(directory, name))

class Demangler(object):
    def __init__(self, desc, run, sample=''):
        self.desc = desc
        self.inner = run
        self.sample = sample

    def run(self, names, **kwargs):
        if isinstance(names, str):
            names = names.encode('utf-8')
        else:
            print(type(names))
            print(names)
            raise ValueError("Name is not string")
        return self.inner(names, **kwargs)

def run_cpp(names, compiler='auto'):
    argv = ['c++filt', '--format=%s' % compiler]
    return subprocess.check_output(argv, input=names)

def run_dlang(names):
    print(exe_path('d-demangle'))
    return subprocess.check_output(exe_path('d-demangle'), input=names)

def run_swift(names):
    return subprocess.check_output(exe_path('swift-demangle'), input=names)

def run_haskell(names):
    return subprocess.check_output(exe_path('haskell-demangle'), input=names)

demanglers = collections.OrderedDict([
    ('cpp', Demangler('C++ (g++)', run_cpp, '_ZNSt6vectorIiSaIiEE9push_backERKi')),
    ('dlang', Demangler('D (Dlang)', run_dlang, '_D4main4testFifZv')),
    ('swift', Demangler('Swift/Linux', run_swift, '_TFC9swifttest5Shape17simpleDescriptionfS0_FT_Si')),
    ('haskell', Demangler('Haskell (ghc)', run_haskell, 'base_GHCziIOziEncodingziUTF8_zdwa1')),
])
