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
from ui import Kinetis_uidef
from ui import uidef
from gen import gendef

cpu = 'MKxx'
board = 'FRDM'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x17
romUsbVid = '0x15A2'
romUsbPid = '0x0073'
hasSdpReadRegisterCmd = None
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = None
flashloaderJumpAddr = None
availableCommands = 0x1ffff
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = Kinetis_uidef.kSecureBootType_Latest
hasRemappedFuse = None
availableBootDevices = Kinetis_uidef.kBootDevice_Latest
flexspiNorDevice = None
flexspiNorMemBase0 = None
flexspiNorMemBase1 = None
flexspiFreqs = None
xspiNorCfgInfoOffset = None
flexspiNorEfuseBootCfg0Bits = None
isSipFlexspiNorDevice = None
isNonXipImageAppliableForXipableDeviceUnderClosedHab = None
isEccTypeSetInFuseMiscConf = None
isSwEccSetAsDefaultInNandOpt = None
hasMultiUsdhcBootInstance = None

quadspiNorDevice = None
quadspiNorMemBase = None

registerAddrDict = None
registerDefnDict  = None

efusemapIndexDict = None
efusemapDefnDict  = None
efuseDescDiffDict = None

otpmapIndexDict = None
otpmapDefnDict  = None
otpDescDiffDict = None

ftfxNorMemBase = 0x00000000
c040hdNorMemBase = None

sbLoaderVersion = gendef.kSbLoaderVersion_v1_0

# memory map
memoryRange = {
    # SRAM, 1MByte
    'sram' : MemoryRange(0x1fff0000, 0x100000, 'state_mem0.dat'),

    # FLASH, 4KByte / 2MByte
    'flash': MemoryRange(0x00000000, 0x200000, 'state_flash_mem.dat', True, 4096, 4, 4, 16)
}

reservedRegionDict = {
    # SRAM
    'sram' : [0x1fff0000, 0x1fff1d90]
}
