Summary:        DPMS helper for elementary
Name:           elementary-dpms-helper
Version:        0.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://code.launchpad.net/~codygarver/+junk/elementary-dpms-helper

Source0:        %{name}-%{version}.tar.gz
Source1:        elementary-dpms-helper-bzr.conf

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
* Fri Aug 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev229-1
- Update to latest snapshot.

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev228-1
- Update to latest snapshot.

* Mon Jul 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev227-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev226-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev224-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev223-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev220-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev219-1
- Update to latest snapshot.

* Fri Mar 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev215-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev214-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev212-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev210-1
- Update to version 0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0+rev129-2
- Mass rebuild.

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


