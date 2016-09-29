%global debug_package %{nil}

Summary:        Adjust Locale settings from Switchboard
Name:           switchboard-plug-locale
Version:        0.2.1
Release:        2%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-locale

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Adjust Locale settings from Switchboard

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang locale-plug


%clean
rm -rf %{buildroot}


%files -f locale-plug.lang
%license COPYING

%{_libdir}/switchboard/personal/pantheon-locale/

%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.plug.locale.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.locale.policy


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-2
- Mass rebuild.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.


