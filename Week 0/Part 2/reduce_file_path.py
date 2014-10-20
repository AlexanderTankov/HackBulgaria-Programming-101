def reduce_file_path(path):
    while(path[-1:] == "/"):
        if path[-2:] == "./":
            path = path[:len(path) - 2]
            if(path[-2:] == "/."):
                path = path[:len(path) - 2]
                while (path[:len(path) - 1] != "/" and path != ""):
                    path = path[:len(path) - 1]
                path = path[:len(path) - 1]
        elif(path[-1:] == "/"):
            path = path[:len(path) - 1]
    if path == "":
        path = "/"
    for char in range(0, len(path) - 1):
        if path[char] == "/" and path[char + 1] == "/":
            path = path[:-char] + path[char + 2:]
    return path
