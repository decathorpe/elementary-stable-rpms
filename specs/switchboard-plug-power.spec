%global debug_package %{nil}

Summary:        Switchboard Power Plug
Name:           switchboard-plug-power
Version:        0.3
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-power

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.30.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard

Requires:       elementary-dpms-helper


%description
Control system power consumption with this Switchboard preference plug.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-power-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-power-plug.lang
%{_libdir}/switchboard/hardware/pantheon-power/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.power.policy


%changelog
* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


