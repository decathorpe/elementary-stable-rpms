Summary:        CMake modules for elementary
Name:           cmake-elementary
Version:        0+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://code.launchpad.net/~elementary-os/+junk/cmake-modules

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  pkgconfig

Requires:       intltool

BuildArch:      noarch


%description
Most recent version of elementary's CMake modules.

Used across various projects.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%clean
rm -rf %{buildroot}


%files
%{_datadir}/cmake/Modules/*.cmake


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0+rev27-1
- Update to version 0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev27-2
- Mass rebuild.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0~rev27-1
- Update to version 0.


