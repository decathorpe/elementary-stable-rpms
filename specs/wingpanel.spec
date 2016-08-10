Summary:        Stylish top panel
Name:           wingpanel
Version:        0.4
Release:        1%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/wingpanel

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala >= 0.24.0

BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libnotify)


%description
Stylish top panel that holds indicators and spawns an application launcher

Designed for elementary OS.


%package        devel
Summary:        Stylish top panel (development files)
%description    devel
Stylish top panel that holds indicators and spawns an application launcher

Designed for elementary OS.

This package contains the files required for developing for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang wingpanel


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/wingpanel.desktop


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


%post           devel -p /sbin/ldconfig
%postun         devel -p /sbin/ldconfig


%files -f wingpanel.lang
%license COPYING

%{_bindir}/wingpanel

%{_libdir}/gala/plugins/libwingpanel-interface.so
%{_libdir}/libwingpanel-2.0.so.0
%{_libdir}/libwingpanel-2.0.so.0.2.0

%{_datadir}/applications/wingpanel.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml


%files          devel
%{_includedir}/wingpanel-2.0/

%{_libdir}/libwingpanel-2.0.so
%{_libdir}/pkgconfig/wingpanel-2.0.pc

%{_datadir}/vala/vapi/wingpanel-2.0.deps
%{_datadir}/vala/vapi/wingpanel-2.0.vapi


%changelog
* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.


