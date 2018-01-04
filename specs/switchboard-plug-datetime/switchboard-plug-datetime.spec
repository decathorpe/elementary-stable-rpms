%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-datetime
Summary:        Switchboard Date and Time plug
Version:        0.1.2
Release:        4%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
A switchboard plug to configure date and time settings.


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

%find_lang pantheon-datetime-plug


%files -f pantheon-datetime-plug.lang
%doc README.md

%{_libdir}/switchboard/system/pantheon-datetime/


%changelog
* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Clean up .spec file.

* Sat Apr 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-3
- Clean up spec.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-2
- Mass rebuild.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


