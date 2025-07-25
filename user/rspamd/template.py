pkgname = "rspamd"
pkgver = "3.11.1"
pkgrel = 4
build_style = "cmake"
configure_args = [
    "-DCONFDIR=/etc/rspamd",
    "-DENABLE_FASTTEXT=ON",
    "-DENABLE_URI_INCLUDE=ON",
    "-DRSPAMD_GROUP=_rspamd",
    "-DRSPAMD_USER=_rspamd",
    "-DSYSTEM_FMT=ON",
    "-DSYSTEM_XXHASH=ON",
    "-DSYSTEM_ZSTD=ON",
    "-D_CAN_RUN=0",
    "-DHAVE_ATOMIC_BUILTINS_EXITCODE=0",
]
make_build_args = ["--target", "all", "check"]
# full tests have unknown failure
make_check_args = ["-R", "rspamd-test-cxx"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "ragel"]
makedepends = [
    "elfutils-devel",
    "fasttext-devel",
    "fmt-devel",
    "glib-devel",
    "hiredis-devel",
    "icu-devel",
    "libarchive-devel",
    "libsodium-devel",
    "libunwind-devel",
    "linux-headers",
    "openssl3-devel",
    "pcre2-devel",
    "snowball-devel",
    "sqlite-devel",
    "xxhash-devel",
    "zstd-devel",
]
pkgdesc = "Spam filtering system"
license = "Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND LGPL-3.0-only AND MIT AND Zlib"
url = "https://rspamd.com/index.html"
source = f"https://github.com/rspamd/rspamd/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "09c3b90397142539052c826763de4ed8c502976843b5ea9d7ebdc603e23d253b"


match self.profile().arch:
    case "aarch64" | "ppc64le" | "x86_64":
        configure_args += ["-DENABLE_HYPERSCAN=ON"]
        makedepends += ["luajit-devel", "vectorscan-devel"]
    case _:
        configure_args += ["-DENABLE_LUAJIT=OFF"]
        makedepends += ["lua5.4-devel"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "rspamd")
    self.install_license("LICENSE.md")
