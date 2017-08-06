# elementary-stable-rpms
I use this repository to keep track of files related to packaging / building stable
releases of elementaryOS / Pantheon desktop components and applications for fedora.

I am in the process of submitting these packages to fedora for review and inclusion
in the official fedora repositories, but that will still take some time.

Most components of a Pantheon session and almost all elementary apps are available
from the official fedora repositories now. The packages maintained here have
outstanding problems that prevent them from working right on fedora.


## Known Issues

- The Date & Time switchboard plug doesn't fully work as expected.
- The Locale plug doesn't seem to work at all under fedora.
- The Parental Controls plug might not work as advertised.
- The Power plug needs a patch to not crash and it might not work as expected.
- The Security & Privacy plug doesn't work as expected (and it depends on a non-standard firewall, `ufw`).
- The Sharing plug doesn't work on fedora, since it depends on deprecated / removed gsettings keys.
- The User Accounts plug isn't tested enough to enter fedora repositories.


## Package Status

The current build status can be seen at <https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/monitor/>.


### official elementary apps

| package name                          | f25                   | f26                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| pantheon-mail                         | DONE                  | FTBFS                 | <https://launchpad.net/pantheon-mail>                         |


### Pantheon desktop

| package name                          | f25                   | f26                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| pantheon-agent-geoclue2               | NO RELEASE YET        | NO RELEASE YET        | <https://launchpad.net/pantheon-agent-geoclue2>               |


### switchboard plugs

| package name                          | f25                   | f26                   | Upstream Project URL                                          |
| ------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| switchboard-plug-datetime             | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-datetime>             |
| switchboard-plug-locale               | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-locale>               |
| switchboard-plug-parental-controls    | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-parental-controls>    |
| switchboard-plug-power                | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-power>                |
| switchboard-plug-security-privacy     | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-security-privacy>     |
| switchboard-plug-sharing              | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-sharing>              |
| switchboard-plug-useraccounts         | DONE                  | DONE                  | <https://launchpad.net/switchboard-plug-useraccounts>         |

