from plistlib import *

# list of strings to ignore
ignore_list = ['$null', 'columnA', 'columnB', 'customGroup', 'customGroupString', 'customType', 'customTypeString',
               'Deutsch', 'disabled', 'dueDate', 'English', 'GeniusItem', 'GeniusPair', 'importanceNumber',
               'notesString', 'NSArray', 'NSDate', 'NSDictionary', 'NSKeyedArchiver', 'NSMutableArray',
               'NSMutableDictionary', 'NSMutableString', 'NSObject', 'NSString', 'scoreAB', 'scoreBA', 'scoreNumber']

# the file to parse
in_file = 'GermanVocab.genius'

# the file to write
out_file = in_file.replace('.genius', '.txt')

# recursive method to search the plist file for all strings
def print_strings_recursively(stream, obj):
    if isinstance(obj, str):
        if obj not in ignore_list:
            stream.writelines(obj + '\n')
    elif isinstance(obj, list):
        for listVal in obj:
            print_strings_recursively(stream, listVal)
    elif isinstance(obj, dict):
        for dictVal in obj.values():
            print_strings_recursively(stream, dictVal)


# open the file
with open(in_file, 'rb') as in_stream:
    data = load(in_stream)

# search recursively for strings and print them
with open(out_file, 'w') as out_stream:
    for value in data.values():
        print_strings_recursively(out_stream, value)
