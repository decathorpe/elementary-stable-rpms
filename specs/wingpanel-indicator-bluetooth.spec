%global debug_package %{nil}

Summary:        Bluetooth indicator for wingpanel
Name:           wingpanel-indicator-bluetooth
Version:        2.0
Release:        2%{?dist}
License:        GPLv3
URL:            https://launchpad.net/wingpanel-indicator-bluetooth

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
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang bluetooth-indicator


%clean
rm -rf %{buildroot}


%files -f bluetooth-indicator.lang
%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.bluetooth.gschema.xml


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.


