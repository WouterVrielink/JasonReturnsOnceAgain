from load_and_dump import read_in, data_exists, dump_data, get_data, write_submission
import numpy as np

def sort_books(scores, book_ids):
    return sorted(book_ids, key=lambda book_id: scores[book_id])

def sort_libs(scores, libs):
    return sorted(libs, key=lambda lib: sum([scores[book] for book in lib['books']]))

def transform_format(data):
    output = []

    counter = 0
    for lib in data['libs']:
        output.append((counter, lib['books']))
        counter += 1

    return output


def best_next_lib(data):
    max_scores = []
    for lib in data['remaining_libs']:
        x = max(data['D'] - lib['T'], 0) * lib['M']
        candidate_books = sort_books(data['points'], list(set(lib['books']) - data['used_books']))
        score = sum(data['points'][book] for book in candidate_books[:x])
        max_scores.append(score)
        lib['candidate_books'] = candidate_books
    best_lib = np.argmax(max_scores)
    return data['remaining_libs'][best_lib], best_lib


def greedy_with_deadlines(data):
    output = []
    data['remaining_libs'] = data['libs'].copy()
    data['used_books'] = set()
    while (data['D'] > 0) and data['remaining_libs']:
        best_lib, best_lib_i = best_next_lib(data)
        del data['remaining_libs'][best_lib_i]
        data['D'] = data['D'] - best_lib['T']
        data['used_books'] = data['used_books'] | set(data['libs'][best_lib['id']]['candidate_books'])
        output.append((best_lib['id'], data['libs'][best_lib['id']]['candidate_books']))
    return output


if __name__ == "__main__":
    # filename = 'a_example'
    # filename = 'b_read_on'
    filename = 'c_incunabula'
    # filename = 'd_tough_choices'
    # filename = 'e_so_many_books'
    # filename = 'f_libraries_of_the_world'
    
    algorithm = 'greedy_returns_again'

    data = read_in(filename)

    output = greedy_with_deadlines(data)
    
    write_submission(filename, output, mod=algorithm)
    

    # if not data_exists(filename, algorithm) or algorithm == 'init':
    #     # TODO DOE HIER INIT ALGORITME
    #     print('Running initialisation algorithm...')
    #     init_iets = [None]
    #
    #     print('Dumping data and writing submission file...')
    #     dump_data(filename, init_iets, mod=algorithm)
    #     write_submission(filename, init_iets, mod=algorithm)
    # else:
    #     print('Data loading!')
    #     init_iets = get_data(filename, mod=algorithm)
    #
    # # TODO DOE HIER HILLCLIMBER OFZO
    # print('Running hillclimber...')
    # outcome_hc = [None]
    #
    # print('Dumping data and writing submission file...')
    # dump_data(filename, outcome_hc, mod='hc')
    # write_submission(filename, outcome_hc, mod='hc')
