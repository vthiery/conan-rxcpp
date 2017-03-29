#include <iostream>
#include<string>
#include "rx.hpp"

int main()
{
    auto get_words = [](){return rxcpp::observable<>::from<std::string>(
        "Hello",
        "Oops",
        "Hello World"
        );};

    auto hello_str = [&](){return get_words().map([](std::string n){
        return n + "!";
        }).as_dynamic();};

    hello_str().subscribe(rxcpp::util::println(std::cout));

    return 0;
}
