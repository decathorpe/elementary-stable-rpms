Summary:        Gala window manager
Name:           gala
Version:        0.3.0~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/gala

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libmutter) >= 3.14.4
BuildRequires:  pkgconfig(plank) >= 0.3.0

Requires:       hicolor-icon-theme


%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        libs
Summary: Gala window manager libraries
%description    libs
Gala is Pantheon's Window Manager, part of the elementary project. This package contains the shared libraries.


%package        devel
Summary: Gala window manager
%description    devel
Gala is Pantheon's Window Manager, part of the elementary project. This package contains the development headers.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install
%find_lang gala

rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/plank/*.la


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


%files       -f gala.lang
%{_bindir}/gala

%{_libdir}/gala/

%{_datadir}/applications/gala.desktop
%{_datadir}/applications/gala-multitaskingview.desktop
%{_datadir}/applications/gala-other.desktop
%{_datadir}/applications/gala-wayland.desktop
%{_datadir}/gala/
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg


%files          libs
%{_libdir}/libgala.so.0
%{_libdir}/libgala.so.0.0.0


%files          devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev537-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev536-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev536-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev535-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev534-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev532-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev531-2
- Update for packaging changes.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com>
- Update spec for new gala-other.desktop file

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev531-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev529-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev527-2
- Update for packaging changes.

* Wed Jun 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev527-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev526-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev525-1
- Update to latest snapshot.

* Tue May 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev524-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev523-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev523-2
- Update for packaging changes.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev523-1
- Update to latest snapshot.

* Sun May 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev521-1
- Update to latest snapshot.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev520-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev519-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev518-2
- Update for packaging changes.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev518-1
- Update to latest snapshot.
