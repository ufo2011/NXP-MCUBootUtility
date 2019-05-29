#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import RTxxx_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from main import RT10yy_main

class secBootRTxxxUi(RT10yy_main.secBootRT10yyMain):

    def __init__(self, parent):
        RT10yy_main.secBootRT10yyMain.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initUi()

    def RTxxx_initUi( self ):
        self._RTxxx_initTargetSetupValue()
        self.RTxxx_setTargetSetupValue()

    def _RTxxx_initTargetSetupValue( self ):
        self.m_choice_mcuDevice.Clear()
        self.m_choice_bootDevice.Clear()
        self.m_choice_mcuDevice.SetItems(RTxxx_uidef.kMcuDevice_Latest)
        self.m_choice_bootDevice.SetItems(RTxxx_uidef.kBootDevice_Latest)
        totalSel = self.m_choice_mcuDevice.GetCount()
        if self.toolCommDict['mcuDevice'] < totalSel:
            self.m_choice_mcuDevice.SetSelection(self.toolCommDict['mcuDevice'])
        else:
            self.m_choice_mcuDevice.SetSelection(0)
        totalSel = self.m_choice_bootDevice.GetCount()
        if self.toolCommDict['bootDevice'] < totalSel:
            self.m_choice_bootDevice.SetSelection(self.toolCommDict['bootDevice'])
        else:
            self.m_choice_bootDevice.SetSelection(0)

    def _RTxxx_refreshBootDeviceList( self ):
        if self.tgt.availableBootDevices != None:
            self.m_choice_bootDevice.Clear()
            self.m_choice_bootDevice.SetItems(self.tgt.availableBootDevices)
            retSel = self.m_choice_bootDevice.FindString(self.bootDevice)
            if retSel != wx.NOT_FOUND:
                self.m_choice_bootDevice.SetSelection(retSel)
            else:
                self.m_choice_bootDevice.SetSelection(0)

    def RTxxx_setTargetSetupValue( self ):
        self.mcuDevice = self.m_choice_mcuDevice.GetString(self.m_choice_mcuDevice.GetSelection())
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['mcuDevice'] = self.m_choice_mcuDevice.GetSelection()
        self.RTxxx_createMcuTarget()
        self._RTxxx_refreshBootDeviceList()
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['bootDevice'] = self.m_choice_bootDevice.GetSelection()
