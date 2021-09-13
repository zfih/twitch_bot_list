# Twitch bot ban list
Public collection of bot ban commands to be used with !filesay commands or similar found in many larger twitch chat bots such as StreamElements and Fossabot. The purpose of these is to simply collect a list of files that can be quickly called from chat, mass banning the bots.

This is maintained actively when I need it, if input is sent to me I will try to update the lists, but I also have a life so it wont be instant most days.
If a list is needed immediatly I recommend using pastebin or similar and use same format as these files.

## Format
Each file is max 400 lines of commands banning bots in the format `.ban <botname>`.
The 400 line max is imposed by StreamElements so to keep it general the lists are split every 400 names.

## Usage
Call the !filesay (or equivalent command) with the a given raw text file to run. The bot will execute each line seperatly in sequence.

```!filesay  https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list1.txt```

To use the next file simply change the list1.txt to list2.txt or any other.
I have not tried this with other bots like StreamLabs or Nightbot, so I don't know the requirements of these.
If you want to test if you have access to the command you can run the test file 

`!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/bottest.txt`

which should print the following in chat: `filesay command is available to you and working as intended`

### If you cannot be bothered to type all that go to the "For the lazy" section

## How to add names
To add names to the list, the easiest way is to use the added python script. The script will read the existing files and only add new names to the list, while keeping the lists at 400 names max.

### Usage
Add a list of names using a raw text file with names in the the following format:
```
name1
name2
name3
```
using python3 this can be given to the script as such:

```
python3 addnames.py -i namelist.txt
```

otherwise a short list of names can just be given as input parameters:
```
python3 addnames.py name1 name2 name3
```

To add name make a pull request with updated lists using the script above or the added manually in the correct format. If you don't know how to use python simply submit a list of names in the format above or dm me your list on discord @ zfih#0666 (in raw text, I will not accept files).

## For the lazy

```
!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list1.txt
!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list2.txt
!filesay https://raw.githubusercontent.com/zfih/twitch_bot_list/main/list3.txt
```