# -*- coding: utf-8 -*-
import info
import shutil
from Package.AutoToolsPackageBase import *
from Package.MakeFilePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["libp11-0.4.12"]:
            self.targets[ver] = f"https://github.com/OpenSC/libp11/releases/download/{ver}/{ver}.tar.gz"
            self.targetInstSrc[ver] = ver

        self.targetDigests["libp11-0.4.12"] = (["1e1a2533b3fcc45fde4da64c9c00261b1047f14c3f911377ebd1b147b3321cfd"], CraftHash.HashAlgorithm.SHA256)

        self.description = "A library to handle PKCS#11 cryptographic modules"
        self.defaultTarget = "libp11-0.4.12"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["libs/openssl"] = None
        self.buildDependencies["dev-utils/msys"] = None
        self.buildDependencies["dev-utils/pkg-config"] = None


class PackageMake(MakeFilePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.useShadowBuild = False
        self.subinfo.options.make.supportsMultijob = False
        self.subinfo.options.make.makeProgram = f"nmake.exe"
        self.subinfo.options.make.args += f"/f Makefile.mak OPENSSL_DIR=" + str(CraftCore.standardDirs.craftRoot())
        if CraftCore.compiler.architecture == CraftCompiler.Architecture.x86_64:
             self.subinfo.options.make.args += f" BUILD_FOR=WIN64"

    def install(self):
        pkgConfigDir = os.path.join(self.installDir(), "lib", "pkgconfig")
        utils.createDir(pkgConfigDir)

        # libp11 has a .pc.in file and we need it
        libp11pcSource = os.path.join(self.sourceDir(), "src/libp11.pc.in")
        libp11pcDest = os.path.join(self.installDir(), "lib/pkgconfig/libp11.pc")
        shutil.copyfile(libp11pcSource, libp11pcDest)

        with open(libp11pcDest, "rt") as f:
            content = f.read()

        content = content.replace("@prefix@", str(CraftCore.standardDirs.craftRoot()).replace("\\", "/"))
        content = content.replace("@exec_prefix@", "${prefix}")
        content = content.replace("@libdir@", "${prefix}/lib")
        content = content.replace("@includedir@", "${prefix}/include")
        content = content.replace("@VERSION@", "0.4.12")
        content = content.replace("-lp11", "-llibp11")

        with open(libp11pcDest, "wt") as f:
            f.write(content)

        return (
            utils.copyFile(os.path.join(self.sourceDir(), "src/libp11.h"), os.path.join(self.installDir(), "include/libp11.h"), linkOnly=False)
            and utils.copyFile(os.path.join(self.sourceDir(), "src/p11_err.h"), os.path.join(self.installDir(), "include/p11_err.h"), linkOnly=False)
            and utils.copyFile(os.path.join(self.sourceDir(), "src/libp11.dll"), os.path.join(self.installDir(), "bin/libp11.dll"), linkOnly=False)
            and utils.copyFile(os.path.join(self.sourceDir(), "src/libp11.lib"), os.path.join(self.installDir(), "lib/libp11.lib"), linkOnly=False)
            and utils.copyFile(os.path.join(self.sourceDir(), "src/pkcs11.dll"), os.path.join(self.installDir(), "bin/pkcs11.dll"), linkOnly=False)
            and utils.copyFile(os.path.join(self.sourceDir(), "src/pkcs11.lib"), os.path.join(self.installDir(), "lib/pkcs11.lib"), linkOnly=False)
        )


class PackageAutotools(AutoToolsPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.autoreconf = False

if CraftCore.compiler.isMSVC():

    class Package(PackageMake):
        pass

else:

    class Package(PackageAutotools):
        pass
