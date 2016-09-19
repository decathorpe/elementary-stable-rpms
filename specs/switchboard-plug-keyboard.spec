%global debug_package %{nil}

Summary:        Adjust keyboard settings from Switchboard
Name:           switchboard-plug-keyboard
Version:        0.3
Release:        2%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-keyboard

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
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
This plug can be used to change several keyboard settings, for example
the delay and speed of the key repetition, or the cursor blinking speed.
You can change your keyboard layout, and use multiple layouts at the
same time. Keyboard shortcuts are also part of this plug.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-keyboard-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-keyboard-plug.lang
%{_libdir}/switchboard/hardware/pantheon-keyboard/


%changelog
* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-2
- Spec file cosmetics.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


