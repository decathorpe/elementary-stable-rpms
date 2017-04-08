%global debug_package %{nil}

Summary:        Switchboard User Accounts Plug
Name:           switchboard-plug-useraccounts
Version:        0.1.3
Release:        2%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-useraccounts

Source0:        https://launchpad.net/switchboard-plug-useraccounts/loki/0.1.3/+download/switchboard-plug-useraccounts-0.1.3.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Switchboard Plug for managing local user accounts.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang useraccounts-plug


%clean
rm -rf %{buildroot}


%files -f useraccounts-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/system/pantheon-useraccounts/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.


