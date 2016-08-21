%global debug_package %{nil}

Summary:        Notification configuration management
Name:           switchboard-plug-notifications
Version:        0.1.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-notifications

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
Configure which apps should be allowed to show notifications

A GModule plugin for Switchboard that configures gsettings keys related to the Notifications plugin for Gala.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang notifications-plug


%clean
rm -rf %{buildroot}


%files -f notifications-plug.lang
%{_libdir}/switchboard/personal/pantheon-notifications-plug/


%changelog
* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


