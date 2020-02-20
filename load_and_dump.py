import pickle
import os
import csv
import numpy as np

def build_filestring(filename, mod, folder='data', ftype='pkl'):
    return f'{folder}/{filename}_{mod}.{ftype}'

def dump_data(filename, data, mod):
    pickle.dump(data, open(build_filestring(filename, mod=mod), "wb"))

def get_data(filename, mod):
    fs = build_filestring(filename, mod=mod)

    if os.path.isfile(fs):
        return pickle.load(open(fs, "rb"))
    else:
        print('File does not exist!')

def data_exists(filename, mod):
    return os.path.isfile(build_filestring(filename, mod=mod))

def read_in(filename):
    data = {}

    with open(f'inputs/{filename}.txt', 'r') as df:
        rdr = csv.reader(df, delimiter=' ')

        B, L, D = [int(x) for x in next(rdr)]

        points = [int(x) for x in next(rdr)]

        data['D'] = D
        data['libs'] = []
        data['points'] = points

        # get only books that are worth more than 0
        point_idxs = []
        for index, score in enumerate(data['points']):
            if score > 0:
                point_idxs.append(index)

        for library_index in range(L):
            N, T, M = [int(x) for x in next(rdr)]

            book_ids = [int(x) for x in next(rdr) if int(x) in point_idxs]

            library = {'id': library_index, 'T': T, 'M': M, 'books': book_ids}

            data['libs'].append(library)

    return data

def write_submission(filename, data, mod):
    with open(build_filestring(filename, mod=mod, folder='solutions', ftype='txt'), 'w+') as outfile:
        writer = csv.writer(outfile, delimiter=' ', lineterminator="\n")

        # TODO HEADER GOES HERE
        writer.writerow([len(data)])

        for lib, books in data:
            writer.writerow([lib, len(books)])
            writer.writerow(books)
