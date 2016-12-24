Summary:        Modular Desktop Settings Hub
Name:           switchboard
Version:        2.2.0
Release:        2%{?dist}
License:        LGPLv2.1, LGPLv3
URL:            http://launchpad.net/switchboard

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.21.0

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(unity) >= 4.0.0


%description
This project is about the container app only and its library. For
plugins that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.

Designed for elementary OS.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
%description    devel
This project is about the container app only and its library. For
plugins that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.

Designed for elementary OS.

This package contains the files required for developing for switchboard.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang switchboard


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f switchboard.lang
%license COPYING

%{_bindir}/switchboard

%{_libdir}/libswitchboard-2.0.so.0
%{_libdir}/libswitchboard-2.0.so.2.0
%{_libdir}/switchboard/

%{_datadir}/appdata/switchboard.appdata.xml
%{_datadir}/applications/org.pantheon.switchboard.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.gschema.xml


%files          devel
%{_includedir}/switchboard-2.0/

%{_libdir}/libswitchboard-2.0.so
%{_libdir}/pkgconfig/switchboard-2.0.pc

%{_datadir}/vala/vapi/switchboard-2.0.deps
%{_datadir}/vala/vapi/switchboard-2.0.vapi


%changelog
* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-2
- Enable libunity support.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Spec file cosmetics.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.


