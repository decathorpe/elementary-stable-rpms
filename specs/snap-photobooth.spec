Summary:        fast and beautiful camera app
Name:           snap-photobooth
Version:        0.3.0.1
Release:        3%{?dist}
License:        GPLv3
URL:            https://launchpad.net/snap-elementary

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)


%description
A fast and beautiful camera app.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang snap-photobooth


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%files -f snap-photobooth.lang
%{_bindir}/snap-photobooth

%{_datadir}/appdata/org.pantheon.snap.appdata.xml
%{_datadir}/applications/org.pantheon.snap.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.snap.gschema.xml


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-2
- Spec file cosmetics.

* Sun Sep 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-1
- Update to version 0.3.0.1.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


