FILEPATH = "text.txt"

def get_list(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        list_local = file_local.readlines()
    return list_local

def write_list(list_arg,filepath=FILEPATH):
    # list = list_arg
    with open(filepath, "w") as file_local:
        file_local.writelines(list_arg)


greeting_text = """
greeting from functions file
"""
if __name__ == "__main__":
    print(greeting_text)
    print(greeting_text)