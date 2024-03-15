import os, sys
INTERP = "/usr/bin/python3"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
print(sys.version)
from app import app