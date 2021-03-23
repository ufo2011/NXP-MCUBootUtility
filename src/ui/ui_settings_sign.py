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

    def _recoverLastSettings ( self ):
        pass

    def callbackSignPart( self, event ):
        pass

    def _getSignedStart( self ):
        pass

    def _getSignedSize( self ):
        pass

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
