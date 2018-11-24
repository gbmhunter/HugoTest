---
author: gbmhunter
date: 2013-04-25 01:44:56+00:00
draft: false
title: C Related File Extensions
type: page
url: /programming/languages/c/c-related-file-extensions
---

# Overview




The following table lists the standard file extensions used for C-related files. The extension normally indicates how far the file is through the compilation process. Note that many integrated development environments (IDE's), and command-line compilers hide most of the individual compiler steps from the user.


<table style="width: 500px;" >
<tbody >
<tr >

<td width="120" >**File Extension**
</td>

<td >**Description**
</td>
</tr>
<tr >

<td width="120" >file-name.c
</td>

<td >C source code which must be preprocessed.
</td>
</tr>
<tr >

<td width="120" >file-name.i
</td>

<td >C source code which should not be preprocessed.
</td>
</tr>
<tr >

<td width="120" >file-name.h
</td>

<td >C header file (not to be compiled or linked).
</td>
</tr>
<tr >

<td width="120" >file-name.s
</td>

<td >Assembler code.
</td>
</tr>
<tr >

<td width="120" >file-name.S
</td>

<td >Assembler code which must be preprocessed.
</td>
</tr>
<tr >

<td width="120" >file-name.o
</td>

<td >Object file by default, the object file name for a source file is made by replacing the extension .c, .i, .s etc with .o. This can be changed with a command line parameter.
</td>
</tr>
<tr >

<td width="120" >file-name
</td>

<td >If the file has no extension, this is usually the final executable (NIX systems).
</td>
</tr>
<tr >

<td width="120" >file-name.exe, .dll, .com
</td>

<td >The final executable on a Windows system.
</td>
</tr>
</tbody>
</table>