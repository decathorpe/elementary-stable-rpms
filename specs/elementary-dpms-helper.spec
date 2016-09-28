Summary:        DPMS helper for elementary
Name:           elementary-dpms-helper
Version:        0+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://code.launchpad.net/~codygarver/+junk/elementary-dpms-helper

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig

Requires:       /usr/bin/gsettings
Requires:       xorg-x11-server-utils

BuildArch:      noarch


%description
elementary DPMS helper


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mkdir -p %{buildroot}/%{_bindir}
cp dpms/elementary-dpms-helper %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp dpms/elementary-dpms-helper.desktop %{buildroot}/%{_sysconfdir}/xdg/autostart/


%clean
rm -rf %{buildroot}


%files
%{_sysconfdir}/xdg/autostart/elementary-dpms-helper.desktop

%{_bindir}/elementary-dpms-helper

%{_datadir}/glib-2.0/schemas/org.pantheon.dpms.gschema.xml


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0+rev129-1
- Update to version 0.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-4
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-3
- Spec file cosmetics.

* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-2
- Update for packaging changes.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-1
- Update to version 0.


