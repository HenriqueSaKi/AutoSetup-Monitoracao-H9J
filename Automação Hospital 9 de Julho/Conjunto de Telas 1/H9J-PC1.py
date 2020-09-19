from SetupTela4 import SetupTela4 as SPC4
from SetupTela6 import SetupTela6 as SPC6
from SetupTela7 import SetupTela7 as SPC7
from SetupTela8 import SetupTela8 as SPC8


class OpenTabs:
    def __init__(self):
        pass

    def OpenWindows(self):
        SPC4().run() #SetupTela4
        SPC6().run() #SetupTela6
        SPC7().run() # SetupTela7
        SPC8().run() # SetupTela8

    def Run(self):
        self.OpenWindows()

OT = OpenTabs()
OT.Run()