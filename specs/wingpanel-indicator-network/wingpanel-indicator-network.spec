%global debug_package %{nil}

Summary:        Network indicator for wingpanel
Name:           wingpanel-indicator-network
Version:        2.0.2
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/wingpanel-indicator-network

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libnm-gtk)
BuildRequires:  pkgconfig(libnm-util)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
A network indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang network-indicator


%clean
rm -rf %{buildroot}


%files -f network-indicator.lang
%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.network.gschema.xml


%changelog
* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Spec file cleanups.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.


