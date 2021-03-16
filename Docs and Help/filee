# Qwire Documentation
`[]` are optional inputs<br>
`<>` are required inputs<br>
`<option1 | option2>` are options<br>
Commands are named without the prefix

## Music Commands
Some commands to play music on the bot with a YouTube, Soundcloud, Bandacamp or Viemo link or make the bot search for a song with a query.
| Command  | Aliases | Description |
| ------------- | ------------- | ------------- |
| **join**      | None | Makes Qwire join the voice channel you're in. |
| **summon <br> [voice channel]**      | None | Only usable by those with the DJ role or Manage Channel permissions, <br> makes the bot join a specified voice channel. |
| **disconnect** | dc, leave | Makes bot disconnect from its channel. |
| **play \<url or query>** | None | Plays a song from a YouTube, SoundCloud, Vimeo link or from a query. |
| **pause** | None | Pauses the audio. |
| **resume** | None | Resumes playing audio. |
| **stop** | None | Stops music and clears the queue. |
| **skip** | None | Skips the current song to the next in queue. If there are more than 2 people, a there will be a vote set. |
| **forceskip** | fs | Only usable by those with the DJ role or Manage Channel permissions, <br> Skips song while bypassing voting. |
| **loop** | None | Starts looping the current song. |
| **unloop** | None | Unloops the current song. |
| **shuffle** | None | Shuffle the songs in the queue. |
| **seek \<position>** | None | Using key letters to indicate time such as h, s and m, <br> go to that position of the playing audio. |
| **current** | now | Shows the song currently playing. |
| **ytsearch \<query>** | youtubesearch | Shows the first 5 results of a search on YouTube. |
| **scsearch \<query>** | soundcloudsearch | Shows the first 5 results of a search on SoundCloud. |
| **queue** | None | Displays everything in the queue. |
| **queue add \<url or query>** | None | Add a song to the end of the queue. |
| **queue remove \<index>** | None | Removes song of the index position in the queue excluding the current song. |
| **queue insert <br> \<index> \<url or query>** | None | Insert a song to the index position of the queue excluding the current song. |

## Moderation Commands
These are for helping moderate on your server.
| Command  | Aliases | Required Permissions | Description |
| ------------- | ------------- | ---------- | ------------- |
| **whois \<user>** | uinfo | None | Gets information on someone. |
| **members** | membercount | None | Get the number of members and bots in the server. |
| **roles** | None | None | Get a list of all the roles in the server. |
| **emojis** | None | None | Get list of all server emojis. |
| **avatar [member]** | av | None | Get the avatar of a member. |
| **serverinfo** | None | None | Get information on the settings of the server. |
| **kick \<member(s)> [reason]** | None | Kick Members | Kick a member or multiple members. The reason will be sent to the kicked member and appear in Audit Logs. |
| **ban \<member(s)> [reason]** | None | Ban Members | Ban a member or multiple members. The reason will be sent to the banned member and appear in Audit Logs. |
| **unban \<user> [reason]** | None | Ban Members | Unbans a member. You can use a name or ID of the person you want to unban. |
| **purge \<number of messages>** | clear | Manage Messages | Deletes a certain number of messages in the chat. |
| **slowmode [channel] \<time>** | smode, sm | Manage Channels | With the help with these keys: s, m, h, +, -, you can set the slowmode of a <br>channel. You can also use without the keys to set in seconds. |
| **nuke [channel]** | None | Manage Channels | Completely clear the channel of messages. Confirmation is asked for. |
| **muterole \<role>** | None | Manage Roles | Set the muterole for muting. Generation of muterole coming soon. |
| **mute \<member> [reason]** | None | Manage Roles | Mute a person, reason will appear in Audit Logs. |
| **unmute \<member> [reason]** | None | Manage Roles | Unmute a person, reason will appear in Audit Logs. |

