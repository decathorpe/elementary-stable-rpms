Summary:        Metapackage to pull in pantheon session components
Name:           pantheon-session
Version:        0.4
Release:        1%{?dist}
License:        GPLv2
URL:            https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/

# Pantheon desktop components
Requires:       capnet-assist
Requires:       cerbere
Requires:       gala
Requires:       plank
Requires:       pantheon-agent-polkit
Requires:       pantheon-session-settings
Requires:       wingpanel


BuildArch:      noarch


%description
This metapackage pulls in all packages that are part of a pantheon
desktop session.


%files


%changelog
* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Adapt to package changes.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

