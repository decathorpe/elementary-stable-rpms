%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-pantheon-shell
Summary:        Switchboard Pantheon Shell plug
Version:        0.2.5
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-pantheon-shell

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        %{name}.conf

Patch0:         00-fix-compilation.patch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       contractor

Supplements:    switchboard


%description
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other
desktop settings such as the panel, app launcher, and window manager.


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

%find_lang pantheon-desktop-plug


%files -f pantheon-desktop-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/personal/pantheon-desktop/

%{_libexecdir}/switchboard-plug-pantheon-shell/

%{_datadir}/contractor/set-wallpaper.contract


%changelog
* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Update to version 0.2.5.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-3
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-2
- Spec file cosmetics.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.


