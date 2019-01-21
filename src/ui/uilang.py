#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

kLanguageIndex_English = 0x0
kLanguageIndex_Chinese = 0x1

kMenuPosition_File     = 0x0
kMenuPosition_Edit     = 0x1
kMenuPosition_View     = 0x2
kMenuPosition_Tools    = 0x3
kMenuPosition_Window   = 0x4
kMenuPosition_Help     = 0x5

kPanelIndex_GenSeq   = 0x0
kPanelIndex_LoadSeq  = 0x1
kPanelIndex_fuseUtil = 0x2
kPanelIndex_memView  = 0x3

kMainLanguageContentDict = {
        'menu_file':                          ['File',                                  u"文件"],
        'mItem_exit':                         ['Exit',                                  u"退出"],
        'menu_edit':                          ['Edit',                                  u"编辑"],
        'menu_view':                          ['View',                                  u"查看"],
        'subMenu_language':                   ['Language',                              u"语言"],
        'mItem_english':                      ['English',                               u"英文"],
        'mItem_chinese':                      ['Chinese',                               u"简体中文"],
        'menu_tools':                         ['Tools',                                 u"工具"],
        'subMenu_runMode':                    ['Run Mode',                              u"软件运行模式"],
        'mItem_runModeEntry':                 ['Entry',                                 u"入门级"],
        'mItem_runModeMaster':                ['Master',                                u"专家级"],
        'subMenu_usbDetection':               ['USB Detection',                         u"USB识别模式"],
        'mItem_usbDetectionAuto':             ['Auto',                                  u"动态"],
        'mItem_usbDetectionStatic':           ['Static',                                u"静态"],
        'subMenu_soundEffect':                ['Sound Effect',                          u"音效模式"],
        'mItem_soundEffectMario':             ['Mario',                                 u"马里奥"],
        'mItem_soundEffectQuiet':             ['Quiet',                                 u"静音"],
        'menu_window':                        ['Window',                                u"界面"],
        'menu_help':                          ['Help',                                  u"帮助"],
        'mItem_homePage':                     ['Home Page',                             u"软件主页"],
        'mItem_aboutAuthor':                  ['About Author',                          u"关于作者"],
        'mItem_specialThanks':                ['Special Thanks',                        u"特别感谢"],
        'mItem_revisionHistory':              ['Revision History',                      u"版本历史"],

        'panel_targetSetup':                  ['Target Setup',                          u"目标器件设置"],
        'sText_mcuSeries':                    ['MCU Series:',                           u"微控制器系列："],
        'sText_mcuDevice':                    ['MCU Device:',                           u"微控制器型号："],
        'sText_bootDevice':                   ['Boot Device:',                          u"启动设备类型："],
        'button_bootDeviceConfiguration':     ['Boot Device Configuration',             u"配置启动设备"],
        'button_deviceConfigurationData':     ['Device Configuration Data (DCD)',       u"配置DCD数据"],

        'panel_portSetup':                    ['Port Setup',                            u"下载接口设置"],
        'radioBtn_uart':                      ['UART',                                  u"串口"],
        'radioBtn_usbhid':                    ['USB-HID',                               u"HID设备"],
        'checkBox_oneStepConnect':            ['One Step',                              u"一键连接"],

        'panel_deviceStatus':                 ['Device Status',                         u"目标器件状态"],

        'sText_secureBootType':               ['Secure Boot Type',                      u"安全启动模式："],
        'button_allInOneAction':              ['All-In-One Action',                     u"一键启动"],

        'panel_genSeq':                       ['Image Generation Sequence',             u"       生成可启动程序       "],
        'sText_serial':                       ['Serial (8 digits):',                    u"序列号（仅8位数字）："],
        'sText_keyPass':                      ['key_pass (text):',                      u"密钥因子（任意字符）："],
        'button_advCertSettings':             ['Advanced Cert Settings',                u"配置认证参数"],
        'sText_certFmt':                      ['Certificate Format:',                   u"证书格式："],
        'sText_hashAlgo':                     ['Hash Algorithm:',                       u"哈希算法："],
        'sText_appPath':                      ['Application Image File:',               u"源应用程序镜像文件："],
        'sText_appBaseAddr':                  ['Base Address for Raw Binary Image:',    u"程序链接起始地址（仅Bin格式）："],
        'sText_habCryptoAlgo':                ['HAB Encryption Algorithm:',             u"HAB加密算法："],
        'sText_enableCertForBee':             ['Enable Certificate for BEE Encryption:',u"是否为BEE加密添加认证："],
        'sText_keyStorageRegion':             ['Key Storage Region:',                   u"密钥存储区域："],
        'sText_availBeeEngines':              ['Max Available BEE Engines:',            u"最大可用BEE引擎数："],
        'button_advKeySettings':              ['Advanced Key Settings',                 u"配置密钥参数"],
        'sText_beeCryptoAlgo':                ['BEE Encryption Algorithm:',             u"BEE加密算法："],
        'sText_maxFacCnt':                    ['Max Protection Regions:',               u"最大可保护区域数："],

        'panel_loadSeq':                      ['Image Loading Sequence',                u"       下载可启动程序       "],
        'sText_srk256bit':                    ['Burn below SRK data\n (256bits) into Fuse\n SRK0-7 Region:',                                  u"烧写如下SRK数据进\nFuse SRK0-7区域："],
        'sText_beeKeyInfo':                   ['Burn below user DEK\n data (128bits * n) into\n below Region for BEE:',                       u"烧写如下DEK进Fuse BEE\n密钥区域："],
        'sText_showImage':                    ['Program final bootable image\n to boot device:',                                              u"下载最终可启动应用程序镜像\n文件进启动设备："],
        'sText_habDek128bit':                 ['Use below DEK data (128bits)\n to generate keyblob and\n program it to flash for HAB:',       u"根据如下DEK动态生成KeyBlob\n并下载进启动设备："],

        'panel_fuseUtil':                     ['eFuse Operation Utility',               u"       专用eFuse烧写       "],
        'button_scan':                        ['Scan',                                  u"扫描"],
        'button_burn':                        ['Burn',                                  u"烧写"],

        'panel_memView':                      ['Boot Device Memory',                    u"       通用Flash编程       "],
        'sText_memStart':                     ['Start / Offset:',                       u"首地址/偏移："],
        'sText_memLength':                    ['Byte Length:',                          u"字节长度："],
        'sText_memBinFile':                   ['Bin File:',                             u"源文件"],
        'button_readMem':                     ['Read',                                  u"回读"],
        'button_eraseMem':                    ['Erase',                                 u"擦除"],
        'button_writeMem':                    ['Write',                                 u"下载"],
        'button_viewMem':                     ['View Bootable Image',                   u"回读查看标注的程序"],
        'button_clearMem':                    ['Clear The Screen',                      u"清除屏幕显示"],
        'checkBox_saveImageData':             ['Save image/data file to',               u"将程序/数据保存到"],

        'panel_log':                          ['Log',                                   u"操作日志"],
        'button_clearLog':                    ['Clear',                                 u"清除"],
        'button_SaveLog':                     ['Save',                                  u"保存"],

}

