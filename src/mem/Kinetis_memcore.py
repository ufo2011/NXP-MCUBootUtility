#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import boot
import memdef
import Kinetis_memdef
sys.path.append(os.path.abspath(".."))
from run import Kinetis_runcore
from gen import Kinetis_gendef
from ui import Kinetis_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from utils import misc

class secBootKinetisMem(Kinetis_runcore.secBootKinetisRun):

    def __init__(self, parent):
        Kinetis_runcore.secBootKinetisRun.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_Kinetis:
            self.Kinetis_initMem()

    def Kinetis_initMem( self ):

        self.needToShowCfgIntr = None
        self.needToShowImageIntr = None
        self._Kinetis_initShowIntr()

    def _Kinetis_initShowIntr( self ):
        self.needToShowCfgIntr = True
        self.needToShowImageIntr = True

    def Kinetis_readProgrammedMemoryAndShow( self ):
        if not os.path.isfile(self.destAppFilename):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotProgImage'][self.languageIndex])
            return
        self.clearMem()

        imageMemBase = 0
        readoutMemLen = 0
        imageFileLen = os.path.getsize(self.destAppFilename)
        if self.bootDevice == Kinetis_uidef.kBootDevice_InternalNor:
            imageMemBase = self.bootDeviceMemBase
        else:
            pass
        readoutMemLen += imageFileLen

        memFilename = 'bootableImageFromBootDevice.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        status, results, cmdStr = self.blhost.readMemory(imageMemBase, readoutMemLen, memFilename)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False

        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        addr = imageMemBase
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self.getOneLineContentToShow(addr, memLeft, fileObj)
                memLeft -= len(memContent)
                addr += len(memContent)
                self.printMem(contentToShow)
            fileObj.close()
        self._Kinetis_initShowIntr()
        self.tryToSaveImageDataFile(memFilepath)
