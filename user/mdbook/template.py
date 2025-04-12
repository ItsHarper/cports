pkgname = "mdbook"
pkgver = "0.4.52"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=failing_tests",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = (
    "Create book from markdown files. Like Gitbook but implemented in Rust"
)
license = "MPL-2.0"
url = "https://rust-lang.github.io/mdBook"
source = (
    f"https://github.com/rust-lang/mdBook/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "d46f3b79e210eed383b6966847ea86ec441b6b505e9d9d868294bb9742130c9c"
