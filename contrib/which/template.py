pkgname = "which"
pkgver = "2.21"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Displays where a particular program in your path is located"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "GPL-3.0-or-later"
url = "http://savannah.gnu.org/projects/which"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f4a245b94124b377d8b49646bf421f9155d36aa7614b6ebf83705d3ffc76eaad"
tool_flags = {"CXXFLAGS": ["-std=gnu++98"]}
# no check target
options = ["!check"]
