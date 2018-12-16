---
author: gbmhunter
date: 2017-01-13 16:23:00+00:00
draft: false
title: cp (copy)
type: page
url: /programming/operating-systems/linux/programs/cp-copy
---

# Overview

If you want to move or rename files (instead of copying), please checkout the [mv command](/programming/operating-systems/linux/programs/mv-move).

# Copying A Single File

This is the simplist cp procedure:

```sh
$ cp ~/original_file.txt ~/copied_file.txt
```

# Coping Multiple, Specific Files To A Directory

This can be done with the syntax:

```sh    
$ cp ~/{file1,file2,file3,file4} ~/destination_folder/
```

Note that there must be no spaces between the comma-separated files.