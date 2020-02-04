---
author: "gbmhunter"
categories: [ "Programming", "Programming Languages", "Python" ]
date: 2020-02-03
description: "A tutorial on using dates and times in Python."
draft: true
lastmod: 2020-02-03
tags: [ "programming", "programming languages", "Python", "dates", "times", "tutorial", "datetime", "time zones", "UTC", "strftime", "strptime", "modules", "tzinfo" ]
title: "How To Use Dates And Times In Python"
type: "page"
---

## Overview

There are many ways of representing and manipulating dates and times in Python.

## The Inbuilt datetime Module

Python comes with a built-in module suitable for common and basic datetime use cases. Somewhat confusingly, `datetime` is both the name of the module and a name of one of the classes in the module, so if you want to use the `datetime` class, you'll see something like this:

`from datetime import datetime`

To create a `datetime` object and store the current time you can use the `.now()` function:

```python
my_time = datetime.now()
print(my_time)
# stdout: 2020-02-04 10:21:43.860130
```

Note that a `datetime` object stores both the date and the time (hence the name). The time is printed with a default resolution of `1us` (note that this is not it's accuracy, only the resolution).

You can create a `datetime` object representing an arbitrary time using the constructor which takes in the year, month, day and optional hour, minute, second and microsecond:

```python
my_time = datetime(2087, 7, 23, 18, 43, 3, 690)
print(my_time)
# stdout: 2087-07-23 18:43:03.000690
```

When you only provide the date and not the time, the time will default to `00:00:00.000000`:

```python
my_time = datetime(2087, 7, 23)
print(my_time)
# stdout: 2087-07-23 00:00:00
```

### Time Zones and the tzinfo Attribute

Date and time objects from the `datetime` module fall into two categories, they can either be `naive` or `aware`.

* `naive`: The object is not aware of the time zone it is in. It is up to the programmer to remember the time zone and apply applicable transformations to the dates and times when needed.
* `aware`: The object is aware of the time zone it is in.

Most basic uses of the `datetime` module will end up creating a `naive` object (which is fine if you only run the program in one time zone and don't need to interact with other time zones). However, most of the objects have an optional `tzinfo` attribute (which stands for _time zone info_) which when not `None`, capture information about the time zone that the datetime is in.

If you want more information on `naive` and `aware` objects, see [Determining If An Object Is Aware Or Naive](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive) in the official Python docs.

### strftime()

`strftime()` converts a `datetime` object into a string representation of the `datetime`, based on a format you specify.

```python
my_time = datetime(2020, 1, 6, 14, 37, 53)
print(datetime.strftime(my_time, '%Y'))
# stdout: 2020
```

### strptime()

`strptime()` converts a string into a `datetime` object. It takes two mandatory parameters, the first is the date and time as a string, the second describes the format of the date and time (the first param) so `strptime()` knows how to parse it (the format uses the same syntax as `strftime()`).

```python
my_time = datetime.strptime('2020-01-17 13:24:03', '%Y-%m-%d %H:%M:%S')

# my_time is a datetime object
print(type(my_time))
# stdout: <class 'datetime.datetime'>
print(my_time)
# stdout: 2020-01-17 13:24:03
```

## Astropy's time Module

## Panda's Timestamp Class