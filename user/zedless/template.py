pkgname = "zedless"
pkgver = "0.198.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--package", "zed", "--package", "cli"]
make_build_env = {
    "RELEASE_VERSION": f"{pkgver}-chimera-linux-{pkgrel}",
    "ZED_UPDATE_EXPLANATION": "Update Zedless using the apk package manager",
}
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
    "rust-bindgen",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Fork of the Zed text editor focused on privacy and being local-first"
license = "GPL-3.0-only"
url = "https://github.com/zedless-editor/zed"
# TODO(Harper): Switch to a mainline zedless commit, then to a tag
# source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
source = "https://github.com/ItsHarper/zedless/archive/7bccf84d6e153f27fe096acfd46ac2465fd5cbf7.tar.gz"
sha256 = "eec6c6a3cb95b6045cb802c653dbc4c936b28ab497b8ef735cbf9640d838d153"
# TODO(Harper): Attempt to enable hardening after I have a better feel for stability as-is
# hardening = ["vis", "cfi"]
# Feel free to try getting the tests working
options = ["!check"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/zed",
        "usr/lib/zedless",
        name="zedless-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="zedless",
    )
    self.install_file(
        "crates/zed/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="zedless.png",
    )
    self.install_file(
        "crates/zed/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="zedless.png",
    )
    self.install_file(
        "crates/zed/resources/zed.desktop.in",
        "usr/share/applications",
        name="org.zedless.Zedless.desktop",
    )
    self.install_license("LICENSE-GPL")
