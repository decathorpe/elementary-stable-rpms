%global appname com.github.lainsce.quilter

Name:           quilter
Summary:        Focus on your writing
Version:        1.6.3
Release:        2%{?dist}
# quilter is GPLv3
# highlight.js is BSD
# katex is MIT
License:        GPLv3 and BSD and MIT

URL:            https://github.com/lainsce/%{name}
Source0:        https://github.com/lainsce/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libmarkdown-devel
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

Provides:       bundled(highlight.js)
Provides:       bundled(katex)


%description
Quilter is a text editor that let's you focus on writing.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/%{appname}/
%{_datadir}/fonts/truetype/quilt/QuiltMono.ttf
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/quilter*.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.3-2
- Fix build with newer vala versions.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.3-1
- Update to version 1.6.3.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.2-1
- Update to version 1.6.2.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.1-1
- Update to version 1.6.1.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.6-1
- Update to version 1.5.6.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.5-1
- Initial package.

