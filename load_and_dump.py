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

# TODO OUDE UIT FOTOS
def read_in(filename):
    data = []

    with open(f'inputs/{filename}.txt', 'r') as df:
        rdr = csv.reader(df, delimiter=' ')

        N = int(next(rdr)[0])

        for i in range(N):
            line = next(rdr)
            o, M, tags = line[0], line[1], line[2:]

            photo = Photo(i, o, M, tags)
            # photo['id'] = i
            # photo['orientation'] = o
            # photo['#tags'] = M
            # photo['tags'] = tags

            data.append(photo)

    return data

def write_submission(filename, iets, mod):
    with open(build_filestring(filename, mod=mod, folder='solutions', ftype='txt'), 'w+') as outfile:
        writer = csv.writer(outfile, delimiter=' ', lineterminator="\n")

        # TODO HEADER GOES HERE
        writer.writerow(["hehe"])

        for el in iets:
            writer.writerow([el])
