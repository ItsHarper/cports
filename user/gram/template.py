pkgname = "gram"
pkgver = "1.2.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--package", "gram", "--package", "cli"]
make_build_env = {
    "RELEASE_VERSION": f"{pkgver}-chimera-linux-r{pkgrel}",
    "GRAM_UPDATE_EXPLANATION": "Update Gram using the apk package manager",
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
pkgdesc = "Code editor for humanoid apes and grumpy toads, forked from Zed"
license = "GPL-3.0-only"
url = "https://gram.liten.app"
source = f"https://codeberg.org/GramEditor/gram/archive/{pkgver}.tar.gz"
sha256 = "a7197aa1803f0301c6826507a10c671349e9349851b2efbd52ae0200139bf748"
# Feel free to try getting the tests working
options = ["!check"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/gram",
        "usr/lib/gram",
        name="gram-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="gram",
    )
    self.install_file(
        "crates/gram/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/gram.desktop.in",
        "usr/share/applications",
        name="app.liten.Gram.desktop",
    )
    self.install_license("LICENSE-GPL")
