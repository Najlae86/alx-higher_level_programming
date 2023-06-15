#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def n_list(n):
        return (n if n != search else replace)
    return list(map(n_list, my_list))
