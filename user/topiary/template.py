pkgname = "topiary"
pkgver = "0.7.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Universal code formatter"
license = "MIT"
url = "https://topiary.tweag.io"
source = f"https://github.com/tweag/topiary/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3d7495caf3c0ae234bd6def6f33193e026564f7818d5909641be119de811f18e"
# Tests require network access to download tree-sitter grammars
options = ["!check"]


def build(self):
	# TODO(Harper): Enable building manpages once they have a less cursed setup for doing so
	#               (currently they use the unmaintained `mdbook-man` plus a custom pre-and-post processor)
    # self.do("make", wrksrc="docs/manpages")
    self.cargo.build()


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/topiary",
        name="topiary",
    )
    self.install_license("LICENSE")
