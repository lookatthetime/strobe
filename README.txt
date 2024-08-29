Strobe.

This game was created by Look at the Time Studios. 
Please do not redistribute or take credit for this creation in any way, shape, or form. 

Thanks in advance!

Strobe Release Version 2.0 (Commands and Collisions Update (also added blur))

Download updates from "tinyurl.com/lattstudios"

DISCLAIMER: LatT Studios is not liable for anything positive or negative that happens in this game unless it is endorsed by LatT Studios. LatT Studios is also not liable for anything that happens in relation to the base game, and what may happen because of this. This is a free game, do not abuse that!

Thanks for playing!



*Strobe Developer Console Docs

**In the following docs: A_NAME_IN_CAPS_LOCK means that you replace it with the value (eg. POSITION would be replaced with a number)

**Important feature: you can use $px to get the player's x position, $py to get the player's y position, and $score to get the player's score

**How to get it: press [/]. You can do this in game for the normal console or on the title screen for an... interesting console that will be mentioned shortly

**Permarun: the Permarun console comes up when you press [/] on the title screen. This console runs the given command every frame


- /name - "/name NAME_OF_WINDOW" - name the window
- /spawn - "/spawn TYPE POSITION" - spawn an attack - types: blast, streak, lightstreak, slide
- /noclip - "/noclip" - toggle noclip
- /tp - "/tp X_POSITION Y_POSITION" - teleport to a position


Premade commands:
"I'm gonna rush!" (noclip needed): /spawn slide 1000
"BLAST ME!" (can be put in Permarun): /spawn blast $py
"Useless": /tp $px $py
"Moving on the ground" (put in Permarun): /tp $score $score
"OH GOD NO PLEASE NO I HAVE A WIFE AND 2 CHILDREN!!!" (put on Permarun): /spawn lightstreak $py