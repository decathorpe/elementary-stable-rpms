Summary:        Pantheon file manager
Name:           pantheon-files
Version:        0.3.0.2
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/pantheon-files

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.29
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libnotify) >= 0.7.2
BuildRequires:  pkgconfig(pango) >= 1.1.2
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%description
The simple, powerful, and sexy file manager from elementary.
Designed for elementary OS.


%package        libs
Summary: pantheon-files libraries
%description    libs
The simple, powerful, and sexy file manager from elementary.
This package contains the libraries.


%package        devel
Summary: pantheon-files development headers
%description    devel
The simple, powerful, and sexy file manager from elementary.
This package contains the development headers.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-files


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/org.pantheon.files.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig


%files      -f pantheon-files.lang
%doc AUTHORS HACKING README
%license COPYING

%{_bindir}/pantheon-files
%{_bindir}/pantheon-files-daemon
%{_bindir}/pantheon-files-pkexec

%{_libdir}/pantheon-files/
%{_libdir}/gtk-3.0/modules/libpantheon-filechooser-module.so

%{_datadir}/appdata/org.pantheon.files.appdata.xml
%{_datadir}/applications/org.pantheon.files.desktop
%{_datadir}/dbus-1/services/pantheon-files.service
%{_datadir}/glib-2.0/schemas/org.pantheon.files.gschema.xml

%{_datadir}/pantheon-files/
%{_datadir}/pixmaps/pantheon-files/

%{_datadir}/polkit-1/actions/net.launchpad.pantheon-files.policy


%files      libs
%{_libdir}/libpantheon-files-core.so.0
%{_libdir}/libpantheon-files-core.so.0.1
%{_libdir}/libpantheon-files-widgets.so.0
%{_libdir}/libpantheon-files-widgets.so.0.1


%files      devel
%{_includedir}/pantheon-files-core
%{_includedir}/pantheon-files-widgets

%{_libdir}/libpantheon-files-core.so
%{_libdir}/libpantheon-files-widgets.so

%{_libdir}/pkgconfig/pantheon-files-core.pc
%{_libdir}/pkgconfig/pantheon-files-widgets.pc

%{_datadir}/vala/vapi/pantheon-files-core-C.vapi
%{_datadir}/vala/vapi/pantheon-files-core.deps
%{_datadir}/vala/vapi/pantheon-files-core.vapi
%{_datadir}/vala/vapi/pantheon-files-widgets.deps
%{_datadir}/vala/vapi/pantheon-files-widgets.vapi


%changelog
* Fri Sep 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.2-1
- Update to version 0.3.0.2.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-1
- Update to version 0.3.0.1.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


