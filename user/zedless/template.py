pkgname = "zedless"
pkgver = "0.198.0"
pkgrel = 4
pkgdesc = "Code editor"
license = "GPL-3.0-only"
url = "https://github.com/zedless-editor/zed"

hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "rust-bindgen",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "sqlite-devel",
    "zstd-devel",
]
build_style = "cargo"
make_build_args = ["--package", "zed", "--package", "cli"]
make_build_env = {
    "RELEASE_VERSION": f"{pkgver}-chimera-linux-{pkgrel}",
    "ZED_UPDATE_EXPLANATION": "Update Zedless using the apk package manager",
}
# TODO(Harper): Switch to mainline zedless commit, then tag
# source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
source = "https://github.com/ItsHarper/zedless/archive/8ad583be355bb480d83ff637ac22b6c11aa3f7ba.tar.gz"
sha256 = "680a2b4279373fece3362009e6e3ec9933babda58f6bacb094475e81386e629f"
# TODO(Harper): Attempt to enable hardening after I have a better feel for stability as-is
# hardening = ["vis", "cfi"]
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
