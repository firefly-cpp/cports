pkgname = "akregator"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-devel",
    "grantleetheme-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "syndication-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE RSS feed reader"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/akregator"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akregator-{pkgver}.tar.xz"
sha256 = "b7035b4b644fda7e95417ed5706e44a7331a7728bd506d99650ba1bfb23072d0"
# INT: probably a shift overflow in remap.cpp:CalcHash
hardening = ["!int"]
