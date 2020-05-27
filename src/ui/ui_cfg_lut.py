#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import shutil
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_LUT
from mem import memdef

class secBootUiCfgLut(bootDeviceWin_LUT.bootDeviceWin_LUT):

    def __init__(self, parent):
        bootDeviceWin_LUT.bootDeviceWin_LUT.__init__(self, parent)
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        pass

    def callbackSetLutGroup( self, event ):
        pass

    def callbackOk( self, event ):
        self.Show(False)

    def callbackCancel( self, event ):
        self.Show(False)

    def callbackClose( self, event ):
        self.Show(False)

