Summary:        Get apps for elementary OS
Name:           appcenter
Version:        0.1.3
Release:        2%{?dist}
License:        GPLv3
URL:            https://launchpad.net/appcenter

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(unity) >= 4.0.0

Requires:       PackageKit


%description
Get apps for elementary OS.

AppCenter is a native Gtk+ app store built on AppStream and Packagekit.


%prep
%autosetup


%build
mkdir build
pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang appcenter


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files -f appcenter.lang
%doc AUTHORS
%license COPYING

%{_bindir}/appcenter

%{_datadir}/appdata/appcenter.appdata.xml
%{_datadir}/applications/org.pantheon.appcenter.desktop
%{_datadir}/applications/org.pantheon.appcenter-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.appcenter.gschema.xml


%changelog
* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Enable libunity support.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Build out of tree.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Fri Oct 07 2016 Neal Gompa <ngompa13@gmail.com> - 0.1.1-4
- Add patch to support AppStream 0.10.0 in F25 (LP#1626398)

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Require PackageKit.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


