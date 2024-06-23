import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def registerOptions(self):
        self.options.dynamic.registerOption("buildTests", True)

        if CraftCore.compiler.isMacOS:
            self.options.dynamic.registerOption("osxArchs", "arm64")
            self.options.dynamic.registerOption("buildMacOSBundle", True)
            self.options.dynamic.registerOption("buildFileProviderModule", False)
            self.options.dynamic.registerOption("sparkleLibPath", "")

    def setTargets(self):
        self.svnTargets["master"] = "[git]https://github.com/nextcloud/desktop"

        self.description = "Nextcloud Desktop Client"
        self.displayName = "Nextcloud"
        self.webpage = "https://nextcloud.com"

        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["dev-utils/cmake"] = None
        self.runtimeDependencies["libs/qt6/qtbase"] = None
        self.runtimeDependencies["libs/qt6/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt6/qtwebengine"] = None
        self.runtimeDependencies["libs/qt6/qtwebsockets"] = None
        self.runtimeDependencies["libs/qt6/qtmultimedia"] = None
        self.runtimeDependencies["libs/qt/qtsvg"] = None
        self.runtimeDependencies["libs/qt6/qt5compat"] = None
        self.runtimeDependencies["libs/zlib"] = None
        self.runtimeDependencies["libs/libp11"] = None
        self.runtimeDependencies["qt-libs/qtkeychain"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["libs/openssl"] = None

class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def boolToCmakeBool(value: bool) -> str:
            return "ON" if value else "OFF"

        buildTests = boolToCmakeBool(self.subinfo.options.dynamic.buildTests)
        self.subinfo.options.configure.args += [f"-DBUILD_TESTING={buildTests}"]

        if self.subinfo.options.dynamic.osxArchs:
            self.subinfo.options.configure.args += [f"-DCMAKE_OSX_ARCHITECTURES={self.subinfo.options.dynamic.osxArchs}"]
        if self.subinfo.options.dynamic.buildMacOSBundle:
            self.subinfo.options.configure.args += ["-DBUILD_OWNCLOUD_OSX_BUNDLE=ON"]
        if self.subinfo.options.dynamic.buildFileProviderModule:
            self.subinfo.options.configure.args += ["-DBUILD_FILE_PROVIDER_MODULE=ON"]
        if self.subinfo.options.dynamic.sparkleLibPath != "":
            self.subinfo.options.configure.args += [f"-DSPARKLE_LIBRARY={self.subinfo.options.dynamic.sparkleLibPath}"]

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["appname"] = "nextcloud"
        self.defines["company"] = "Nextcloud GmbH"
        self.applicationExecutable = "nextcloud"

        self.ignoredPackages += ["binary/mysql"]
        if not CraftCore.compiler.isLinux:
            self.ignoredPackages += ["libs/dbus"]

        return super().createPackage()
