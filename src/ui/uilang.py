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
        'button_advCertSettings':             ['Advanced Certificate Settings',         u"配置认证参数"],
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

        #cert
        'panel_certOpt':                      ['Certificate Option'                     u"证书选项"]
        'sText_cstVersion':                   ['CST Version'                            u"CST版本"]
        'sText_useExistingCaKey':             ['Use Existing CA Key'                    u"使用现有的CA密钥"]
        'sText_useEcc':                       ['Use Elliptic Curve Crypto'              u"使用椭圆曲线加密"]
        'sText_pkiTreeKeyLen':                ['Key Length for PKI Tree (bits)'         u"PKI树的密钥长度 (位)"]
        'sText_pkiTreeDuration':              ['PKI Tree Duration (years)'              u"PKI树持续时间 (年)"]
        'sText_SRKs':                         ['Super Root Keys'                        u"超级权限密钥"]
        'sText_caFlagSet':                    ['SRK Cert to have CA flag Set'           u"具有CA标志设置的SRK证书"]
        'button_cert_ok':                     ['Ok'                                     u"确认"]
        'button_cert_cancel':                 ['Cancel'                                 u"取消"]

        #dcd
        'panel_dcdOpt':                       ['DCD Option'                             u"DCD选项"]
        'sText_dcdSource':                    ['DCD Source'                             u"DCD源"]
        'sText_dcdBinFile':                   ['DCD bin file'                           u"DCD bin文件"]
        'sText_dcdCfgFile':                   ['DCD cfg file'                           u"DCD cfg文件"]
        'sText_dcdPurpose':                   ['DCD Purpose'                            u"DCD目标"]
        'sText_sdramBase':                    ['SDRAM Base'                             u"SDRAM基地址"]
        'panel_dcdDesc':                      ['DCD Descriptor'                         u"DCD描述"]
        'sText_dcdModel':                     ['Device Model'                           u"设备模式"]
        'button_dcd_ok':                      ['Ok'                                     u"确认"]
        'button_dcd_cancel':                  ['Cancel'                                 u"取消"]

        #flexspinor
        'sText_deviceModel':                  ['Use Typical Device Model'               u"使用典型设备型号"]
        'panel_norOpt0':                      ['Nor Option0'                            u"选项0"]
        'sText_deviceType':                   ['Device Type'                            u"设备类型"]
        'sText_queryPads':                    ['Query Pads'                             u"查询板"]
        'sText_cmdPads':                      ['Cmd Pads'                               u"CMD板"]
        'sText_quadModeSetting':              ['Quad Mode Setting'                      u"四路模式设置"]
        'sText_miscMode':                     ['Misc Mode'                              u"Misc模式"]
        'sText_maxFrequency':                 ['Max Frequency'                          u"最大频率"]
        'sText_hasOption1':                   ['Has Option1'                            u"是否有选项1"]
        'panel_norOpt1':                      ['Nor Option1'                            u"选项1"]
        'sText_flashConnection':              ['Flash Connection'                       u"Flash连接"]
        'sText_driveStrength':                ['Drive Strength'                         u"驱动长度"]
        'sText_dqsPinmuxGroup':               ['DQS Pinmux Group'                       u"DQS Pinmux 组"]
        'sText_enableSecondPinmux':           ['Enable Second Pinmux'                   u"使能第二个Pinmux"]
        'sText_statusOverride':               ['Status Override'                        u"状态覆盖"]
        'sText_dummyCycles':                  ['Dummy Cycles'                           u"虚拟循环"]
        'button_flexspinor_ok':               ['Ok'                                     u"确认"]
        'button_flexspinor_cancel':           ['Cancel'                                 u"取消"]

        #lpspinor
        'panel_memOpt':                       ['Memory Option'                          u"存储器选项"]
        'sText_deviceType':                   ['Device Type'                            u"设备类型"]
        'sText_pageSize':                     ['Page Size (Bytes)'                      u"页面大小（字节）"]
        'sText_sectorSize':                   ['Sector Size (KBytes）'                  u"扇区大小（千字节）"]
        'sText_totalSize':                    ['Total Size (KBytes)'                    u"总计大小（千字节）"]
        'panel_spiOpt':                       ['Spi Option'                             u"Spi串口选项"]
        'sText_spiIndex':                     ['Spi Index'                              u"Spi串口指数"]
        'sText_spiPcs':                       ['Spi Pcs'                                u"Spi串口Pcs"]
        'sText_spiSpeed':                     ['Spi Speed'                              u"Spi串口速度"]
        'button_lpspinor_ok':                 ['Ok'                                     u"确认"]
        'button_lpspinor_ok':                 ['Cancel'                                 u"取消"]

        #semcnand
        'panel_nandOpt':                      ['Nand Option'                            u"Nand闪存选项"]
        'sText_onfiVersion':                  ['ONFI Version'                           u"ONFI版本"]
        'sText_onfiTimingMode':               ['ONFI Timing Mode'                       u"ONFI时钟模式"]
        'sText_edoMode':                      ['EDO Mode'                               u"EDO模式"]
        'sText_ioPortSize':                   ['I/O Port Size'                          u"输入/输出端口大小"]
        'sText_pcsPort':                      ['PCS Port'                               u"PCS端口"]
        'sText_eccType':                      ['ECC Type'                               u"ECC类型"]
        'sText_eccStatus':                    ['Initial ECC status'                     u"初始化ECC状态"]
        'panel_fcbOpt':                       ['FCB Option'                             u"FCB选项"]
        'sText_searchCount':                  ['Search Count'                           u"搜索计数"]
        'sText_searchStride':                 ['Search Stride'                          u"搜索步长"]
        'sText_imageCopies':                  ['Image Copies'                           u"程序复制"]
        'panel_imageInfo':                    ['Image Info'                             u"程序信息"]
        'sText_blockIndex':                   ['Block Index'                            u"限制指数"]
        'sText_blockCount':                   ['Block Count'                            u"限制计数"]
        'button_semcnand_ok':                 ['Ok'                                     u"确认"]
        'button_semcnand_cancel':             ['Cancel'                                 u"取消"]

        #otpmk
        'panel_encryptionOpt':                ['Encryption Option'                      u"加密选项"]
        'sText_keySource':                    ['Key Source'                             u"密钥源"]
        'sText_aesMode':                      ['AES Mode'                               u"AES模式"]
        'sText_regionCnt':                    ['Region Count'                           u"区域占取"]
        'panel_regionInfo':                   ['Encrypted Region Info'                  u"加密空间信息"]
        'sText_regionStart':                  ['Region Start'                           u"空间首地址"]
        'sText_regionLength':                 ['Region Length'                          u"空间长度"]
        'button_fixedotpmkkey_ok':            ['Ok'                                     u"确认"]
        'button_fixedotpmkkey_cancel':        ['Cancel'                                 u"取消"]

        #user
        'panel_encryptionOpt':                ['Encryption Option'                      u"加密选项"]
        'sText_engineSel':                    ['Engine Selection'                       u"引擎选择"]
        'sText_beeEngKeySel':                 ['BEE Engine Key Selection'               u"BEE引擎密钥选择"]
        'sText_imageType':                    ['Image Type'                             u"程序类型"]
        'sText_xipBaseAddr':                  ['XIP Base Address'                       u"XIP基地址"]
        'panel_engine0Info':                  ['BEE Engine 0 Info'                      u"BEE引擎0信息"]
        'sText_engine0keySource':             ['Key Source'                             u"密钥源"]
        'sText_engine0UserKeyData':           ['User Key Data'                          u"用户密钥数据"]
        'sText_engine0AesMode':               ['AES Mode'                               u"AES模式"]
        'sText_engine0FacCnt':                ['Protected Region Count'                 u"受保护空间计数"]
        'sText_engine0Fac0Start':             ['Protected Region 0 Start'               u"受保护空间0的首地址"]
        'sText_engine0Fac0Length':            ['Protected Region 0 Length'              u"受保护空间0的长度"]
        'sText_engine0Fac1Start':             ['Protected Region 1 Start'               u"受保护空间1的首地址"]
        'sText_engine0Fac1Length':            ['Protected Region 1 Length'              u"受保护空间1的长度"]
        'sText_engine0Fac2Start':             ['Protected Region 2 Start'               u"受保护空间2的首地址"]
        'sText_engine0Fac2Length':            ['Protected Region 2 Length'              u"受保护空间2的长度"]
        'sText_engine0AccessPermision':       ['Access Permision'                       u"允许访问"]
        'sText_engine0Lock':                  ['Region Lock'                            u"空间锁定"]
        'panel_engine1Info':                  ['BEE Engine 1 Info'                      u"BEE引擎1信息"]
        'sText_engine1keySource':             ['Key Source'                             u"密钥源"]
        'sText_engine1UserKeyData':           ['User Key Data'                          u"用户密钥数据"]
        'sText_engine1AesMode':               ['AES Mode'                               u"AES模式"]
        'sText_engine1FacCnt':                ['Protected Region Count'                 u"受保护空间计数"]
        'sText_engine1Fac0Start':             ['Protected Region 0 Start'               u"受保护空间0的首地址"]
        'sText_engine1Fac0Length':            ['Protected Region 0 Length'              u"受保护空间0的长度"]
        'sText_engine1Fac1Start':             ['Protected Region 1 Start'               u"受保护空间1的首地址"]
        'sText_engine1Fac1Length':            ['Protected Region 1 Length'              u"受保护空间1的长度"]
        'sText_engine1Fac2Start':             ['Protected Region 2 Start'               u"受保护空间2的首地址"]
        'sText_engine1Fac2Length':            ['Protected Region 2 Length'              u"受保护空间2的长度"]
        'sText_engine1AccessPermision':       ['Access Permision'                       u"允许访问"]
        'sText_engine1Lock':                  ['Region Lock'                            u"空间锁定"]
        'button_flexibleuserkeys_genRandomKey':            ['Generate Random User Key'                     u"随机生产用户密钥"]
        'button_flexibleuserkeys_ok':         ['Ok'                                     u"确认"]
        'button_flexibleuserkeys_cancel':     ['Cancel'                                 u"取消"]


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


        'illegalInput':                       ['Illegal input detected! You should input like this format: 0x5000',
                                              u"检测到非法输入!您应该输入类似于此格式: 0x5000（十六进制数）。"],

