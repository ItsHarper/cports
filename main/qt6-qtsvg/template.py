pkgname = "qt6-qtsvg"
pkgver = "6.9.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "module_includes"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-private-devel"]
pkgdesc = "Qt6 SVG component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsvg-everywhere-src-{pkgver}.tar.xz"
sha256 = "2dfc5de5fd891ff2afd9861e519bf1a26e6deb729b3133f68a28ba763c9abbd5"
# FIXME
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtsvg-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
