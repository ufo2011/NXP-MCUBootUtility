#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import advSettingsWin_Sign
from utils import sound

class secBootUiSettingsSign(advSettingsWin_Sign.advSettingsWin_Sign):

    def __init__(self, parent):
        advSettingsWin_Sign.advSettingsWin_Sign.__init__(self, parent)
        self._setLanguage()
        signSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Sign)
        self.signSettingsDict = signSettingsDict.copy()
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_signOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_signOpt'][langIndex])
        self.m_staticText_signPart.SetLabel(uilang.kSubLanguageContentDict['sText_signPart'][langIndex])
        self.m_staticText_signStart.SetLabel(uilang.kSubLanguageContentDict['sText_signStart'][langIndex])
        self.m_staticText_signSize.SetLabel(uilang.kSubLanguageContentDict['sText_signSize'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_sign_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_sign_cancel'][langIndex])

    def _updateSignRegionField ( self, isEnabled ):
        if isEnabled:
            self.m_textCtrl_signStart.Enable( True )
            self.m_textCtrl_signSize.Enable( True )
        else:
            self.m_textCtrl_signStart.Enable( False )
            self.m_textCtrl_signSize.Enable( False )

    def _recoverLastSettings ( self ):
        self.m_textCtrl_signStart.Clear()
        self.m_textCtrl_signStart.write(str(hex(self.signSettingsDict['signedStart'])))
        self.m_textCtrl_signSize.Clear()
        self.m_textCtrl_signSize.write(str(hex(self.signSettingsDict['signedSize'])))
        if self.signSettingsDict['isPartSigned']:
            self.m_choice_signPart.SetSelection(1)
        else:
            self.m_choice_signPart.SetSelection(0)
        self._updateSignRegionField(self.signSettingsDict['isPartSigned'])

    def callbackSignPart( self, event ):
        isPartSigned = False
        if self.m_choice_signPart.GetString(self.m_choice_signPart.GetSelection()) == 'Yes':
            isPartSigned = True
        self.signSettingsDict['isPartSigned'] = isPartSigned
        self._updateSignRegionField(isPartSigned)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _convertRegionInfoToVal32( self, regionInfoStr ):
        status = False
        val32 = None
        if len(regionInfoStr) > 2 and regionInfoStr[0:2] == '0x':
            try:
                val32 = int(regionInfoStr[2:len(regionInfoStr)], 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x5000')
        return status, val32

    def _getSignedStart( self ):
        convertStatus, val = self._convertRegionInfoToVal32(self.m_textCtrl_signStart.GetLineText(0))
        if not convertStatus:
            return False
        self.signSettingsDict['signedStart'] = val

    def _getSignedSize( self ):
        convertStatus, val = self._convertRegionInfoToVal32(self.m_textCtrl_signSize.GetLineText(0))
        if not convertStatus:
            return False
        self.signSettingsDict['signedSize'] = val

    def callbackOk( self, event ):
        self._getSignedStart()
        self._getSignedSize()
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Sign, self.signSettingsDict)
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
