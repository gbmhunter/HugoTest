---
author: gbmhunter
date: 2018-12-03
draft: false
title: vim
type: page
url: /programming/integrated-development-environments-ides/vim
---

# Overview

vim is a command-line based text editor.

It is very useful for editing code and config files when you only have access to a command-line, e.g. when your are ssh'ed into a remote machine.

# Find And Replace

To find every occurrence of `foo` and replace it with `bar` we can use the substitute command (`s`):

```
:%s/foo/bar/g
```

The `%` at the start forces vim to check all lines, not just the current one. The `g` at the end stands for global, which force vim to replace all occurrences, not just the first.

The _search pattern_ (which above is `foo`) supports regex. 

You can add a `c` at the end to ask for confirmation on each replace:

```
:%s/foo/bar/gc
```

When searching, `.`, `*`, `\`, `[`, `^` and `$` have special functions. Place a backslash before each to instead search for that actual character (e.g. `\*` will search for a `*`.)

## Advanced Find And Replace Using Backreferences

vim supports advanced find/replace operations which involve manipulating the input into the output using regex back references.
