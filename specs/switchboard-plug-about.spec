%global debug_package %{nil}

Summary:        Switchboard plug to show system information
Name:           switchboard-plug-about
Version:        0.2.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-about

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

Patch0:         00-s-elementaryos-fedora.patch

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
Switchboard plug to show system information.

Designed for elementary OS.


%prep
%setup -q
%patch0 -p1


%build
%cmake
%make_build


%install
%make_install
%find_lang about-plug


%clean
rm -rf %{buildroot}


%files -f about-plug.lang
%{_libdir}/switchboard/system/pantheon-about/about.plugin
%{_libdir}/switchboard/system/pantheon-about/libabout.so


%changelog
* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.


