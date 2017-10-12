%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-useraccounts
Summary:        Switchboard User Accounts Plug
Version:        0.1.6
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Switchboard Plug for managing local user accounts.


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

%find_lang useraccounts-plug


%files -f useraccounts-plug.lang
%doc README.md
%license COPYING COPYRIGHT

%{_libdir}/switchboard/system/pantheon-useraccounts/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-1
- Update to version 0.1.6.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-2
- Clean up .spec file.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Update to version 0.1.4.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.


