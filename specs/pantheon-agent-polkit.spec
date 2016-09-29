Summary:        Pantheon Polkit Agent
Name:           pantheon-agent-polkit
Version:        0.1
Release:        3%{?dist}
License:        GPLv3
URL:            https://launchpad.net/pantheon-agent-polkit

Source0:        %{name}-%{version}.tar.xz
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
%cmake
%make_build


%install
%make_install
%find_lang pantheon-agent-polkit

mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp -p %{SOURCE1} %{buildroot}/%{_sysconfdir}/xdg/autostart/

mv %{buildroot}/usr/lib %{buildroot}/%{_libexecdir}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%clean
rm -rf %{buildroot}


%files -f pantheon-agent-polkit.lang
%{_sysconfdir}/xdg/autostart/pantheon-agent-polkit.desktop

%{_libexecdir}/policykit-1-pantheon/

%{_datadir}/applications/org.pantheon.agent-polkit.desktop


%changelog
* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-3
- Mass rebuild.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Add autostart file yoinked from debian packaging files.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


