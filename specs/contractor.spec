Summary:        Desktop-wide extension service
Name:           contractor
Version:        0.3.2
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/contractor

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus


%description
An extension service that allows apps to use the exposed functionality of registered apps. This way, apps don't have to have the functions hard coded into them.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/contractor


%clean
rm -rf %{buildroot}


%files
%doc HACKING

%{_bindir}/contractor

%{_datadir}/contractor/
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-1
- Update to version 0.3.2.