kSubLanguageContentDict = {
        'cert_title':                         ['Advanced Certificate Settings',         u"配置认证参数"],
        'panel_certOpt':                      ['Certificate Option',                    u"证书选项"],
        'sText_cstVersion':                   ['CST Version:',                          u"CST版本："],
        'sText_useExistingCaKey':             ['Use Existing CA Key:',                  u"复用已有CA密钥："],
        'sText_useEcc':                       ['Use Elliptic Curve Crypto:',            u"采用椭圆曲线加密："],
        'sText_pkiTreeKeyLen':                ['Key Length for PKI Tree (bits):',       u"PKI密钥比特长度："],
        'sText_pkiTreeDuration':              ['PKI Tree Duration (years):',            u"PKI保密时间（年）："],
        'sText_SRKs':                         ['Super Root Keys:',                      u"SRK密码组数："],
        'sText_caFlagSet':                    ['SRK Cert to have CA flag Set:',         u"证书CA标志选项："],
        'button_cert_ok':                     ['Ok',                                    u"确定"],
        'button_cert_cancel':                 ['Cancel',                                u"取消"],

}

kRevision_1_0_0_en =  "【v1.0.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT1021, i.MXRT1051/1052, i.MXRT1061/1062, i.MXRT1064 SIP \n" + \
                      "     2. Support both UART and USB-HID serial downloader modes \n" + \
                      "     3. Support various user application image file formats (elf/axf/srec/hex/bin) \n" + \
                      "     4. Can validate the range and applicability of user application image \n" + \
                      "     5. Support for converting bare image into bootable image \n" + \
                      "     6. Support for loading bootable image into FlexSPI NOR and SEMC NAND boot devices \n" + \
                      "     7. Support for loading bootable image into LPSPI NOR/EEPROM recovery boot device \n" + \
                      "     8. Support DCD which can help load image to SDRAM \n" + \
                      "     9. Support development boot case (Unsigned) \n" + \
                      "    10. Support HAB encryption secure boot case (Signed only, Signed and Encrypted) \n" + \
                      "    11. Can back up certificate with time stamp \n" + \
                      "    12. Support BEE encryption secure boot case (SNVS Key, User Keys) \n" + \
                      "    13. Support common eFuse memory operation \n" + \
                      "    14. Support common boot device memory operation \n" + \
                      "    15. Support for reading back and marking bootable image(NFCB/DBBT/FDCB/EKIB/EPRDB/IVT/Boot Data/DCD/Image/CSF/DEK KeyBlob) from boot device \n\n"
