import os
import sys
import locale
from random import uniform
from pyo import *

#! -*- encoding: utf-8 -*-

### The encoding line is for E-Pyo tempfile only.
### sys.getfilesystemencoding() should be used to set
### the encoding line added by E-Pyo.

print("Default encoding: ", sys.getdefaultencoding())
print("File system encoding: ", sys.getfilesystemencoding())
print("Locale preferred encoding: ", locale.getpreferredencoding())
print("Locale default encoding: ", locale.getdefaultlocale())

s = Server().boot()

### Need a python layer to encode the path in python 3.
# Python 3
#p = 'b�b�tte/noise.aif'.encode(sys.getfilesystemencoding())
# Python 2
p = 'b�b�tte/noise.aif'

########## SNDINFO ###############
info = sndinfo(p)
print("sndinfo output:\n", info)

####### SAVEFILE ##############
sr, dur, chnls, path = 44100, 5, 2, os.path.join("b�b�tte", 'savefile.aif')
samples = [[uniform(-0.5,0.5) for i in range(sr*dur)] for i in range(chnls)]
savefile(samples=samples, path=path, sr=sr, channels=chnls, fileformat=1, sampletype=1)
print("Savefile record:", os.path.isfile(os.path.join("b�b�tte", 'savefile.aif')))

####### SAVEFILEFROMTABLE #########
home = os.path.expanduser('~')
path1 = SNDS_PATH + '/transparent.aif'
path2 = os.path.join("b�b�tte", 'savefileFromTable.aif')
t = SndTable(path1)
savefileFromTable(table=t, path=path2, fileformat=1, sampletype=1)
print("SavefileFromTable record:", os.path.isfile(os.path.join("b�b�tte", 'savefileFromTable.aif')))

##### UPSAMP/DOWNSAMP ######
# upsample a signal 3 times
upfile = os.path.join("b�b�tte", 'upsamp.aif')
upsamp(p, upfile, 2, 256)
print("upsamp record:", os.path.isfile(os.path.join("b�b�tte", 'upsamp.aif')))
# downsample the upsampled signal 3 times
downfile = os.path.join("b�b�tte", 'downsamp.aif')
downsamp(upfile, downfile, 3, 256)
print("downsamp record:", os.path.isfile(os.path.join("b�b�tte", 'downsamp.aif')))

sf = SfPlayer(p, mul=0.1).out()
sf.setPath(downfile)

######### SfMarker ###########
#sf = SfMarkerLooper('b�b�tte/transparent.aif', mul=0.3).out()

s.gui(locals(), exit=False)

if os.path.isfile(os.path.join("b�b�tte", 'savefile.aif')):
    os.remove(os.path.join("b�b�tte", 'savefile.aif'))
if os.path.isfile(os.path.join("b�b�tte", 'savefileFromTable.aif')):
    os.remove(os.path.join("b�b�tte", 'savefileFromTable.aif'))
if os.path.isfile(os.path.join("b�b�tte", 'upsamp.aif')):
    os.remove(os.path.join("b�b�tte", 'upsamp.aif'))
if os.path.isfile(os.path.join("b�b�tte", 'downsamp.aif')):
    os.remove(os.path.join("b�b�tte", 'downsamp.aif'))

"""
1 - Adapt encoding line for E-Pyo tempfile. **done**

2 - Use widestring in C layer.

3 - "if sys.version > 2" -> path.encode(sys.getfilesystemencoding())
    For python2, don't do anything.
 
Objects with file input:
sndinfo, savefile, savefileFromTable, upsamp, downsamp **done**
Sf_family, CvlVerb, SndTable, ControlRead, ControlRec, Expr
NoteinRead, NoteinRec, Record
Server: recordOptions, recstart
PyoTableObject: save, write, read  
PyoMatrixObject: write, read  

"""
