%global debug_package %{nil}

Summary:        Datetime indicator for wingpanel
Name:           wingpanel-indicator-datetime
Version:        2.0
Release:        3%{?dist}
License:        GPLv3
URL:            https://launchpad.net/wingpanel-indicator-datetime

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
BuildRequires:  pkgconfig(libecal-1.2)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
A datetime indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang datetime-indicator


%clean
rm -rf %{buildroot}


%files -f datetime-indicator.lang
%license COPYING

%{_libdir}/wingpanel/libdatetime.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.datetime.gschema.xml


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.


