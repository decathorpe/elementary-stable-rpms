%global debug_package %{nil}

Summary:        Application configuration management
Name:           switchboard-plug-applications
Version:        0.1.1
Release:        4%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/switchboard-plug-applications

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
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang applications-plug


%clean
rm -rf %{buildroot}


%files -f applications-plug.lang
%{_libdir}/switchboard/personal/pantheon-applications-plug/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-4
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Spec file cosmetics.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Add Supplements: switchboard tag.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


