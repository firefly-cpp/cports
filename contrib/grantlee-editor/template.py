pkgname = "grantlee-editor"
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
    "akonadi-contacts-devel",
    "grantleetheme-devel",
    "karchive-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kimap-devel",
    "kio-devel",
    "kmime-devel",
    "ktextaddons-devel",
    "kxmlgui-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE editor for Grantlee themes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/grantlee-editor"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantlee-editor-{pkgver}.tar.xz"
)
sha256 = "38537f69b1d24347ef8143e5c729ba183c3a0eaf55d63a7929a4f43204dc8efe"
