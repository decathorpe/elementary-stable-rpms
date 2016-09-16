Summary:        Single signon authentication library for GLib applications
Name:           libgsignon-glib
Version:        2.4.1~git%{date}~%{rev}
Release:        1%{?dist}
License:        LGPLv2.1
URL:            https://gitlab.com/accounts-sso/libgsignon-glib

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(sqlite3)


%description
This project is a library for managing single signon credentials which can be used from GLib applications. It is effectively a GLib binding for the D-Bus API provided by gsignond.


%package        devel
Summary:        Single signon authentication library for GLib applications development files
%description    devel
This project is a library for managing single signon credentials which can be used from GLib applications. It is effectively a GLib binding for the D-Bus API provided by gsignond.


%prep
%autosetup


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error"

./autogen.sh
%configure --enable-dbus-type=session
%make_build


%install
%make_install

rm %{buildroot}/%{_libdir}/*.la


%clean
rm -rf %{buildroot}


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post    devel -p /sbin/ldconfig
%postun  devel -p /sbin/ldconfig


%files
%{_libdir}/libgsignon-glib.so.1
%{_libdir}/libgsignon-glib.so.1.0.0
%{_libdir}/girepository-1.0/gSignon-1.0.typelib


%files          devel
%{_bindir}/gsso-example

%{_includedir}/libgsignon-glib/

%{_libdir}/libgsignon-glib.so
%{_libdir}/pkgconfig/libgsignon-glib.pc

%{_datadir}/gir-1.0/gSignon-1.0.gir
%{_datadir}/vala/vapi/libgsignon-glib.deps
%{_datadir}/vala/vapi/libgsignon-glib.vapi


%changelog
* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.1~git160715.081154~bf917794-1
- Update to version 2.4.1.


