import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = "[git]https://github.com/getsentry/sentry-native"

        self.targets["0.7.15"] = f"https://github.com/getsentry/sentry-native/releases/download/0.7.15/sentry-native.zip"
        self.targetDigests["0.7.15"] = (["9880614984c75fc6ed1967b7aa29aebbea2f0c88f2d7c707b18391b5632091c0"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Official Sentry SDK for C/C++ "
        self.displayName = "sentry-native"
        self.webpage = "https://github.com/getsentry/sentry-native"

        self.defaultTarget = "0.7.15"

    def setDependencies(self):
        self.buildDependencies["dev-utils/cmake"] = None
        self.runtimeDependencies["libs/qt6/qtbase"] = None

class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.subinfo.options.configure.args += [
            f"-DSENTRY_BACKEND=crashpad",
            f"-DSENTRY_INTEGRATION_QT=YES",
        ]

