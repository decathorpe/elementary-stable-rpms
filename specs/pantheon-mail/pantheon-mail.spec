%global srcname mail

Name:           pantheon-mail
Summary:        E-Mail client for Pantheon
Version:        1.0.6
Release:        2%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        https://github.com/elementary/mail/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.1

BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.17
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(unity) >= 5.12.0
BuildRequires:  pkgconfig(webkitgtk-3.0)


%description
Pantheon Mail is the E-Mail client for the Pantheon desktop.


%package        contract
Summary:        E-Mail client for Pantheon (contractor support)

Requires:       contractor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    contract
Pantheon Mail is the E-Mail client for the Pantheon desktop.
This package contains the contractor support.


%prep
%autosetup -n %{srcname}-%{version}


%build
mkdir build && pushd build
%cmake .. \
    -DICON_UPDATE:BOOL=OFF \
    -DDESKTOP_UPDATE:BOOL=OFF
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-mail


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pantheon.mail.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-mail-autostart.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files -f pantheon-mail.lang
%doc README.md
%license COPYING

%{_bindir}/pantheon-mail

%{_datadir}/accounts/applications/pantheon-mail.application
%{_datadir}/applications/org.pantheon.mail.desktop
%{_datadir}/applications/pantheon-mail-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.mail.gschema.xml
%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files contract
%{_bindir}/mail-attach
%{_datadir}/contractor/mail-attach.contract


%changelog
* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-2
- Rebuild for the granite 0.5 soname bump.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Initial package.

