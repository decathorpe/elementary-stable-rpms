Summary:        A tiny, simple calculator written in GTK+ and Vala.
Name:           pantheon-calculator
Version:        0.1.1.1
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-calculator

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6


%description
A tiny, simple calculator written in GTK+ and Vala.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-calculator


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


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


%files -f pantheon-calculator.lang
%doc AUTHORS
%license COPYING

%{_bindir}/pantheon-calculator

%{_datadir}/appdata/org.pantheon.calculator.appdata.xml
%{_datadir}/applications/org.pantheon.calculator.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.calculator.gschema.xml


%changelog
* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Spec file cosmetics.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


