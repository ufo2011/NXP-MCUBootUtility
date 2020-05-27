#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import array
import struct
import shutil
import uidef
import uivar
import uilang
import ui_cfg_lut
import uidef_fdcb
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_FDCB
from mem import memdef
from utils import sound

kAccessType_Set = 0
kAccessType_Get = 1

class secBootUiCfgFdcb(bootDeviceWin_FDCB.bootDeviceWin_FDCB):

    def __init__(self, parent):
        bootDeviceWin_FDCB.bootDeviceWin_FDCB.__init__(self, parent)
        self.mcuSeries = None
        self.cfgFdcbBinFilename = None
        self.fdcbBuffer = array.array('c', [chr(0xff)]) * memdef.kMemBlockSize_FDCB

    def setNecessaryInfo( self, mcuSeries, flexspiFreqs, cfgFdcbBinFilename ):
        if flexspiFreqs != None:
            self.m_choice_serialClkFreq.Clear()
            self.m_choice_serialClkFreq.SetItems(flexspiFreqs)
            self.m_choice_serialClkFreq.SetSelection(0)
            self.m_choice_ipcmdSerialClkFreq.Clear()
            self.m_choice_ipcmdSerialClkFreq.SetItems(flexspiFreqs)
            self.m_choice_ipcmdSerialClkFreq.SetSelection(0)
        self.mcuSeries = mcuSeries
        self.cfgFdcbBinFilename = cfgFdcbBinFilename
        self._defnMcuSeriesDifference()
        self._recoverLastSettings()

    def _defnMcuSeriesDifference( self ):
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.m_staticText_readSampleClkSrc.SetLabel("readSamplingOption:")
            self.m_staticText_lutCustomSeqEnable.SetLabel("N/A")
            self.m_staticText_commandInterval.SetLabel("N/A")
            self.m_staticText_dataValidTime0time_100ps.SetLabel("coarseTuning:")
            self.m_staticText_dataValidTime0delay_cells.SetLabel("fineTuning:")
            self.m_staticText_dataValidTime1time_100ps.SetLabel("samplePoint:")
            self.m_staticText_dataValidTime1delay_cells.SetLabel("dataHoldTime:")
            self.m_staticText_lutCustomSeq0Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq0Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq1Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq1Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq2Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq2Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq3Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq3Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq4Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq4Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq5Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq5Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq6Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq6Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq7Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq7Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq8Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq8Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq9Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq9Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq10Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq10Id.SetLabel("N/A")
            self.m_staticText_lutCustomSeq11Num.SetLabel("N/A")
            self.m_staticText_lutCustomSeq11Id.SetLabel("N/A")
            self.m_staticText_isDataOrderSwapped.SetLabel("N/A")
            self.m_staticText_serialNorType.SetLabel("N/A")
            self.m_staticText_needExitNoCmdMode.SetLabel("N/A")
            self.m_staticText_halfClkForNonReadCmd.SetLabel("N/A")
            self.m_staticText_needRestoreNoCmdMode.SetLabel("N/A")
        elif self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.m_staticText_isNonBlockingMode.SetLabel("N/A")
        else:
            pass

    def _convertPackFmt( self, byteNum ):
        fmt = '<B'
        if byteNum == 4:
            fmt = '<I'
        elif byteNum == 2:
            fmt = '<H'
        #elif byteNum == 1:
        else:
            pass
        return fmt

    def _getMemberFromFdcb( self, buf, offset, byteNum ):
        return struct.unpack_from(self._convertPackFmt(byteNum), buf[offset:offset+byteNum], 0)

    def _setMemberForFdcb( self, offset, byteNum, data ):
        struct.pack_into(self._convertPackFmt(byteNum), self.fdcbBuffer, offset, data)

    def _accessTag( self, accessType=kAccessType_Get, fdcbBuf=None):
        if accessType == kAccessType_Set:
            tag = self._getMemberFromFdcb(fdcbBuf, uidef_fdcb.kFlexspiFdcbOffset_tag, uidef_fdcb.kFlexspiFdcbLength_tag)
            self.m_textCtrl_tag.Clear()
            self.m_textCtrl_tag.write(str(hex(tag[0])))
        else:
            self._setMemberForFdcb(uidef_fdcb.kFlexspiFdcbOffset_tag, uidef_fdcb.kFlexspiFdcbLength_tag, int(self.m_textCtrl_tag.GetLineText(0), 16))

    def _accessVersion( self, accessType=kAccessType_Get, fdcbBuf=None):
        if accessType == kAccessType_Set:
            version = self._getMemberFromFdcb(fdcbBuf, uidef_fdcb.kFlexspiFdcbOffset_version, uidef_fdcb.kFlexspiFdcbLength_version)
            self.m_textCtrl_version.Clear()
            self.m_textCtrl_version.write(str(hex(version[0])))
        else:
            self._setMemberForFdcb(uidef_fdcb.kFlexspiFdcbOffset_version, uidef_fdcb.kFlexspiFdcbLength_version, int(self.m_textCtrl_version.GetLineText(0), 16))

    def _recoverLastSettings ( self ):
        if os.path.isfile(self.cfgFdcbBinFilename):
            self.m_filePicker_binFile.SetPath(self.cfgFdcbBinFilename)
            fdcbBuf = None
            with open(self.cfgFdcbBinFilename, 'rb') as fileObj:
                fdcbBuf = fileObj.read()
                fileObj.close()
            self._accessTag(kAccessType_Set, fdcbBuf)
            self._accessVersion(kAccessType_Set, fdcbBuf)

    def callbackSetLookupTable( self, event ):
        lutFrame = ui_cfg_lut.secBootUiCfgLut(None)
        lutFrame.SetTitle(u"LUT Configuration")
        lutFrame.Show(True)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def callbackSelectFdcbFile( self, event ):
        fdcbPath = self.m_filePicker_binFile.GetPath()
        if os.path.isfile(fdcbPath) and os.path.getsize(fdcbPath) == memdef.kMemBlockSize_FDCB:
            if self.cfgFdcbBinFilename != fdcbPath:
                shutil.copy(fdcbPath, self.cfgFdcbBinFilename)
            self._recoverLastSettings()
        else:
            self.popupMsgBox('FDCB file should be 512 bytes raw binary')
            self.m_filePicker_binFile.SetPath('')

    def callbackOk( self, event ):
        self._accessTag(kAccessType_Get)
        self._accessVersion(kAccessType_Get)
        with open(self.cfgFdcbBinFilename, 'wb') as fileObj:
            fdcbBuf = fileObj.write(self.fdcbBuffer)
            fileObj.close()
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

