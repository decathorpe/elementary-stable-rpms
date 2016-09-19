Summary:        Pantheon's LightDM Login Screen
Name:           pantheon-greeter
Version:        
Release:        0%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-greeter

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(liblightdm-gobject-1) >= 1.2.1
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
Pantheon's LightDM Login Screen

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
# %find_lang pantheon-greeter


%clean
rm -rf %{buildroot}


%files
# -f pantheon-greeter.lang


%changelog

