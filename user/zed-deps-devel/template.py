pkgname = "zed-deps-devel"
pkgver = "0.192.0"
pkgrel = 6
build_style = "meta"
pkgdesc = "Code editor"
license = "custom:meta"
url = "https://github.com/zedless-editor/zed"

depends = [
    # Executables
    "cargo",
    "cmake",
    "gmake",
    "go",
    "rust-bindgen",
    "pkgconf",
    "protobuf-protoc",

    # Libraries
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "sqlite-devel",
    "zstd-devel",
]
