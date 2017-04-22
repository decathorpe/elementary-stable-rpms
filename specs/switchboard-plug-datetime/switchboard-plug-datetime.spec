%global debug_package %{nil}

Summary:        Switchboard plug to configure DateTime settings
Name:           switchboard-plug-datetime
Version:        0.1.2
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-datetime

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
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
Configure the date & time of the user.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-datetime-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-datetime-plug.lang
%{_libdir}/switchboard/system/pantheon-datetime/


%changelog
* Sat Apr 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-3
- Clean up spec.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-2
- Mass rebuild.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


