%global appname com.github.parnold-x.nasc

Name:           nasc
Summary:        Do maths like a normal person
Version:        0.4.7
Release:        3%{?dist}
License:        GPLv3

URL:            https://github.com/parnold-x/%{name}
Source0:        https://github.com/parnold-x/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libsoup-2.4)

Recommends:     gnuplot
Requires:       hicolor-icon-theme


%description
NaSC is an app where you do maths like a normal person. It lets you type
whatever you want and smartly figures out what is math and spits out an
answer on the right pane. Then you can plug those answers in to future
equations and if that answer changes, so does the equations it's used
in.


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

# Manually install libqalculatenasc.so, upstream CMake error
mkdir -p %{buildroot}/%{_libdir}
cp -pav libqalculatenasc/libqalculatenasc.so %{buildroot}/%{_libdir}/
popd


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{name}

# FIXME the unversioned library is bad
%{_libdir}/libqalculatenasc.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/qalculate/styles/*


%changelog
* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.7-3
- Add missing BR: gcc, gcc-c++.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.7-2
- Fix installing libqalculatenasc.so.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.7-1
- Update to version 0.4.7.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.6-1
- Initial package.

