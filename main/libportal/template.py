pkgname = "libportal"
pkgver = "0.8.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dbackend-gtk3=enabled",
    "-Dbackend-gtk4=enabled",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "gtk+3-devel", "gtk4-devel"]
pkgdesc = "Flatpak portal library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://github.com/flatpak/libportal"
source = f"{url}/releases/download/{pkgver}/libportal-{pkgver}.tar.xz"
sha256 = "ca38cd186e98388e4e92859506c9ecbd01db650ef871838b357b117d147f1541"


@subpackage("libportal-gtk3")
def _(self):
    self.subdesc = "Gtk+3 backend"

    return ["usr/lib/girepository-1.0/XdpGtk3*", "usr/lib/libportal-gtk3.so.*"]


@subpackage("libportal-gtk4")
def _(self):
    self.subdesc = "Gtk4 backend"

    return ["usr/lib/girepository-1.0/XdpGtk4*", "usr/lib/libportal-gtk4.so.*"]


@subpackage("libportal-devel")
def _(self):
    return self.default_devel()
