from SetupTela2 import SetupTela2 as SPC2
from SetupTela1 import SetupTela1 as SPC1

class OpenTabs:
    def __init__(self):
        pass

    def OpenWindows(self):
        SPC1().run() #SetupTela1
        SPC2().run() #SetupTela2

    def Run(self):
        self.OpenWindows()

OT = OpenTabs()
OT.Run()
