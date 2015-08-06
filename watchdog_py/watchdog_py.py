#!/usr/bin/env python

import sh

a = sh.grep(sh.ps("afx"), 'bin/dpi-engine')

if a == '':
    print('dpi proc is found')
else:
    print('dpi not found')