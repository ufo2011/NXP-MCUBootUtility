# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class efuseWin_BootCfg2
###########################################################################

class efuseWin_BootCfg2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 860,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_byteIdx = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_address = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_address.Wrap( -1 )

		self.m_staticText_address.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_address, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx0 = wx.StaticText( self, wx.ID_ANY, u"               0x470[7:0]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx0.Wrap( -1 )

		self.m_staticText_byteIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx0, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx1 = wx.StaticText( self, wx.ID_ANY, u"               0x470[15:8]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx1.Wrap( -1 )

		self.m_staticText_byteIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx1, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx2 = wx.StaticText( self, wx.ID_ANY, u"               0x470[23:16]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx2.Wrap( -1 )

		self.m_staticText_byteIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx2, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx3 = wx.StaticText( self, wx.ID_ANY, u"               0x470[31:24]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx3.Wrap( -1 )

		self.m_staticText_byteIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx3, 0, wx.ALL, 5 )


		wSizer_win.Add( bSizer_byteIdx, 1, wx.EXPAND, 5 )

		bSizer_bitIdx = wx.BoxSizer( wx.VERTICAL )

		wSizer_bitIdx = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_bitIdx7 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx7.Wrap( -1 )

		self.m_staticText_bitIdx7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx7, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx6 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx6.Wrap( -1 )

		self.m_staticText_bitIdx6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx6, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx5 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx5.Wrap( -1 )

		self.m_staticText_bitIdx5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx5, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx4 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx4.Wrap( -1 )

		self.m_staticText_bitIdx4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx4, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx3 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx3.Wrap( -1 )

		self.m_staticText_bitIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx3, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx2 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx2.Wrap( -1 )

		self.m_staticText_bitIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx2, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx1 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx1.Wrap( -1 )

		self.m_staticText_bitIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx1, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx0 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx0.Wrap( -1 )

		self.m_staticText_bitIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx0, 0, wx.ALL, 5 )

		self.m_staticText_bit7 = wx.StaticText( self, wx.ID_ANY, u"DLL Override", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit7.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit7, 0, wx.ALL, 5 )

		self.m_staticText_bit6 = wx.StaticText( self, wx.ID_ANY, u"SD1_RST_PO_SEL", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit6.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit6, 0, wx.ALL, 5 )

		self.m_staticText_bit5 = wx.StaticText( self, wx.ID_ANY, u"SD2 VOLTAGE", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit5.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit5, 0, wx.ALL, 5 )

		self.m_staticText_bit4 = wx.StaticText( self, wx.ID_ANY, u"UART_Ser-D_Dis", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit4.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit4, 0, wx.ALL, 5 )

		self.m_staticText_bit3 = wx.StaticText( self, wx.ID_ANY, u"Dis_SDMMC_manu", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit3.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit3, 0, wx.ALL, 5 )

		self.m_staticText_bit2 = wx.StaticText( self, wx.ID_ANY, u"L1 I-Cache Dis", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit2.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit2, 0, wx.ALL, 5 )

		self.m_staticText_bit1 = wx.StaticText( self, wx.ID_ANY, u"L1_D-Cache_DIS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit1.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit1, 0, wx.ALL, 5 )

		self.m_staticText_bit0 = wx.StaticText( self, wx.ID_ANY, u"Override_Pad_Set", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit0.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit0, 0, wx.ALL, 5 )

		m_choice_bit7Choices = [ u"0 -Slave Mode", u"1 -Override Mode" ]
		self.m_choice_bit7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit7Choices, 0 )
		self.m_choice_bit7.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit7, 0, wx.ALL, 5 )

		m_choice_bit6Choices = [ u"0 -Reset Low", u"1 -Reset High" ]
		self.m_choice_bit6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit6Choices, 0 )
		self.m_choice_bit6.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit6, 0, wx.ALL, 5 )

		m_choice_bit5Choices = [ u"0 -3.3V ", u"1 -1.8V" ]
		self.m_choice_bit5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit5Choices, 0 )
		self.m_choice_bit5.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit5, 0, wx.ALL, 5 )

		m_choice_bit4Choices = [ u"0 -Not Disable ", u"1 -Disable" ]
		self.m_choice_bit4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit4Choices, 0 )
		self.m_choice_bit4.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit4, 0, wx.ALL, 5 )

		m_choice_bit3Choices = [ u"0 -Enable ", u"1 -Disable" ]
		self.m_choice_bit3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit3Choices, 0 )
		self.m_choice_bit3.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit3, 0, wx.ALL, 5 )

		m_choice_bit2Choices = [ u"0 ", u"1 " ]
		self.m_choice_bit2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit2Choices, 0 )
		self.m_choice_bit2.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit2, 0, wx.ALL, 5 )

		m_choice_bit1Choices = [ u"0 -Enable ", u"1 -Disable" ]
		self.m_choice_bit1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit1Choices, 0 )
		self.m_choice_bit1.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit1, 0, wx.ALL, 5 )

		m_choice_bit0Choices = [ u"0", u"1" ]
		self.m_choice_bit0 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit0Choices, 0 )
		self.m_choice_bit0.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit0, 0, wx.ALL, 5 )

		self.m_staticText_bit15 = wx.StaticText( self, wx.ID_ANY, u"SD2_RST_PO_SEL", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit15.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit15, 0, wx.ALL, 5 )

		self.m_staticText_bit14 = wx.StaticText( self, wx.ID_ANY, u"RE_TO_PRE-IDLE", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit14.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit14, 0, wx.ALL, 5 )

		self.m_staticText_bit13 = wx.StaticText( self, wx.ID_ANY, u"Override_HYS_bit", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit13.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit13, 0, wx.ALL, 5 )

		self.m_staticText_bit12 = wx.StaticText( self, wx.ID_ANY, u"USDHC_PAD_DOWN", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit12.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit12, 0, wx.ALL, 5 )

		self.m_staticText_bit11 = wx.StaticText( self, wx.ID_ANY, u"ENA_EMMC_22K_PULLUP", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit11.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit11, 0, wx.ALL, 5 )

		self.m_staticText_bit10 = wx.StaticText( self, wx.ID_ANY, u"BootFailIndiPinSelect[4]", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit10.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit10, 0, wx.ALL, 5 )

		self.m_staticText_bit9 = wx.StaticText( self, wx.ID_ANY, u"USDHC_IOMUX_SION_BIT_ENA", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit9.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit9, 0, wx.ALL, 5 )

		self.m_staticText_bit8 = wx.StaticText( self, wx.ID_ANY, u"USDHC_IOMUX_SRE_Ena", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit8.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit8, 0, wx.ALL, 5 )

		m_choice_bit15Choices = [ u"0 -Reset Low", u"1 -Reset High" ]
		self.m_choice_bit15 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit15Choices, 0 )
		self.m_choice_bit15.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit15, 0, wx.ALL, 5 )

		m_choice_bit14Choices = [ u"0", u"1" ]
		self.m_choice_bit14 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit14Choices, 0 )
		self.m_choice_bit14.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit14, 0, wx.ALL, 5 )

		m_choice_bit13Choices = [ u"0", u"1" ]
		self.m_choice_bit13 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit13Choices, 0 )
		self.m_choice_bit13.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit13, 0, wx.ALL, 5 )

		m_choice_bit12Choices = [ u"0 -no action", u"1 -pull down" ]
		self.m_choice_bit12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit12Choices, 0 )
		self.m_choice_bit12.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit12, 0, wx.ALL, 5 )

		m_choice_bit11Choices = [ u"0 -47K pullup", u"1 -22K pullup" ]
		self.m_choice_bit11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit11Choices, 0 )
		self.m_choice_bit11.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit11, 0, wx.ALL, 5 )

		m_choice_bit10Choices = [ u"0", u"1" ]
		self.m_choice_bit10 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit10Choices, 0 )
		self.m_choice_bit10.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit10, 0, wx.ALL, 5 )

		m_choice_bit9Choices = [ u"0 -Disable", u"1 -Enable" ]
		self.m_choice_bit9 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit9Choices, 0 )
		self.m_choice_bit9.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit9, 0, wx.ALL, 5 )

		m_choice_bit8Choices = [ u"0 -Disable", u"1 -Enable" ]
		self.m_choice_bit8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit8Choices, 0 )
		self.m_choice_bit8.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit8, 0, wx.ALL, 5 )

		self.m_staticText_bit23 = wx.StaticText( self, wx.ID_ANY, u"USDHC_CMD_OE_PRE_EN", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit23.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit23, 0, wx.ALL, 5 )

		self.m_staticText_bit22_21 = wx.StaticText( self, wx.ID_ANY, u"LPB_BOOT", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit22_21.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit22_21, 0, wx.ALL, 5 )

		self.m_staticText_bit20 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit20.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit20, 0, wx.ALL, 5 )

		self.m_staticText_bit19_16 = wx.StaticText( self, wx.ID_ANY, u"Boot Failure Indicator Pin Select[3:0]", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit19_16.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit19_16, 0, wx.ALL, 5 )

		m_choice_bit23Choices = [ u"0", u"1" ]
		self.m_choice_bit23 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit23Choices, 0 )
		self.m_choice_bit23.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit23, 0, wx.ALL, 5 )

		m_choice_bit22_21Choices = [ u"00 -Div by 1", u"01 -Div by 2", u"10 -Div by 3", u"11 -Div by 4" ]
		self.m_choice_bit22_21 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit22_21Choices, 0 )
		self.m_choice_bit22_21.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit22_21, 0, wx.ALL, 5 )

		m_choice_bit20Choices = [ u"x" ]
		self.m_choice_bit20 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit20Choices, 0 )
		self.m_choice_bit20.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit20, 0, wx.ALL, 5 )

		m_choice_bit19_16Choices = []
		self.m_choice_bit19_16 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit19_16Choices, 0 )
		self.m_choice_bit19_16.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit19_16, 0, wx.ALL, 5 )

		self.m_staticText_bit31 = wx.StaticText( self, wx.ID_ANY, u"OverNAND_PadSet", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit31.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit31, 0, wx.ALL, 5 )

		self.m_staticText_bit30_24 = wx.StaticText( self, wx.ID_ANY, u"MMC_DLL_DLY[6:0]", wx.DefaultPosition, wx.Size( 620,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit30_24.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit30_24, 0, wx.ALL, 5 )

		m_choice_bit31Choices = [ u"0", u"1" ]
		self.m_choice_bit31 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit31Choices, 0 )
		self.m_choice_bit31.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit31, 0, wx.ALL, 5 )

		m_choice_bit30_24Choices = []
		self.m_choice_bit30_24 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 620,-1 ), m_choice_bit30_24Choices, 0 )
		self.m_choice_bit30_24.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit30_24, 0, wx.ALL, 5 )

		self.m_staticText_null0BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 420,-1 ), 0 )
		self.m_staticText_null0BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null0BitIdx, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_cancel, 0, wx.ALL, 5 )

		self.m_staticText_null1BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 720,1 ), 0 )
		self.m_staticText_null1BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null1BitIdx, 0, wx.ALL, 5 )


		bSizer_bitIdx.Add( wSizer_bitIdx, 1, wx.EXPAND, 5 )


		wSizer_win.Add( bSizer_bitIdx, 1, wx.EXPAND, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


