# rina-iOS-posting

Use case:  Making tweet-like posts for when I am away from my computer/local network, but still feel compelled to let the internet know about an inane thought I had.

Bonus: Add the shortcut to your homescreen!  Who needs an Apple Developer account?

Setup on iPhone (in Shortcuts app) below.  I'm SSH-ing into my Raspberry Pi (through a custom domain! not it's ip address 😁) which runs code to add the content to a PostgreSQL database.  The other scripts are available in this repo.  `mobileposting.py` adds the psycopg2 tuple to a txt file, so that I can update my local (PC) database I use for keeping a backup.

![](https://github.com/marikamcc/rina-iOS-posting/blob/main/shortcuts-setup.jpg?raw=true)
