---
author: gbmhunter
date: 2013-04-15 10:32:03+00:00
draft: false
title: Extending The Background
type: page
url: /programming/website-design/opencart/extending-the-background
---

Sometimes you run into the issue of the background "running out" before the page has finished, as shown below.




[singlepic id=1112 w=800 h=700 float=center template=caption]




This can be either a case of the image running out, or the object that the image is contained in finishing.




If it is because the object the image is in has finished, you can modify the CSS to make the parent element encompass the child elements. The "Getting DIVS To Expand Vertically" article by Robert Sandy (http://www.rmsjr.com/blog/web-design/getting-divs-to-expand-vertically/, **as of Dec 2017, URL is inactive**) explains this problem in more detail and how to fix it.




I found trick 3 (the overflow/height method) to work the best since it is has the least side-effects.




All I had to do was add the line overflow: hidden; to the OpenCarts theme stylesheet.css file.



    
    #mainsite{
    	margin:0;
    	padding:0;
    	/* Original background */
    	/* background: url('../image/bg-conteiner.png') no-repeat; */
    	/* Geo's Edit: Make sure image is long enough to cover full page */
    	background: url('../image/bg-conteiner-new.png') no-repeat;
    	overflow: hidden;
    }


