%global debug_package %{nil}

Summary:        Switchboard Privacy and Security Plug
Name:           switchboard-plug-security-privacy
Version:        0.1.1.1
Release:        1%{?dist}
License:        LGPLv2.1, LGPLv3
URL:            https://launchpad.net/switchboard-plug-security-privacy

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Supplements:    switchboard

Requires:       elementary-dpms-helper
Requires:       light-locker


%description
The security & privacy plug is a section in Switchboard, the elementary
System Settings app, where users can configure the security and the
level of privacy according to his needs.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-security-privacy-plug



%files -f pantheon-security-privacy-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/personal/pantheon-security-privacy/

%{_datadir}/polkit-1/actions/org.pantheon.security-privacy.policy


%changelog
* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-4
- Add Requires: light-locker.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Spec file cosmetics.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com>
- Add Requires: elementary-dpms-helper.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


