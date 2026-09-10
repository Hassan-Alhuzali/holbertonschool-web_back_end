#!/usr/bin/env python3

'''
index_range - returns a tuple of start and end indexes for a given page and page size
'''
def index_range(page, page_size):
    '''
    Calculates the start and end indexes for a given page and page size
    
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    print(f"page: {start_index}, number of items: {end_index}")
    return (start_index, end_index)