#        'USB-HID_NotFound':                   ['Cannnot find USB-HID device (vid=%s, pid=%s), Please connect USB cable to your board first!',
#                                              u"找不到USB-HID设备 (vid =% s, pid =% s), 请先将USB电缆连接到您的主板!"],
        
        '8digitsSerial':                      ['Serial must be 8 digits!',
                                              u"串行必须是8位数字!"],

        'Key_PasstoSet':                      ['You forget to set key_pass!',
                                              u"您忘了设置密钥！"],

        'operImgError_notRec/Convert':        ['Cannot recognise/convert the format of image file: ',
                                              u"无法识别/转换image文件的格式:"],

        'operDCDError_notGenerated':          ['DCD binary is not generated successfully! Check your DCD descriptor file and make sure you don\'t put the tool in path with blank space!',
                                              u"DCD二进制文件未成功生成!检查您的DCD描述符文件, 并确保您保存该工具的路径中没有空格!"],

        'invalidVecAddress':                  ['Invalid vector address found in image file: ',
                                              u"image文件中存在无效的矢量地址:"],

        'NON-XIPAppDetcted':                 ['Non-XIP Application is detected but it is not in the range of ITCM/DTCM/OCRAM/SDRAM!',
                                              u"检测到非XIP应用程序,但它不在 ITCM/DTCM/OCRAM/SDRAM的范围内!"],

        'XIPAppNotAppliableDected':           ['XIP Application is detected but it is not appliable for HAB Encrypted image boot!',
                                              u"XIP应用程序被检测到, 但它不适用于HAB加密映像启动!"],

        'NON-XIPAppNotForBEEDetcted':         ['Non-XIP Application is detected but it is not appliable for BEE Encrypted image boot!',
                                              u"检测到非XIP应用程序, 但它不适用于BEE加密映像启动!"],

        'specifyASourceImageFile':            ['You should first specify a source image file (.elf/.axf/.srec/.hex/.bin)!',
                                              u"您应该首先指定一个image文件 (. elf/. axf/. srec/. srec/. hacn)!"],

