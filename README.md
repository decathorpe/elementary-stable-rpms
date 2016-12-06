# elementary-stable-rpms
I use this repository to keep track of files related to packaging / building stable
releases of elementaryOS / pantheon desktop components and applications for fedora.

I am starting the process of submitting these packages to fedora for review and inclusion
in the official fedora repositories, but that will still take some time.


## Known Issues

- GTK3 > 3.18 is not yet supported by the elementary GTK theme
- the pantheon wayland session doesn't work yet


## Package Status

The current build status can be seen at <https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/monitor/>.


### official elementary apps

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| appcenter                             | OOD  (up to 0.1.1)    | DONE                  | <https://launchpad.net/appcenter>                             |
| audience                              | DONE                  | DONE                  | <https://launchpad.net/audience>                              |
| maya-calendar                         | DONE                  | DONE                  | <https://launchpad.net/maya>                                  |
| noise                                 | DONE                  | DONE                  | <https://launchpad.net/noise>                                 |
| pantheon-calculator                   | DONE                  | DONE                  | <https://launchpad.net/pantheon-calculator>                   |
| pantheon-files                        | OOD (up to 0.3.0.3.1) | DONE                  | <https://launchpad.net/pantheon-files>                        |
| pantheon-mail                         | WONTFIX               | WONTFIX               | <https://launchpad.net/pantheon-mail>                         |
| pantheon-photos                       | DONE                  | DONE                  | <https://launchpad.net/pantheon-photos>                       |
| pantheon-terminal                     | DONE                  | DONE                  | <https://launchpad.net/pantheon-terminal>                     |
| scratch-text-editor                   | DONE                  | DONE                  | <https://launchpad.net/scratch>                               |
| screenshot-tool                       | DONE                  | DONE                  | <https://launchpad.net/screenshot-tool>                       |
| snap-photobooth                       | DONE                  | DONE                  | <https://launchpad.net/snap-elementary>                       |
| switchboard                           | DONE                  | DONE                  | <https://launchpad.net/switchboard>                           |

- appcenter requires `appstream >= 0.10` (not available on f24) since version `0.1.2`
- pantheon-files requires `vala >= 0.34.0` (not available on f24) since version `0.3.0.4`
- pantheon-mail requires `gsignond`, which doesn't compile on fedora


### Pantheon desktop

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| cerbere                               | DONE                  | DONE                  | <https://launchpad.net/cerbere>                               |
| contractor                            | DONE                  | DONE                  | <https://launchpad.net/contractor>                            |
| gala                                  | DONE (bzr snapshot)   | DONE (bzr snapshot)   | <https://launchpad.net/gala>                                  |
| plank                                 | DONE                  | DONE                  | <https://launchpad.net/plank>                                 |
| pantheon-agent-polkit                 | DONE                  | DONE                  | <https://launchpad.net/pantheon-agent-polkit>                 |
| pantheon-greeter                      | WONTFIX               | DONE                  | <https://launchpad.net/pantheon-greeter>                      |
| pantheon-session-settings             | DONE (git snapshot)   | DONE (git snapshot)   | <https://github.com/decathorpe/pantheon-session-settings>     |
| slingshot-launcher                    | DONE                  | DONE                  | <https://launchpad.net/slingshot>                             |
| wingpanel                             | DONE                  | DONE                  | <https://launchpad.net/wingpanel>                             |

- gala does not yet provide a stable release
- pantheon-greeter requires a newer version of lightdm than the one available on f24
- pantheon-session-settings is a fork of the ubuntu-specific session settings bzr branch for fedora, which has no official release yet (blame me!)


### elementary artwork

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| elementary-icon-theme                 | DONE                  | DONE                  | <https://launchpad.net/elementaryicons>                       |
| elementary-themes                     | DONE                  | DONE                  | <https://launchpad.net/egtk>                                  |
| elementary-wallpapers                 | DONE                  | DONE                  | <https://github.com/elementary/wallpapers>                    |


### switchboard plugs

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| switchboard-plug-about                | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-about>                |
| switchboard-plug-a11y                 | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-a11y>                 |
| switchboard-plug-applications         | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-applications>         |
| switchboard-plug-datetime             | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-datetime>             |
| switchboard-plug-display              | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-display>              |
| switchboard-plug-keyboard             | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-keyboard>             |
| switchboard-plug-locale               | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-locale>               |
| switchboard-plug-mouse-touchpad       | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-mouse-touchpad>       |
| switchboard-plug-networking           | DONE (up to 0.1.0.2)  | DONE (up to 0.1.0.2)  | <https://launchpad.net/switchboard-plug-networking>           |
| switchboard-plug-notifications        | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-notifications>        |
| switchboard-plug-onlineaccounts       | WONTFIX               | WONTFIX               | <https://launchpad.net/switchboard-plug-onlineaccounts>       |
| switchboard-plug-pantheon-shell       | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-pantheon-shell>       |
| switchboard-plug-parental-controls    | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-parental-controls>    |
| switchboard-plug-power                | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-power>                |
| switchboard-plug-printers             | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-printers>             |
| switchboard-plug-security-privacy     | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-security-privacy>     |
| switchboard-plug-sharing              | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-sharing>              |
| switchboard-plug-useraccounts         | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-useraccounts>         |

- switchboard-plug-networking builds currentrly don't build due to a bug in `vala` which lead to corrupt `.vapi` files being generated for `NetworkManager`
- switchboard-plug-onlineaccounts requires `gsignond`, which doesn't compile on fedora


### wingpanel indicators

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| wingpanel-indicator-ayatana           | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-ayatana>           |
| wingpanel-indicator-bluetooth         | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-bluetooth>         |
| wingpanel-indicator-datetime          | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-datetime>          |
| wingpanel-indicator-keyboard          | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-keyboard>          |
| wingpanel-indicator-network           | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-network>           |
| wingpanel-indicator-notifications     | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-notifications>     |
| wingpanel-indicator-power             | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-power>             |
| wingpanel-indicator-session           | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-session>           |
| wingpanel-indicator-sound             | DONE                  | DONE                  | <https://launchpad.net/wingpanel-indicator-sound>             |


### elementary / pantheon libraries and other shared dependencies

| package name                          | f24                   | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| cmake-elementary                      | DONE (bzr snapshot)   | DONE (bzr snapshot)   |                                                               |
| gsignond                              | WONTFIX               | WONTFIX               | <https://gitlab.com/accounts-sso/gsignond>                    |
| granite                               | DONE                  | DONE                  | <https://launchpad.net/granite>                               |
| libgsignon-glib                       | WONTFIX               | WONTFIX               | <https://gitlab.com/accounts-sso/libgsignon-glib>             |

- cmake-elementary does not yet provide a stable release
- gsignond doesn't compile on fedora
- libgsignon-glib depends on `gsignond`

