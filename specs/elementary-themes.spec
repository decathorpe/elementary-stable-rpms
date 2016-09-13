Summary:        elementary GTK+ Stylesheet
Name:           elementary-themes
Version:        5.0.1
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/egtk

Source0:        elementary.tar.xz
Source1:        %{name}.conf

BuildArch:      noarch

Requires:       gtk-murrine-engine


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS and its desktop environment: Pantheon.


%prep
%setup -q -n elementary


%build


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS HACKING
%license COPYING

%{_datadir}/themes/elementary


%changelog
* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.


