#!/usr/bin/env python

# Copyright (c) 2014 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys, os
sys.path.append(os.path.abspath(".."))
from boot.memoryrange import MemoryRange
from ui import uidef
from ui import uidef_efuse

cpu = 'MIMXRT1064'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x0135'
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = 0x20000000
flashloaderJumpAddr = 0x20000400
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
hasRemappedFuse = True
flexspiNorDevice = uidef.kFlexspiNorDevice_None
flexspiNorMemBase = 0x70000000
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isSipFlexspiNorDevice = True
isEccTypeSetInFuseMiscConf = True

efuse_0x400_bit7     = {'GP4_R':    ['0 - Unlock', '1 - RP']}
efuse_0x400_bit15    = {'ROM_PATCH':['0 - Unlock', '1 - W,0P']}
efuse_0x400_bit17    = {'OTPMK':    ['0 - Unlock', '1 - W,0,RP']}
efuse_0x400_bit20    = {'OTPMK_CRC':['0 - Unlock', '1 - W,0P']}
efuse_0x400_bit25_24 = {'GP4':      ['00 - Unlock', '01 - WP', '10 - OP', '01 - W,OP']}
efuse_0x460_bit13_12 = {'BEE_KEY0_SEL':['00 - From Register', '01 - GP4[127:0]', '10 - Reserved', '11 - From SW-GP2']}
efuse_0x460_bit15_14 = {'BEE_KEY1_SEL':['00 - From Register', '01 - GP4[127:0]', '10 - Reserved', '11 - From SW-GP2']}
efuse_0x460_bit31_30 = {'SD_BT_Power_Cycle_SEL':['00 - 20ms', '01 - 10ms', '10 - 5ms', '11 - 2.5ms']}
efuseDescDiffDict = {'0x400_lock_bit7' :   efuse_0x400_bit7,
                     '0x400_lock_bit14':   uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit15':   efuse_0x400_bit15,
                     '0x400_lock_bit17':   efuse_0x400_bit17,
                     '0x400_lock_bit20':   efuse_0x400_bit20,
                     '0x400_lock_bit25_24':efuse_0x400_bit25_24,
                     '0x460_bootcfg1_bit13_12':efuse_0x460_bit13_12,
                     '0x460_bootcfg1_bit15_14':efuse_0x460_bit15_14,
                     '0x460_bootcfg1_bit31_30':efuse_0x460_bit31_30,
                     '0x6d0_miscconf0_bit19_16':uidef_efuse.efuse_0x6d0_flexramPartion512KB,
                    }

# memory map
memoryRange = {
    # ITCM, 512KByte
    'itcm' : MemoryRange(0x00000000, 0x80000, 'state_mem0.dat'),
    # DTCM, 512KByte
    'dtcm' : MemoryRange(0x20000000, 0x80000, 'state_mem1.dat'),
    # OCRAM, 1MByte
    'ocram' : MemoryRange(0x20200000, 0x100000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 1MB
    'ram' : [0x20203800, 0x20207F58]
}

