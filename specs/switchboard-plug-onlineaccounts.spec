%global debug_package %{nil}

Summary:        Online Account Plug for Switchboard
Name:           switchboard-plug-onlineaccounts
Version:        
Release:        0%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-onlineaccounts

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Supplements:    switchboard


%description
The elementary plug for Online Accounts management.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-online-accounts


%clean
rm -rf %{buildroot}


%files -f pantheon-online-accounts.lang
# %{_libdir}/switchboard/network/pantheon-network/


%changelog

