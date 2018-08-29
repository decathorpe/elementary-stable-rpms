%global appname com.github.sgpthomas.hourglass

# https://github.com/sgpthomas/hourglass/issues/46
# daemon crashes at launch

Name:           hourglass
Summary:        Simple time keeping application
Version:        1.1.1
Release:        2%{?dist}
License:        GPLv3

URL:            https://github.com/sgpthomas/%{name}
Source0:        https://github.com/sgpthomas/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# remove empty <releases> section from appdata.xml, fixing validation
Patch0:         00-remove-empty-releases.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)

Requires:       hicolor-icon-theme


%description
A simple time keeping application, supporting alarms, a stopwatch, and
timers.


%prep
%autosetup -p1


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang %{name}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{name}.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}
%{_bindir}/%{appname}-daemon

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/pixmaps/%{name}.svg


%changelog
* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-2
- Add missing BR: gcc, gcc-c++.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Initial package.

