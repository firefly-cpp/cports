pkgname = "akonadi-mime"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
# broken for some reason
make_check_args = ["-E", "mailserializerplugintest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "akonadi-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kmime-devel",
    "kxmlgui-devel",
    "libxslt-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi mime libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/akonadi-mime/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-mime-{pkgver}.tar.xz"
)
sha256 = "eb0829466f694daf0c4ce047073c299fd3e24be72447bdf407561822bcf1022c"


@subpackage("akonadi-mime-devel")
def _(self):
    self.depends += ["akonadi-devel"]
    return self.default_devel()
