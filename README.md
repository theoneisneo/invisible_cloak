This is the python 3 version of  
https://github.com/umpox/zero-width-detection  
only contain the encode/decode parts. (no web page)

See also  
https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66  
and demo site  
https://umpox.github.io/zero-width-detection/  

How to use this in your python (or other languages if you want) project?  
A very easy example:  
```
cloak = putOnInvisibleCloak(wantToHide)  # now cloak is a zero-width string
someSlogan = "Stat do not lie but I."
stringForCopy = someSlogan + cloak

reveal = takeOffInvisibleCloak(stringForCopy[len(someSlogan):])  # now reveal should equal to wantToHide
```
You can use more complex way to generate stringForCopy, but test it first.  
The print out of someSlogan and stringForCopy should have the same look for human, at least.  
note that if any char of what you want to hide is special, may have to modify zeroPadding() and binaryToChar().
