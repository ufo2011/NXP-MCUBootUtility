#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
sys.path.append(os.path.abspath(".."))
from win import efuseWin_BootCfg1

class secBootUiEfuseBootCfg1(efuseWin_BootCfg1.efuseWin_BootCfg1):

    def __init__(self, parent):
        efuseWin_BootCfg1.efuseWin_BootCfg1.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()
        self._recoverLastSettings()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        pass

    def _recoverLastSettings ( self ):
        pass

    def _getEfuseWord( self ):
        pass

    def callbackOk( self, event ):
        self._getEfuseWord()
        uivar.setEfuseSettings(self.efuseDict)
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

