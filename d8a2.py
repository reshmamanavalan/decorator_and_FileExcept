import sys
RFILE= sys.argv[1]
text = []
try:
    fh = open(RFILE, 'r')
except IOError:
    print('cannot open', RFILE)
else:
    text = fh.readlines()
    fh.close()
if text:
    print(text[100])
