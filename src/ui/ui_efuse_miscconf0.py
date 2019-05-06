#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
sys.path.append(os.path.abspath(".."))
from win import efuseWin_MiscConf0

class secBootUiEfuseMiscConf0(efuseWin_MiscConf0.efuseWin_MiscConf0):

    def __init__(self, parent):
        efuseWin_MiscConf0.efuseWin_MiscConf0.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()
        self._recoverLastSettings()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        pass

    def _recoverLastSettings ( self ):
        self.m_choice_bit5_0.SetSelection(self.efuseDict['0x6d0_miscConf0'] & 0x0000003f)
        self.m_choice_bit6.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000040) >> 6)        
        self.m_choice_bit7.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000080) >> 7)        

        self.m_choice_bit11_8.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000f00) >> 8)        
        self.m_choice_bit12.Enable( False )
        self.m_choice_bit15_13.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x0000e000) >> 13)        

        self.m_choice_bit19_16.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x000f0000) >> 16)        
        self.m_choice_bit21_20.Enable( False )       
        self.m_choice_bit23_22.Enable( False )

        self.m_choice_bit24.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x01000000) >> 24)        
        self.m_choice_bit26_25.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x06000000) >> 25)        
        self.m_choice_bit27.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x08000000) >> 27)        
        self.m_choice_bit29_28.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x30000000) >> 28)
        self.m_choice_bit31_30.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0xc0000000) >> 30)        
        

    def _getEfuseWord( self ):
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffffc0) | self.m_choice_bit5_0.GetSelection() 
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfffff0ff) | (self.m_choice_bit11_8.GetSelection() << 8)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffff1fff) | (self.m_choice_bit15_13.GetSelection() << 13)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfff0ffff) | (self.m_choice_bit19_16.GetSelection() << 16)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfeffffff) | (self.m_choice_bit24.GetSelection() << 24)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xf9ffffff) | (self.m_choice_bit26_25.GetSelection() << 25)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xf7ffffff) | (self.m_choice_bit27.GetSelection() << 27)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xcfffffff) | (self.m_choice_bit29_28.GetSelection() << 28)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0x3fffffff) | (self.m_choice_bit31_30.GetSelection() << 30)

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

