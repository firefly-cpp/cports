pkgname = "kruler"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libxcb-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE screen measuring tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kruler"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kruler-{pkgver}.tar.xz"
sha256 = "77aaff2f677eed3386cd9a2df88679fdcd19404c32d861556b3cc4dbe54e91bf"
