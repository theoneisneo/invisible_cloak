This is the python 3 version of
https://github.com/umpox/zero-width-detection
only contain the encode/decode parts. (no web page)

See also
https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66
and demo site
https://www.umpox.com/zero-width-detection/

How to use this in your python (or other languages if you want) project?
A very easy example:

cloak = putOnInvisibleCloak(wantToHide)  # now cloak is a zero-width string
someSlogan = "Stat do not lie but I."
stringForCopy = someSlogan + cloak

reveal = takeOffInvisibleCloak(stringForCopy)  # now reveal should equal to wantToHide

note that if any char of what you want to hide is special, should check zeroPadding() and binaryToChar() need rewrite or not.