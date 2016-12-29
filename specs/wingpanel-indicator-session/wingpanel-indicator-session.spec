%global debug_package %{nil}

Summary:        Session Indicator for wingpanel
Name:           wingpanel-indicator-session
Version:        2.0.1
Release:        1%{?dist}
License:        GPLv3, LGPLv3
URL:            https://launchpad.net/wingpanel-indicator-session

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
A session Indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang session-indicator


%clean
rm -rf %{buildroot}


%files -f session-indicator.lang
%license COPYING

%{_libdir}/wingpanel/libsession.so


%changelog
* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to latest snapshot.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com>
- Weak inverse require wingpanel.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

