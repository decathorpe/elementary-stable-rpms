Summary:        simple screen capture tool
Name:           screenshot-tool
Version:        0.1
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/screenshot-tool

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12


%description
A simple screen capture tool made for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang screenshot-tool


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/screenshot-tool.desktop


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


%files -f screenshot-tool.lang
%{_bindir}/screenshot-tool

%{_datadir}/appdata/screenshot-tool.appdata.xml
%{_datadir}/applications/screenshot-tool.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.screenshot.gschema.xml


%changelog
* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


