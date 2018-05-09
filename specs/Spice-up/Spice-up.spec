%global appname com.github.philip-scott.spice-up

Name:           Spice-up
Summary:        Create simple and beautiful presentations on the Linux desktop
Version:        1.3.2
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/Philip-Scott/%{name}
Source0:        https://github.com/Philip-Scott/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)

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
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/%{appname}/
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/icons/hicolor/*/mimetypes/application-x-spiceup.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.mime.xml


%changelog
* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Initial package.


