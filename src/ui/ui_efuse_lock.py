#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import math
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import efuseWin_Lock

class secBootUiEfuseLock(efuseWin_Lock.efuseWin_Lock):

    def __init__(self, parent):
        efuseWin_Lock.efuseWin_Lock.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()
        self._recoverLastSettings()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x400_lock_bit7']:
            self.m_staticText_bit7.SetLabel(key)
            self.m_choice_bit7.Clear()
            self.m_choice_bit7.SetItems(efuseDescDiffDict['0x400_lock_bit7'][key])
            self.m_choice_bit7.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit14']:
            self.m_staticText_bit14.SetLabel(key)
            self.m_choice_bit14.Clear()
            self.m_choice_bit14.SetItems(efuseDescDiffDict['0x400_lock_bit14'][key])
            self.m_choice_bit14.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit15']:
            self.m_staticText_bit15.SetLabel(key)
            self.m_choice_bit15.Clear()
            self.m_choice_bit15.SetItems(efuseDescDiffDict['0x400_lock_bit15'][key])
            self.m_choice_bit15.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit17']:
            self.m_staticText_bit17.SetLabel(key)
            self.m_choice_bit17.Clear()
            self.m_choice_bit17.SetItems(efuseDescDiffDict['0x400_lock_bit17'][key])
            self.m_choice_bit17.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit20']:
            self.m_staticText_bit20.SetLabel(key)
            self.m_choice_bit20.Clear()
            self.m_choice_bit20.SetItems(efuseDescDiffDict['0x400_lock_bit20'][key])
            self.m_choice_bit20.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit25_24']:
            self.m_staticText_bit25_24.SetLabel(key)
            self.m_choice_bit25_24.Clear()
            self.m_choice_bit25_24.SetItems(efuseDescDiffDict['0x400_lock_bit25_24'][key])
            self.m_choice_bit25_24.SetSelection(0)

    def _recoverLastSettings ( self ):
        pass

    def callbackOk( self, event ):
        uivar.setEfuseSettings(self.efuseDict)
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

