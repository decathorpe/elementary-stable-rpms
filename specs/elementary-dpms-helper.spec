Summary:        DPMS helper for elementary
Name:           elementary-dpms-helper
Version:        0~rev%{rev}
Release:        2%{?dist}
License:        GPLv3
URL:            https://code.launchpad.net/~codygarver/+junk/elementary-dpms-helper

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig

Requires:       /usr/bin/gsettings
Requires:       xorg-x11-server-utils

BuildArch:      noarch


%description
elementary DPMS helper


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mkdir -p %{buildroot}/%{_bindir}
cp dpms/elementary-dpms-helper %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp dpms/elementary-dpms-helper.desktop %{buildroot}/%{_sysconfdir}/xdg/autostart/


%clean
rm -rf %{buildroot}


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%{_sysconfdir}/xdg/autostart/elementary-dpms-helper.desktop

%{_bindir}/elementary-dpms-helper

%{_datadir}/glib-2.0/schemas/org.pantheon.dpms.gschema.xml


%changelog
* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-2
- Update for packaging changes.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev129-1
- Update to version 0.


