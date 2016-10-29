Summary:        Metapackage to pull in pantheon session components
Name:           pantheon-session
Version:        0.1
Release:        1%{?dist}
License:        GPLv2
URL:            https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/

Requires:       cerbere
Requires:       gala
Requires:       plank
Requires:       pantheon-agent-polkit
Requires:       pantheon-session-settings
Requires:       slingshot-launcher
Requires:       wingpanel


BuildArch:      noarch


%description
This metapackage pulls in all packages that are part of a pantheon
desktop session.


%files


%changelog
* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

