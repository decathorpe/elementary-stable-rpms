Summary:        The terminal of the 21st century.
Name:           pantheon-terminal
Version:        0.4
Release:        4%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-terminal

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vte-2.91)


%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.

Designed for elementary OS.


%prep
%autosetup


%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="$RPM_OPT_FLAGS -fPIC"

%cmake
%make_build


%install
%make_install
%find_lang pantheon-terminal


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%files -f pantheon-terminal.lang
%doc AUTHORS HACKING README
%license LICENSE

%{_bindir}/pantheon-terminal

%{_datadir}/appdata/pantheon-terminal.appdata.xml
%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/org.pantheon.terminal.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.terminal.gschema.xml
%{_datadir}/pantheon-terminal/


%changelog
* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-4
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-3
- Spec file cosmetics.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-2
- Add -fPIC compiler switch to fix build.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.


