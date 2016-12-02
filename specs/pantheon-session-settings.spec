Summary:        pantheon session configuration files
Name:           pantheon-session-settings
Version:        0.6.0+git%{date}.%{rev}
Release:        3%{?dist}
License:        GPLv2
URL:            https://github.com/decathorpe/pantheon-session-settings

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch

BuildRequires:  /usr/bin/install

Requires:       cerbere
Requires:       gnome-session
Requires:       gnome-settings-daemon

Obsoletes:      pantheon-xsession-settings


%description
This package installs a fully usable X login session and provides some
session-specific configuration files and defaults. Installing this package will
add a session called Pantheon to your login screen.


%package        overrides
Summary:        Pantheon session default settings overrides
%description    overrides
This package installs a fully usable X login session and provides some
session-specific configuration files and defaults. Installing this
ackage will add a session called Pantheon to your login screen.

This subpackage contains system-wide overrides for pantheon-session
default settings.

Requires:       google-roboto-mono-fonts
Requires:       open-sans-fonts


%package        wayland
Summary:        Pantheon session settings for wayland
%description    wayland
This package installs a fully usable X login session and provides some
session-specific configuration files and defaults. Installing this
ackage will add a session called Pantheon to your login screen.

This subpackage contains the settings files for the (not yet supported)
wayland session.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart

mkdir -p %{buildroot}/%{_datadir}/gnome-session/sessions
mkdir -p %{buildroot}/%{_datadir}/pantheon/applications
mkdir -p %{buildroot}/%{_datadir}/wayland-sessions
mkdir -p %{buildroot}/%{_datadir}/xsessions
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas

rm autostart/cerbere.desktop
install -p autostart/* %{buildroot}/%{_sysconfdir}/xdg/autostart/

ln -s %{_datadir}/applications/cerbere.desktop %{buildroot}/%{_sysconfdir}/xdg/autostart/cerbere.desktop

install -p gnome-session/* %{buildroot}/%{_datadir}/gnome-session/sessions/
install -p applications/* %{buildroot}/%{_datadir}/pantheon/applications
install -p wayland-sessions/pantheon-wayland.desktop %{buildroot}/%{_datadir}/wayland-sessions/
install -p xsessions/pantheon.desktop %{buildroot}/%{_datadir}/xsessions/
install -p overrides/20-org.pantheon.desktop-interface.gschema.override %{buildroot}/%{_datadir}/glib-2.0/schemas/


%postun         overrides
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans      overrides
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%{_sysconfdir}/xdg/autostart/*.desktop

%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/pantheon/
%{_datadir}/xsessions/pantheon.desktop

%files      overrides
%{_datadir}/glib-2.0/schemas/20-org.pantheon.desktop-interface.gschema.override

%files      wayland
%{_datadir}/gnome-session/sessions/pantheon-wayland.session
%{_datadir}/wayland-sessions/pantheon-wayland.desktop


%changelog
* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0+git160919.154120.5d95d50d-3
- Move wayland files into a subpackage.

* Wed Oct 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0+git160919.154120.5d95d50d-2
- Add glib-compile-schemas scriptlet to -overrides subpackage.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0+git160919.154120.5d95d50d-1
- Update to version 0.6.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160919.154120~5d95d50d-2
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160919.154120~5d95d50d-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160919.122259~bbca0223-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160816.150620~a374988e-2
- Spec file cosmetics. Add overrides subpackage.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160816.150620~a374988e-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160511.103851~c38f740b-5
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160511.103851~c38f740b-4
- Update for packaging changes.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160511.103851~c38f740b-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160511.103851~c38f740b-2
- Update for packaging changes.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.0~git160511.103851~c38f740b-1
- Update to version 0.6.0.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.5.0~rev65-3
- Update for packaging changes.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.5.0~rev65-2
- Update for packaging changes.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.5.0~rev%{rev}-1
- Initial package.


