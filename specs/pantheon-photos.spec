Summary:        The elementary continuation of Shotwell
Name:           pantheon-photos
Version:        0.2
Release:        4%{?dist}
License:        LGPLv2.1
URL:            http://launchpad.net/pantheon-photos

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-photos


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%if %{?fedora} < 25
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif


%files -f pantheon-photos.lang
%doc AUTHORS MAINTAINERS NEWS README THANKS
%license COPYING

%{_bindir}/pantheon-photos

%{_libdir}/pantheon-photos/

%{_datadir}/appdata/pantheon-photos.appdata.xml
%{_datadir}/applications/pantheon-photos.desktop
%{_datadir}/applications/pantheon-photos-viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pantheon-photos/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2-2
- Spec file cosmetics.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2-1
- Update to version 0.2.


