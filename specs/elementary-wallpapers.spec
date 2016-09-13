Summary:        Wallpapers for elementary OS
Name:           elementary-wallpapers
Version:        0~git%{date}~%{rev}
Release:        1%{?dist}
License:        CC-BY-SA
URL:            http://github.com/elementary/wallpapers

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch


%description
Wallpapers for elementary OS


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/backgrounds/elementary

cp -p *.jpg %{buildroot}/%{_datadir}/backgrounds/elementary/
cp -pr extra %{buildroot}/%{_datadir}/backgrounds/elementary/


%clean
rm -rf %{buildroot}


%files
%{_datadir}/backgrounds/elementary


%changelog
* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0~git160615.091501~71cd2c90-1
- Update to version 0.


