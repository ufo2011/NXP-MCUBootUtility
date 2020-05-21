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
from win import bootDeviceWin_FDCB
from mem import memdef
from utils import sound

class secBootUiCfgFdcb(bootDeviceWin_FDCB.bootDeviceWin_FDCB):

    def __init__(self, parent):
        bootDeviceWin_FDCB.bootDeviceWin_FDCB.__init__(self, parent)
        self.cfgFdcbBinFilename = None

    def setNecessaryInfo( self, cfgFdcbBinFilename ):
        self.cfgFdcbBinFilename = cfgFdcbBinFilename
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        if os.path.isfile(self.cfgFdcbBinFilename):
            self.m_filePicker_binFile.SetPath(self.cfgFdcbBinFilename)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def callbackSelectFdcbFile( self, event ):
        fdcbPath = self.m_filePicker_binFile.GetPath()
        if os.path.isfile(fdcbPath) and os.path.getsize(fdcbPath) == memdef.kMemBlockSize_FDCB:
            if self.cfgFdcbBinFilename != fdcbPath:
                shutil.copy(fdcbPath, self.cfgFdcbBinFilename)
        else:
            self.popupMsgBox('FDCB file should be 512 bytes raw binary')
            self.m_filePicker_binFile.SetPath('')

    def callbackOk( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], uidef.kSoundEffectFilename_Progress)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

