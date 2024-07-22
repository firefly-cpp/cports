pkgname = "liborcus"
pkgver = "0.19.2"
pkgrel = 3
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "python"]
makedepends = [
    "boost-devel",
    "ixion-devel",
    "mdds",
    "python-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for processing spreadsheets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/orcus/orcus"
source = f"{url}/-/archive/{pkgver}/liborcus-{pkgver}.tar.gz"
sha256 = "f4668f050f4f3f28fac5b821a4580929d130ffa1fcd5d74bb8ce06db63480270"


@subpackage("liborcus-progs")
def _libs(self):
    return self.default_progs()


@subpackage("liborcus-python")
def _python(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("liborcus-devel")
def _devel(self):
    return self.default_devel()
