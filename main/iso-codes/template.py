pkgname = "iso-codes"
pkgver = "4.16.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gettext", "python", "pkgconf", "gmake"]
pkgdesc = "List of country, language and currency names"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://salsa.debian.org/iso-codes-team/iso-codes"
source = f"$(DEBIAN_SITE)/main/i/iso-codes/iso-codes_{pkgver}.orig.tar.xz"
sha256 = "d37ff1b2b76e63926e8043b42e0ff806bb4e41e2a57d93c9d4ec99c06b409530"
