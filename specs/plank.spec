Summary:        Stupidly simple Dock
Name:           plank
Version:        0.11.2
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/plank

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.2.92
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       bamf-daemon
Requires:       hicolor-icon-theme


%description
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.


%package        libs
Summary: Stupidly simple Dock (shared libraries)
%description    libs
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.
This package contains the shared libraries.


%package        devel
Summary: Stupidly simple Dock (development files)
%description    devel
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.
This package contains development headers and files.


%prep
%autosetup


%build
%configure --disable-apport
%make_build


%install
%make_install
%find_lang plank

rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/plank/*.la


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post           libs -p /sbin/ldconfig
%postun         libs -p /sbin/ldconfig

%post           devel -p /sbin/ldconfig
%postun         devel -p /sbin/ldconfig


%files -f plank.lang
%{_bindir}/plank

%{_libdir}/plank/

%{_datadir}/appdata/plank.appdata.xml
%{_datadir}/applications/plank.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.plank.gschema.xml
%{_datadir}/icons/hicolor/*/apps/plank.svg
%{_datadir}/plank/

%{_mandir}/man1/plank.1.gz


%files libs
%{_libdir}/libplank.so.1
%{_libdir}/libplank.so.1.0.0


%files devel
%{_libdir}/libplank.so
%{_libdir}/pkgconfig/plank.pc

%{_includedir}/plank/

%{_datadir}/vala/vapi/plank.deps
%{_datadir}/vala/vapi/plank.vapi


%changelog
* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2-1
- Update to version 0.11.2.


