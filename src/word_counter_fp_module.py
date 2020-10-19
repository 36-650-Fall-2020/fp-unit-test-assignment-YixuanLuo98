import itertools
import csv
import os
import path
import inspect

#Impure function
def read(file_name):
    csv_words = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            csv_words.append(row[1])
    return csv_words

def find_parent_directory():
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return os.path.dirname(current_dir)

def use_absolute_state_data_file():
    return 'data/us-states.csv'

def use_state_data_file():
    return os.path.join(find_parent_directory(), use_absolute_state_data_file())

def count_words(file_name):
    return {k:len(list(v)) for k,v in itertools.groupby(sorted(list(itertools.chain.from_iterable(x.split() for x in read(file_name)))))}




