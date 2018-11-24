---
author: gbmhunter
date: 2017-11-09 17:56:40+00:00
draft: false
title: Auto (Specifier)
type: page
url: /programming/languages/c-plus-plus/auto-specifier
---

# Overview




The auto specifier (commonly referred to as a keyword) was introduced in C++11. It allows the programmer to tell the compiler to work out the type of the variable, rather than the programmer having to specify it in the code.



    
    auto x = 5;




The compiler works out what the type of a auto variable should be from it's initializer (the right-hand side the equals sign). For the example above, the compiler determines the type of x as an integer, as this is the default type for an integer value.




# Auto Functions




auto can be used as the return type for functions, both for traditional functions and lambdas.




For the above function Foo(), the compiler deduces the return type as int, as this is again the default type for an integer.



    
    auto Foo() {
       return 4;
    }




In the below example, the auto return type saves much typing/code mess!



    
    auto Foo() {
       std::map<std::string, std::vector<uint8_t>> myVar;
       return myVar;
    }




# decltype




Although they are similar and often used in the same lines of code, auto should not be confused with decltype. auto operates on types, while decltype operates on expressions.