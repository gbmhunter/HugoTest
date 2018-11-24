---
author: gbmhunter
date: 2011-09-15 07:34:05+00:00
draft: false
title: Version Control Systems
type: page
url: /programming/version-control-systems
---

# Child Pages




[sb_child_list template=2 orderby=title order=asc nest_level=1]




# Overview




Version control systems are designed for organising and retaining file information in a environment where the 'watched' files are constantly changing. They are used exetnsively in programming, project file management and general file management.




The primary functions of a SCM are:





	  * Retaining all versions of a watched file
	  * Ease of use (this is a big one!)
	  * The capability of retaining only the changed data, as to make the amount of space an SCM uses up is kept to a minimum (you can imagine how big the SCM would get if it saved a new copy of a file every time you modified it slightly).
	  * Multi-user capability, this has it's own sub-functions  

 - A checkout system for files  

 - The ability to merge individual changes on one file together



Version control systems usually originate from command-line roots, and then get GUI'ed up once they gain popularity. Using modern SCM's like Git and Mercurial is trivial through a command-line.




# Mercurial




Mercurial will not copy folders into the repo if there are no files in them. Why would you have empty foler you ask? Well, one reason would be if you had a template folder structure for new projects that you wanted in the repo.




One of my favourite SCMs! It is very similar to Git, and hence Git it also one of my favourite. Mercurial only creates one folder in the root directory of your project (SVN creates one in every folder). [TortoiseHG](http://tortoisehg.bitbucket.org/) is an awesome Windows shell extension for Mercurial. I never get errors and irreversable lockouts with Mercurial as I did with SVN.




Mercurial assigns every commit on your machine a revision number. This **IS NOT a unique number**! It is very much likely that another user of the repo will have the exact same revision number for a different commit. If you after a unique number, you have to use the changeset ID. This is a 160-bit number (Mercurial normally only shows you the first 10 characters) found by using the [SHA-1 hash](http://en.wikipedia.org/wiki/SHA-1) on the current commit data, the previous commits hash, the username, and the date. Note that when I say unique, I mean probablistically impossible, although two different revisions could in theory produce the same changeset ID (as of July 2012, no collisions have been discovered).




# Mercurial Ignore Files




Ignore files are handy for excluding unwanted files from any mercurial repository, such as the 'millions' of junk files created by programming and design software. Below are ignore files I have made for certain software packages.




The ignore file has to be called .hgignore and be placed in the root folder location of the repo. It is versioned just like any other file in the repository, but is a special file that Mercurial parses to determine which files to ignore from the repo, using string matching with either the regexp (greater power, flexibility, but harder to understand), or glob syntax (less power, but easy to understand, syntax much like Windows path formats).




Glob Syntax (no longer maintained):





	  * [Altium Designer](http://blog.mbedded.ninja/programming/microcontrollers/general/version-control-systems/altium-version-control-with-mercurial)
	  * [PSoC Creator](http://blog.mbedded.ninja/programming/microcontrollers/general/version-control-systems/mercurial-ignore-file-code-for-psoc-creator)
	  * [uVision 4](http://blog.mbedded.ninja/programming/microcontrollers/general/version-control-systems/uvision-version-control-with-mercurial)
	  * [Visual C#](http://blog.mbedded.ninja/programming/microcontrollers/general/version-control-systems/visual-studio-version-control-with-mercurial)



**Mercurial/Tortoise HG Error Messages**





	  * "Unknown Parent" - Occurs when trying to pull changesets from another repository. Normally means some part of your repo is corrupted. The only solution I have found is to delete your repo and clone a working one, after copying all the files you want to save of course...
	  * "The system cannot find the file specified" error message occuring when you attempt to commit your repo. This is normally due to one of two reasons. The first one is if you deleted a file between clicking the 'Refresh files' button and clicking 'Commit'. The second reason is if the absolute path name of the file exceeds 255 characters. Tortoise HG will recognise the file and display it, but will fail when trying to commit. There is an extension called ['Win32LongFileNamesExtension' (aka win32lfn)](https://www.mercurial-scm.org/wiki/Win32LongFileNamesExtension) that is meant to fix this, but I have not be able to get it to work.
	  * "abandoned transaction found - run hg recover" - This normally occurs if the connection between the local and remote repo is disconnected mid-way through a push/pull operation.  

 [singlepic id=767 w=300 h=150 float=center]



# How To Make A Mercurial Repo Remember A Local Server Location To Push To




You need to add the path of the server to the hgrc file in the Mercurial .hg folder that it creates at the root location of your repo. It can also be done through the UI.




The syntax follows:



    
    [paths]
    default = \\<server-name>\<repo location>




For example:



    
    [paths]
    default = \\mainserver\projects\Electric Skateboa




# Long File Names




Long file names of over 260 characters in Windows can cause issues for Mercurial (you normally get cannot find file errors when trying to commit). There is a 3rd party extension, called [win32lfn](https://www.mercurial-scm.org/wiki/Win32LongFileNamesExtension), which allows Mercurial to handle these longer file names.




# SVN




A very popular version control system that is well integrated into a fair amount of third party software. Manages on a file-to-file basis, which gives the main benefit of a user being able to checkout a section of a project, work on it, and commit it back to the main repository without ever downloading the rest.




An annoying problem of SVN is the errors I keep getting. I am not sure if I use it right, but somewhere along the line of using  SVN for project (be it a day, or a few weeks later), a clash arises from trying to merge to files together or accidently renaming a folder. This normally locks the directory and I can never get the clean up function to work properly, resulting in SVN becoming useless. This is why I prefer Mercurial/Git.




# CVS




CVS (concurrent versions system) is a tool for version control of files (normally code/text-files). It is older and considered inferior to newer CMS's such as Git or Mercurial. As of 2013, it is being used by [Sourceforge](https://sourceforge.net/).




CVS can be installed onto a Linux system using:



    
    sudo apt-get install cvs


