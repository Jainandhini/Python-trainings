#this is an example recurring function

def print_lol(the_list) :
    '''this is a multiline comment sample'''
    for each_item in the_list :
        if isinstance(each_item,list) :
            print_lol(each_item)
        else:
            print( each_item)
            
 
