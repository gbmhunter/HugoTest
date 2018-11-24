---
author: gbmhunter
date: 2017-04-20 16:03:52+00:00
draft: false
title: du (disk usage)
type: page
url: /programming/operating-systems/linux/programs/du-disk-usage
---

# Overview




du (disk usage) is a UNIX-based program that is used for displaying estimated file space usage. It can recursively iterate through directories, listing the total space used by that directory and it's contents. Note that the common ls command cannot do this, and will only display the space used by the directory and not it's contents (typically around 4kB for a directory).




# Typical Usage




To produce a human-readable summary of the sizes of files/directories in the current working directory, use:



    
    du -sh *




This may take some time, as the command has to traverse the directory structure and count up all the file sizes.