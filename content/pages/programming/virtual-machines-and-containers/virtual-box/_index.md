---
author: gbmhunter
date: 2013-05-23 00:40:38+00:00
draft: false
title: VirtualBox
type: page
url: /programming/virtual-machines-and-containers/virtual-box
---

# Overview




VirtualBox is virtual machine software by Oracle.




# gedit "File Busy" Error




A long-standing bug with Oracles VirtualBox and the popular Linux text editor, Gedit (or any other text editor, for that matter), is the "File Busy" error that you get when trying to save a file across a mounted, shared folder from within Linux system running Gedit (e.g. saving into a Windows-hosted folder).




[singlepic id=1136 w=800 h=300 float=center template=caption]




The problem comes from shared folders which are mounted using the command:



    
    $ sudo mount -t vboxsf shared-name folder-to-mount-to




The only workaround I am aware of is to enable the "Save Backup Copy" option in the preferences, and hit the save button twice. Annoying and far from perfect, but you can get quick at doing this (Ctrl-S, Enter, Ctrl-S does the trick).




[singlepic id=1135 w=500 h=400 float=center template=caption]




You will also have to delete all the .goutputstream-XXXXXX files that are created in the directory (these are the backup files).




# SVN In Shared Folders




SVN can throw svn: Can't move '.svn/tmp/entries' to '.svn/entries': Operation not permitted. errors when attempting to checkout a SVN repository into a shared folder when using VirtualBox.




One work around it to use git-svn (install with sudo apt-get install git-svn) to clone the SVN repository instead.



    
    git svn clone https://svn-repository local-folder




Cloning a SVN repo using git-svn can take some time!