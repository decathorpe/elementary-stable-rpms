Summary:        elementary Icons
Name:           elementary-icon-theme
Version:        4.0.1.1
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/elementaryicons

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildArch:      noarch


%description
An original set of vector icons designed specifically for elementary OS
and its desktop environment: Pantheon.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/icons/elementary

cp -pr * %{buildroot}/%{_datadir}/icons/elementary/

rm %{buildroot}/%{_datadir}/icons/elementary/AUTHORS
rm %{buildroot}/%{_datadir}/icons/elementary/CONTRIBUTORS
rm %{buildroot}/%{_datadir}/icons/elementary/COPYING
rm %{buildroot}/%{_datadir}/icons/elementary/README.md
rm %{buildroot}/%{_datadir}/icons/elementary/pre-commit


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS
%license COPYING

%{_datadir}/icons/elementary


%changelog
* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1-1
- Update to version 4.0.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1-3
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1-2
- Spec file cosmetics.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1-1
- Update to version 4.0.1.


