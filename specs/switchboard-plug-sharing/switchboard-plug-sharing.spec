%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        0.1.1
Release:        3%{?dist}
License:        GPLv3

URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Configure the sharing of system services.


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

%find_lang pantheon-sharing


%files -f pantheon-sharing.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/network/pantheon-sharing/


%changelog
* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Clean up .spec file.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


