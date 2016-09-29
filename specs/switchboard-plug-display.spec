%global debug_package %{nil}

Summary:        Switchboard plug to show displays information
Name:           switchboard-plug-display
Version:        0.1.2
Release:        2%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-display

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
A switchboard plug to show displays information.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-display-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-display-plug.lang
%{_libdir}/switchboard/hardware/pantheon-display/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Mass rebuild.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.


