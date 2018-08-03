%global appname com.github.danrabbit.nimbus

Name:           nimbus
Summary:        Minimal weather applet
Version:        0.3.1
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/danrabbit/%{name}
Source0:        https://github.com/danrabbit/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gweather-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)

Requires:       hicolor-icon-theme


%description
See the current temperature and weather conditions for your location
with this minimal color-changing applet.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
%meson_test

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Initial package.


