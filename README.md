# Twitch bot ban list
Public collection of bot ban commands to be used with !filesay commands or similar found in many larger twitch chat bots such as StreamElements and Fossabot. The purpose of these is to simply collect a collection of files that can be quickly called from chat - mass banning the bots.

This is maintained actively when I need it, if input is sent to me I will try to update the lists, but I also have a life so it wont be instant most days.
If a list is needed immediatly I recommend using pastebin or similar and use same format as these files.

## Format
Each file is max 400 lines of commands banning bots in the format `.ban <botname>`.
The 400 line max is imposed by StreamElements so to keep it general the lists are split every 400 names.

## Usage
Call the !filesay (or equivalent command) with the a given raw text file to run. The bot will execute each line seperatly in sequence.

```!filesay  https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list1.txt```

To use the next file simply change the list1.txt to list2.txt or any other.
Copy paste of all available files for the lazy:
```
!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list1.txt
!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list2.txt
```

## Help out
To add name make a pull request with the bot names or dm me your list on discord @ zfih#0666