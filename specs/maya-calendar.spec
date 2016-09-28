Summary:        The official elementary calendar
Name:           maya-calendar
Version:        0.4.0.2
Release:        5%{?dist}
License:        GPLv3
URL:            http://launchpad.net/maya

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libical)

Requires:       hicolor-icon-theme


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.


%package devel
Summary: The official elementary calendar (devel files)
%description devel
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.

This package contains the development files.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang maya-calendar


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%if %{?fedora} < 25
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%postun
/sbin/ldconfig

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%if %{?fedora} < 25
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f maya-calendar.lang
%doc AUTHORS COPYRIGHT HACKING
%license COPYING

%{_bindir}/maya-calendar
%{_bindir}/maya-calendar-daemon

%{_libdir}/libmaya-calendar.so.0
%{_libdir}/libmaya-calendar.so.0.1
%{_libdir}/maya-calendar/

%{_datadir}/appdata/maya-calendar.appdata.xml
%{_datadir}/applications/maya-calendar.desktop
%{_datadir}/applications/maya-calendar-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.maya.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/calendar-go-today.svg
%{_datadir}/maya-calendar/


%files          devel
%{_includedir}/maya-calendar/

%{_libdir}/libmaya-calendar.so
%{_libdir}/pkgconfig/maya-calendar.pc

%{_datadir}/vala/vapi/maya-calendar.deps
%{_datadir}/vala/vapi/maya-calendar.vapi


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2-5
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2-4
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2-3
- Validate all .desktop files.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2-2
- Spec file cosmetics.

* Tue Sep 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2-1
- Update to version 0.4.0.2.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-1
- Update to version 0.4.0.1.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.


