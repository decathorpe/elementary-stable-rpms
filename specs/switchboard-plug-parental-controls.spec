%global debug_package %{nil}

Summary:        An easy parental controls plug
Name:           switchboard-plug-parental-controls
Version:        0.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-parental-controls

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
An easy parental controls plug


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mv %{buildroot}/lib %{buildroot}/usr/lib
rm %{buildroot}/%{_libdir}/*.a

%find_lang pantheon-parental-controls-plug


%clean
rm -rf %{buildroot}


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%post
%systemd_post pantheon-parental-controls.service

%preun
%systemd_preun pantheon-parental-controls.service

%postun
%systemd_postun_with_restart pantheon-parental-controls.service


%files -f pantheon-parental-controls-plug.lang
%doc AUTHORS
%license COPYING

%{_sysconfdir}/dbus-1/system.d/org.pantheon.ParentalControls.conf

%{_bindir}/pantheon-parental-controls-cli
%{_bindir}/pantheon-parental-controls-client
%{_bindir}/pantheon-parental-controls-daemon

%{_libdir}/switchboard/system/pantheon-parental-controls/libpantheon-parental-controls.so

%{_datadir}/applications/pantheon-parental-controls-client.desktop
%{_datadir}/dbus-1/system-services/org.pantheon.ParentalControls.service
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.parental-controls.policy

%{_unitdir}/pantheon-parental-controls.service


%changelog
* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