kRevision_1_0_0_zh = u"【v1.0.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持i.MXRT全系列MCU，包含i.MXRT1021、i.MXRT1051/1052、i.MXRT1061/1062、i.MXRT1064 SIP \n" + \
                     u"     2. 支持UART和USB-HID两种串行下载方式（COM端口/USB设备自动识别） \n" + \
                     u"     3. 支持五种常用格式(elf/axf/srec/hex/bin)裸源image文件输入并检查其链接地址的合法性 \n" + \
                     u"     4. 能够检查用户源image文件的适用性与合法性 \n" + \
                     u"     5. 支持将裸源image文件自动转换成i.MXRT能启动的Bootable image \n" + \
                     u"     6. 支持下载Bootable image进主动启动设备 - FlexSPI NOR、SEMC NAND接口Flash \n" + \
                     u"     7. 支持下载Bootable image进备份启动设备 - LPSPI接口NOR/EEPROM Flash \n" + \
                     u"     8. 支持DCD配置功能，可用于加载image进SDRAM执行 \n" + \
                     u"     9. 支持用于开发阶段的非安全加密启动（未签名加密） \n" + \
                     u"    10. 支持基于HAB实现的安全加密启动（单签名，签名和加密） \n" + \
                     u"    11. 能够自动备份证书并用时间戳记录 \n" + \
                     u"    12. 支持基于BEE实现的安全加密启动（唯一SNVS key，用户自定义key） \n" + \
                     u"    13. 支持MCU芯片内部eFuse的回读和烧写操作（即专用eFuse烧写器） \n" + \
                     u"    14. 支持外部启动设备的任意读写擦操作（即通用Flash编程器） \n" + \
                     u"    15. 支持从外部启动设备回读Bootable image，并对其组成部分（NFCB/DBBT/FDCB/EKIB/EPRDB/IVT/Boot Data/DCD/Image/CSF/DEK KeyBlob）进行标注 \n\n"
