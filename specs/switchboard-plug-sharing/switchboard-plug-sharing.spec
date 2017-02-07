%global debug_package %{nil}

Summary:        Switchboard Sharing Plug
Name:           switchboard-plug-sharing
Version:        0.1.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-sharing

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
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
Configure the sharing of system services.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-sharing


%clean
rm -rf %{buildroot}


%files -f pantheon-sharing.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/network/pantheon-sharing/


%changelog
* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


