Name:           switchboard-plug-power
Summary:        Switchboard Power Plug
Version:        0.3.1
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.30.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}

Requires:       elementary-dpms-helper


%description
Control system power consumption with this Switchboard preference plug.


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

%find_lang pantheon-power-plug


%files -f pantheon-power-plug.lang
%{_libdir}/switchboard/hardware/pantheon-power/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.power.policy


%changelog
* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-2
- Mass rebuild.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


