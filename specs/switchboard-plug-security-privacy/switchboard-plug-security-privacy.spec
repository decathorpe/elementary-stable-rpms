%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-security-privacy
Summary:        Switchboard Privacy and Security Plug
Version:        0.1.2
Release:        3%{?dist}
License:        LGPLv2.1, LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
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

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       light-locker
Requires:       ufw


%description
The security & privacy plug is a section in Switchboard, the elementary
System Settings app, where users can configure the security and the
level of privacy according to his needs.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-security-privacy-plug


%files -f pantheon-security-privacy-plug.lang
%doc AUTHORS README.md 
%license COPYING

%{_libdir}/switchboard/personal/pantheon-security-privacy/

%{_datadir}/glib-2.0/schemas/org.pantheon.security-privacy.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.security-privacy.policy


%changelog
* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-3
- Remove unnecessary Requires: e-dpms-helper.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Clean up .spec file.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-3
- Add missing Requires: firewalld.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-2
- Add patch to support firewalld instead of UFW.

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


