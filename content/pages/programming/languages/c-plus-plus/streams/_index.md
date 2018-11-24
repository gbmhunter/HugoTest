---
author: gbmhunter
date: 2017-11-10 17:57:19+00:00
draft: false
title: Streams
type: page
url: /programming/languages/c-plus-plus/streams
---

# Overloading << Operator For ostream




A common and useful practise is to overload the << operator for an ostream on your own classes. This allows you to then write things such as:



    
    MyClass myClass;
    std::cout << "My class = " << myClass << std::endl;




One way to do this is to overload the operator from within your class header file, declaring std::ostream as a friend:



    
    #include <sstream>
    
    class MyClass {
    public:
       friend std::ostream& operator<<(std::ostream &out, const MyClass& rhs);
    private:
       int myVar_;
    };




And then the definition in the .cpp would look like:



    
    std::ostream &operator<<(std::ostream &out, const MyClass& rhs) {
       out << "{ ";
       out << std::to_string(myVar_);
       out << " }";
       return out;
    }




# A Generic Overload For All Classes




Since C++11, you can make a generic overload that will work for all classes that contain a public method called Print(std::ostream&)const.



    
    template<class T>
    auto operator<<(std::ostream& os, const T& t) -> decltype(t.Print(os), os) { 
        t.Print(os); 
        return os; 
    }




This saves you to work of having to overload the << operator for each class you design!