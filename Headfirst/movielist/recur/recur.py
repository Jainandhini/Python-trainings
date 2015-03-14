#this is an example recurring function

def print_lol(the_list) :
    '''this is a multiline comment sample'''
    for each_item in the_list :
        if isinstance(each_item,list) :
            print_lol(each_item)
        else:
            print( each_item)
            
        
movies=["titanic",1995,["Jack","Rose",["Steven","Spielberg"]],"when harry met sally",1989,['Harry',['Sally','Silly']],"superb"]
print('normal list')
print(movies)
print('after calling recursive method')
print_lol(movies)
