pkgname = "pjzed"
pkgver = "0.179.0"
pkgrel = 0
_commit = "7ed9321efefbaf94f66da9eca1817167319d202d"
# wasmtime
archs = ["aarch64", "x86_64"]
build_style = "cargo"
prepare_after_patch = True
make_build_args = ["--package", "zed", "--package", "cli"]
make_build_env = {
    "RELEASE_VERSION": pkgver,
    "ZED_UPDATE_EXPLANATION": "Managed by system package manager",
    "ZED_RELEASE_CHANNEL": "stable",
}
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "curl-devel",
    "libgit2-devel",
    "libxkbcommon-devel",
    "rust-bindgen",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# otherwise downloads a non-working one
depends = ["nodejs"]
pkgdesc = "Graphical text editor"
license = "GPL-3.0-or-later AND AGPL-3.0-or-later AND Apache-2.0"
url = "https://zed.dev"
source = (
    f"https://github.com/panekj/zed/archive/{_commit}.tar.gz"
)
sha256 = "9263aee8850ce46b435803316e09994fcd6d24ef671f99d89fc671041884fa02"
# workaround code that fails with default gc-sections with lld
# https://github.com/zed-industries/zed/issues/15902
tool_flags = {"RUSTFLAGS": ["-Clink-arg=-Wl,-z,nostart-stop-gc"]}
# no
options = ["!check", "!cross"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/zed",
        "usr/lib/zed",
        name="zed-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="z",
    )
    self.install_file(
        "crates/zed/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="dev.zed.Zed.png",
    )
    self.install_file(
        "crates/zed/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="dev.zed.Zed.png",
    )
    self.install_file(
        "crates/zed/resources/zed.desktop.in",
        "usr/share/applications",
        name="dev.zed.Zed.desktop",
    )
    self.install_license("LICENSE-AGPL")
