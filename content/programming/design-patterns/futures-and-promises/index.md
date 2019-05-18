---
author: gbmhunter
categories: [ "Programming", "Design Patterns" ]
date: 2015-04-23
draft: false
tags: [ "programming", "futures", "promises", "design pattern" ]
title: Futures And Promsises
type: page
---

<h2>Overview</h2>

<p>Futures and promises are a way of dealing with asynchronous events in a multi-threaded environment.</p>

{{< img src="futures-and-promises-cpp-icon.png" width="211px" caption="Icon for futures and promises." >}}

<p>A promise is used by the producer of the operation, and the future is used by the consumer. The producer writes a value to the promise. A future is used to read back the value, which can be done from a different thread (e.g. asynchronously).</p>

<h2>C++</h2>

<p>The main problem with the C++ implementation of futures and promises is that you cannot block on more than one future at a time. This is called a lack of being able to <i>compose futures</i>. If you had many futures, and you didn't know if what order they would return, you <b>cannot do a single block</b> on all of them. The best you can do it poll them individually in a loop, <b>burning up processor power</b>.</p>