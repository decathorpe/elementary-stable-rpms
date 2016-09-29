%global debug_package %{nil}

Summary:        Mouse and Touchpad configuration management
Name:           switchboard-plug-mouse-touchpad
Version:        0.1.1
Release:        2%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-mouse-touchpad

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

Patch0:         00-gschema-path.patch

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
This is a switchboard plug for elementary os.


%prep
%setup -q
%patch0 -p0


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mouse-touchpad


%clean
rm -rf %{buildroot}


%files -f pantheon-mouse-touchpad.lang
%{_libdir}/switchboard/hardware/pantheon-mouse-touchpad/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


