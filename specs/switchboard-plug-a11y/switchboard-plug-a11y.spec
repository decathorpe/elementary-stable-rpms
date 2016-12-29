%global debug_package %{nil}

Summary:        Accessibility plug for Switchboard
Name:           switchboard-plug-a11y
Version:        0.1
Release:        4%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-a11y

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
The accessibility plug is a section in the Switchboard (System Settings)
that allows the user to manage accessibility settings.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-accessibility-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-accessibility-plug.lang
%{_libdir}/switchboard/system/pantheon-accessibility/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Spec file cosmetics.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


