Summary:        The official elementary music player
Name:           noise
Version:        0.4
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/noise

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme
Requires:       libgda-sqlite


%description
Noise is a fast and beautiful GTK3 audio player with a focus on music and libraries. It handles external devices, CDs, and album art. Noise utilizes Granite for a consistent and slick UI.

In elementary OS, Noise is known as Music.


%package        devel
Summary:        noise development headers
%description    devel
Noise is a fast and beautiful GTK3 audio player with a focus on music and libraries. It handles external devices, CDs, and album art. Noise utilizes Granite for a consistent and slick UI.

In elementary OS, Noise is known as Music.

This package contains files needed for developing with noise.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang noise


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post           devel -p /usr/sbin/ldconfig
%postun         devel -p /usr/sbin/ldconfig


%files       -f noise.lang
%doc AUTHORS NEWS README
%license COPYING

%{_bindir}/noise

%{_libdir}/libnoise-core.so.0
%{_libdir}/libnoise-core.so.0.1

%{_libdir}/noise/

%{_datadir}/applications/org.pantheon.noise.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.noise.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multimedia-audio-player.svg
%{_datadir}/metainfo/org.pantheon.noise.appdata.xml
%{_datadir}/noise/


%files          devel
%{_libdir}/libnoise-core.so
%{_libdir}/pkgconfig/noise-core.pc

%{_includedir}/noise-core/

%{_datadir}/vala/vapi/noise-core.deps
%{_datadir}/vala/vapi/noise-core.vapi


%changelog
* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.


