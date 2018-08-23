%global appname  com.github.philip-scott.spice-up
%global dbusname com.github.philip_scott.spice_up

Name:           Spice-up
Summary:        Create simple and beautiful presentations on the Linux desktop
Version:        1.5.0
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/Philip-Scott/%{name}
Source0:        https://github.com/Philip-Scott/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme


%description
Spice-up is a modern and intuitive desktop presentation app based upon
SpiceOfDesign's presentation concept. Built from the ground up for
elementary, it gives you everything you need to create simple and
beautiful presentations.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{dbusname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/%{appname}/
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/icons/hicolor/*/mimetypes/application-x-spiceup.svg
%{_datadir}/metainfo/%{dbusname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.mime.xml


%changelog
* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Initial package.


