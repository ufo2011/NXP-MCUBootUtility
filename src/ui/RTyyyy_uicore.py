#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from mem import memcore
from run import RTyyyy_rundef
from run import rundef
from fuse import RTyyyy_fusedef

class secBootRTyyyyUi(memcore.secBootMem):

    def __init__(self, parent):
        memcore.secBootMem.__init__(self, parent)
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_initUi()

    def RTyyyy_initUi( self ):
        self.isXipableDevice = False
        self.isNandDevice = False
        self.isSdmmcCard = False
        self._RTyyyy_initTargetSetupValue()
        self.RTyyyy_setTargetSetupValue()

        self.secureBootType = None
        self.keyStorageRegion = None
        self.isCertEnabledForHwCrypto = None
        self._RTyyyy_initSecureBootSeqValue()
        self._RTyyyy_initSecureBootSeqColor()

        self.RTyyyy_setLanguage()

    def _RTyyyy_initTargetSetupValue( self ):
        self.m_choice_bootDevice.Clear()
        self.m_choice_bootDevice.SetItems(RTyyyy_uidef.kBootDevice_Latest)
        totalSel = self.m_choice_bootDevice.GetCount()
        if self.toolCommDict['bootDevice'] < totalSel:
            self.m_choice_bootDevice.SetSelection(self.toolCommDict['bootDevice'])
        else:
            self.m_choice_bootDevice.SetSelection(0)

    def RTyyyy_setTargetSetupValue( self ):
        self.showPageInMainBootSeqWin(uidef.kPageIndex_ImageGenerationSequence)
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.RTyyyy_createMcuTarget()
        self.refreshBootDeviceList()
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['bootDevice'] = self.m_choice_bootDevice.GetSelection()
        if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.isXipableDevice = True
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'flexspinor'
            self.sbAccessBootDeviceMagic = ''
            self.setFlexspiNorDeviceForEvkBoard()
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor:
            self.isXipableDevice = True
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'semcnor'
            self.sbAccessBootDeviceMagic = ''
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_LpspiNor:
            self.isXipableDevice = False
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'spieeprom'
            self.sbAccessBootDeviceMagic = 'spieeprom'
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNand:
            self.isXipableDevice = False
            self.isNandDevice = True
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'flexspinand'
            self.sbAccessBootDeviceMagic = 'flexspinand'
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNand:
            self.isXipableDevice = False
            self.isNandDevice = True
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'semcnand'
            self.sbAccessBootDeviceMagic = 'semcnand'
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_UsdhcSd:
            self.isXipableDevice = False
            self.isNandDevice = True
            self.isSdmmcCard = True
            self.sbEnableBootDeviceMagic = 'sdcard'
            self.sbAccessBootDeviceMagic = 'sdcard'
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_UsdhcMmc:
            self.isXipableDevice = False
            self.isNandDevice = True
            self.isSdmmcCard = True
            self.sbEnableBootDeviceMagic = 'mmccard'
            self.sbAccessBootDeviceMagic = 'mmccard'
        else:
            pass

    def _RTyyyy_initSecureBootSeqValue( self ):
        if not self.initSecureBootTypeList():
            self.m_choice_secureBootType.Clear()
            self.m_choice_secureBootType.SetItems(RTyyyy_uidef.kSecureBootType_Latest)
        totalSel = self.m_choice_secureBootType.GetCount()
        if self.toolCommDict['secBootType'] < totalSel:
            self.m_choice_secureBootType.SetSelection(self.toolCommDict['secBootType'])
        else:
            self.m_choice_secureBootType.SetSelection(0)
        self.m_textCtrl_serial.Clear()
        self.m_textCtrl_serial.write(self.toolCommDict['certSerial'])
        self.m_textCtrl_keyPass.Clear()
        self.m_textCtrl_keyPass.write(self.toolCommDict['certKeyPass'])
        if self.toolCommDict['appFilename'] != None:
            self.m_filePicker_appPath.SetPath(self.toolCommDict['appFilename'])
        self.m_choice_appFormat.SetSelection(self.toolCommDict['appFormat'])
        self._setUserBinaryBaseField()
        self.m_textCtrl_appBaseAddr.Clear()
        self.m_textCtrl_appBaseAddr.write(self.toolCommDict['appBinBaseAddr'])
        self.m_choice_keyStorageRegion.SetSelection(self.toolCommDict['keyStoreRegion'])
        self.m_choice_enableCertForHwCrypto.SetSelection(self.toolCommDict['certOptForHwCrypto'])

    def _RTyyyy_initSecureBootSeqColor ( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
        self.RTyyyy_setSecureBootSeqColor()

    def RTyyyy_setSecureBootButtonColor( self, needToPlaySound=True ):
        activeColor = None
        optionalColor = None
        setEnable = None
        if self.toolRunMode == uidef.kToolRunMode_Entry:
            activeColor = uidef.kBootSeqColor_Invalid
            optionalColor = uidef.kBootSeqColor_Invalid
            setEnable = False
        else:
            activeColor = uidef.kBootSeqColor_Active
            optionalColor = uidef.kBootSeqColor_Optional
            setEnable = True
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        if self.secureBootType == RTyyyy_uidef.kSecureBootType_Development:
            self.m_button_genImage.Enable( setEnable )
            self.m_button_genImage.SetBackgroundColour( activeColor )
            self.m_button_flashImage.Enable( setEnable )
            self.m_button_flashImage.SetBackgroundColour( activeColor )
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabAuth:
            self.m_button_genCert.Enable( setEnable )
            self.m_button_genCert.SetBackgroundColour( activeColor )
            self.m_button_genImage.Enable( setEnable )
            self.m_button_genImage.SetBackgroundColour( activeColor )
            self.m_button_progSrk.Enable( setEnable )
            self.m_button_progSrk.SetBackgroundColour( activeColor )
            self.m_button_flashImage.Enable( setEnable )
            self.m_button_flashImage.SetBackgroundColour( activeColor )
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto:
            if (self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor and self.bootDevice != RTyyyy_uidef.kBootDevice_SemcNor) or \
               self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab:
                self.m_button_genCert.Enable( setEnable )
                self.m_button_genCert.SetBackgroundColour( activeColor )
                self.m_button_genImage.Enable( setEnable )
                self.m_button_genImage.SetBackgroundColour( activeColor )
                self.m_button_progSrk.Enable( setEnable )
                self.m_button_progSrk.SetBackgroundColour( activeColor )
                self.m_button_flashImage.Enable( setEnable )
                self.m_button_flashImage.SetBackgroundColour( activeColor )
                self.m_button_progDek.Enable( setEnable )
                self.m_button_progDek.SetBackgroundColour( activeColor )
        elif self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto:
            if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
                if self.isCertEnabledForHwCrypto:
                    self.m_button_genCert.Enable( setEnable )
                    self.m_button_genCert.SetBackgroundColour( optionalColor )
                    self.m_button_progSrk.Enable( setEnable )
                    self.m_button_progSrk.SetBackgroundColour( optionalColor )
                if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                    self.m_button_prepHwCrypto.Enable( setEnable )
                    self.m_button_prepHwCrypto.SetBackgroundColour( activeColor )
                elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                    self.m_button_prepHwCrypto.Enable( setEnable )
                    self.m_button_prepHwCrypto.SetBackgroundColour( activeColor )
                    self.m_button_operHwCrypto.Enable( setEnable )
                    self.m_button_operHwCrypto.SetBackgroundColour( activeColor )
                    userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_UserKeys)
                    if self.secureBootType == RTyyyy_uidef.kSecureBootType_BeeCrypto:
                        userKeyCmdDict['hw_eng'] = 'bee'
                    elif self.secureBootType == RTyyyy_uidef.kSecureBootType_OtfadCrypto:
                        userKeyCmdDict['hw_eng'] = 'otfad'
                    else:
                        pass
                    uivar.setAdvancedSettings(uidef.kAdvancedSettings_UserKeys, userKeyCtrlDict, userKeyCmdDict)
                else:
                    pass
                self.m_button_genImage.Enable( setEnable )
                self.m_button_genImage.SetBackgroundColour( activeColor )
                self.m_button_flashImage.Enable( setEnable )
                self.m_button_flashImage.SetBackgroundColour( activeColor )
        else:
            pass
        self.m_button_allInOneAction.Enable( True )
        self.m_button_allInOneAction.SetBackgroundColour( uidef.kBootSeqColor_Active )
        self.Refresh()
        if needToPlaySound:
            self.soundEffectFilenameForTask = uidef.kSoundEffectFilename_Restart

    def _RTyyyy_getImgName( self ):
        memType = ''
        hasDcd = ''
        if self.isNandDevice:
            if self.isSdmmcCard:
                memType = 'sdmmc_'
            else:
                memType = 'nand_'
        else:
            memType = 'nor_'
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            hasDcd = 'dcd_'
        return memType, hasDcd

    def RTyyyy_setSecureBootSeqColor( self , needToPlaySound=True ):
        self.hasDynamicLableBeenInit = True
        self.showPageInMainBootSeqWin(uidef.kPageIndex_ImageGenerationSequence)
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.refreshSecureBootTypeList()
        self.toolCommDict['secBootType'] = self.m_choice_secureBootType.GetSelection()
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.resetSecureBootSeqColor()
        self.m_button_genCert.SetLabel(uilang.kMainLanguageContentDict['button_genCert'][self.languageIndex])
        self.m_button_progSrk.SetLabel(uilang.kMainLanguageContentDict['button_progSrk'][self.languageIndex])
        self.m_button_operHwCrypto.SetLabel(uilang.kMainLanguageContentDict['button_operHwCrypto'][self.languageIndex])
        self.m_button_progDek.SetLabel(uilang.kMainLanguageContentDict['button_progDek'][self.languageIndex])
        if self.secureBootType == RTyyyy_uidef.kSecureBootType_Development:
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_u'][self.languageIndex])
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType, strHasDcd = self._RTyyyy_getImgName()
            imgPath = "../img/RT10yy/" + strMemType + "image_" + strHasDcd + "unsigned.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_u'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabAuth:
            self.m_panel_doAuth1_certInput.Enable( True )
            self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_panel_doAuth2_certFmt.Enable( True )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_s'][self.languageIndex])
            self.m_panel_progSrk1_showSrk.Enable( True )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType, strHasDcd = self._RTyyyy_getImgName()
            imgPath = "../img/RT10yy/" + strMemType + "image_" + strHasDcd + "signed.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_s'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto:
            if (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
               (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
                self.resetSecureBootSeqColor()
            else:
                self.m_panel_doAuth1_certInput.Enable( True )
                self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
                self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
                self.m_panel_doAuth2_certFmt.Enable( True )
                self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage1_browseApp.Enable( True )
                self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage2_habCryptoAlgo.Enable( True )
                self.m_panel_genImage2_habCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_se'][self.languageIndex])
                self.m_panel_progSrk1_showSrk.Enable( True )
                self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_flashImage1_showImage.Enable( True )
                self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
                strMemType, strHasDcd = self._RTyyyy_getImgName()
                imgPath = "../img/RT10yy/" + strMemType + "image_" + strHasDcd + "signed_hab_encrypted_nodek.png"
                self.showImageLayout(imgPath.encode('utf-8'))
                self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_e'][self.languageIndex])
                self.m_panel_progDek1_showHabDek.Enable( True )
                self.m_panel_progDek1_showHabDek.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto:
            if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
                self.m_panel_genImage1_browseApp.Enable( True )
                self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage3_enableCertForHwCrypto.Enable( True )
                self.m_panel_genImage3_enableCertForHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.setKeyStorageRegionColor()
                self.setHwCryptoCertColor()
                self.m_panel_flashImage1_showImage.Enable( True )
                self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            else:
                self.resetSecureBootSeqColor()
        else:
            pass
        self.RTyyyy_setSecureBootButtonColor(needToPlaySound)
        self.Refresh()

    def updateImgPictureAfterFlashDek( self ):
        strMemType, strHasDcd = self._RTyyyy_getImgName()
        imgPath = "../img/RT10yy/" + strMemType + "image_" + strHasDcd + "signed_hab_encrypted.png"
        self.showImageLayout(imgPath.encode('utf-8'))

    def getSerialAndKeypassContent( self ):
        serialContent = self.m_textCtrl_serial.GetLineText(0)
        keypassContent = self.m_textCtrl_keyPass.GetLineText(0)
        self.toolCommDict['certSerial'] = serialContent
        self.toolCommDict['certKeyPass'] = keypassContent
        return serialContent, keypassContent

    def setHwCryptoCertColor( self ):
        txt = self.m_choice_enableCertForHwCrypto.GetString(self.m_choice_enableCertForHwCrypto.GetSelection())
        self.toolCommDict['certOptForHwCrypto'] = self.m_choice_enableCertForHwCrypto.GetSelection()
        strMemType, strHasDcd = self._RTyyyy_getImgName()
        imgPath = ""
        strHwCryptoType = ""
        if self.secureBootType == RTyyyy_uidef.kSecureBootType_BeeCrypto:
            strHwCryptoType = 'bee'
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_OtfadCrypto:
            strHwCryptoType = 'otfad'
        else:
            pass
        if txt == 'No':
            self.isCertEnabledForHwCrypto = False
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_u'][self.languageIndex])
            imgPath = "../img/RT10yy/nor_image_" + strHasDcd + "unsigned_" + strHwCryptoType + "_encrypted.png"
        elif txt == 'Yes':
            self.isCertEnabledForHwCrypto = True
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_s'][self.languageIndex])
            imgPath = "../img/RT10yy/nor_image_" + strHasDcd + "signed_" + strHwCryptoType + "_encrypted.png"
        else:
            pass
        self.showImageLayout(imgPath.encode('utf-8'))
        self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_e'][self.languageIndex])
        self.resetCertificateColor()
        if self.isCertEnabledForHwCrypto:
            activeColor = None
            if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                activeColor = uidef.kBootSeqColor_Active
            elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                activeColor = uidef.kBootSeqColor_Optional
            else:
                pass
            self.m_panel_doAuth1_certInput.Enable( True )
            self.m_panel_doAuth1_certInput.SetBackgroundColour( activeColor )
            self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_panel_doAuth2_certFmt.Enable( True )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( activeColor )
            self.m_button_genCert.Enable( True )
            self.m_button_genCert.SetBackgroundColour( activeColor )
            self.m_panel_progSrk1_showSrk.Enable( True )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( activeColor )
            self.m_button_progSrk.Enable( True )
            self.m_button_progSrk.SetBackgroundColour( activeColor )
        self.Refresh()

    def setKeyStorageRegionColor( self ):
        self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
        self.toolCommDict['keyStoreRegion'] = self.m_choice_keyStorageRegion.GetSelection()
        self.resetKeyStorageRegionColor()
        self.m_panel_prepHwCrypto1_hwCryptoKeyRegion.Enable( True )
        self.m_panel_prepHwCrypto1_hwCryptoKeyRegion.SetBackgroundColour( uidef.kBootSeqColor_Active )
        self.m_panel_prepHwCrypto2_hwCryptoAlgo.Enable( True )
        self.m_panel_prepHwCrypto2_hwCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
        if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
            self.m_choice_enableCertForHwCrypto.Clear()
            self.m_choice_enableCertForHwCrypto.SetItems(['Yes'])
            self.m_choice_enableCertForHwCrypto.SetSelection(0)
            self.setHwCryptoCertColor()
            self.m_choice_availHwCryptoEngines.Clear()
            self.m_choice_availHwCryptoEngines.SetItems(['1'])
            self.m_choice_availHwCryptoEngines.SetSelection(0)
            self.m_button_prepHwCrypto.Enable( True )
            self.m_button_prepHwCrypto.SetLabel(uilang.kMainLanguageContentDict['button_prepHwCrypto_p'][self.languageIndex])
            self.m_button_prepHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
            enableCertForHwCryptoTxt = self.m_choice_enableCertForHwCrypto.GetString(self.m_choice_enableCertForHwCrypto.GetSelection())
            self.m_choice_enableCertForHwCrypto.Clear()
            self.m_choice_enableCertForHwCrypto.SetItems(['No', 'Yes'])
            self.m_choice_enableCertForHwCrypto.SetSelection(self.m_choice_enableCertForHwCrypto.FindString(enableCertForHwCryptoTxt))
            self.setHwCryptoCertColor()
            self.m_choice_availHwCryptoEngines.Clear()
            if self.secureBootType == RTyyyy_uidef.kSecureBootType_BeeCrypto:
                self.m_choice_availHwCryptoEngines.SetItems([str(RTyyyy_uidef.kMaxHwCryptoCount_Bee)])
            elif self.secureBootType == RTyyyy_uidef.kSecureBootType_OtfadCrypto:
                self.m_choice_availHwCryptoEngines.SetItems([str(RTyyyy_uidef.kMaxHwCryptoCount_Otfad)])
            else:
                pass
            self.m_choice_availHwCryptoEngines.SetSelection(0)
            self.m_button_prepHwCrypto.Enable( True )
            self.m_button_prepHwCrypto.SetLabel(uilang.kMainLanguageContentDict['button_prepHwCrypto_e'][self.languageIndex])
            self.m_button_prepHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operHwCrypto1_hwCryptoKeyInfo.Enable( True )
            self.m_panel_operHwCrypto1_hwCryptoKeyInfo.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operHwCrypto2_showGp4Dek.Enable( True )
            self.m_panel_operHwCrypto2_showGp4Dek.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operHwCrypto3_showSwgp2Dek.Enable( True )
            self.m_panel_operHwCrypto3_showSwgp2Dek.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_operHwCrypto.Enable( True )
            self.m_button_operHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Active )
        else:
            pass
        self.m_choice_maxFacCnt.Clear()
        if self.secureBootType == RTyyyy_uidef.kSecureBootType_BeeCrypto:
            self.m_choice_maxFacCnt.SetItems([str(RTyyyy_uidef.kMaxFacRegionCount_Bee)])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_OtfadCrypto:
            self.m_choice_maxFacCnt.SetItems([str(RTyyyy_uidef.kMaxFacRegionCount_Otfad)])
        else:
            pass
        self.m_choice_maxFacCnt.SetSelection(0)
        self.Refresh()

    def printSrkData( self, srkStr ):
        self.m_textCtrl_srk256bit.write(srkStr + "\n")

    def clearSrkData( self ):
        self.m_textCtrl_srk256bit.Clear()

    def printHabDekData( self, dekStr ):
        self.m_textCtrl_habDek128bit.write(dekStr + "\n")

    def clearHabDekData( self ):
        self.m_textCtrl_habDek128bit.Clear()

    def printOtpmkDekData( self, dekStr ):
        #self.m_textCtrl_otpmkDek128bit.write(dekStr + "\n")
        pass

    def clearOtpmkDekData( self ):
        #self.m_textCtrl_otpmkDek128bit.Clear()
        pass

    def printGp4DekData( self, dekStr ):
        self.m_textCtrl_gp4Dek128bit.write(dekStr + "\n")

    def clearGp4DekData( self ):
        self.m_textCtrl_gp4Dek128bit.Clear()

    def printSwGp2DekData( self, dekStr ):
        self.m_textCtrl_swgp2Dek128bit.write(dekStr + "\n")

    def clearSwGp2DekData( self ):
        self.m_textCtrl_swgp2Dek128bit.Clear()

    def RTyyyy_updateFuseGroupText( self ):
        self.clearUserFuses()
        if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.m_button_fuse400.SetLabel('Lock')
            self.m_staticText_fuse410.SetLabel('UUID0')
            self.m_staticText_fuse420.SetLabel('UUID1')
            self.m_staticText_fuse430.SetLabel('0x430')
            self.m_staticText_fuse440.SetLabel('0x440')
            self.m_button_fuse450.SetLabel('Cfg0')
            self.m_button_fuse460.SetLabel('Cfg1')
            self.m_button_fuse470.SetLabel('Cfg2')
            self.m_staticText_fuse480.SetLabel('0x480')
            self.m_staticText_fuse490.SetLabel('0x490')
            self.m_staticText_fuse4a0.SetLabel('0x4a0')
            self.m_staticText_fuse4b0.SetLabel('0x4b0')
            self.m_staticText_fuse4c0.SetLabel('0x4c0')
            self.m_staticText_fuse4d0.SetLabel('0x4d0')
            self.m_staticText_fuse4e0.SetLabel('0x4e0')
            self.m_staticText_fuse4f0.SetLabel('0x4f0')
            self.m_staticText_fuse500.SetLabel('OTPMK')
            self.m_staticText_fuse510.SetLabel('OTPMK')
            self.m_staticText_fuse520.SetLabel('OTPMK')
            self.m_staticText_fuse530.SetLabel('OTPMK')
            self.m_staticText_fuse540.SetLabel('OTPMK')
            self.m_staticText_fuse550.SetLabel('OTPMK')
            self.m_staticText_fuse560.SetLabel('OTPMK')
            self.m_staticText_fuse570.SetLabel('OTPMK')
            self.m_staticText_fuse580.SetLabel('SRK0')
            self.m_staticText_fuse590.SetLabel('SRK1')
            self.m_staticText_fuse5a0.SetLabel('SRK2')
            self.m_staticText_fuse5b0.SetLabel('SRK3')
            self.m_staticText_fuse5c0.SetLabel('SRK4')
            self.m_staticText_fuse5d0.SetLabel('SRK5')
            self.m_staticText_fuse5e0.SetLabel('SRK6')
            self.m_staticText_fuse5f0.SetLabel('SRK7')
            self.m_staticText_fuse600.SetLabel('0x600')
            self.m_staticText_fuse610.SetLabel('0x610')
            self.m_staticText_fuse620.SetLabel('0x620')
            self.m_staticText_fuse630.SetLabel('0x630')
            self.m_staticText_fuse640.SetLabel('0x640')
            self.m_staticText_fuse650.SetLabel('0x650')
            self.m_staticText_fuse660.SetLabel('0x660')
            self.m_staticText_fuse670.SetLabel('0x670')
            self.m_staticText_fuse680.SetLabel('0x680')
            self.m_staticText_fuse690.SetLabel('SwGp2')
            self.m_staticText_fuse6a0.SetLabel('SwGp2')
            self.m_staticText_fuse6b0.SetLabel('SwGp2')
            self.m_staticText_fuse6c0.SetLabel('SwGp2')
            self.m_button_fuse6d0.SetLabel('Conf0')
            self.m_button_fuse6e0.SetLabel('Conf1')
            self.m_staticText_fuse6f0.SetLabel('0x6f0')
            self.m_staticText_fuse700.SetLabel('0x700')
            self.m_staticText_fuse710.SetLabel('0x710')
            self.m_staticText_fuse720.SetLabel('0x720')
            self.m_staticText_fuse730.SetLabel('0x730')
            self.m_staticText_fuse740.SetLabel('0x740')
            self.m_staticText_fuse750.SetLabel('0x750')
            self.m_staticText_fuse760.SetLabel('0x760')
            self.m_staticText_fuse770.SetLabel('0x770')
            self.m_staticText_fuse780.SetLabel('0x780')
            self.m_staticText_fuse790.SetLabel('0x790')
            self.m_staticText_fuse7a0.SetLabel('0x7a0')
            self.m_staticText_fuse7b0.SetLabel('0x7b0')
            self.m_staticText_fuse7c0.SetLabel('0x7c0')
            self.m_staticText_fuse7d0.SetLabel('0x7d0')
            self.m_staticText_fuse7e0.SetLabel('0x7e0')
            self.m_staticText_fuse7f0.SetLabel('0x7f0')
            self.m_staticText_fuse800.SetLabel('0x800')
            self.m_staticText_fuse810.SetLabel('0x810')
            self.m_staticText_fuse820.SetLabel('0x820')
            self.m_staticText_fuse830.SetLabel('0x830')
            self.m_staticText_fuse840.SetLabel('0x840')
            self.m_staticText_fuse850.SetLabel('0x850')
            self.m_staticText_fuse860.SetLabel('0x860')
            self.m_staticText_fuse870.SetLabel('0x870')
            self.m_staticText_fuse880.SetLabel('0x880')
            self.m_staticText_fuse890.SetLabel('0x890')
            self.m_staticText_fuse8a0.SetLabel('0x8a0')
            self.m_staticText_fuse8b0.SetLabel('0x8b0')
            self.m_staticText_fuse8c0.SetLabel('Gp4')
            self.m_staticText_fuse8d0.SetLabel('Gp4')
            self.m_staticText_fuse8e0.SetLabel('Gp4')
            self.m_staticText_fuse8f0.SetLabel('Gp4')
        elif self.mcuSeries == uidef.kMcuSeries_iMXRT11yy:
            if self.efuseGroupSel == 0:
                self.m_button_fuse400.SetLabel('800H')
                self.m_staticText_fuse410.SetLabel('0x810')
                self.m_staticText_fuse420.SetLabel('0x820')
                self.m_staticText_fuse430.SetLabel('0x830')
                self.m_staticText_fuse440.SetLabel('0x840')
                self.m_button_fuse450.SetLabel('850H')
                self.m_button_fuse460.SetLabel('860H')
                self.m_button_fuse470.SetLabel('870H')
                self.m_staticText_fuse480.SetLabel('0x880')
                self.m_staticText_fuse490.SetLabel('0x890')
                self.m_staticText_fuse4a0.SetLabel('0x8a0')
                self.m_staticText_fuse4b0.SetLabel('0x8b0')
                self.m_staticText_fuse4c0.SetLabel('0x8c0')
                self.m_staticText_fuse4d0.SetLabel('0x8d0')
                self.m_staticText_fuse4e0.SetLabel('0x8e0')
                self.m_staticText_fuse4f0.SetLabel('0x8f0')
                self.m_staticText_fuse500.SetLabel('UUID0')
                self.m_staticText_fuse510.SetLabel('UUID1')
                self.m_staticText_fuse520.SetLabel('0x920')
                self.m_staticText_fuse530.SetLabel('0x930')
                self.m_staticText_fuse540.SetLabel('Cfg0')
                self.m_staticText_fuse550.SetLabel('Cfg1')
                self.m_staticText_fuse560.SetLabel('0x960')
                self.m_staticText_fuse570.SetLabel('0x970')
                self.m_staticText_fuse580.SetLabel('0x980')
                self.m_staticText_fuse590.SetLabel('0x990')
                self.m_staticText_fuse5a0.SetLabel('0x9a0')
                self.m_staticText_fuse5b0.SetLabel('0x9b0')
                self.m_staticText_fuse5c0.SetLabel('0x9c0')
                self.m_staticText_fuse5d0.SetLabel('0x9d0')
                self.m_staticText_fuse5e0.SetLabel('0x9e0')
                self.m_staticText_fuse5f0.SetLabel('0x9f0')
                self.m_staticText_fuse600.SetLabel('0xa00')
                self.m_staticText_fuse610.SetLabel('0xa10')
                self.m_staticText_fuse620.SetLabel('0xa20')
                self.m_staticText_fuse630.SetLabel('0xa30')
                self.m_staticText_fuse640.SetLabel('0xa40')
                self.m_staticText_fuse650.SetLabel('0xa50')
                self.m_staticText_fuse660.SetLabel('0xa60')
                self.m_staticText_fuse670.SetLabel('0xa70')
                self.m_staticText_fuse680.SetLabel('0xa80')
                self.m_staticText_fuse690.SetLabel('0xa90')
                self.m_staticText_fuse6a0.SetLabel('0xaa0')
                self.m_staticText_fuse6b0.SetLabel('0xab0')
                self.m_staticText_fuse6c0.SetLabel('0xac0')
                self.m_button_fuse6d0.SetLabel('ad0H')
                self.m_button_fuse6e0.SetLabel('ae0H')
                self.m_staticText_fuse6f0.SetLabel('0xaf0')
                self.m_staticText_fuse700.SetLabel('M7SRK')
                self.m_staticText_fuse710.SetLabel('M7SRK')
                self.m_staticText_fuse720.SetLabel('M7SRK')
                self.m_staticText_fuse730.SetLabel('M7SRK')
                self.m_staticText_fuse740.SetLabel('M7SRK')
                self.m_staticText_fuse750.SetLabel('M7SRK')
                self.m_staticText_fuse760.SetLabel('M7SRK')
                self.m_staticText_fuse770.SetLabel('M7SRK')
                self.m_staticText_fuse780.SetLabel('M4SRK')
                self.m_staticText_fuse790.SetLabel('M4SRK')
                self.m_staticText_fuse7a0.SetLabel('M4SRK')
                self.m_staticText_fuse7b0.SetLabel('M4SRK')
                self.m_staticText_fuse7c0.SetLabel('M4SRK')
                self.m_staticText_fuse7d0.SetLabel('M4SRK')
                self.m_staticText_fuse7e0.SetLabel('M4SRK')
                self.m_staticText_fuse7f0.SetLabel('M4SRK')
                self.m_staticText_fuse800.SetLabel('0xc00')
                self.m_staticText_fuse810.SetLabel('0xc10')
                self.m_staticText_fuse820.SetLabel('0xc20')
                self.m_staticText_fuse830.SetLabel('0xc30')
                self.m_staticText_fuse840.SetLabel('0xc40')
                self.m_staticText_fuse850.SetLabel('0xc50')
                self.m_staticText_fuse860.SetLabel('0xc60')
                self.m_staticText_fuse870.SetLabel('0xc70')
                self.m_staticText_fuse880.SetLabel('0xc80')
                self.m_staticText_fuse890.SetLabel('0xc90')
                self.m_staticText_fuse8a0.SetLabel('0xca0')
                self.m_staticText_fuse8b0.SetLabel('0xcb0')
                self.m_staticText_fuse8c0.SetLabel('0xcc0')
                self.m_staticText_fuse8d0.SetLabel('0xcd0')
                self.m_staticText_fuse8e0.SetLabel('0xce0')
                self.m_staticText_fuse8f0.SetLabel('0xcf0')
            elif self.efuseGroupSel == 1:
                self.m_button_fuse400.SetLabel('OTPMK')
                self.m_staticText_fuse410.SetLabel('OTPMK')
                self.m_staticText_fuse420.SetLabel('OTPMK')
                self.m_staticText_fuse430.SetLabel('OTPMK')
                self.m_staticText_fuse440.SetLabel('OTPMK')
                self.m_button_fuse450.SetLabel('OTPMK')
                self.m_button_fuse460.SetLabel('OTPMK')
                self.m_button_fuse470.SetLabel('OTPMK')
                self.m_staticText_fuse480.SetLabel('0xd80')
                self.m_staticText_fuse490.SetLabel('0xd90')
                self.m_staticText_fuse4a0.SetLabel('0xda0')
                self.m_staticText_fuse4b0.SetLabel('0xdb0')
                self.m_staticText_fuse4c0.SetLabel('0xdc0')
                self.m_staticText_fuse4d0.SetLabel('0xdd0')
                self.m_staticText_fuse4e0.SetLabel('0xde0')
                self.m_staticText_fuse4f0.SetLabel('0xdf0')
                self.m_staticText_fuse500.SetLabel('KEY1')
                self.m_staticText_fuse510.SetLabel('KEY1')
                self.m_staticText_fuse520.SetLabel('KEY1')
                self.m_staticText_fuse530.SetLabel('KEY1')
                self.m_staticText_fuse540.SetLabel('KEY1')
                self.m_staticText_fuse550.SetLabel('KEY1')
                self.m_staticText_fuse560.SetLabel('KEY1')
                self.m_staticText_fuse570.SetLabel('KEY1')
                self.m_staticText_fuse580.SetLabel('KEY2')
                self.m_staticText_fuse590.SetLabel('KEY2')
                self.m_staticText_fuse5a0.SetLabel('KEY2')
                self.m_staticText_fuse5b0.SetLabel('KEY2')
                self.m_staticText_fuse5c0.SetLabel('KEY2')
                self.m_staticText_fuse5d0.SetLabel('KEY2')
                self.m_staticText_fuse5e0.SetLabel('KEY2')
                self.m_staticText_fuse5f0.SetLabel('KEY2')
                self.m_staticText_fuse600.SetLabel('KEY3')
                self.m_staticText_fuse610.SetLabel('KEY3')
                self.m_staticText_fuse620.SetLabel('KEY3')
                self.m_staticText_fuse630.SetLabel('KEY3')
                self.m_staticText_fuse640.SetLabel('KEY3')
                self.m_staticText_fuse650.SetLabel('KEY3')
                self.m_staticText_fuse660.SetLabel('KEY3')
                self.m_staticText_fuse670.SetLabel('KEY3')
                self.m_staticText_fuse680.SetLabel('KEY4')
                self.m_staticText_fuse690.SetLabel('KEY4')
                self.m_staticText_fuse6a0.SetLabel('KEY4')
                self.m_staticText_fuse6b0.SetLabel('KEY4')
                self.m_staticText_fuse6c0.SetLabel('KEY4')
                self.m_button_fuse6d0.SetLabel('KEY4')
                self.m_button_fuse6e0.SetLabel('KEY4')
                self.m_staticText_fuse6f0.SetLabel('KEY4')
                self.m_staticText_fuse700.SetLabel('KEY5')
                self.m_staticText_fuse710.SetLabel('KEY5')
                self.m_staticText_fuse720.SetLabel('KEY5')
                self.m_staticText_fuse730.SetLabel('KEY5')
                self.m_staticText_fuse740.SetLabel('KEY5')
                self.m_staticText_fuse750.SetLabel('KEY5')
                self.m_staticText_fuse760.SetLabel('KEY5')
                self.m_staticText_fuse770.SetLabel('KEY5')
                self.m_staticText_fuse780.SetLabel('1080H')
                self.m_staticText_fuse790.SetLabel('1090H')
                self.m_staticText_fuse7a0.SetLabel('10a0H')
                self.m_staticText_fuse7b0.SetLabel('10b0H')
                self.m_staticText_fuse7c0.SetLabel('10c0H')
                self.m_staticText_fuse7d0.SetLabel('10d0H')
                self.m_staticText_fuse7e0.SetLabel('10e0H')
                self.m_staticText_fuse7f0.SetLabel('10f0H')
                self.m_staticText_fuse800.SetLabel('RomP1')
                self.m_staticText_fuse810.SetLabel('RomP1')
                self.m_staticText_fuse820.SetLabel('RomP1')
                self.m_staticText_fuse830.SetLabel('RomP1')
                self.m_staticText_fuse840.SetLabel('RomP1')
                self.m_staticText_fuse850.SetLabel('RomP1')
                self.m_staticText_fuse860.SetLabel('RomP1')
                self.m_staticText_fuse870.SetLabel('RomP1')
                self.m_staticText_fuse880.SetLabel('RomP1')
                self.m_staticText_fuse890.SetLabel('RomP1')
                self.m_staticText_fuse8a0.SetLabel('RomP1')
                self.m_staticText_fuse8b0.SetLabel('RomP1')
                self.m_staticText_fuse8c0.SetLabel('RomP1')
                self.m_staticText_fuse8d0.SetLabel('RomP1')
                self.m_staticText_fuse8e0.SetLabel('RomP1')
                self.m_staticText_fuse8f0.SetLabel('RomP1')
            elif self.efuseGroupSel == 2:
                self.m_button_fuse400.SetLabel('RomP2')
                self.m_staticText_fuse410.SetLabel('RomP2')
                self.m_staticText_fuse420.SetLabel('RomP2')
                self.m_staticText_fuse430.SetLabel('RomP2')
                self.m_staticText_fuse440.SetLabel('RomP2')
                self.m_button_fuse450.SetLabel('RomP2')
                self.m_button_fuse460.SetLabel('RomP2')
                self.m_button_fuse470.SetLabel('RomP2')
                self.m_staticText_fuse480.SetLabel('RomP2')
                self.m_staticText_fuse490.SetLabel('RomP2')
                self.m_staticText_fuse4a0.SetLabel('RomP2')
                self.m_staticText_fuse4b0.SetLabel('RomP2')
                self.m_staticText_fuse4c0.SetLabel('RomP2')
                self.m_staticText_fuse4d0.SetLabel('RomP2')
                self.m_staticText_fuse4e0.SetLabel('RomP2')
                self.m_staticText_fuse4f0.SetLabel('RomP2')
                self.m_staticText_fuse500.SetLabel('GP1')
                self.m_staticText_fuse510.SetLabel('GP1')
                self.m_staticText_fuse520.SetLabel('GP1')
                self.m_staticText_fuse530.SetLabel('GP1')
                self.m_staticText_fuse540.SetLabel('GP1')
                self.m_staticText_fuse550.SetLabel('GP1')
                self.m_staticText_fuse560.SetLabel('GP1')
                self.m_staticText_fuse570.SetLabel('GP1')
                self.m_staticText_fuse580.SetLabel('GP1')
                self.m_staticText_fuse590.SetLabel('GP1')
                self.m_staticText_fuse5a0.SetLabel('GP1')
                self.m_staticText_fuse5b0.SetLabel('GP1')
                self.m_staticText_fuse5c0.SetLabel('GP1')
                self.m_staticText_fuse5d0.SetLabel('GP1')
                self.m_staticText_fuse5e0.SetLabel('GP1')
                self.m_staticText_fuse5f0.SetLabel('GP1')
                self.m_staticText_fuse600.SetLabel('GP2')
                self.m_staticText_fuse610.SetLabel('GP2')
                self.m_staticText_fuse620.SetLabel('GP2')
                self.m_staticText_fuse630.SetLabel('GP2')
                self.m_staticText_fuse640.SetLabel('GP2')
                self.m_staticText_fuse650.SetLabel('GP2')
                self.m_staticText_fuse660.SetLabel('GP2')
                self.m_staticText_fuse670.SetLabel('GP2')
                self.m_staticText_fuse680.SetLabel('GP2')
                self.m_staticText_fuse690.SetLabel('GP2')
                self.m_staticText_fuse6a0.SetLabel('GP2')
                self.m_staticText_fuse6b0.SetLabel('GP2')
                self.m_staticText_fuse6c0.SetLabel('GP2')
                self.m_button_fuse6d0.SetLabel('GP2')
                self.m_button_fuse6e0.SetLabel('GP2')
                self.m_staticText_fuse6f0.SetLabel('GP2')
                self.m_staticText_fuse700.SetLabel('GP3')
                self.m_staticText_fuse710.SetLabel('GP3')
                self.m_staticText_fuse720.SetLabel('GP3')
                self.m_staticText_fuse730.SetLabel('GP3')
                self.m_staticText_fuse740.SetLabel('GP3')
                self.m_staticText_fuse750.SetLabel('GP3')
                self.m_staticText_fuse760.SetLabel('GP3')
                self.m_staticText_fuse770.SetLabel('GP3')
                self.m_staticText_fuse780.SetLabel('GP3')
                self.m_staticText_fuse790.SetLabel('GP3')
                self.m_staticText_fuse7a0.SetLabel('GP3')
                self.m_staticText_fuse7b0.SetLabel('GP3')
                self.m_staticText_fuse7c0.SetLabel('GP3')
                self.m_staticText_fuse7d0.SetLabel('GP3')
                self.m_staticText_fuse7e0.SetLabel('GP3')
                self.m_staticText_fuse7f0.SetLabel('GP3')
                self.m_staticText_fuse800.SetLabel('GP4')
                self.m_staticText_fuse810.SetLabel('GP4')
                self.m_staticText_fuse820.SetLabel('GP4')
                self.m_staticText_fuse830.SetLabel('GP4')
                self.m_staticText_fuse840.SetLabel('GP4')
                self.m_staticText_fuse850.SetLabel('GP4')
                self.m_staticText_fuse860.SetLabel('GP4')
                self.m_staticText_fuse870.SetLabel('GP4')
                self.m_staticText_fuse880.SetLabel('GP4')
                self.m_staticText_fuse890.SetLabel('GP4')
                self.m_staticText_fuse8a0.SetLabel('GP4')
                self.m_staticText_fuse8b0.SetLabel('GP4')
                self.m_staticText_fuse8c0.SetLabel('GP4')
                self.m_staticText_fuse8d0.SetLabel('GP4')
                self.m_staticText_fuse8e0.SetLabel('GP4')
                self.m_staticText_fuse8f0.SetLabel('GP4')
            elif self.efuseGroupSel == 3:
                self.m_button_fuse400.SetLabel('GP5')
                self.m_staticText_fuse410.SetLabel('GP5')
                self.m_staticText_fuse420.SetLabel('GP5')
                self.m_staticText_fuse430.SetLabel('GP5')
                self.m_staticText_fuse440.SetLabel('GP5')
                self.m_button_fuse450.SetLabel('GP5')
                self.m_button_fuse460.SetLabel('GP5')
                self.m_button_fuse470.SetLabel('GP5')
                self.m_staticText_fuse480.SetLabel('GP5')
                self.m_staticText_fuse490.SetLabel('GP5')
                self.m_staticText_fuse4a0.SetLabel('GP5')
                self.m_staticText_fuse4b0.SetLabel('GP5')
                self.m_staticText_fuse4c0.SetLabel('GP5')
                self.m_staticText_fuse4d0.SetLabel('GP5')
                self.m_staticText_fuse4e0.SetLabel('GP5')
                self.m_staticText_fuse4f0.SetLabel('GP5')
                self.m_staticText_fuse500.SetLabel('1800H')
                self.m_staticText_fuse510.SetLabel('1810H')
                self.m_staticText_fuse520.SetLabel('1820H')
                self.m_staticText_fuse530.SetLabel('1830H')
                self.m_staticText_fuse540.SetLabel('1840H')
                self.m_staticText_fuse550.SetLabel('1850H')
                self.m_staticText_fuse560.SetLabel('1860H')
                self.m_staticText_fuse570.SetLabel('1870H')
                self.m_staticText_fuse580.SetLabel('1880H')
                self.m_staticText_fuse590.SetLabel('1890H')
                self.m_staticText_fuse5a0.SetLabel('18a0H')
                self.m_staticText_fuse5b0.SetLabel('18b0H')
                self.m_staticText_fuse5c0.SetLabel('18c0H')
                self.m_staticText_fuse5d0.SetLabel('18d0H')
                self.m_staticText_fuse5e0.SetLabel('18e0H')
                self.m_staticText_fuse5f0.SetLabel('18f0H')
                self.m_staticText_fuse600.SetLabel('N/A')
                self.m_staticText_fuse610.SetLabel('N/A')
                self.m_staticText_fuse620.SetLabel('N/A')
                self.m_staticText_fuse630.SetLabel('N/A')
                self.m_staticText_fuse640.SetLabel('N/A')
                self.m_staticText_fuse650.SetLabel('N/A')
                self.m_staticText_fuse660.SetLabel('N/A')
                self.m_staticText_fuse670.SetLabel('N/A')
                self.m_staticText_fuse680.SetLabel('N/A')
                self.m_staticText_fuse690.SetLabel('N/A')
                self.m_staticText_fuse6a0.SetLabel('N/A')
                self.m_staticText_fuse6b0.SetLabel('N/A')
                self.m_staticText_fuse6c0.SetLabel('N/A')
                self.m_button_fuse6d0.SetLabel('N/A')
                self.m_button_fuse6e0.SetLabel('N/A')
                self.m_staticText_fuse6f0.SetLabel('N/A')
                self.m_staticText_fuse700.SetLabel('N/A')
                self.m_staticText_fuse710.SetLabel('N/A')
                self.m_staticText_fuse720.SetLabel('N/A')
                self.m_staticText_fuse730.SetLabel('N/A')
                self.m_staticText_fuse740.SetLabel('N/A')
                self.m_staticText_fuse750.SetLabel('N/A')
                self.m_staticText_fuse760.SetLabel('N/A')
                self.m_staticText_fuse770.SetLabel('N/A')
                self.m_staticText_fuse780.SetLabel('N/A')
                self.m_staticText_fuse790.SetLabel('N/A')
                self.m_staticText_fuse7a0.SetLabel('N/A')
                self.m_staticText_fuse7b0.SetLabel('N/A')
                self.m_staticText_fuse7c0.SetLabel('N/A')
                self.m_staticText_fuse7d0.SetLabel('N/A')
                self.m_staticText_fuse7e0.SetLabel('N/A')
                self.m_staticText_fuse7f0.SetLabel('N/A')
                self.m_staticText_fuse800.SetLabel('N/A')
                self.m_staticText_fuse810.SetLabel('N/A')
                self.m_staticText_fuse820.SetLabel('N/A')
                self.m_staticText_fuse830.SetLabel('N/A')
                self.m_staticText_fuse840.SetLabel('N/A')
                self.m_staticText_fuse850.SetLabel('N/A')
                self.m_staticText_fuse860.SetLabel('N/A')
                self.m_staticText_fuse870.SetLabel('N/A')
                self.m_staticText_fuse880.SetLabel('N/A')
                self.m_staticText_fuse890.SetLabel('N/A')
                self.m_staticText_fuse8a0.SetLabel('N/A')
                self.m_staticText_fuse8b0.SetLabel('N/A')
                self.m_staticText_fuse8c0.SetLabel('N/A')
                self.m_staticText_fuse8d0.SetLabel('N/A')
                self.m_staticText_fuse8e0.SetLabel('N/A')
                self.m_staticText_fuse8f0.SetLabel('N/A')
            else:
                pass
        else:
            pass

    def RTyyyy_updateFuseRegionField( self ):
        self.resetFuseOtpRegionField()
        color = None
        if self.toolRunMode == uidef.kToolRunMode_Entry:
            color = wx.SYS_COLOUR_GRAYTEXT
            if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
                self.m_textCtrl_fuse400.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                self.m_textCtrl_fuse430.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse440.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                self.m_textCtrl_fuse480.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse490.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse4f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse500.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse510.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse520.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse530.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse540.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse550.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse560.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse570.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                self.m_textCtrl_fuse600.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse610.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse620.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse630.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse640.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse650.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse660.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse670.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse680.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                self.m_textCtrl_fuse6f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse700.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse710.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse720.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse730.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse740.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse750.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse760.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse770.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse780.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse790.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse7f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse800.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse810.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse820.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse830.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse840.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse850.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse860.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse870.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse880.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse890.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse8a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                self.m_textCtrl_fuse8b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
            elif self.mcuSeries == uidef.kMcuSeries_iMXRT11yy:
                if self.efuseGroupSel == 0:
                    self.m_textCtrl_fuse400.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse410.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse420.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse430.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse440.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse450.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse460.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse470.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse480.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse490.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                    self.m_textCtrl_fuse5c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse5d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse5e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse5f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse600.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse610.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse620.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse630.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse640.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse650.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse660.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse670.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse680.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse690.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                    self.m_textCtrl_fuse6f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                    self.m_textCtrl_fuse800.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse810.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse820.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse830.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse840.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse850.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse860.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                    self.m_textCtrl_fuse8b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                elif self.efuseGroupSel == 1:
                    self.m_textCtrl_fuse400.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse410.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse420.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse430.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse440.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse450.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse460.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse470.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse480.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse490.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

                    self.m_textCtrl_fuse780.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse790.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse800.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse810.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse820.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse830.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse840.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse850.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse860.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse870.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse880.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse890.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                elif self.efuseGroupSel == 2:
                    self.m_textCtrl_fuse400.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse410.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse420.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse430.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse440.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse450.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse460.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse470.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse480.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse490.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse4f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                elif self.efuseGroupSel == 3:
                    self.m_textCtrl_fuse600.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse610.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse620.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse630.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse640.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse650.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse660.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse670.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse680.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse690.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse6f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse700.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse710.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse720.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse730.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse740.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse750.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse760.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse770.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse780.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse790.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse7f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse800.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse810.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse820.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse830.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse840.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse850.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse860.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse870.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse880.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse890.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                    self.m_textCtrl_fuse8f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
                else:
                    pass
            else:
                pass
        self.Refresh()

    def RTyyyy_showScannedFuses( self , scannedFuseList ):
        efuseDict = uivar.getEfuseSettings()

        self.clearUserFuses()

        self.m_textCtrl_fuse400.write(self.parseReadFuseValue(scannedFuseList[0]))
        efuseDict['0x400_lock'] = scannedFuseList[0]
        self.m_textCtrl_fuse410.write(self.parseReadFuseValue(scannedFuseList[1]))
        self.m_textCtrl_fuse420.write(self.parseReadFuseValue(scannedFuseList[2]))
        self.m_textCtrl_fuse430.write(self.parseReadFuseValue(scannedFuseList[3]))
        self.m_textCtrl_fuse440.write(self.parseReadFuseValue(scannedFuseList[4]))
        self.m_textCtrl_fuse450.write(self.parseReadFuseValue(scannedFuseList[5]))
        efuseDict['0x450_bootCfg0'] = scannedFuseList[5]
        self.m_textCtrl_fuse460.write(self.parseReadFuseValue(scannedFuseList[6]))
        efuseDict['0x460_bootCfg1'] = scannedFuseList[6]
        self.m_textCtrl_fuse470.write(self.parseReadFuseValue(scannedFuseList[7]))
        efuseDict['0x470_bootCfg2'] = scannedFuseList[7]
        self.m_textCtrl_fuse480.write(self.parseReadFuseValue(scannedFuseList[8]))
        self.m_textCtrl_fuse490.write(self.parseReadFuseValue(scannedFuseList[9]))
        self.m_textCtrl_fuse4a0.write(self.parseReadFuseValue(scannedFuseList[10]))
        self.m_textCtrl_fuse4b0.write(self.parseReadFuseValue(scannedFuseList[11]))
        self.m_textCtrl_fuse4c0.write(self.parseReadFuseValue(scannedFuseList[12]))
        self.m_textCtrl_fuse4d0.write(self.parseReadFuseValue(scannedFuseList[13]))
        self.m_textCtrl_fuse4e0.write(self.parseReadFuseValue(scannedFuseList[14]))
        self.m_textCtrl_fuse4f0.write(self.parseReadFuseValue(scannedFuseList[15]))

        self.m_textCtrl_fuse500.write(self.parseReadFuseValue(scannedFuseList[16]))
        self.m_textCtrl_fuse510.write(self.parseReadFuseValue(scannedFuseList[17]))
        self.m_textCtrl_fuse520.write(self.parseReadFuseValue(scannedFuseList[18]))
        self.m_textCtrl_fuse530.write(self.parseReadFuseValue(scannedFuseList[19]))
        self.m_textCtrl_fuse540.write(self.parseReadFuseValue(scannedFuseList[20]))
        self.m_textCtrl_fuse550.write(self.parseReadFuseValue(scannedFuseList[21]))
        self.m_textCtrl_fuse560.write(self.parseReadFuseValue(scannedFuseList[22]))
        self.m_textCtrl_fuse570.write(self.parseReadFuseValue(scannedFuseList[23]))
        self.m_textCtrl_fuse580.write(self.parseReadFuseValue(scannedFuseList[24]))
        self.m_textCtrl_fuse590.write(self.parseReadFuseValue(scannedFuseList[25]))
        self.m_textCtrl_fuse5a0.write(self.parseReadFuseValue(scannedFuseList[26]))
        self.m_textCtrl_fuse5b0.write(self.parseReadFuseValue(scannedFuseList[27]))
        self.m_textCtrl_fuse5c0.write(self.parseReadFuseValue(scannedFuseList[28]))
        self.m_textCtrl_fuse5d0.write(self.parseReadFuseValue(scannedFuseList[29]))
        self.m_textCtrl_fuse5e0.write(self.parseReadFuseValue(scannedFuseList[30]))
        self.m_textCtrl_fuse5f0.write(self.parseReadFuseValue(scannedFuseList[31]))

        self.m_textCtrl_fuse600.write(self.parseReadFuseValue(scannedFuseList[32]))
        self.m_textCtrl_fuse610.write(self.parseReadFuseValue(scannedFuseList[33]))
        self.m_textCtrl_fuse620.write(self.parseReadFuseValue(scannedFuseList[34]))
        self.m_textCtrl_fuse630.write(self.parseReadFuseValue(scannedFuseList[35]))
        self.m_textCtrl_fuse640.write(self.parseReadFuseValue(scannedFuseList[36]))
        self.m_textCtrl_fuse650.write(self.parseReadFuseValue(scannedFuseList[37]))
        self.m_textCtrl_fuse660.write(self.parseReadFuseValue(scannedFuseList[38]))
        self.m_textCtrl_fuse670.write(self.parseReadFuseValue(scannedFuseList[39]))
        self.m_textCtrl_fuse680.write(self.parseReadFuseValue(scannedFuseList[40]))
        self.m_textCtrl_fuse690.write(self.parseReadFuseValue(scannedFuseList[41]))
        self.m_textCtrl_fuse6a0.write(self.parseReadFuseValue(scannedFuseList[42]))
        self.m_textCtrl_fuse6b0.write(self.parseReadFuseValue(scannedFuseList[43]))
        self.m_textCtrl_fuse6c0.write(self.parseReadFuseValue(scannedFuseList[44]))
        self.m_textCtrl_fuse6d0.write(self.parseReadFuseValue(scannedFuseList[45]))
        efuseDict['0x6d0_miscConf0'] = scannedFuseList[45]
        self.m_textCtrl_fuse6e0.write(self.parseReadFuseValue(scannedFuseList[46]))
        efuseDict['0x6e0_miscConf1'] = scannedFuseList[46]
        self.m_textCtrl_fuse6f0.write(self.parseReadFuseValue(scannedFuseList[47]))

        self.m_textCtrl_fuse700.write(self.parseReadFuseValue(scannedFuseList[48]))
        self.m_textCtrl_fuse710.write(self.parseReadFuseValue(scannedFuseList[49]))
        self.m_textCtrl_fuse720.write(self.parseReadFuseValue(scannedFuseList[50]))
        self.m_textCtrl_fuse730.write(self.parseReadFuseValue(scannedFuseList[51]))
        self.m_textCtrl_fuse740.write(self.parseReadFuseValue(scannedFuseList[52]))
        self.m_textCtrl_fuse750.write(self.parseReadFuseValue(scannedFuseList[53]))
        self.m_textCtrl_fuse760.write(self.parseReadFuseValue(scannedFuseList[54]))
        self.m_textCtrl_fuse770.write(self.parseReadFuseValue(scannedFuseList[55]))
        self.m_textCtrl_fuse780.write(self.parseReadFuseValue(scannedFuseList[56]))
        self.m_textCtrl_fuse790.write(self.parseReadFuseValue(scannedFuseList[57]))
        self.m_textCtrl_fuse7a0.write(self.parseReadFuseValue(scannedFuseList[58]))
        self.m_textCtrl_fuse7b0.write(self.parseReadFuseValue(scannedFuseList[59]))
        self.m_textCtrl_fuse7c0.write(self.parseReadFuseValue(scannedFuseList[60]))
        self.m_textCtrl_fuse7d0.write(self.parseReadFuseValue(scannedFuseList[61]))
        self.m_textCtrl_fuse7e0.write(self.parseReadFuseValue(scannedFuseList[62]))
        self.m_textCtrl_fuse7f0.write(self.parseReadFuseValue(scannedFuseList[63]))

        self.m_textCtrl_fuse800.write(self.parseReadFuseValue(scannedFuseList[64]))
        self.m_textCtrl_fuse810.write(self.parseReadFuseValue(scannedFuseList[65]))
        self.m_textCtrl_fuse820.write(self.parseReadFuseValue(scannedFuseList[66]))
        self.m_textCtrl_fuse830.write(self.parseReadFuseValue(scannedFuseList[67]))
        self.m_textCtrl_fuse840.write(self.parseReadFuseValue(scannedFuseList[68]))
        self.m_textCtrl_fuse850.write(self.parseReadFuseValue(scannedFuseList[69]))
        self.m_textCtrl_fuse860.write(self.parseReadFuseValue(scannedFuseList[70]))
        self.m_textCtrl_fuse870.write(self.parseReadFuseValue(scannedFuseList[71]))
        self.m_textCtrl_fuse880.write(self.parseReadFuseValue(scannedFuseList[72]))
        self.m_textCtrl_fuse890.write(self.parseReadFuseValue(scannedFuseList[73]))
        self.m_textCtrl_fuse8a0.write(self.parseReadFuseValue(scannedFuseList[74]))
        self.m_textCtrl_fuse8b0.write(self.parseReadFuseValue(scannedFuseList[75]))
        self.m_textCtrl_fuse8c0.write(self.parseReadFuseValue(scannedFuseList[76]))
        self.m_textCtrl_fuse8d0.write(self.parseReadFuseValue(scannedFuseList[77]))
        self.m_textCtrl_fuse8e0.write(self.parseReadFuseValue(scannedFuseList[78]))
        self.m_textCtrl_fuse8f0.write(self.parseReadFuseValue(scannedFuseList[79]))

        uivar.setEfuseSettings(efuseDict)

    def enterSettableEfuse( self, fuseIndex ):
        efuseDict = uivar.getEfuseSettings()
        if fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_LOCK']:
            efuseDict['0x400_lock'] = self.parseUserFuseValue(self.m_textCtrl_fuse400.GetLineText(0))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG0']:
            efuseDict['0x450_bootCfg0'] = self.parseUserFuseValue(self.m_textCtrl_fuse450.GetLineText(0))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG1']:
            efuseDict['0x460_bootCfg1'] = self.parseUserFuseValue(self.m_textCtrl_fuse460.GetLineText(0))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG2']:
            efuseDict['0x470_bootCfg2'] = self.parseUserFuseValue(self.m_textCtrl_fuse470.GetLineText(0))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF0']:
            efuseDict['0x6d0_miscConf0'] = self.parseUserFuseValue(self.m_textCtrl_fuse6d0.GetLineText(0))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF1']:
            efuseDict['0x6e0_miscConf1'] = self.parseUserFuseValue(self.m_textCtrl_fuse6e0.GetLineText(0))
        else:
            pass
        uivar.setEfuseSettings(efuseDict)

    def showSettedEfuse( self , fuseIndex, fuseValue ):
        if fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_LOCK']:
            self.m_textCtrl_fuse400.Clear()
            self.m_textCtrl_fuse400.write(self.parseReadFuseValue(fuseValue))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG0']:
            self.m_textCtrl_fuse450.Clear()
            self.m_textCtrl_fuse450.write(self.parseReadFuseValue(fuseValue))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG1']:
            self.m_textCtrl_fuse460.Clear()
            self.m_textCtrl_fuse460.write(self.parseReadFuseValue(fuseValue))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG2']:
            self.m_textCtrl_fuse470.Clear()
            self.m_textCtrl_fuse470.write(self.parseReadFuseValue(fuseValue))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF0']:
            self.m_textCtrl_fuse6d0.Clear()
            self.m_textCtrl_fuse6d0.write(self.parseReadFuseValue(fuseValue))
        elif fuseIndex == self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF1']:
            self.m_textCtrl_fuse6e0.Clear()
            self.m_textCtrl_fuse6e0.write(self.parseReadFuseValue(fuseValue))
        else:
            pass

    def RTyyyy_setLanguage( self ):
        langIndex = self.languageIndex
        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_GenSeq, uilang.kMainLanguageContentDict['panel_genSeq'][langIndex])
        self.m_staticText_serial.SetLabel(uilang.kMainLanguageContentDict['sText_serial'][langIndex])
        self.m_staticText_keyPass.SetLabel(uilang.kMainLanguageContentDict['sText_keyPass'][langIndex])
        self.m_button_advCertSettings.SetLabel(uilang.kMainLanguageContentDict['button_advCertSettings'][langIndex])
        self.m_staticText_certFmt.SetLabel(uilang.kMainLanguageContentDict['sText_certFmt'][langIndex])
        self.m_staticText_hashAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_hashAlgo'][langIndex])
        self.m_staticText_appPath.SetLabel(uilang.kMainLanguageContentDict['sText_appPath'][langIndex])
        self.m_staticText_appBaseAddr.SetLabel(uilang.kMainLanguageContentDict['sText_appBaseAddr'][langIndex])
        self.m_button_advSignSettings.SetLabel(uilang.kMainLanguageContentDict['button_advSignSettings'][langIndex])
        self.m_staticText_habCryptoAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_habCryptoAlgo'][langIndex])
        self.m_staticText_enableCertForHwCrypto.SetLabel(uilang.kMainLanguageContentDict['sText_enableCertForHwCrypto'][langIndex])
        self.m_staticText_keyStorageRegion.SetLabel(uilang.kMainLanguageContentDict['sText_keyStorageRegion'][langIndex])
        self.m_staticText_availHwCryptoEngines.SetLabel(uilang.kMainLanguageContentDict['sText_availHwCryptoEngines'][langIndex])
        self.m_button_advKeySettings.SetLabel(uilang.kMainLanguageContentDict['button_advKeySettings'][langIndex])
        self.m_staticText_hwCryptoAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_hwCryptoAlgo'][langIndex])
        self.m_staticText_maxFacCnt.SetLabel(uilang.kMainLanguageContentDict['sText_maxFacCnt'][langIndex])

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_LoadSeq, uilang.kMainLanguageContentDict['panel_loadSeq'][langIndex])
        self.m_staticText_srk256bit.SetLabel(uilang.kMainLanguageContentDict['sText_srk256bit'][langIndex])
        self.m_staticText_hwCryptoKeyInfo.SetLabel(uilang.kMainLanguageContentDict['sText_hwCryptoKeyInfo'][langIndex])
        self.m_staticText_showImage.SetLabel(uilang.kMainLanguageContentDict['sText_showImage'][langIndex])
        self.m_staticText_habDek128bit.SetLabel(uilang.kMainLanguageContentDict['sText_habDek128bit'][langIndex])

        if self.hasDynamicLableBeenInit:
            self.RTyyyy_setSecureBootSeqColor(False)
            if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                self.m_button_prepHwCrypto.SetLabel(uilang.kMainLanguageContentDict['button_prepHwCrypto_p'][self.languageIndex])
            elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                self.m_button_prepHwCrypto.SetLabel(uilang.kMainLanguageContentDict['button_prepHwCrypto_e'][self.languageIndex])
            else:
                pass

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_fuseUtil, uilang.kMainLanguageContentDict['panel_fuseUtil'][langIndex])
        self.m_button_scan.SetLabel(uilang.kMainLanguageContentDict['button_scan'][langIndex])
        self.m_button_burn.SetLabel(uilang.kMainLanguageContentDict['button_burn'][langIndex])

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_memView, uilang.kMainLanguageContentDict['panel_memView'][langIndex])
        self.m_staticText_memStart.SetLabel(uilang.kMainLanguageContentDict['sText_memStart'][langIndex])
        self.m_staticText_memLength.SetLabel(uilang.kMainLanguageContentDict['sText_memLength'][langIndex])
        self.m_staticText_memBinFile.SetLabel(uilang.kMainLanguageContentDict['sText_memBinFile'][langIndex])
        self.m_button_readMem.SetLabel(uilang.kMainLanguageContentDict['button_readMem'][langIndex])
        self.m_button_eraseMem.SetLabel(uilang.kMainLanguageContentDict['button_eraseMem'][langIndex])
        self.m_button_writeMem.SetLabel(uilang.kMainLanguageContentDict['button_writeMem'][langIndex])
        self.m_button_executeApp.SetLabel(uilang.kMainLanguageContentDict['button_executeApp'][langIndex])
        self.m_button_viewMem.SetLabel(uilang.kMainLanguageContentDict['button_viewMem'][langIndex])
        self.m_button_clearMem.SetLabel(uilang.kMainLanguageContentDict['button_clearMem'][langIndex])
        self.m_checkBox_saveImageData.SetLabel(uilang.kMainLanguageContentDict['checkBox_saveImageData'][langIndex])