kRevision_1_1_0_en =  "【v1.1.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT1015 \n" + \
                      "     2. Add Language option in Menu/View and support Chinese\n" + \
                      "  Improvement: \n" + \
                      "     1. USB device auto-detection can be disabled \n" + \
                      "     2. Original image can be a bootable image (with IVT&BootData/DCD) \n" + \
                      "     3. Show boot sequence page dynamically according to action \n" + \
                      "  Interest: \n" + \
                      "     1. Add sound effect (Mario) \n\n"
kRevision_1_1_0_zh = u"【v1.1.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持i.MXRT1015 \n" + \
                     u"     2. 支持界面中文显示\n" + \
                     u"  改进: \n" + \
                     u"     1. USB自动识别的功能可以禁掉 \n" + \
                     u"     2. 用户输入的源程序文件可以包含i.MXRT启动头 (IVT&BootData/DCD) \n" + \
                     u"     3. 根据操作过程自动跟随显示操作页面 \n" + \
                     u"  个性: \n" + \
                     u"     1. 增加马里奥音效 \n\n"

kMsgLanguageContentDict = {
        'homePage_title':                     ['Home Page',                             u"项目主页"],
        'homePage_info':                      ['https://github.com/JayHeng/NXP-MCUBootUtility.git \n',                             u"https://github.com/JayHeng/NXP-MCUBootUtility.git \n"],
        'aboutAuthor_title':                  ['About Author',                          u"关于作者"],
        'aboutAuthor_author':                 [u"Author:  痞子衡 \n",                   u"作者：痞子衡 \n"],
        'aboutAuthor_email1':                 ['Email:     jie.heng@nxp.com \n',        u"邮箱：jie.heng@nxp.com \n"],
        'aboutAuthor_email2':                 ['Email:     hengjie1989@foxmail.com \n', u"邮箱：hengjie1989@foxmail.com \n"],
        'aboutAuthor_blog':                   [u"Blog:      痞子衡嵌入式 https://www.cnblogs.com/henjay724/ \n",                   u"博客：痞子衡嵌入式 https://www.cnblogs.com/henjay724/ \n"],
        'specialThanks_title':                ['Special Thanks',                        u"特别感谢"],
        'specialThanks_info':                 [u"Special thanks to 周小朋Clare、杨帆、刘华东Howard、沈浩杰Jayson \n",              u"特别感谢我亲爱的同事们：周小朋Clare、杨帆、刘华东Howard、沈浩杰Jayson \n"],
        'revisionHistory_title':              ['Revision History',                      u"版本历史"],
        'revisionHistory_v1_0_0':             [kRevision_1_0_0_en,                      kRevision_1_0_0_zh],
        'revisionHistory_v1_1_0':             [kRevision_1_1_0_en,                      kRevision_1_1_0_zh],

        'bootDeviceInfo_hasOnchipSerialNor':  ['MCU has on-chip QSPI NOR Flash (4MB, 133MHz), so you don\'t need to configure this boot device!',
                                              u"微控制器内置4MB的QSPI NOR Flash，所以无需配置该启动设备！"],
        'connectError_cannotSetOneStep':      ['One Step mode cannot be set under Entry Mode, Please switch to Master Mode and try again!',
                                              u"在软件入门级模式下，[一键连接]模式不可改，请切换到软件专家级模式下再试！"],
        'connectError_failToJumpToFl':        ['MCU has entered ROM SDP mode but failed to jump to Flashloader, Please reset board and try again!',
                                              u"微控制器已成功进入ROM SDP模式，但是未能跳转进入Flashloader，请复位板子再试！"],
        'connectError_doubleCheckBmod':       ['Make sure that you have put MCU in SDP (Serial Downloader Programming) mode (BMOD[1:0] pins = 2\'b01)!',
                                              u"请检查BMOD[1:0]引脚状态是否为2\'b01以确认微控制器处于ROM SDP模式！"],
        'connectError_failToPingFl':          ['Failed to ping Flashloader, Please reset board and consider updating flashloader.srec file under /src/targets/ then try again!',
                                              u"微控制器未能与Flashloader建立连接，请复位板子并考虑更新/src/targets/目录下相应的flashloader.srec文件再试！"],
        'connectError_failToCfgBootDevice':   ['MCU has entered Flashloader but failed to configure external memory, Please reset board and set proper boot device then try again!',
                                              u"微控制器已与Flashloader建立连接，但是未能识别启动设备。请复位板子并配置正确的启动设备再试！"],
        'connectError_hasnotCfgBootDevice':   ['Please configure boot device via Flashloader first!',
                                              u"请先借助Flashloader去完成启动设备的配置！"],
        'connectError_hasnotEnterFl':         ['Please connect to Flashloader first!',
                                              u"请先连接到Flashloader！"],
        'certGenError_notEnabledForBee':      ['Certificate is not enabled for BEE, You can enable it then try again!',
                                              u"当前BEE加密启动模式下没有使能认证，请先使能认证再试！"],
        'certGenError_noNeedToSetForUnsigned':['No need to set certificate option when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要配置认证参数！"],
        'certGenError_noNeedToGenForUnsigned':['No need to generate certificate when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要生成证书！"],
        'certGenInfo_reuseOldCert':           ["There is available certificate, Do you want to reuse existing certificate? \n",
                                              u"当前目录下已有证书文件，你想复用已有的证书吗？"],
        'certGenInfo_haveNewCert':            ["New certificate will be different even you don’t change any settings, Do you really want to have new certificate? \n",
                                              u"即使不改任何认证参数，新证书也会不同于已有证书，你依旧想生成新证书吗？"],
        'keyGenError_onlyForBee':             ['Key setting is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"配置密钥参数仅在BEE加密启动模式下有效！"],
        'operBeeError_onlyForBee':            ['BEE encryption is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"BEE加密操作仅在BEE加密启动模式下有效！"],
        'operBeeError_onlyForFlexspiNor':     ['Action is not available because BEE encryption boot is only designed for FlexSPI NOR device!',
                                              u"在软件入门级模式下，单步操作不被支持，请直接使用[一键启动]！"],
        'operBeeError_failToPrepareForSnvs':  ['Failed to prepare for fixed OTPMK SNVS encryption, Please reset board and try again!',
                                              u"未能准备好OTPMK SNVS加密，请复位板子再试！！"],
        'operKeyError_srkNotForUnsigned':     ['No need to burn SRK data when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要烧写SRK！"],
        'operKeyError_dekOnlyForBee':         ['BEE DEK Burning is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"烧写DEK操作仅在BEE加密启动模式下有效！"],
        'operKeyError_dekNotForSnvs':         ['No need to burn BEE DEK data as OTPMK key is selected!',
                                              u"当前选择OTPMK SNVS区域存储密钥下不需要烧写DEK！"],
        'operMemError_notAvailUnderEntry':    ['Common memory operation is not available under Entry Mode, Please switch to Master Mode and try again!',
                                              u"在软件入门级模式下，通用Flash操作没有使能，请切换到软件专家级模式下再试！"],
        'separActnError_notAvailUnderEntry':  ['Separated action is not available under Entry Mode, You should use All-In-One Action!',
                                              u"在软件入门级模式下，单步操作不被支持，请直接使用[一键启动]！"],
        'operImgError_failToFlashImage':      ['Failed to flash bootable image into external memory, Please reset board and try again!',
                                              u"未能将应用程序下载进启动设备，请复位板子再试！！"],
        'operImgError_keyBlobOnlyForHab':     ['KeyBlob loading is only available when booting HAB encrypted image!',
                                              u"下载KeyBlob操作仅在HAB加密启动模式下有效！"],
        'operImgError_hasnotFlashImage':      ['Please flash image into boot device first!',
                                              u"请先将应用程序下载进启动设备！"],
}