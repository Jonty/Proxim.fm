Proxim.fm
=========

A small hack for Stockholm Music Hack Day that scans for bluetooth devices around the 
computer that have Last.fm usernames as the device name, then causes the Last.fm
client to play the intersection of their libraries.

Useful at parties, cafes and other situations where music is required.

It _should_ be cross platform, but it's only tested on Linux. Good luck and god speed.

Notes
-----

Proxim.fm looks for devices with their name set to something like "lfm-USERNAME", so
set your device name to that if you want to hear your tunes.

As the iPhone is lame and doesn't allow you to easily set the device name (you can do
it in the iTunes desktop software if you must), you can put mac->username mappings
in the "macMap.txt" file to allow them to be found.

As the gPhone is also lame, it only stays discoverable for a short time, so Proxim.fm
sporadically prods the devices it's seen in the past to see if they're still there
and not discoverable. Flip discoverable on and it should spot you and keep working.
If you don't want to have to do this, put the mac/username in the macMap.txt file.
