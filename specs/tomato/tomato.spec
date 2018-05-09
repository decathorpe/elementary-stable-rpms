%global appname com.github.luizaugustomm.tomato

Name:           tomato
Summary:        Simple, usable and efficient pomodoro app
Version:        2.0.2
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/luizaugustomm/%{name}
Source0:        https://github.com/luizaugustomm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Patch to remove spurious U+200B characters from appdata.xml file
Patch0:         00-appdata-unicode-cleanup.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(unity)

Requires:       hicolor-icon-theme


%description
Tomato is a simple, usable and efficient pomodoro app.


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

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/%{appname}/
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.png
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/pixmaps/%{appname}.svg


%changelog
* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Initial package.

