Summary:        Modular Desktop Settings Hub
Name:           switchboard
Version:        2.1.0
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
%cmake -DUSE_UNITY:BOOL=OFF
%make_build


%install
%make_install
%find_lang switchboard

mkdir -p %{buildroot}/%{_libdir}/switchboard/hardware
mkdir -p %{buildroot}/%{_libdir}/switchboard/network
mkdir -p %{buildroot}/%{_libdir}/switchboard/personal
mkdir -p %{buildroot}/%{_libdir}/switchboard/system


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


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


%files -f switchboard.lang
%license COPYING

%{_bindir}/switchboard

%{_libdir}/libswitchboard-2.0.so.0
%{_libdir}/libswitchboard-2.0.so.2.0
%{_libdir}/switchboard

%{_datadir}/appdata/switchboard.appdata.xml
%{_datadir}/applications/switchboard.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.gschema.xml


%files          devel
%{_includedir}/switchboard-2.0/

%{_libdir}/libswitchboard-2.0.so
%{_libdir}/pkgconfig/switchboard-2.0.pc

%{_datadir}/vala/vapi/switchboard-2.0.deps
%{_datadir}/vala/vapi/switchboard-2.0.vapi


%changelog
* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Spec file cosmetics.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.


