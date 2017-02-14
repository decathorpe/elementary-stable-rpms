Name:           capnet-assist
Summary:        Captive Portal Assistant for Pantheon
Version:        0.2.1
Release:        1%{?dist}
License:        GPLv3+
URL:            https://launchpad.net/capnet-assist

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
#BuildRequires:  gettext
BuildRequires:  vala >= 0.26
#BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       NetworkManager


%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities, etc.

Upon detection, the assistant appears showing the captive portal. Once a
connection is known to have been established, it dismisses itself.

Written in Vala and using WebkitGtk+.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

# %find_lang


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
# -f pantheon-agent-polkit.lang


%changelog
* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Initial package.


