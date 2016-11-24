%global series 0.4

Name:           granite
Summary:        elementary Development Library
Version:        0.4.0.1
Release:        5%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/granite

Source0:        https://launchpad.net/%{name}/%{series}/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires:       hicolor-icon-theme


%description
An extension to GTK+ that provides several useful widgets and classes
to ease application development.


%package        devel
Summary:        Granite Toolkit development headers
%description    devel
An extension to GTK+ that provides several useful widgets and classes
to ease application development.

This package contains the development headers.


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

%find_lang granite


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f granite.lang
%doc AUTHORS HACKING NEWS README
%license COPYING

%{_libdir}/libgranite.so.3
%{_libdir}/libgranite.so.3.0.1
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg


%files          devel
%{_bindir}/granite-demo

%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite/

%{_datadir}/applications/granite-demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
* Thu Nov 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-5
- Spec file cosmetics.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-2
- Spec file cosmetics.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-1
- Update to version 0.4.0.1.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.