## Join and Leave Settings
These commands are for setting up and configuring welcome and leave messages on your server. Only admins can edit these settings.
### Join Settings
| Command | Description |
| -------- | -------- |
| **joinsettings** | Shows all the options for the join settings. |
| **joinsettings settings** | Displays the current join message settings. |
| **joinsettings enable** | Enables join messages. |
| **joinsettings disable** | Disable join messages. |
| **joinsettings channel \<channel>** | Set the channel where join messages will be sent. |
| **joinsettings message \<message>** | Set the join message to be sent.<br> * Insert `[user.mention]` to ping the new member.<br> * Insert `[user.name]` to just say the name of the new member.<br> * Insert `[user]` to say that name and the tag. (e.g. CoolGuy#2021)<br> * Insert `[count]` to give the current member count.<br> * Insert `[server]` to say the name of the server. |
| **joinsettings test** | Sends a preview of the join message in the set channel. |
### Leave Settings
| Command | Description |
| -------- | -------- |
| **leavesettings** | Shows all the options for the leave settings. |
| **leavesettings settings** | Displays the current leave message settings. |
| **leavesettings enable** | Enables leave messages. |
| **leavesettings disable** | Disable leave messages. |
| **leavesettings channel \<channel>** | Set the channel where leave messages will be sent. |
| **leavesettings message \<message>** | Set the leave message to be sent.<br> * Insert `[user.name]` to just say the name of the new member.<br> * Insert `[user]` to say that name and the tag. (e.g. CoolGuy#2021)<br> * Insert `[count]` to give the current member count.<br> * Insert `[server]` to say the name of the server. |
| **leavesettings test** | Sends a preview of the leave message in the set channel. |

## Leveling
### Leveling Settings
These are commands to setup and to change settings of Leveling and Message counting. Only administrators can use these commands.<br>
Manage Roles pemissions is needed for level roles.

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
### Leveling Commands
| Command | Aliases | Description |
| ------- | ------ | ------- |
| **rank [user]** | level | Get the leveling stats of yourself or another user. |
| **messages [user]** | None | Get how many messages a ceratin user has sent. |
| **clearlevels \<user>** | None | Administrator perms required, remove level information of a user. |
| **setlevel \<user> \<level>** | None | Administrator perms required, change the level of a user. |

## Economy Commands
Semi-deprecated part of the bot. Undeveloped commands I will not show here and generally unused.
| Command | Aliases | Description |
| ------- | ------ | ------- |
| **balance [user]** | bal | Get the balance of ones account and amount in their wallet. |
| **beg** | None | Just to get a few coins. |
| **deposit \<amount>** | dep | Put some money into your bank. |
| **withdraw \<amount>** | with | Take some money from your bank. |
| **give \<member> \<amount>** | None | Give some of your pocket money to someone else. |
| **transact \<member> \<amount>** | None | Same thing as 'give' except you move money in bank. |
| **steal \<member>** | rob | Atempt to steal some money from and unlucky someone. |
| **work** | None | Work a bit for a job and get some cash. |


## Other Commands
Some commands for non server-management stuff.
### Fun Commands
| Command | Description |
| ------- | ----------- |
| **meme [subreddit]** | Shows a meme. You can specify a subreddit. |
| **define \<word>** | Shows the definition of a word. |
| **quoteit \<text>** | Turns your message into quote form. |
| **kill [user]** | Gives a random death message. |
| **revive [user]** | Gives a random revival message. |
| **you_there** | This command and the two above are, I think, the oldest commands on the bot so I'm just keeping them here. |
### Image commands
| Command | Description |
| ------- | ----------- |
| **wanted [user]** | Create a wanted poster for sombody. |
| **die [user]** | "Guess I'll Die" |
| **slap \<user>** | Slap em' |
| **achievement \<the achievement>** | Make a minecraft achievement. |
| **wasted [member]** | Wasted |
| **gay [member]** | \*Gay Pride Music Starts Playing* |
| **drip [member]** | Gottem |
