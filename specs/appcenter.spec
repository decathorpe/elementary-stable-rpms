Summary:        Get apps for elementary OS
Name:           appcenter
Version:        
Release:        0%{?dist}
License:        GPLv3
URL:            https://launchpad.net/appcenter

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

Source10:       FindGirCompiler.cmake
Source11:       FindVala.cmake
Source12:       GObjectIntrospectionMacros.cmake
Source13:       GResource.cmake
Source14:       GSettings.cmake
Source15:       Tests.cmake
Source16:       Translations.cmake
Source17:       Uninstall.cmake
Source18:       ValaPrecompile.cmake
Source19:       ValaVersion.cmake

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(appstream) >= 0.9.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(packagekit-glib2)


%description
Get apps for elementary OS.

AppCenter is a native Gtk+ app store built on AppStream and Packagekit


%prep
%autosetup


%build
mkdir cmake
cp %{SOURCE10} cmake/
cp %{SOURCE11} cmake/
cp %{SOURCE12} cmake/
cp %{SOURCE13} cmake/
cp %{SOURCE14} cmake/
cp %{SOURCE15} cmake/
cp %{SOURCE16} cmake/
cp %{SOURCE17} cmake/
cp %{SOURCE18} cmake/
cp %{SOURCE19} cmake/

%cmake
%make_build


%install
%make_install
%find_lang appcenter


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f appcenter.lang
%doc AUTHORS
%license COPYING


%changelog

