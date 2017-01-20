Name:           elementary-theme
Summary:        elementary GTK+ Stylesheet
Version:        5.0.3
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/elementary/stylesheet

Source0:        https://launchpad.net/egtk/5.x/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildArch:      noarch

Suggests:       %{name}-gtk2


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%package        gtk2
Summary:        elementary GTK+ Stylesheet for GTK+2
Requires:       %{name} = %{version}-%{release}
Requires:       gtk-murrine-engine
%description    gtk2
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+2 theme.


%package        gtk3
Summary:        elementary GTK+ Stylesheet for GTK+3
Requires:       %{name} = %{version}-%{release}
%description    gtk3
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+3 theme.


%package        plank
Summary:        elementary GTK+ Stylesheet for plank
Requires:       %{name} = %{version}-%{release}
%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the plank theme.


%prep
%autosetup


%build
# Nothing to do


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%files
%doc AUTHORS CONTRIBUTORS HACKING
%license COPYING

%dir %{_datadir}/themes/elementary
%{_datadir}/themes/elementary/index.theme

%files          gtk2
%{_datadir}/themes/elementary/gtk-2.0/

%files          gtk3
%{_datadir}/themes/elementary/gtk-3.0/

%files          plank
%{_datadir}/themes/elementary/plank/


%changelog
* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Initial package.


