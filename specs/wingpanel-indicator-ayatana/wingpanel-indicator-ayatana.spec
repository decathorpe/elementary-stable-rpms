%global debug_package %{nil}

Summary:        Ayatana indicator for wingpanel
Name:           wingpanel-indicator-ayatana
Version:        2.0.2
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/wingpanel-indicator-ayatana

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
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
An ayatana indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%clean
rm -rf %{buildroot}


%files
%{_libdir}/wingpanel/libayatana_compatibility.so


%changelog
* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.


