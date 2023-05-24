import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def registerOptions(self):
        self.options.dynamic.registerOption("osxArchs", "x86_64")

    def setTargets(self):
        self.svnTargets["master"] = "[git]https://github.com/nextcloud/desktop"

        self.description = "Nextcloud Desktop Client"
        self.displayName = "Nextcloud"
        self.webpage = "https://nextcloud.com"

        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["dev-utils/cmake"] = None
        self.buildDependencies["binary/inkscape"] = "1.1"
        self.buildDependencies["libs/pixman"] = "0.40.0"
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtwebengine"] = None
        self.runtimeDependencies["libs/qt5/qtwebsockets"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["libs/qt5/qtgraphicaleffects"] = None
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = None
        self.runtimeDependencies["libs/zlib"] = None
        self.runtimeDependencies["qt-libs/qtkeychain"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["libs/openssl"] = "3.0"
        
        if OsUtils.isMac():
            self.runtimeDependencies["libs/qt5/qtmacextras"] = None

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        
        if self.subinfo.options.dynamic.osxArchs:
            self.subinfo.options.configure.args += [f"-DCMAKE_OSX_ARCHITECTURES={self.subinfo.options.dynamic.osxArchs}"]

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["appname"] = "nextcloud"
        self.defines["company"] = "Nextcloud GmbH"
        self.applicationExecutable = "nextcloud"

        self.ignoredPackages += ["binary/mysql"]
        if not CraftCore.compiler.isLinux:
            self.ignoredPackages += ["libs/dbus"]
        if CraftCore.compiler.isMacOs:
            

        return super().createPackage()
