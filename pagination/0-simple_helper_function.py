#!/usr/bin/env python3

'''
returns a tuple of start and end indexes for a given page and page size
'''
def index_range(page, page_size):
    '''
    Calculates the start and end indexes for a given page and page size
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return tuple([start_index, end_index])
