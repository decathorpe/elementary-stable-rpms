Summary:        Pantheon Polkit Agent
Name:           pantheon-agent-polkit
Version:        0.1.3
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/pantheon-agent-polkit

Source0:        https://launchpad.net/%{name}/loki/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        pantheon-agent-polkit.desktop

Source2:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)


%description
An agent for Polkit authorization designed for Pantheon.


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

%find_lang pantheon-agent-polkit


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files -f pantheon-agent-polkit.lang
%{_sysconfdir}/xdg/autostart/org.pantheon.agent-polkit-daemon.desktop

%{_libexecdir}/policykit-1-pantheon/

%{_datadir}/applications/org.pantheon.agent-polkit.desktop


%changelog
* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-3
- Mass rebuild.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Add autostart file yoinked from debian packaging files.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


