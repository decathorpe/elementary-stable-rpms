Summary:        simple screen capture tool
Name:           screenshot-tool
Version:        0.1.0.3
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/screenshot-tool

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12


%description
A simple screen capture tool made for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang screenshot-tool


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%files -f screenshot-tool.lang
%{_bindir}/screenshot-tool

%{_datadir}/appdata/screenshot-tool.appdata.xml
%{_datadir}/applications/screenshot-tool.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.screenshot.gschema.xml


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-3
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-2
- Add BR: intltool to hopefully fix f25 build.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-1
- Update to version 0.1.0.3.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2-2
- Spec file cosmetics.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2-1
- Update to version 0.1.0.2.

* Wed Sep 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1-1
- Update to version 0.1.0.1.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


