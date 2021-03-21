# Leveling
`[]` are optional inputs<br>
`<>` are required inputs<br>
`<option1 | option2>` are options<br>
Do not literally put the `[]` and `<>` characters.<br>
Commands are named without the prefix

## Leveling Settings
These are commands for managing leveling settings. Can only be used by Administrators.
| Command | Aliases | Description |
| ------- | ------ | ------- |
| **leveling** | None | Shows all the options for leveling and message counting settings. |
| **leveling enable** | None | Enables leveling on the server. |
| **leveling disable** | None | Disables leveling on the server. |
| **leveling rolesettings** | None | Displays all the level role rewards. |
| **leveling roleset \<level> \<role>** | None | Set a role to be achievable at a level. |
| **leveling roleremove \<level>** | rolerem, rolepop,<br>roledelete, roledel | Remove a role from being achievable. |
| **leveling channel** | None | Shows the current leveling channel. If it is none, level up messages will appear in the channel the user levelled up. |
| **leveling channelset \<channel>** | chset | Set the leveling channel. |
| **leveling channelunset** | chunset | Remove the leveling channel. |
| **leveling messagesenable** | None | Enable message counting. |
| **leveling messagesdisable** | None | Disable message counting. |
| **leveling blacklistchannel** | None | Displays all the blacklisted channels, channels where people will not gain xp in. |
| **leveling blacklistchannel add \<channel>** | None | Add a channel to blacklist. |
| **leveling blacklistchannel remove \<channel>** | rem, pop, <br>delete, del | Remove a blacklisted channel from blacklist. |
| **leveling blacklistrole** | None | Displays all the blacklisted roles, people with these roles will not gain xp. |
| **leveling blacklistrole add \<role>** | None | Add a role to blacklist. |
| **leveling blacklistrole remove \<role>** | rem, pop, delete, del | Remove a blacklisted role from blacklist. |
| **clearlevels \<user>** | None | Administrator perms required, remove level information of a user. |
| **setlevel \<user> \<level>** | None | Administrator perms required, change the level of a user. |
## Leveling Commands
Leveling commands usable by the users.
| Command | Aliases | Description |
| ------- | ------ | ------- |
| **rank [user]** | level | Get the leveling stats of yourself or another user. |
| **messages [user]** | None | Get how many messages a ceratin user has sent. |
