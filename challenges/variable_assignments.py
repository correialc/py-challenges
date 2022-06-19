import ast

def find_variable_assignments(source, target_var_names):
    tree = ast.parse(source)
        
    node_ids = find_node_ids(tree) # Look for variable assignments
    node_args = find_node_args(tree) # Look for argument names
    node_names = find_node_names(tree) # Look for class or function names
    
    # Consolidates results in one single set with unique names
    names = set().union(node_ids, node_args, node_names) 
    
    # Compares the list of names found in the source with the target names provided
    # Returns a list with the matched names
    return [name for name in names if name in target_var_names]

def find_node_ids(tree):
    # Variable assignments are ast.Name nodes with node.ctx of type ast.Store
    return {node.id 
                for node in ast.walk(tree) 
                    if isinstance(node, ast.Name) 
                        if isinstance(node.ctx, ast.Store)
            }

def find_node_args(tree):
    # Argument names can be found in nodes of type ast.arguments
    args_lists = [node.args for node in ast.walk(tree) if isinstance(node, ast.arguments)]
    
    # There is a nested loop here to get individual arguments
    # Nested loops should be avoided in large collections due to time complexity
    # But in this case it's assumed the parsed code will not generate large collections per code unit
    arguments = {arg.arg for args_list in args_lists for arg in args_list}
    return arguments

def find_node_names(tree):
    # Function and class names can be found as ast.FunctionDef and ast.ClassDef respectively
    return {node.name 
                for node in ast.walk(tree) 
                    if isinstance(node, ast.FunctionDef)
                    or isinstance(node, ast.ClassDef)
            }