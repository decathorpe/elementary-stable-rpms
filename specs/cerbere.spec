Summary:        simple service to relaunch Pantheon components
Name:           cerbere
Version:        0.2.2
Release:        4%{?dist}
License:        GPLv2
URL:            https://launchpad.net/cerbere

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.16
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0

Recommends:     gala
Recommends:     plank
Recommends:     wingpanel


%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a
predefined list of processes (configurable through dconf) and relaunches
them if they end. This is helpful to keep the panel, dock, and wallpaper
running, even if they crash or are killed by another process.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%clean
rm -rf %{buildroot}


%files
%{_bindir}/cerbere

%{_datadir}/applications/cerbere.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-4
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-3
- Validate .desktop file.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-2
- Spec file cosmetics.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-1
- Update to version 0.2.2.


