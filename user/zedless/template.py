pkgname = "zedless"
pkgver = "0.192.0"
pkgrel = 0
pkgdesc = "Code editor"
license = "GPL-3.0-only"
url = "https://github.com/zedless-editor/zed"

# TODO(Harper): Switch to cargo-auditable
hostmakedepends = [
    "cargo",
    "cmake",
    "rust-bindgen",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "sqlite-devel",
    "zstd-devel",
]
build_style = "cargo"
source = f"https://github.com/zedless-editor/zed/archive/3ab1a186f16d5554c3b91e1963f4e4e4acfcc5e4.tar.gz"
sha256 = "2a55e2e43c75f8c1c3efea2bfd556e419ba770cfeadcc7ed63fcce03abddd983"

# TODO(Harper): Compile WebRTC
#               Currently, livekit's webrtc-sys crate tries to download prebuilt webrtc binaries
#               instead of building from source.
#               Prebuilt archive (contains header files, the .a binary, and files documenting the ninja and gn configuration that was used): https://github.com/livekit/rust-sdks/releases/download/webrtc-ed96590/webrtc-linux-x64-release.zip
#               GitHub Actions workflow that manages the build process: https://github.com/livekit/rust-sdks/blob/3268abacfe5ea788144b44c7a676652c3fada3d7/.github/workflows/webrtc-builds.yml
#               Script that actually builds the binaries: https://github.com/livekit/rust-sdks/blob/3268abacfe5ea788144b44c7a676652c3fada3d7/webrtc-sys/libwebrtc/build_linux.sh
#
# Unfortunately, WebRTC does not have releases, so every software that uses it just bumps the commit being used occasionally. Therefore, it doesn't make any sense to
# create a `webrtc` package for Chimera. We could do what nixpkgs does, which is create a livekit-webrtc package.

# Also look at the alpine package for zed (which uses prebuilt webrtc, but may have patches helpful for use with musl)
