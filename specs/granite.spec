Summary:        Granite Toolkit
Name:           granite
Version:        0.4.0.1
Release:        4%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/granite

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires: hicolor-icon-theme


%description
Granite is a library of toolkit addons to GTK+ and is part of the
elementary project.


%package        devel
Summary:        Granite Toolkit development headers
%description    devel
Granite is a library of toolkit addons to GTK+ and is part of the
elementary project.

This package contains files needed for developing with granite.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang granite


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%clean
rm -rf %{buildroot}


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


