index_partial_path = ".ragatouille/colbert/indexes"
    
def get_index_full_path(index_name):
    return "".join([index_partial_path,"/",index_name])