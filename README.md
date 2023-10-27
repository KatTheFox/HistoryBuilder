# HistoryBuilder

HistoryBuilder is a framework for building custom origins in [Book of Hours](https://store.steampowered.com/app/1028310/BOOK_OF_HOURS/), a 2023 game by Weather Factory.

## How do I use this?

First, you'll need to either download the [latest release](https://github.com/KatTheFox/HistoryBuilder/releases/latest) or [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). They should both be the same.

Then, you need to find the Book of Hours content directory. First locate the Book of Hours game directory by right clicking the game in Steam and clicking 'browse local files'. Then, you'll need to go to the Book Of Hours content directory, which will be either `Book of Hours/bh_Data/StreamingAssets/bhcontent/core` (on Linux or Windows) or `Book of Hours/OSX.app/Contents/Resources/Data/StreamingAssets/bhcontent/core/` (on Mac). Put the `__historybuilder_mod` folder there. (Or, if you're more tech savvy, want easier updates, and you cloned the repo, make a symlink there, pointing to the `__historybuilder_mod` folder in this repo. If you don't know what that means, ignore this.)

If you're just playing someone else's origins, you can stop there. The `__historybuilder_mod` folder is offered as a standalone download for that purpose. Put the origin mods you want to play with in the same folder you put the `__historybuilder_mod` folder in (`bhcontent/core/`) and it should work out of the box.

If you're making custom origins yourself, you'll need to do some more setup.

## Custom Origins

To make a custom origin, all you need to do is make a copy of `template_origin.json` and edit the values inside it. Once you've customized it to your liking, run the python script included here (`main.py`) and point it to your origin json.

For example, to process the `template_origin.json` directly (DO NOT DO THIS, IT IS JUST AN EXAMPLE) you would run `python main.py template_origin.json` in your terminal of choice. The script will process your json file and generate a folder named similarly to your json (in this example, the script would make a folder called `_template_origin`).

That output folder is your origin mod; put it in the Book of Hours content folder next to the `_historybuilder_mod` folder from earlier. Start the game and verify that everything works as intended; you should be able to select your custom origin right away.

## How does it look in-game?

When you start a new game in Book of Hours, you usually pick from 2 sets of soul elements. With this mod installed, you'll also get cards which give you the option to skip that process entirely and start a modded origin directly. Note that if you choose your first soul element, you're locked out of modded origins for that run- so be sure of what you want.

## Help, my modded origin has no fet, shapt, or chor, and I'm softlocked!

The beginning of the game is designed so that you'll always have one of fet, shapt, or chor, and they're needed for progression. If your modded origin starts without any of those, you'll need to add recipes to start the game without them. Samples are provided here as `additional_start.json`; if you want to enable all elements being used to start the game, you can just copy that file into your mod's folder directly. Otherwise, pick and choose the ones you need. (And you may want to rewrite the text- I'm not a writer, they're provided to solve a technical issue.)

## Why do I need to define vanilla images for my journal and setup icon? Why can't I make my own?

Loading custom images is currently not possible in Book of Hours. It's technically possible to make a working imageloader, but that's far outside the scope of this project, and would require constant maintenance as the game updates.

## I have an issue not covered here, how do I contact you?

If you run into issues not covered here, you can find me in the [Cultist Simulator discord server](https://discord.gg/KxyFTZkUbQ). That's where most of the modding discussion happens anyway.

## Disclaimers

Modding is not officially supported in Book of Hours. Do not contact Weather Factory with bugs resulting from the use of this mod. As the game updates, expect potential breakages. I am not affiliated with Weather Factory in any way.
