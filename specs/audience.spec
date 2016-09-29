Summary:        Audience video player
Name:           audience
Version:        0.2.0.2
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/audience

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)


%description
A modern video player that brings the lessons learned from the web home
to the desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang audience


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


%files -f audience.lang
%doc AUTHORS README
%license COPYING

%{_bindir}/audience

%{_datadir}/appdata/org.pantheon.audience.appdata.xml
%{_datadir}/applications/org.pantheon.audience.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.audience.gschema.xml


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2-2
- Spec file cleanups.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2-1
- Update to version 0.2.0.2.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1-2
- Spec file cosmetics.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1-1
- Update to version 0.2.0.1.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2-1
- Update to version 0.2.


