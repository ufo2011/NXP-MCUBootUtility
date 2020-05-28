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
import uidef_fdcb
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_LUT
from mem import memdef

kAccessType_Set = 0
kAccessType_Get = 1

kLutGroup_Members = 16

class secBootUiCfgLut(bootDeviceWin_LUT.bootDeviceWin_LUT):

    def __init__(self, parent):
        bootDeviceWin_LUT.bootDeviceWin_LUT.__init__(self, parent)
        self.cfgFdcbBinFilename = None
        self.fdcbBuffer = array.array('c', [chr(0x00)]) * memdef.kMemBlockSize_FDCB
        self.lutGroup = 0

    def setNecessaryInfo( self, cfgFdcbBinFilename ):
        self.cfgFdcbBinFilename = cfgFdcbBinFilename
        if os.path.isfile(self.cfgFdcbBinFilename):
            with open(self.cfgFdcbBinFilename, 'rb+') as fileObj:
                fdcbBytes = fileObj.read()
                for i in range(memdef.kMemBlockSize_FDCB):
                    self.fdcbBuffer[i] = fdcbBytes[i]
                fileObj.close()
            self._recoverLastSettings()

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

    def _getLookupTableItem( self, index ):
        lookupTable = self._getMemberFromFdcb(self.fdcbBuffer, uidef_fdcb.kFlexspiFdcbOffset_lookupTable + index * 4, 4)
        op0 = (lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Op0) >> uidef_fdcb.kFlexspiLutRegShift_Op0
        pad0 = (lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Pad0) >> uidef_fdcb.kFlexspiLutRegShift_Pad0
        cmd0 = int(((lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Cmd0) >> uidef_fdcb.kFlexspiLutRegShift_Cmd0))
        op1 = (lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Op1) >> uidef_fdcb.kFlexspiLutRegShift_Op1
        pad1 = (lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Pad1) >> uidef_fdcb.kFlexspiLutRegShift_Pad1
        cmd1 = int((lookupTable[0] & uidef_fdcb.kFlexspiLutRegMask_Cmd1) >> uidef_fdcb.kFlexspiLutRegShift_Cmd1)
        return (op0, pad0, cmd0, op1, pad1, cmd1)

    def _findMatchedOpSelection( self, choiceObj, op ):
        count = choiceObj.GetCount()
        for i in range(count):
            content = choiceObj.GetString(i)
            value = int(content[0:4], 16)
            if value == op:
                return i
        return 0

    def _setLookupTableItem( self, index, op0, pad0, cmd0, op1, pad1, cmd1 ):
        lookupTable = 0
        lookupTable = lookupTable | (op0 << uidef_fdcb.kFlexspiLutRegShift_Op0)
        lookupTable = lookupTable | (pad0 << uidef_fdcb.kFlexspiLutRegShift_Pad0)
        lookupTable = lookupTable | (cmd0 << uidef_fdcb.kFlexspiLutRegShift_Cmd0)
        lookupTable = lookupTable | (op1 << uidef_fdcb.kFlexspiLutRegShift_Op1)
        lookupTable = lookupTable | (pad1 << uidef_fdcb.kFlexspiLutRegShift_Pad1)
        lookupTable = lookupTable | (cmd1 << uidef_fdcb.kFlexspiLutRegShift_Cmd1)
        self._setMemberForFdcb(uidef_fdcb.kFlexspiFdcbOffset_lookupTable + index * 4, 4, lookupTable)

    def _accessLut16n( self, accessType=kAccessType_Get):
        if accessType == kAccessType_Set:
            op0, pad0, cmd0, op1, pad1, cmd1 = self._getLookupTableItem(self.lutGroup * kLutGroup_Members)
            self.m_choice_op0_16n.SetSelection(self._findMatchedOpSelection(self.m_choice_op0_16n, op0))
            self.m_choice_pad0_16n.SetSelection(pad0)
            self.m_textCtrl_cmd0_16n.Clear()
            self.m_textCtrl_cmd0_16n.write(str(hex(cmd0)))
            self.m_choice_op1_16n.SetSelection(self._findMatchedOpSelection(self.m_choice_op1_16n, op1))
            self.m_choice_pad1_16n.SetSelection(pad1)
            self.m_textCtrl_cmd1_16n.Clear()
            self.m_textCtrl_cmd1_16n.write(str(hex(cmd1)))
        else:
            content = self.m_choice_op0_16n.GetString(self.m_choice_op0_16n.GetSelection())
            op0 = int(content[0:4], 16)
            pad0 = self.m_choice_pad0_16n.GetSelection()
            cmd0 = int(self.m_textCtrl_cmd0_16n.GetLineText(0), 16)
            content = self.m_choice_op1_16n.GetString(self.m_choice_op1_16n.GetSelection())
            op1 = int(content[0:4], 16)
            pad1 = self.m_choice_pad1_16n.GetSelection()
            cmd1 = int(self.m_textCtrl_cmd1_16n.GetLineText(0), 16)
            self._setLookupTableItem(self.lutGroup * kLutGroup_Members, op0, pad0, cmd0, op1, pad1, cmd1)

    def _recoverLastSettings ( self ):
        self._accessLut16n(kAccessType_Set)

    def callbackSetLutGroup( self, event ):
        self.lutGroup = self.m_choice_lutGroup.GetSelection()

    def callbackOk( self, event ):
        self._accessLut16n(kAccessType_Get)
        with open(self.cfgFdcbBinFilename, 'wb') as fileObj:
            fileObj.write(self.fdcbBuffer)
            fileObj.close()
        self.Show(False)

    def callbackCancel( self, event ):
        self.Show(False)

    def callbackClose( self, event ):
        self.Show(False)

