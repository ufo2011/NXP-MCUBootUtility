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
        self.m_choice_bit0.SetSelection(self.efuseDict['0x470_bootCfg2'] & 0x00000001)
        self.m_choice_bit1.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000002) >> 1)
        self.m_choice_bit2.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000004) >> 2)
        self.m_choice_bit3.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000008) >> 3)
        self.m_choice_bit4.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000010) >> 4)
        self.m_choice_bit5.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000020) >> 5)
        self.m_choice_bit6.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000040) >> 6)
        self.m_choice_bit7.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000080) >> 7)

        self.m_choice_bit8.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000100) >> 8)
        self.m_choice_bit9.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000200) >> 9)
        self.m_choice_bit10.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000400) >> 10)
        self.m_choice_bit11.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000800) >> 11)
        self.m_choice_bit12.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00001000) >> 12)
        self.m_choice_bit13.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00002000) >> 13)
        self.m_choice_bit14.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00004000) >> 14)
        self.m_choice_bit15.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00008000) >> 15)

        self.m_choice_bit19_16.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x000f0000) >> 16)
        self.m_choice_bit20.Enable( False )
        self.m_choice_bit22_21.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00600000) >> 21)
        self.m_choice_bit23.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00800000) >> 23)

        self.m_choice_bit30_24.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x7f000000) >> 24)
        self.m_choice_bit31.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x80000000) >> 31)

    def _getEfuseWord( self ):
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffe) | self.m_choice_bit0.GetSelection()
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffd) | (self.m_choice_bit1.GetSelection() << 1)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffb) | (self.m_choice_bit2.GetSelection() << 2)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffff7) | (self.m_choice_bit3.GetSelection() << 3)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffef) | (self.m_choice_bit4.GetSelection() << 4)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffdf) | (self.m_choice_bit5.GetSelection() << 5)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffeff) | (self.m_choice_bit8.GetSelection() << 8)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffdff) | (self.m_choice_bit9.GetSelection() << 9)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffbff) | (self.m_choice_bit10.GetSelection() << 10)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffff7ff) | (self.m_choice_bit11.GetSelection() << 11)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffefff) | (self.m_choice_bit12.GetSelection() << 12)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffdfff) | (self.m_choice_bit13.GetSelection() << 13)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffbfff) | (self.m_choice_bit14.GetSelection() << 14)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffff7fff) | (self.m_choice_bit15.GetSelection() << 15)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfff0ffff) | (self.m_choice_bit19_16.GetSelection() << 16)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xff9fffff) | (self.m_choice_bit22_21.GetSelection() << 21)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xff7fffff) | (self.m_choice_bit23.GetSelection() << 23)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0x80ffffff) | (self.m_choice_bit30_24.GetSelection() << 24)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0x7fffffff) | (self.m_choice_bit31.GetSelection() << 31)

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

