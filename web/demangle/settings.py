import os

p = os.path
SETTINGS_DIR = p.dirname(p.abspath(__file__))
BIN_DIR = p.abspath(p.join(SETTINGS_DIR, '../../bin'))

