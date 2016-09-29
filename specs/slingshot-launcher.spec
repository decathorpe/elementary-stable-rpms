%global debug_package %{nil}

Summary:        Lightweight and stylish app launcher
Name:           slingshot-launcher
Version:        2.0
Release:        3%{?dist}
License:        GPLv3
URL:            https://launchpad.net/slingshot

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       zeitgeist


%description
The lightweight and stylish app launcher from elementary.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake -DUSE_UNITY:BOOL=OFF -DUSE_ZEITGEIST:BOOL=ON
%make_build


%install
%make_install
%find_lang slingshot


%clean
rm -rf %{buildroot}


%files -f slingshot.lang
%doc AUTHORS
%license COPYING

%{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.slingshot.gschema.xml


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.


