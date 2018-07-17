# elementary-stable-rpms
I use this repository to keep track of files related to packaging / building
stable releases of elementaryOS / Pantheon desktop components and applications
for fedora - where they aren't already available from the official fedora
repositories.

Most components of a Pantheon session and almost all elementary apps are
available from the official fedora repositories. The packages maintained here
have outstanding problems that prevent them from working right on fedora, or
have issues that would prevent a successful package review.


## Known Issues

- The Date & Time plug doesn't fully work as expected.
- The Locale plug doesn't seem to work at all under fedora - mainly due to
  assuming `apt` to be the package manager on the system.
- The Parental Controls plug might not work as advertised.
- The Power plug needs a patch to not crash, which leads to reduced
  functionality, and it might not work as expected.
- The Security & Privacy plug doesn't work as expected (and it depends on a
  non-standard firewall, `ufw`).
- The Sharing plug doesn't work on fedora, since it depends on deprecated or
  removed GSettings keys.
- The User Accounts plug isn't tested enough to enter fedora repositories - I
  don't want this to break users' machines.


## Package Status

The current build status of all non-official fedora packages can be seen at
<https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/monitor/>.


### Pantheon desktop

These meta-packages are provided only as a convenience to pull in all Pantheon
desktop components (`pantheon-session`) or the whole elementaryOS experience
(`pantheon-desktop`).

| package name     | f27  | f28  | rawhide |
| ---------------- | ---- | ---- | ------- |
| pantheon-desktop | DONE | DONE | DONE    |
| pantheon-session | DONE | DONE | DONE    |


### switchboard plugs

These switchboard plugs have issues as outlined above. There are unofficial
packages for them for completeness, but it is not guaranteed that they work at
all (or as expected).

| package name                         | f27  | f28  | rawhide |
| ------------------------------------ | ---- | ---- | ------- |
| [switchboard-plug-datetime]          | DONE | DONE | DONE    |
| [switchboard-plug-locale]            | DONE | DONE | DONE    |
| [switchboard-plug-parental-controls] | DONE | DONE | DONE    |
| [switchboard-plug-power]             | DONE | DONE | DONE    |
| [switchboard-plug-security-privacy]  | DONE | DONE | DONE    |
| [switchboard-plug-sharing]           | DONE | DONE | DONE    |
| [switchboard-plug-useraccounts]      | DONE | DONE | DONE    |


### "Made for elementary" applications

These "made for elementary" applications are not yet ready for inclusion in the
official fedora repositories due to outstanding issues.

| package name | f27  | f28  | rawhide |
| ------------ | ---- | ---- | ------- |
| [bookworm]   | DONE | DONE | DONE    |
| [hourglass]  | DONE | DONE | DONE    |
| [nasc]       | DONE | DONE | DONE    |
| [nimbus]     | DONE | ---- | ----    |
| [quilter]    | DONE | DONE | DONE    |
| [Spice-up]   | ---- | DONE | DONE    |
| [tomato]     | DONE | DONE | DONE    |

[switchboard-plug-datetime]: https://github.com/elementary/switchboard-plug-datetime
[switchboard-plug-locale]: https://github.com/elementary/switchboard-plug-locale
[switchboard-plug-parental-controls]: https://github.com/elementary/switchboard-plug-parental-controls
[switchboard-plug-power]: https://github.com/elementary/switchboard-plug-power
[switchboard-plug-security-privacy]: https://github.com/elementary/switchboard-plug-security-privacy
[switchboard-plug-sharing]: https://github.com/elementary/switchboard-plug-sharing
[switchboard-plug-useraccounts]: https://github.com/elementary/switchboard-plug-useraccounts

[bookworm]: https://github.com/babluboy/bookworm
[hourglass]: https://github.com/sgpthomas/hourglass
[nasc]: https://github.com/parnold-x/nasc
[nimbus]: https://github.com/danrabbit/nimbus
[quilter]: https://github.com/lainsce/quilter
[Spice-up]: https://github.com/Philip-Scott/Spice-up
[tomato]: https://github.com/luizaugustomm/tomato

