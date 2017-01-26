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

| package name                          | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | ------------------------------------------------------------- |
| pantheon-mail                         | WONTFIX               | <https://launchpad.net/pantheon-mail>                         |

- pantheon-mail requires `gsignond`, which doesn't compile on fedora


### Pantheon desktop

| package name                          | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | ------------------------------------------------------------- |
| pantheon-agent-polkit                 | DONE                  | <https://launchpad.net/pantheon-agent-polkit>                 |
| pantheon-greeter                      | DONE                  | <https://launchpad.net/pantheon-greeter>                      |
| pantheon-session-settings             | DONE (git snapshot)   | <https://github.com/decathorpe/pantheon-session-settings>     |


### switchboard plugs

| package name                          | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | ------------------------------------------------------------- |
| switchboard-plug-about                | DONE                  | <https://launchpad.net/switchboard-plug-about>                |
| switchboard-plug-a11y                 | DONE                  | <https://launchpad.net/switchboard-plug-a11y>                 |
| switchboard-plug-applications         | DONE                  | <https://launchpad.net/switchboard-plug-applications>         |
| switchboard-plug-datetime             | DONE                  | <https://launchpad.net/switchboard-plug-datetime>             |
| switchboard-plug-display              | DONE                  | <https://launchpad.net/switchboard-plug-display>              |
| switchboard-plug-keyboard             | DONE                  | <https://launchpad.net/switchboard-plug-keyboard>             |
| switchboard-plug-locale               | DONE                  | <https://launchpad.net/switchboard-plug-locale>               |
| switchboard-plug-mouse-touchpad       | DONE                  | <https://launchpad.net/switchboard-plug-mouse-touchpad>       |
| switchboard-plug-networking           | DONE                  | <https://launchpad.net/switchboard-plug-networking>           |
| switchboard-plug-notifications        | DONE                  | <https://launchpad.net/switchboard-plug-notifications>        |
| switchboard-plug-onlineaccounts       | WONTFIX               | <https://launchpad.net/switchboard-plug-onlineaccounts>       |
| switchboard-plug-pantheon-shell       | DONE                  | <https://launchpad.net/switchboard-plug-pantheon-shell>       |
| switchboard-plug-parental-controls    | DONE                  | <https://launchpad.net/switchboard-plug-parental-controls>    |
| switchboard-plug-power                | DONE                  | <https://launchpad.net/switchboard-plug-power>                |
| switchboard-plug-printers             | DONE                  | <https://launchpad.net/switchboard-plug-printers>             |
| switchboard-plug-security-privacy     | DONE                  | <https://launchpad.net/switchboard-plug-security-privacy>     |
| switchboard-plug-sharing              | DONE                  | <https://launchpad.net/switchboard-plug-sharing>              |
| switchboard-plug-useraccounts         | DONE                  | <https://launchpad.net/switchboard-plug-useraccounts>         |

- switchboard-plug-onlineaccounts requires `gsignond`, which doesn't compile on fedora


### elementary / pantheon libraries and other shared dependencies

| package name                          | f25                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | ------------------------------------------------------------- |
| gsignond                              | WONTFIX               | <https://gitlab.com/accounts-sso/gsignond>                    |
| libgsignon-glib                       | WONTFIX               | <https://gitlab.com/accounts-sso/libgsignon-glib>             |

- gsignond doesn't compile on fedora
- libgsignon-glib depends on `gsignond`

