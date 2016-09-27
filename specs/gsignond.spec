Summary:        GSignOn daemon
Name:           gsignond
Version:        
Release:        0%{?dist}
License:        GPLv3
URL:            https://gitlab.com/accounts-sso/gsignond

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(sqlite3)


%description
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.


%package        libs
Summary:        GSignOn daemon libraries
%description    libs
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.


%package        devel
Summary:        GSignOn daemon development files
%description    devel
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.


%prep
%autosetup


%build
./autogen.sh
%configure --disable-static --enable-dbus-type=session
%make_build


%install
%make_install

rm %{buildroot}/%{_libdir}/*.la


%clean
rm -rf %{buildroot}


%post    libs -p /sbin/ldconfig
%postun  libs -p /sbin/ldconfig


%files
%{_bindir}/gsignond
%{_libdir}/gsignond/

%{_sysconfdir}/gsignond.conf

%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.gSingleSignOn.*.xml
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOn.service


%files          libs
%{_libdir}/libgsignond-common.so.0
%{_libdir}/libgsignond-common.so.0.0.0
%{_libdir}/girepository-1.0/gSignond-1.0.typelib


%files          devel
%{_includedir}/gsignond/

%{_libdir}/libgsignond-common.so
%{_libdir}/pkgconfig/gsignond.pc

%{_datadir}/gir-1.0/gSignond-1.0.gir
%{_datadir}/vala/vapi/gsignond.deps
%{_datadir}/vala/vapi/gsignond.vapi


%changelog

