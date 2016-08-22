%global debug_package %{nil}

Summary:        Configure all available networks
Name:           switchboard-plug-networking
Version:        0.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-networking

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
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libnm-gtk)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Configure all available networks

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-network-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-network-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/network/pantheon-network/


%changelog
* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


