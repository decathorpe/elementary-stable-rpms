%global debug_package %{nil}

Summary:        Switchboard plug to show system information
Name:           switchboard-plug-about
Version:        0.2.1.1
Release:        3%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-about

Source0:        https://launchpad.net/switchboard-plug-about/loki/0.2.1.1/+download/switchboard-plug-about-0.2.1.1.tar.xz
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
%{_libdir}/switchboard/system/pantheon-about/


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1-2
- Spec file cleanups.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1-1
- Update to version 0.2.1.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.


