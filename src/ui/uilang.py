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
        'button_advKeySettings':              ['Advanced Key Settings',                 u"配置加密参数"],
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

