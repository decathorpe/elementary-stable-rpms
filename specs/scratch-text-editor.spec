Summary:        Scratch - the text editor that works.
Name:           scratch-text-editor
Version:        2.3
Release:        2%{?dist}
License:        GPLv3
URL:            http://launchpad.net/scratch

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-devel

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkitgtk-3.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible.
Keep things super lightweight and simple, or install extensions to turn
Scratch into a full-blown IDE; it's your choice. And with a handful of
useful preferences, you can tweak the behavior and interface to your
liking.

It's elementary. Scratch is made to be the perfect text editor for
elementary, meaning it closely follows the high standards of design,
speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala,
scripting with PHP, or marking things up in HTML, Scratch has you
covered. Experience full syntax highlighting with nearly all
programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS,
.Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua,
Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing
this software in your language!

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%package        devel
Summary:        Scratch - the text editor that works.
%description    devel
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

This package contains the development headers.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang scratch-text-editor


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f scratch-text-editor.lang
%doc HACKING README
%license COPYING

%{_bindir}/scratch-text-editor

%{_libdir}/scratch/
%{_libdir}/libscratchcore.so.0
%{_libdir}/libscratchcore.so.0.0

%{_datadir}/appdata/scratch-text-editor.appdata.xml
%{_datadir}/applications/scratch-text-editor.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.folder-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.spell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.terminal.gschema.xml

%{_datadir}/scratch/


%files          devel
%{_includedir}/scratch

%{_libdir}/libscratchcore.so
%{_libdir}/pkgconfig/scratchcore.pc

%{_datadir}/vala/vapi/scratchcore.deps
%{_datadir}/vala/vapi/scratchcore.vapi


%changelog
* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3-2
- Spec file cosmetics.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3-1
- Update to version 2.3.


