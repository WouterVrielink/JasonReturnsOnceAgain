import pickle
import os
import csv
import numpy as np

def build_filestring(filename, mod='init', folder='data'):
    return f'{folder}/{filename}_{mod}.pkl'

def dump_data(data, filename, mod='init'):
    pickle.dump(data, open(build_filestring(filename, mod=mod), "wb"))

def get_data(filename, mod='init'):
    fs = build_filestring(filename, mod=mod)

    if os.path.isfile(fs):
        print('Data loading!')
        return pickle.load(open(fs, "wb"))
    else:
        print('File does not exist!')

def data_exists(filename, mod='init'):
    return os.path.isfile(build_filestring(filename, mod=mod))

# TODO OUDE UIT FOTOS
def read_in(filename):
    data = []

    with open(f'inputs/{filename}', 'r') as df:
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

def write_submission(filename, iets):
    with open(build_filestring(filename, mod='hc', folder='solutions'), 'w+') as outfile:
        writer = csv.writer(outfile, delimiter=' ', lineterminator="\n")

        # TODO HEADER GOES HERE
        writer.writerow()

        for el in iets:
            writer.writerow(el)
