---
author: gbmhunter
date: 2013-04-03 06:17:59+00:00
draft: false
title: How To Use C++ With PSoC Creator
type: post
url: /programming-2/how-to-use-c-with-psoc-creator
categories:
- Programming
tags:
- c
- compiler
- cplusplus
- creator
- programming
- psoc
---

Ever wanted to write C++ for the PSoC 5 or 5LP chips in PSoC Creator?

Well, although PSoC Creator doesn't natively support it, you can quite easily **do a few 'hacks', and you'll be writing in C++ in no time**.

A new page "[Using C++ With PSoC Creator](http://blog.mbedded.ninja/programming/microcontrollers/psoc/using-cplusplus-with-psoc-creator)", under Programming->[PSoC](http://blog.mbedded.ninja/programming/microcontrollers/psoc), explains the steps required to compile C++ code in Cypress's PSoC Creator.

It covers the four main steps:


## 1) Compiling with G++ rather than GCC using custom compiler flags


[singlepic id=854 w=500 h=500 float=center template=caption]


## 2) Wrapping C code with guards


extern C{< C code goes here>}


## 3) Defining the operators new and delete (this is optional)


void* operator new(size_t size)


## 4) Prevent Exception Functionality


Preventing exception functionality to prevent linker errors such as "undefined reference to __gxx_personality_v0" and "undefined reference to __cxa_end_cleanup" (again, this is optional, and only applied if you want to use new and delete)[singlepic id=1099 w=600 h=100 float=center template=caption]

The steps have pictures and code examples to help you through the process.

Checkout the page [here](http://blog.mbedded.ninja/programming/microcontrollers/psoc/using-cplusplus-with-psoc-creator).