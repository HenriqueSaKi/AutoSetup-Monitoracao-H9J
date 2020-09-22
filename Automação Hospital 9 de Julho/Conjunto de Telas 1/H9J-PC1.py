from SetupTela4 import SetupTela4 as SPC4
from SetupTela6 import SetupTela6 as SPC6
from SetupTela7 import SetupTela7 as SPC7
from SetupTela8 import SetupTela8 as SPC8
from Position import ScreenPosition

SP = ScreenPosition()

SP.EnableExtension()
SP.moveUntil(8)
SPC8().MaxScreen()
SP.EnableExtension()
SP.moveUntil(7)
SPC7().MaxScreen()
SP.EnableExtension()
SP.moveUntil(6)
SPC6().MaxScreen()
SP.EnableExtension()
SP.moveUntil(4)
SPC4().MaxScreen()