#        'exceededSizeXIPAppDected':           ['XIP Application is detected but the size exceeds maximum XIP size 0x%s ! ',
#                                              u"XIP应用程序被检测到, 但大小超过最大XIP大小!"],

#        'exceededSizeXIPAppDected':           ['XIP Application is detected but the size exceeds maximum XIP size 0x%s !',
#                                              u"XIP应用程序被检测到, 但大小超过最大XIP大小!"],

        'genCerFirst':                        ['You should first generate certificates, or make sure you don\'t put the tool in path with blank space!',
                                              u"您应该首先生成证书, 或者确保该工具存放的路径中没有空格!"],

        'BootableImageNotGen':                ['Bootable image is not generated successfully! Make sure you don\'t put the tool in path with blank space!',
                                              u"Bootable image未成功生成!请确保该工具存放的路径中没有空格!"],

        'FlashloaderImageNotUsable':          ['Default Flashloader image file is not usable!',
                                              u"默认的Flashloaderimage文件不可用!"],

        'genCertificates':                    ['You should first generate certificates!',
                                              u"您应该首先生成证书。"],

        'FuseSRKnotBurned':                   ['Fuse SRK Regions were not burned successfully!',
                                              u"Fuse SRK Regions未成功烧录!"],

        'program-onceFuseSRKBurned':          ['Fuse SRK Regions have been burned, it is program-once!',
                                              u"Fuse SRK Regions已经被烧录，它只可被烧写一次！"],

        'SuperRootKeysnotGen':                ['Super Root Keys hasn\'t been generated!',
                                              u"Super Root Keys还未生成！"],

        'FuseLOCKSW_GP2notBurned':            ['Fuse LOCK SW_GP2 region was not burned successfully!',
                                              u"Fuse LOCK SW_GP2 region未成功烧录!"],

        'FuseLOCKGP4notBurned':               ['Fuse LOCK GP4 region was not burned successfully!',
                                              u"Fuse LOCK GP4 region未成功烧录!"],

        'FuseSW_GP2notBurned':                ['Fuse SW_GP2 Regions were not burned successfully!',
                                              u"Fuse SW_GP2 Regions未成功烧录!"],

        'program-onceFuseSW_GP2Burned':       ['Fuse SW_GP2 Regions have been burned/locked, it is program-once!',
                                              u"Fuse SW_GP2 Regions已经被烧录/锁定，它只可被烧写一次！"],

        'FuseGP4notBurned':                   ['Fuse GP4 Regions were not burned successfully!',
                                              u"Fuse GP4 Regions未成功烧录!"],

        'program-onceFuseGP4Burned':          ['Fuse GP4 Regions have been burned/locked, it is program-once!',
                                              u"Fuse GP4 Regions已经被烧录/锁定，它只可被烧写一次！"],

        'program-onceFuseMISC_CONF1Burned':   ['Fuse MISC_CONF1[31:0] has been burned, it is program-once!',
                                              u"Fuse MISC_CONF1[31:0]已经被烧录，它只可被烧写一次！"],

        'FuseMISC_CONF1notBurned':            ['Fuse MISC_CONF1[31:0] region was not burned successfully!',
                                              u"Fuse MISC_CONF1[31:0]region未成功烧录！"],

        'program-onceFuseMISC_CONF0Burned':   ['Fuse MISC_CONF0[28:24] has been burned, it is program-once!',
                                              u"Fuse MISC_CONF0[28:24]已经被烧录，它只可被烧写一次！"],

        'FuseMISC_CONF0notBurned':            ['Fuse MISC_CONF0[28:24] region was not burned successfully!',
                                              u"Fuse MISC_CONF0[28:24] region未成功烧录！"],

        'program-onceFuseBOOT_CFG1Burned':    ['Fuse BOOT_CFG1[5:4] BEE_KEY0_SEL has been burned, it is program-once!',
                                              u"Fuse BOOT_CFG1[5:4] BEE_KEY0_SEL已经被烧录，它只可被烧写一次！"],

        'program-onceFuseBOOT_CFG1[7:6]Burned':    ['Fuse BOOT_CFG1[7:6] BEE_KEY1_SEL has been burned, it is program-once!',
                                                   u"Fuse BOOT_CFG1[7:6] BEE_KEY1_SEL已经被烧录，它只可被烧写一次！"],

        'FuseBOOT_CFG1[7:4]notBurned':        ['Fuse BOOT_CFG1[7:4] BEE_KEY0/1_SEL region was not burned successfully!',
                                              u"Fuse BOOT_CFG1[7:4] BEE_KEY0/1_SEL region未成功烧录！"],

        'DekFilenotGen':                      ['Dek file hasn\'t been generated!',
                                              u"DEK文件尚未生成!"],

        'FuseBOOT_CFG1[1]notBurned':          ['Fuse BOOT_CFG1[1] SEC_CONFIG[1] region was not burned successfully!',
                                              u"Fuse BOOT_CFG1[1] SEC_CONFIG[1]region未成功烧录！"],

        'SRK_LOCKnotAllowedSet':              ['Fuse 0x400[14] - SRK_LOCK is not allowed to be set, because SRK will be OP+RP+WP if SRK_LOCK is set and then ROM cannot get SRK!',
                                              u"Fuse 0x400[14] - SRK_LOCK不允许被设置，因为如果SRK_LOCK被设置，SRK将会被覆盖保护，访问保护和写保护，之后ROM不能得到SRK!"],

        'programImageFirst':                  ['You should program your image first!',
                                              u"您应该首先编写你的image文件！"],

#        'failedRead':                         ['Failed to read boot device, error code is %d !',
#                                              u"读取启动设备失败，错误的代码是"],

#        'failedErase':                        ['Failed to erase boot device, error code is %d !',
#                                              u"擦除启动设备失败，错误的代码是"],

#       'StartAddress':                        ['Start Address should be aligned with 0x%x !',
#                                              u"启动地址应该与 一致"],

#        'failedErase':                        ['Failed to erase boot device, error code is %d !',
#                                              u"擦除启动设备失败，错误的代码是"],

#        'failedWrite':                        ['Failed to write boot device, error code is %d, You may forget to erase boot device first!',
#                                              u"写入启动设备失败，错误的代码是 ，或许你忘了先把启动设备擦除！"],

}