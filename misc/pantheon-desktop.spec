Summary:        Metapackage to pull in pantheon desktop components
Name:           pantheon-desktop
Version:        0.4
Release:        1%{?dist}
License:        GPLv2
URL:            https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/

Requires:       pantheon-session

# elementary desktop applications
Recommends:     appcenter
Recommends:     audience
Recommends:     maya-calendar
Recommends:     noise
Recommends:     pantheon-calculator
Recommends:     pantheon-files
Recommends:     pantheon-photos
Recommends:     pantheon-terminal
Recommends:     scratch-text-editor
Recommends:     screenshot-tool
Recommends:     snap-photobooth
Recommends:     switchboard

# elementary artwork
Recommends:     elementary-icon-theme
Recommends:     elementary-theme
Recommends:     elementary-wallpapers


BuildArch:      noarch


%description
This metapackage pulls in all packages that are part of a pantheon
desktop.


%files


%changelog
* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Adapt to elementary-wallpapers renaming.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Adapt to renamed elementary-theme package.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

