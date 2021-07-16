import shutil

import info
from Package.BinaryPackageBase import *


class subinfo(info.infoclass):
    vlc_ver = None

    def setTargets(self):
        self.targets["1.1"] = f"https://inkscape.org/gallery/item/26934/inkscape-1.1-x{CraftCore.compiler.bits}.7z"
        self.targetInstSrc["1.1"] = f"inkscape"
        self.webpage = "https://inkscape.org/"
        self.description = "A powerful, free design tool"

        self.defaultTarget = "1.1"

    def setDependencies(self):
        self.buildDependencies["virtual/bin-base"] = None


class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

    def install(self):
        utils.mergeTree(self.sourceDir(), os.path.join(self.installDir()))

        return True
