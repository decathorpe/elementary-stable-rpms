%global appname com.github.babluboy.bookworm

#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_dict.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_dict.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_dict.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_html.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_html.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_html.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_index.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_index.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_index.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_k8proc.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_k8proc.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_k8proc.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_ncx.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_ncx.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_ncx.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_opf.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_opf.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_opf.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_split.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_split.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_split.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_uncompress.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_uncompress.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_uncompress.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_unpack.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_unpack.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_unpack.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/mobi_lib/mobi_utils.py 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/mobi_lib/mobi_utils.py 705
#bookworm.x86_64: E: wrong-script-interpreter /usr/share/bookworm/scripts/mobi_lib/mobi_utils.py /usr/bin/env python2
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/tasks/com.github.babluboy.bookworm.htmlscripts.txt 404
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/tasks/com.github.babluboy.bookworm.monitor.sh 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/tasks/com.github.babluboy.bookworm.monitor.sh 705
#bookworm.x86_64: E: non-readable /usr/share/bookworm/scripts/tasks/com.github.babluboy.bookworm.search.sh 705
#bookworm.x86_64: E: non-standard-executable-perm /usr/share/bookworm/scripts/tasks/com.github.babluboy.bookworm.search.sh 705
#bookworm.x86_64: E: invalid-lc-messages-dir /usr/share/locale/bh/LC_MESSAGES/com.github.babluboy.bookworm.mo
#bookworm.x86_64: E: invalid-lc-messages-dir /usr/share/locale/mo/LC_MESSAGES/com.github.babluboy.bookworm.mo
#bookworm.x86_64: E: incorrect-locale-subdir /usr/share/locale/sr_Latn/LC_MESSAGES/com.github.babluboy.bookworm.mo
#bookworm.x86_64: E: invalid-lc-messages-dir /usr/share/locale/sr_Latn/LC_MESSAGES/com.github.babluboy.bookworm.mo

Name:           bookworm
Summary:        Simple ebook reader
Version:        0.9.9
Release:        2%{?dist}
License:        GPLv3

URL:            https://github.com/babluboy/%{name}
Source0:        https://github.com/babluboy/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       contractor
Requires:       hicolor-icon-theme


%description
Read the books you love without having to worry about the different
format complexities like epub, pdf, mobi, cbr, etc. This version
supports EPUB, PDF and Comics (CBR and CBZ) formats with support for
more formats to follow soon.


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

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/%{name}/
%{_datadir}/contractor/%{appname}.contract
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.*
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.9-2
- Add missing BR: gcc, gcc-c++.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.9-1
- Initial package.


