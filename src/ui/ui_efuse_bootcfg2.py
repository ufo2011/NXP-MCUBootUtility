#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
sys.path.append(os.path.abspath(".."))
from win import efuseWin_BootCfg2

class secBootUiEfuseBootCfg2(efuseWin_BootCfg2.efuseWin_BootCfg2):

    def __init__(self, parent):
        efuseWin_BootCfg2.efuseWin_BootCfg2.__init__(self, parent)
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

